# 第16章：Presto/Trino查询执行流程 (Presto/Trino Query Execution Flow)

理解Presto/Trino如何执行一个SQL查询是掌握其内核的关键。与Spark和Flink类似，Presto/Trino也将用户的声明式SQL转换为一系列可在分布式集群上执行的物理操作。本章将详细分解Presto/Trino的查询执行流程，从SQL的解析与分析开始，经历逻辑计划生成与优化，再到物理计划（Stage和Task）的创建，最后由Coordinator调度并在Worker上以流水线（Pipelined）方式执行。

## 16.1 查询解析与分析 (Parsing & Analysis)

查询执行的第一步始于客户端（如CLI、JDBC驱动）将SQL语句发送给Coordinator。

1.  **解析 (Parsing):**
    *   Coordinator接收到SQL字符串后，首先调用**解析器 (Parser)**。
    *   解析器（通常使用ANTLR等工具生成）将SQL文本转换为**抽象语法树 (Abstract Syntax Tree, AST)**。
    *   AST是一种树状结构，表示了SQL语句的语法结构，例如SELECT、FROM、WHERE子句及其包含的表达式、表名、列名等。
    *   **示例AST (简化):**
        ```mermaid
        graph TD
            Select --> SelectList;
            Select --> From[FROM TableA];
            Select --> Where[WHERE Condition];
            SelectList --> Col1[Column: user_id];
            SelectList --> Col2[Function: COUNT(*)];
            From --> TableRef[Table: clicks];
            Where --> Comparison[Comparison: >];
            Comparison --> Col3[Column: timestamp];
            Comparison --> Literal[Literal: '2023-01-01'];
        ```

2.  **分析 (Analyzing):**
    *   生成AST后，**分析器 (Analyzer)** 接手。
    *   分析器负责**语义检查**和**元数据绑定**: 
        *   **验证:** 检查AST中引用的Schema、Table、Column是否存在于元数据存储（通过Connector访问）中。
        *   **类型检查:** 验证函数调用、表达式、比较操作等涉及的数据类型是否兼容和合法。
        *   **作用域解析:** 确定列名等标识符引用的具体对象。
        *   **权限检查 (可选):** 验证用户是否有权限访问查询涉及的表和列。
    *   分析阶段会将AST转换为**逻辑查询计划 (Logical Query Plan)**。逻辑计划是一种更结构化的表示，描述了需要执行的操作（如Scan, Filter, Project, Aggregate, Join）及其之间的数据流关系，但还不涉及具体的执行方式或分布式细节。

## 16.2 逻辑计划生成与优化 (Logical Planning & Optimization)

分析器产生的初步逻辑计划通常不是最优的。接下来，**逻辑规划器 (Logical Planner)** 和 **优化器 (Optimizer)** 会对其进行一系列转换和优化。

*   **逻辑计划表示:** 通常使用关系代数操作符（如 σ (select/filter), π (project), ⋈ (join), γ (aggregate)）的树状结构来表示。

*   **优化目标:** 减少查询执行的资源消耗（CPU、内存、网络I/O），缩短查询时间。

*   **优化技术 (详见第17章):** Presto/Trino的优化器会应用多种技术：
    *   **规则优化 (Rule-Based Optimization, RBO):** 应用一系列预定义的启发式规则来重写逻辑计划。例如：
        *   **谓词下推 (Predicate Pushdown):** 将`WHERE`子句中的过滤条件尽可能早地应用，靠近数据源（Scan操作），以减少后续操作处理的数据量。
        *   **列裁剪 (Column Pruning / Projection Pushdown):** 只读取查询最终需要的列，避免读取不必要的列数据。
        *   **常量折叠 (Constant Folding):** 预先计算常量表达式的值 (e.g., `1 + 2` -> `3`)。
        *   **Limit下推:** 将`LIMIT`子句下推到数据源或Join操作中。
    *   **成本优化 (Cost-Based Optimization, CBO):** （可选，且在持续发展中）基于数据的统计信息（如表大小、列基数、数据分布等）来估算不同执行计划的成本，并选择成本最低的计划。例如：
        *   **Join顺序选择:** 选择最优的Join执行顺序（例如，先Join小表）。
        *   **Join算法选择:** 选择合适的Join实现（如Hash Join, Broadcast Join）。
        *   **聚合策略选择:** 选择Hash Aggregation或Sort-based Aggregation。

