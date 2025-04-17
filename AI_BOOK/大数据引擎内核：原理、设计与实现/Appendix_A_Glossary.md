# 附录A: 关键术语表 (Glossary)

**注意:** 本术语表旨在解释本书中使用的关键概念，定义可能根据上下文略有简化。

*   **ACID:** 数据库事务的四个关键属性：原子性 (Atomicity)、一致性 (Consistency)、隔离性 (Isolation)、持久性 (Durability)。数据湖表格式（如Delta Lake, Iceberg, Hudi）试图在数据湖上提供类似ACID的保证。
*   **Action (行动操作 - Spark):** 触发Spark作业执行的操作，例如 `count()`, `collect()`, `save()`, `foreach()`。与惰性求值的转换操作相对。
*   **Ad-hoc Query (即席查询):** 用户根据临时需求发起的、非预定义的查询，通常用于数据探索和快速分析。Presto/Trino擅长此类查询。
*   **Adaptive Query Execution (AQE - Spark):** Spark SQL的一种运行时优化机制，允许在执行过程中根据真实的中间数据统计信息调整执行计划，例如合并小分区、改变Join策略、处理倾斜。
*   **Aggregation (聚合):** 将多行数据汇总为单行或少量结果的操作，例如 `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `GROUP BY`。
*   **Apache Arrow:** 一种跨语言、跨平台的列式内存数据格式，旨在加速大数据系统之间的数据传输和处理。
*   **Apache Avro:** 一种数据序列化系统，基于Schema，常用于Hadoop生态和Kafka消息。
*   **Apache Calcite:** 一个开源的SQL解析、验证、优化和执行框架，被许多大数据项目（包括Flink Table API/SQL）用作查询处理的基础。
*   **Apache Hadoop:** 一个开源的分布式计算基础框架，核心组件包括HDFS（分布式文件系统）和YARN（资源管理器）。MapReduce是其早期的计算模型。
*   **Apache Hudi (Heard Under Data Incubation):** 一种数据湖存储格式，提供记录级别的插入、更新、删除能力，以及增量处理、快照隔离等特性。
*   **Apache Iceberg:** 由Netflix开发并开源的数据湖表格式，提供事务、Schema演进、时间旅行、分区演进、隐藏分区等强大功能，旨在解决Hive等传统数仓在数据湖上的局限性。
*   **Apache Kafka:** 一个分布式流处理平台，通常用作高吞吐量、可持久化的消息队列或流数据总线。
*   **Apache Parquet:** 一种开源的列式存储格式，广泛用于Hadoop生态系统，具有高效的压缩和编码方案，特别适合OLAP查询。
*   **Apache Pulsar:** 一个云原生的分布式消息流平台，提供多租户、跨地域复制等特性。
*   **Apache YARN (Yet Another Resource Negotiator):** Hadoop 2.x引入的资源管理系统，负责集群资源的分配和调度。Spark和Flink都可以运行在YARN上。
*   **Application Master (AM - YARN):** 在YARN中代表一个应用程序（如一个Spark作业或Flink会话）向ResourceManager申请资源，并与NodeManager协作启动和管理任务的组件。
*   **Asynchronous Barrier Snapshotting (异步屏障快照 - Flink):** Flink Checkpoint机制的核心算法。通过在数据流中注入特殊的Barrier，当算子接收到所有输入流的Barrier时，对其状态进行快照，实现分布式系统状态的一致性快照。
*   **At-Least-Once (至少一次):** 一种处理保证，确保每条记录至少被处理一次，但可能重复处理。通常比Exactly-Once更容易实现。
*   **Backpressure (反压):** 在数据流系统中，当下游消费者处理速度跟不上上游生产者时，下游向上游传递压力信号，要求上游减慢发送速率的机制，以防止系统崩溃或内存溢出。Flink有健壮的反压机制。
*   **Barrier (屏障 - Flink):** 在Flink的分布式快照算法中，由JobManager注入到数据流中的特殊标记，用于对齐算子状态进行快照。
*   **Barrier (屏障 - Spark):** 在Spark中，通常指Stage之间的执行依赖关系。后一个Stage必须等待前一个Stage完全结束后才能开始。AQE在Stage结束后利用中间结果信息进行优化。
*   **Batch Processing (批处理):** 一种数据处理模式，将数据收集成批（通常是大量数据），然后一次性处理整个批次。与流处理相对。Spark Core是典型的批处理引擎。
*   **Broadcast Join (广播Join):** 一种Join策略，将较小表的数据完整地复制（广播）到所有持有较大表分区的节点上，然后在本地执行Join。适用于一个表远小于另一个表的场景。Spark和Presto/Trino都支持。
*   **Buffer (缓冲):** 临时存储数据的内存区域，用于缓解生产者和消费者之间的速度不匹配、网络传输等。Flink的Network Buffer是其内存管理的关键部分。
*   **Cache / Persist (缓存/持久化 - Spark):** 将RDD或DataFrame/Dataset的计算结果存储在内存（或磁盘）中，以便后续快速重用，避免重复计算。
*   **CAP理论:** 分布式系统设计的基本定理，指出一个分布式系统无法同时满足一致性 (Consistency)、可用性 (Availability) 和分区容错性 (Partition tolerance) 这三个基本需求，最多只能满足其中两个。
*   **Catalyst Optimizer (Spark):** Spark SQL的核心优化器，基于规则和成本进行多阶段优化，并将逻辑计划转换为物理执行计划，包含Whole-Stage Code Generation。
*   **Checkpointing (检查点):** 在流处理或长时间运行的批处理中，周期性地将系统状态（算子状态、数据源偏移量等）持久化到可靠存储的过程，用于故障恢复。Flink的核心容错机制。Spark Structured Streaming也使用Checkpointing。
*   **ClickHouse:** 一个开源的高性能列式OLAP数据库管理系统，以其极快的查询速度著称。
*   **Client (客户端):** 向大数据引擎提交作业或查询的用户程序或接口。
*   **Cloud-Native (云原生):** 指应用在设计、构建和运行时充分利用云计算优势（弹性、分布式、自动化等）的架构和方法论。
*   **Cluster Manager (集群管理器):** 负责管理集群资源（节点、CPU、内存）并为应用程序分配资源的系统，例如 YARN, Kubernetes, Mesos, Spark Standalone。
*   **Code Generation (Codegen - Spark/Impala/StarRocks):** 一种优化技术，将查询计划的一部分（特别是CPU密集型操作）动态编译成高效的底层代码（如JVM字节码或本地机器码），以减少虚函数调用开销、提高CPU缓存利用率。Spark的Whole-Stage Code Generation是其典型应用。
*   **Columnar Storage (列式存储):** 一种数据存储方式，将同一列的数据连续存储在一起，而不是按行存储。非常适合分析型查询，因为查询通常只涉及少量列。例如 Parquet, ORC, ClickHouse。
*   **Connector (连接器 - Presto/Trino/Flink/Spark):** 用于连接和访问外部数据源的插件或模块。Presto/Trino的强大之处在于其丰富的Connector生态。
*   **Container (容器 - YARN/Docker/K8s):** 由资源管理器分配的资源单元（包含CPU、内存、磁盘等），用于运行应用程序的组件（如Spark Executor, Flink TaskManager）。
*   **Continuous Processing (连续处理 - Flink/Spark):** 一种流处理模式，旨在实现逐条记录的最低延迟处理。Flink是典型的连续处理引擎。Spark也曾尝试过低延迟的连续处理模式（已弃用）。
*   **Coordinator (协调器 - Presto/Trino):** 负责接收客户端查询、解析、优化、生成执行计划，并将任务分发给Worker节点执行，最后汇总结果返回给客户端。类似于Spark Driver或Flink JobManager的角色，但更侧重SQL查询。
*   **Cost-Based Optimization (CBO - 基于成本的优化):** 一种查询优化策略，通过估算不同执行计划的成本（基于数据的统计信息），选择成本最低的计划。与RBO相对。
*   **Credit-based Flow Control (基于信用的流控 - Flink):** Flink网络层使用的一种流控机制，下游消费者向上游生产者授予"信用"（表示可以接收多少数据），避免下游Buffer溢出。
*   **DAG (Directed Acyclic Graph - 有向无环图):** 一种数据结构，用于表示计算任务之间的依赖关系，其中节点代表操作（或数据），边代表数据流或依赖，且图中没有循环。Tez, Spark, Flink都使用DAG来表示作业。
*   **Data Federation (数据联邦):** 在不移动数据的情况下，通过一个统一的接口查询存储在多个异构数据源中的数据的能力。Presto/Trino是典型的数据联邦查询引擎。
*   **Data Lake (数据湖):** 一个集中式的存储库，允许以任意规模存储所有结构化和非结构化数据。通常基于廉价的对象存储（如S3, HDFS）。
*   **Data Lakehouse (湖仓一体):** 一种新的数据管理范式，试图将数据湖的灵活性与数据仓库的管理特性（事务、Schema管理、查询性能）结合起来，通常依赖于开放表格式（Delta Lake, Iceberg, Hudi）。
*   **Data Locality (数据本地性):** 计算任务尽可能在存储其所需数据的节点上执行的原则，以减少网络传输开销。MapReduce, Spark, Impala等都考虑数据本地性。
*   **Data Skew (数据倾斜):** 在分布式计算中，由于数据分布不均，导致少数Task处理了远超其他Task的数据量，成为整个作业的瓶颈。
*   **Data Source API (数据源API - Spark/Flink/Presto):** 引擎提供的用于读写外部数据源的标准接口。
*   **Data Stream (数据流 - Flink):** Flink核心API中的基本抽象，代表一个无限或有限的数据记录序列。
*   **Data Warehouse (数据仓库):** 一个用于报告和数据分析的系统，通常存储来自一个或多个不同来源的集成数据，数据经过清洗、转换和结构化。
*   **DataFrame / Dataset (Spark):** Spark SQL提供的分布式数据集抽象，带有Schema信息，提供了比RDD更高级、更优化的API。Dataset是类型安全的DataFrame。
*   **Delta Lake:** 由Databricks开发并开源的数据湖表格式，在Parquet基础上增加了事务日志，提供ACID事务、时间旅行等功能。
*   **Dispatcher (分发器 - Flink):** Flink集群的入口点，负责接收作业提交，启动JobManager，并提供REST接口用于监控和管理。
*   **Distributed Snapshotting (分布式快照 - Flink):** Flink容错机制的核心思想，通过一致性地保存所有相关组件的状态来创建全局一致的时间点快照。
*   **Driver (驱动器 - Spark):** Spark应用程序的中心协调进程，负责解析用户代码、生成逻辑和物理计划、调度Task到Executor上执行。
*   **Dynamic Partition Pruning (动态分区裁剪 - Spark/Presto):** 一种优化技术，在查询运行时，利用一个表（通常是维度表）的过滤结果来裁剪另一个表（通常是事实表）需要扫描的分区。
*   **Eager Evaluation (急切求值):** 计算操作一旦定义就立即执行。与Lazy Evaluation相对。
*   **Eager Scheduling (急切调度 - Flink):** Flink的一种调度策略，作业启动时就为所有Task申请资源并尝试部署。
*   **ETL (Extract, Transform, Load - 抽取、转换、加载):** 数据处理的常见流程，从源系统提取数据，进行清洗、转换、聚合等操作，然后加载到目标系统（如数据仓库）。
*   **Event Time (事件时间 - Flink/Spark):** 数据记录实际发生的时间，通常嵌入在记录本身。流处理中处理乱序和延迟数据的关键概念。与Processing Time相对。
*   **Exactly-Once (精确一次):** 一种最强的处理保证，确保每条记录都被处理一次且仅一次，即使在发生故障的情况下。实现复杂度最高。Flink的核心目标之一。
*   **Exchange Operator (Presto/Trino):** 在Presto/Trino中负责处理Stage之间数据传输（Shuffle）的算子。
*   **Execution Graph (执行图 - Flink):** Flink作业在运行时的物理执行图，由JobGraph转换而来，包含了具体的并行实例（Subtask）和任务部署信息。
*   **Executor (执行器 - Spark):** 在Worker节点上运行的Spark进程，负责执行Driver分配的Task，并将结果返回给Driver。
*   **Fault Tolerance (容错):** 系统在部分组件发生故障时仍能继续运行并产生正确结果的能力。
*   **Federated Query (联邦查询):** 见 Data Federation。
*   **Filter (过滤):** 根据指定条件筛选数据的操作，例如SQL中的 `WHERE` 子句。
*   **FPGA (Field-Programmable Gate Array - 现场可编程门阵列):** 一种可以被用户或设计者在制造后重新配置逻辑功能的集成电路，可用于加速特定计算任务。
*   **Garbage Collection (GC - 垃圾回收):** JVM自动管理内存的过程，回收不再使用的对象所占用的内存。GC暂停是影响Java应用（包括大数据引擎）性能和稳定性的重要因素。
*   **GPU (Graphics Processing Unit - 图形处理器):** 最初为图形渲染设计，但其大规模并行计算能力使其非常适合加速科学计算、机器学习和部分大数据处理任务。
*   **Graph Processing (图计算):** 针对图结构数据（节点和边）进行分析和处理的技术。Spark GraphX是例子。
*   **Hash Join:** 一种Join实现算法，对其中一个（较小的）表构建哈希表，然后扫描另一个表，用哈希表进行快速匹配。
*   **Hash Partitioning (哈希分区):** 一种数据分区方法，根据记录的Key的哈希值将其分配到不同的分区。Shuffle常用。
*   **High Availability (HA - 高可用):** 系统设计的目标，旨在确保系统在面临故障时能够持续提供服务，通常通过冗余和快速故障切换实现。例如Flink JobManager HA, HDFS NameNode HA。
*   **Hive Metastore:** Apache Hive用于存储表元数据（Schema、分区信息、数据位置等）的服务。被Spark, Flink, Presto/Trino等广泛用于管理数据湖和数据仓库的元数据。
*   **Idempotent (幂等):** 指一个操作执行一次和执行多次产生的效果是相同的。幂等操作对于实现At-Least-Once或Exactly-Once语义非常重要。
*   **Impala:** 由Cloudera开发的MPP SQL查询引擎，主要用于Hadoop环境，以低延迟著称，用C++编写。
*   **In-Memory Computing (内存计算):** 将数据尽可能加载到内存中进行处理，以获得比基于磁盘的计算更高的性能。Spark的核心理念之一。
*   **Interactive Query (交互式查询):** 用户可以快速提交查询并期望在短时间内（秒级）获得结果的查询模式。Presto/Trino的设计目标。
*   **JDBC (Java Database Connectivity):** Java连接数据库的标准API。大数据引擎通常提供JDBC接口供外部工具连接。
*   **Job (作业):** 用户提交给大数据引擎执行的一个完整的计算任务。
*   **JobGraph (作业图 - Flink):** 由StreamGraph优化后生成的逻辑执行图，包含了算子链合并、并行度设置等信息，提交给JobManager执行。
*   **JobManager (作业管理器 - Flink):** Flink集群的主节点（Master），负责接收作业提交、协调Checkpoint、管理TaskManager、监控作业执行。
*   **Join (连接):** 将两个或多个数据集中具有共同字段的行组合起来的操作。是关系代数和SQL的核心操作。
*   **Keyed State (键控状态 - Flink):** 在Flink中，与特定Key关联的状态。只有KeyedStream上的操作才能访问Keyed State。例如 `ValueState`, `MapState`。
*   **Kubernetes (K8s):** 一个开源的容器编排系统，用于自动化容器化应用程序的部署、扩展和管理。Spark和Flink都原生支持在Kubernetes上运行。
*   **Kryo:** 一个快速、高效的Java序列化库，Spark在内部广泛使用。
*   **Lakehouse:** 见 Data Lakehouse。
*   **Latency (延迟):** 从请求发起（或事件发生）到收到响应（或处理完成）所经过的时间。低延迟是流处理和交互式查询的重要目标。
*   **Lazy Evaluation (惰性求值 - Spark):** Spark中的转换操作（Transformations）不会立即执行，而是构建一个执行计划（Lineage）。只有当遇到行动操作（Actions）时才触发实际计算。
*   **Lineage (血缘 - Spark):** RDD记录其如何从父RDD转换而来的依赖关系图。Spark利用Lineage进行容错（重计算丢失的分区）。
*   **Load Balancing (负载均衡):** 将工作负载（如查询、任务）均匀分布到多个计算资源（如节点、Task）上，以避免单点过载，提高整体吞吐量和资源利用率。
*   **Logical Plan (逻辑计划):** 查询或数据处理流程的高层、抽象表示，独立于具体的物理执行细节。优化器首先对逻辑计划进行优化。
*   **Machine Learning (ML - 机器学习):** 人工智能的一个分支，使计算机系统能够从数据中学习并改进性能，而无需显式编程。Spark MLlib是大数据领域的常用ML库。
*   **Map (映射):** 函数式编程概念，对数据集中的每个元素应用一个函数，生成一个新的数据集。MapReduce和Spark中的核心操作。
*   **MapReduce:** Google提出的分布式计算编程模型和框架，包含Map和Reduce两个主要阶段。是早期大数据处理的事实标准。
*   **Massively Parallel Processing (MPP - 大规模并行处理):** 一种分布式计算架构，通常用于数据仓库和分析数据库，将数据分布到多个节点上，并通过节点间的并行处理和高速互连来执行查询。Presto/Trino, Impala, Greenplum, Teradata等都属于MPP架构。
*   **Master (主节点):** 分布式系统中的中心协调节点，负责管理集群资源、调度任务、维护元数据等。例如Spark Driver, Flink JobManager, HDFS NameNode。
*   **Memory Pool (内存池 - Presto/Trino/Flink):** 预先分配和管理的内存区域，用于特定的目的（如查询执行、网络缓冲），以提高内存分配效率和控制内存使用。
*   **Memory Segment (内存段 - Flink):** Flink内存管理的基本单位，通常是固定大小的堆外内存块，用于网络缓冲、排序、哈希表等。
*   **Metadata (元数据):** 描述数据的数据。例如表的Schema、分区信息、文件位置、统计信息等。Hive Metastore是常见的元数据存储。
*   **Micro-Batch Processing (微批处理 - Spark Structured Streaming):** 一种模拟流处理的方法，将连续的数据流切分成一系列非常小的批次，然后使用批处理引擎逐个处理这些微批。
*   **Narrow Dependency (窄依赖 - Spark):** 父RDD的每个分区最多只被子RDD的一个分区依赖的依赖关系。例如 `map`, `filter`。窄依赖允许流水线执行。与Wide Dependency相对。
*   **Network Buffer (网络缓冲 - Flink):** Flink用于在Task之间进行网络数据传输的内存缓冲，通常使用堆外内存，是Flink高性能低延迟的关键。
*   **Node Manager (节点管理器 - YARN):** YARN集群中每个Worker节点上的代理，负责启动和管理该节点上的Container，并向ResourceManager汇报节点状态。
*   **Off-Heap Memory (堆外内存):** 直接由应用程序（或库）管理、不受JVM GC直接管理的内存。优点是可以避免GC暂停，存储更大的数据量。Spark, Flink, Presto/Trino都支持或大量使用堆外内存。
*   **OLAP (Online Analytical Processing - 在线分析处理):** 一类主要用于支持商业智能和决策支持的查询，通常涉及对大量历史数据进行复杂的聚合、切片、钻取等操作。ClickHouse是典型的OLAP引擎。
*   **OLTP (Online Transaction Processing - 在线事务处理):** 一类主要用于支持日常业务操作的应用程序，特点是短时间、高并发的读写事务。例如银行交易系统。
*   **On-Heap Memory (堆内内存):** 由JVM管理的内存区域（Java堆），对象的创建和回收由GC负责。
*   **Operator (算子 - Flink/Presto/Trino):** 数据处理流程中的一个基本计算单元，执行特定的操作，如 `map`, `filter`, `join`, `aggregate`。
*   **Operator Chain (算子链 - Flink):** Flink优化技术，将可以连续执行的多个算子（通常是窄依赖）链接在一起，在同一个线程和Task Slot中执行，以减少线程切换、数据序列化和网络传输开销。
*   **Operator State (算子状态 - Flink):** 与算子并行实例绑定的状态，例如Kafka Connector中记录每个并行实例消费的Offset。与Keyed State相对。
*   **ORC (Optimized Row Columnar):** 另一种流行的开源列式存储格式，由Hortonworks发起，也广泛用于Hadoop生态。
*   **Page (页 - Presto/Trino):** Presto/Trino在内存中处理和传输数据的基本单位，是按列组织的内存块。
*   **Parallelism (并行度):** 一个操作或作业同时执行的实例数量。调整并行度是性能调优的关键手段。
*   **Partition (分区):** 将大数据集划分成更小、更易管理的部分。分区可以在存储层（如Hive分区表）或计算层（如RDD/DataFrame分区，Kafka分区）进行。分区是实现并行处理的基础。
*   **Partition Pruning (分区裁剪):** 查询优化技术，根据查询条件（如 `WHERE` 子句中的分区键过滤）只读取所需的分区数据，避免扫描不相关的数据。
*   **Physical Plan (物理计划):** 查询或作业如何在分布式集群上具体执行的计划，包含了具体的算子实现（如HashJoin vs SortMergeJoin）、数据传输方式（Shuffle）、并行度等细节。由逻辑计划转换而来。
*   **Pipeline / Pipelining (流水线):** 一种执行模式，一个操作的输出直接作为下一个操作的输入，无需等待前一个操作处理完所有数据。可以显著降低延迟。Flink和Presto/Trino的核心执行机制。
*   **Pod (K8s):** Kubernetes中可以创建和管理的、最小的可部署的计算单元。一个Pod包含一个或多个容器。
*   **Predicate (谓词):** 返回布尔值的条件表达式，通常用于数据过滤（如 `WHERE` 子句）。
*   **Predicate Pushdown (谓词下推):** 查询优化技术，将过滤条件（谓词）尽可能地下推到靠近数据源的位置执行，以尽早减少需要处理的数据量。
*   **Processing Time (处理时间 - Flink/Spark):** 数据记录被处理引擎处理的时间。与Event Time相对。处理时间易于实现，但无法保证结果的确定性（受系统负载、网络延迟等影响）。
*   **Projection (投影):** 选择数据集中特定列的操作，例如SQL中的 `SELECT col1, col2`。
*   **Projection Pushdown / Column Pruning (投影下推/列裁剪):** 查询优化技术，只读取查询所需的列，避免读取不必要的列数据。列式存储格式（Parquet, ORC）使得这种优化非常有效。
*   **Push-based Shuffle (推送式Shuffle - Flink):** Flink默认的Shuffle方式，上游Task将数据主动推送到下游Task的网络缓冲区。与Pull-based Shuffle相对。
*   **Pull-based Shuffle (拉取式Shuffle - Spark/Presto):** 下游Task主动向上游Task（或Shuffle Service）拉取所需的数据。
*   **Query Queuing (查询排队 - Presto/Trino):** 当系统负载过高或资源不足时，将新接收的查询放入队列中等待执行的机制，通常通过Resource Group实现。
*   **Range Partitioning (范围分区):** 根据记录Key的范围将其分配到不同分区的分区方法。
*   **RDD (Resilient Distributed Dataset - 弹性分布式数据集 - Spark):** Spark早期核心的数据抽象，一个不可变、可分区、可并行计算的分布式对象集合。支持Lineage和容错。
*   **Reduce (规约):** 函数式编程概念，将数据集中的所有元素通过一个函数聚合成一个单一的值（或少量值）。MapReduce和Spark中的核心操作。
*   **Replayable Source (可重放数据源 - Flink):** 指可以从某个指定的偏移量或时间点重新读取数据的数据源，例如Kafka。这是实现Exactly-Once语义的关键。
*   **Resource Group (资源组 - Presto/Trino):** 用于管理查询资源（并发度、内存、CPU）和调度策略（排队、优先级）的机制，主要用于多租户环境。
*   **Resource Manager (资源管理器 - YARN/Flink):** 负责管理集群资源（节点、Slot）并接受应用程序（如JobManager）的资源请求的组件。
*   **Revocable Memory (可回收内存 - Presto/Trino):** Presto/Trino内存池的一部分，主要用于支持Spill to Disk的算子。在内存不足时，这部分内存可以被回收（通过将数据溢出到磁盘）。
*   **RocksDB:** 一个高性能的嵌入式键值存储库，由Facebook开发。Flink使用RocksDB作为其最常用的状态后端，支持存储远超内存容量的状态。Spark的基于磁盘的State Store也可用RocksDB。
*   **Rolling Window (滚动窗口):** 一种窗口类型，将时间或数据流切分成固定大小、不重叠的片段。
*   **RowSet (行集 - Presto):** Presto早期版本中内存数据表示的一种方式，后来逐渐被基于Page的列式表示取代。
*   **Rule-Based Optimization (RBO - 基于规则的优化):** 一种查询优化策略，应用一系列预定义的、启发式的规则来转换执行计划，使其等价且通常更优。不考虑数据的实际分布。
*   **Savepoint (保存点 - Flink):** 由用户手动触发的、用于备份和恢复Flink作业状态的一致性快照。与自动触发的Checkpoint类似，但通常用于计划性的作业升级、迁移或归档。
*   **Scalability (可扩展性):** 系统通过增加资源（如节点、CPU、内存）来提升处理能力或容量的能力。水平扩展（增加节点）是分布式系统的关键优势。
*   **Schema (模式):** 数据的结构定义，描述了数据包含哪些字段、字段的类型以及它们之间的关系。
*   **Schema Evolution (模式演进):** 在数据生命周期中修改数据模式（例如添加、删除、重命名列）的能力，同时保持对旧数据的兼容性。数据湖表格式（Iceberg, Delta Lake, Hudi）的重要特性。
*   **Scheduler (调度器):** 负责将任务分配给可用资源的组件。例如Spark TaskScheduler, Flink Scheduler, Presto NodeScheduler。
*   **SerDe (Serializer/Deserializer - 序列化/反序列化器):** 用于将内存中的对象转换为字节流（序列化）以便存储或传输，以及将字节流转换回对象（反序列化）的组件。
*   **Serialization (序列化):** 将数据结构或对象状态转换为可以存储或传输的格式（如字节流、JSON、XML）的过程。
*   **Serverless (无服务器):** 一种云计算执行模型，云提供商动态管理计算资源的分配和供应，用户无需管理服务器。
*   **Session Window (会话窗口):** 一种窗口类型，根据活动的间隙对数据进行分组，将没有超过指定非活动间隔的事件分到同一个窗口。
*   **Shuffle (混洗):** 在分布式计算中，重新分发数据以便将具有相同Key或满足特定分区要求的数据聚集到一起进行后续处理的过程。通常涉及大量的磁盘I/O和网络传输，是性能瓶颈点。
*   **Shuffle Sort:** Spark常用的Shuffle Write策略，在将数据写入磁盘前先按分区ID和Key进行排序，以便后续高效读取和合并。
*   **SIMD (Single Instruction, Multiple Data):** CPU指令集的一种类型，允许一条指令同时对多个数据执行相同的操作。向量化执行引擎（如ClickHouse）利用SIMD来加速计算。
*   **Sink (汇 - Flink/Spark Streaming):** 数据处理流程的终点，将处理结果写入外部系统（如数据库、文件系统、消息队列）。
*   **Skew Join Optimization (倾斜Join优化 - Spark AQE):** AQE处理Join数据倾斜的一种技术，将倾斜的Key对应的数据单独拆分出来进行处理。
*   **Sliding Window (滑动窗口):** 一种窗口类型，窗口按指定的步长（Slide）在时间或数据流上滑动，窗口之间可以重叠。
*   **Slot Sharing (槽共享 - Flink):** Flink允许来自**同一个作业**的不同算子的Task共享同一个Task Slot，以提高资源利用率。
*   **Sort Merge Join:** 一种Join实现算法，首先将两个需要Join的表按Join Key排序，然后通过一次归并扫描即可完成Join操作。
*   **Source (源 - Flink/Spark Streaming):** 数据处理流程的起点，从外部系统（如消息队列、文件系统）读取数据。
*   **Speculative Execution (推测执行 - Spark/MapReduce/Flink Batch):** 当某个Task运行特别慢（可能是由于硬件问题、数据倾斜等）时，系统在另一个节点上启动一个相同的备份Task，哪个先完成就采用其结果，并杀掉另一个。
*   **Spill to Disk (溢出到磁盘):** 当内存不足以容纳操作所需的数据（如大型Hash表、排序缓冲）时，将部分数据临时写入磁盘，之后再读回处理。会降低性能，但能防止OOM。Spark和Presto/Trino在某些操作中支持Spill。
*   **Split (分片 - Presto/Trino/MapReduce):** 输入数据的一个逻辑块，通常是Task处理的基本单元。例如HDFS文件的一个块或Hive表的一个分区文件的一部分。
*   **SQL (Structured Query Language - 结构化查询语言):** 用于管理和查询关系数据库的标准语言。Spark SQL, Flink SQL, Presto/Trino都提供SQL接口。
*   **Stage (阶段 - Spark/Presto/Trino):** 作业执行过程中的一个计算阶段。在Spark中，Stage由一组可以并行执行且没有Shuffle依赖的Task组成，Stage之间通过Shuffle连接。在Presto/Trino中，Stage是一组可以在Worker上并行执行的任务，Stage之间通过Exchange Operator连接并流水线执行。
*   **State (状态 - Flink/Spark Streaming):** 在流处理中，算子需要记住的、跨多条输入记录的信息。例如窗口聚合的中间结果、去重操作的已见元素集合等。状态管理是流处理的核心挑战。
*   **State Backend (状态后端 - Flink):** Flink用于存储和管理算子状态的组件，决定了状态存储的位置（内存、文件系统、RocksDB）和Checkpoint的方式。
*   **Stream Processing (流处理):** 一种数据处理模式，对到达的数据进行实时或近实时的处理，通常处理的是无界的、连续的数据流。Flink是典型的流处理引擎。
*   **StreamGraph (流图 - Flink):** Flink作业通过API调用直接生成的最初的逻辑图，表示了算子和数据流向。
*   **Structured Streaming (Spark):** Spark 2.x 引入的基于Spark SQL引擎构建的可扩展、容错的流处理框架，采用Micro-Batch或Continuous Processing（实验性）模型。
*   **Subtask (子任务 - Flink):** Flink中Task的并行实例，是实际在TaskManager的Slot中执行的单元。一个算子的并行度决定了它有多少个Subtask。
*   **Table API (Flink/Spark):** 提供了类似于关系型数据库表的声明式API，比底层的DataStream或RDD API更易用，并且可以被优化器优化。
*   **Task (任务):** 作业执行的基本工作单元。在Spark中，Task在Executor上执行，处理RDD的一个分区。在Flink中，Task（由多个Subtask组成）在TaskManager的Slot中执行。在Presto/Trino中，Task在Worker上执行，处理一个或多个Split。
*   **Task Manager (任务管理器 - Flink):** Flink集群的工作节点（Worker），负责执行JobManager分配的Task（Subtask），管理Task Slot和网络缓冲。
*   **Task Slot (任务槽 - Flink):** TaskManager提供的用于执行Task（Subtask）的资源单元。是Flink资源调度的基本单位。
*   **Tez:** Apache Tez是一个通用的数据处理框架，提供了比MapReduce更灵活的DAG执行模型，常被用作Hive和Pig的执行引擎。
*   **Throughput (吞吐量):** 系统在单位时间内能够处理的数据量或完成的任务数。高吞吐量是批处理引擎的重要目标。
*   **Time Semantics (时间语义 - Flink/Spark):** 定义流处理中"时间"的含义，主要有Event Time（事件发生时间）和Processing Time（系统处理时间）。
*   **Time Travel (时间旅行):** 数据湖表格式（Delta Lake, Iceberg）提供的一种能力，允许用户查询表的历史版本（某个时间点或某个事务ID的状态）。
*   **Transaction (事务):** 一系列操作，要么全部成功执行，要么全部失败回滚，以保证数据的一致性。ACID是事务的关键属性。
*   **Transformation (转换操作 - Spark):** 对RDD或DataFrame/Dataset进行操作并生成新的RDD/DataFrame/Dataset的操作，例如 `map`, `filter`, `join`。转换操作是惰性求值的。
*   **Trigger (触发器 - Flink):** 在Flink窗口操作中，决定窗口何时计算并输出结果的组件。
*   **Tungsten (Spark):** Spark的一个优化项目，旨在通过显式内存管理（堆外内存）、二进制处理（避免序列化开销）和代码生成等技术，大幅提升Spark的内存和CPU效率。
*   **Vectorization / Vectorized Execution (向量化执行):** 一种CPU密集型计算的优化技术，操作按列向量而不是单行进行处理，以更好地利用CPU缓存和SIMD指令。ClickHouse, Presto/Trino, Spark (部分通过Codegen和Arrow) 都采用了向量化技术。
*   **Watermark (水位线 - Flink/Spark):** 在基于事件时间的流处理中，用于表示事件时间进展的一种机制或标记。系统认为不会再有时间戳早于Watermark的"迟到"数据到达，从而可以安全地触发窗口计算。
*   **Wide Dependency / Shuffle Dependency (宽依赖/Shuffle依赖 - Spark):** 父RDD的一个分区被子RDD的多个分区依赖的依赖关系，例如 `groupByKey`, `reduceByKey`, `join` (当没有预分区时)。宽依赖通常需要Shuffle操作。
*   **Window (窗口):** 在流处理中，将无界数据流切分成有界块（基于时间或数量）进行处理的技术。常见的窗口类型有滚动窗口、滑动窗口、会话窗口。
*   **Worker (工作节点):** 分布式系统中的计算节点，负责执行Master分配的任务。例如Spark Executor所在的节点, Flink TaskManager, Presto/Trino Worker。
*   **Whole-Stage Code Generation (WSCG - Spark):** Spark Catalyst优化器的一项关键技术，将一个Stage内的多个物理算子尽可能地融合（Fuse）在一起，并为整个融合后的代码生成单一优化的Java字节码函数，极大减少了虚函数调用和中间数据在内存中的读写开销。
*   **Z-Ordering:** 一种多维空间填充曲线技术，可用于优化数据布局，将多维空间中距离相近的点映射到一维空间中也尽可能相邻的位置，从而提高基于多列过滤查询的性能。Delta Lake等表格式支持Z-Ordering。 