*   **输出:** 优化器最终输出一个优化后的逻辑计划。

## 16.3 物理计划生成：Stage划分与Task生成

优化后的逻辑计划描述了"做什么"，但没有说明"如何在分布式环境中做"。**物理规划器 (Physical Planner)** 负责将逻辑计划转换为可在MPP架构上执行的**物理执行计划 (Physical Execution Plan)**。

1.  **Stage划分 (Stage Generation):**
    *   物理规划器首先将逻辑计划（特别是涉及数据交换的操作，如Join、Aggregate）切分成若干个**阶段 (Stage)**。
    *   Stage是物理执行的基本单元，代表了一组可以**流水线 (Pipelined)** 执行的操作。
    *   Stage之间的边界通常是需要**数据重分区 (Shuffle / Exchange)** 的地方（例如，Join前的Hash分区，聚合前的全局聚合分发）。
    *   一个Stage的输出会作为下一个Stage的输入。
    *   这种划分形成了一个**Stage依赖图 (DAG of Stages)**。

2.  **Task生成 (Task Generation):**
    *   对于每个Stage，物理规划器会根据数据的**分片 (Splits)** 信息（由Connector提供）和目标并行度，将其进一步分解为多个并行的**任务 (Task)**。
    *   一个Task通常负责处理一个或多个数据分片 (Split)。
    *   每个Task内部包含了一系列按流水线方式执行的**算子 (Operator)** 实例（如TableScanOperator, FilterOperator, ProjectOperator, HashBuilderOperator, ExchangeOperator等）。

**物理计划示例 (简化Stage和Task):**

```mermaid
graph TD
    subgraph Logical Plan (Optimized)
        LP_Join(Join: A.id = B.id) --> LP_Agg(Aggregate: COUNT(*));
        LP_ScanA(Scan A) --> LP_FilterA(Filter A.city='NY') --> LP_Join;
        LP_ScanB(Scan B) --> LP_FilterB(Filter B.status='active') --> LP_Join;
    end

    subgraph Physical Plan (Stages & Tasks)
        Stage3((Stage 3: Final Aggregation)) --> Output[Query Output];
        Stage1((Stage 1: Scan & Filter A, Hash A)) -- Exchange --> Stage3;
        Stage2((Stage 2: Scan & Filter B, Build Hash Table B)) -- Exchange --> Stage3;

        subgraph Stage 1 Tasks (Parallel)
            Task1_1(Task 1.1: Scan Split A1, Filter, Hash) --> Exchange1_1(Exchange Client);
            Task1_2(Task 1.2: Scan Split A2, Filter, Hash) --> Exchange1_2(Exchange Client);
        end

        subgraph Stage 2 Tasks (Parallel)
            Task2_1(Task 2.1: Scan Split B1, Filter, Build Hash) --> Exchange2_1(Exchange Sink);
            Task2_2(Task 2.2: Scan Split B2, Filter, Build Hash) --> Exchange2_2(Exchange Sink);
        end

         subgraph Stage 3 Tasks (Parallel)
            Task3_1(Task 3.1: Probe Hash A1, Join, Aggregate) --> Exchange3_1(Output Buffer);
            Task3_2(Task 3.2: Probe Hash A2, Join, Aggregate) --> Exchange3_2(Output Buffer);
        end

         Exchange1_1 --> Task3_1;
         Exchange1_2 --> Task3_2;
         Exchange2_1 --> Task3_1;
         Exchange2_2 --> Task3_2;
         Exchange3_1 --> Output;
         Exchange3_2 --> Output;
    end
```
*   **Split:** Split是数据处理的最小并行单元，由Connector定义。例如，Hive Connector可能会将一个HDFS文件的一个Block视为一个Split。

## 16.4 分布式执行调度 (Coordinator的作用)

生成物理计划（包含Stage、Task、Split分配）后，Coordinator开始调度执行。

*   **资源协商:** Coordinator根据查询的资源组配置和当前集群负载，向Worker节点请求资源（主要是内存）。
*   **Task部署:** Coordinator将每个Stage的Task分配给具体的Worker节点执行。分配时会考虑数据本地性（Data Locality），尽量将处理某个Split的Task调度到存储该Split数据（或其缓存）的Worker上，以减少网络传输。
*   **启动执行:** Coordinator向Worker发送启动Task的指令。
*   **状态监控:** Coordinator持续监控所有Task的执行状态（Running, Finished, Failed）。
    *   如果Task成功完成，Coordinator会调度依赖该Task输出的下游Stage的Task。
    *   如果Task失败，Coordinator可能会根据容错策略（如查询重试）进行处理。
*   **结果收集:** 对于最终Stage的Task，Coordinator负责收集其输出结果，并将其流式返回给客户端。

## 16.5 Pipelined Execution Model

Presto/Trino的核心执行模型是**流水线执行 (Pipelined Execution)**，这也是其实现低延迟交互式查询的关键。

*   **核心思想:** 数据尽可能地在内存中以**Page（页）**为单位（Page是Presto/Trino内部处理数据的基本列式内存格式），像流水一样在同一个Task内部的不同Operator之间，以及不同Task（通过网络Exchange）之间流动，无需等待整个Stage或Task完成。
*   **Task内部流水线:** 在一个Task内部，数据从上一个Operator处理完一个Page后，就立刻传递给下一个Operator处理，形成Operator内部的流水线。
*   **Stage间流水线 (通过Exchange):**
    *   **Exchange Operator:** 负责处理Task之间的数据传输。
    *   **发送端 (Source Task):** Task处理完一个Page后，通过`ExchangeOperator`（或其变体如`PartitioningExhangeOperator`）将其发送到网络缓冲区。
    *   **接收端 (Destination Task):** 下游Task的`ExchangeClient`从网络接收Page，并将其提供给该Task的第一个Operator。
    *   数据不需要等待整个上游Stage完成，只要上游Task产生了输出Page，下游Task就可以开始处理。
*   **优点:**
    *   **低延迟:** 结果可以尽快地流向上游，用户可以更快地看到部分结果。
    *   **内存效率:** 避免了将庞大的中间结果完全物化到磁盘（除非内存不足Spill）。
*   **与Blocking的区别:** 对比之下，传统的MapReduce模型是严格的Blocking模型，Map Task必须完全结束后，Reduce Task才能开始拉取数据。Spark的Stage内部是Pipelined的，但Stage之间（宽依赖）通常是Blocking Shuffle（虽然Spark也在演进）。Presto/Trino尽可能地在所有环节（Task内和Task间）都采用Pipelined模式。

**流水线执行示意图:**

```mermaid
sequenceDiagram
    participant Client
    participant Coord as Coordinator
    participant Worker1 as Worker 1 (Scan Task)
    participant Worker2 as Worker 2 (Join/Agg Task)
    participant DataSource

    Client->>Coord: SQL Query
    Coord->>Coord: Parse, Analyze, Optimize
    Coord->>Coord: Generate Physical Plan (Stages, Tasks)
    Coord->>Worker1: Schedule Scan Task (Split A1)
    Coord->>Worker2: Schedule Join/Agg Task

    Worker1->>DataSource: Read Page 1 (Split A1)
    Worker1->>Worker1: Process Page 1 (Filter, Hash)
    Worker1-->>Worker2: Send Page 1 via Network

    Worker1->>DataSource: Read Page 2 (Split A1)
    Worker2->>Worker2: Receive Page 1
    Worker2->>Worker2: Process Page 1 (Probe, Join, Agg)
    Worker1->>Worker1: Process Page 2 (Filter, Hash)
    Worker1-->>Worker2: Send Page 2 via Network

    Worker1->>Coord: Scan Task Finished
    Worker2->>Worker2: Receive Page 2
    Worker2->>Worker2: Process Page 2 (Probe, Join, Agg)
    Worker2-->>Coord: Send Result Page 1

    Coord-->>Client: Stream Result Page 1
    ...
    Worker2->>Coord: Join/Agg Task Finished
    Coord->>Coord: Aggregate Final Results
    Coord-->>Client: Stream Final Result & Close
```

**总结:** Presto/Trino的查询执行流程是一个精心设计的、将SQL转换为分布式物理计划并高效执行的过程。从解析、分析到逻辑与物理规划，再到Coordinator的调度和Worker上基于流水线模型的并行执行，每一步都旨在优化性能，特别是降低查询延迟，以满足交互式分析的需求。理解这个流程有助于分析查询瓶颈、进行性能调优以及更好地利用Presto/Trino的特性。 