# 第19章：Presto/Trino Connector 机制 (Presto/Trino Connector Mechanism)

Presto/Trino的强大之处不仅在于其高效的MPP执行引擎，更在于其灵活的**Connector（连接器）**机制，这使得它能够"开箱即用"地查询各种异构数据源，并支持跨数据源的联邦查询。Connector是连接Presto/Trino引擎与外部数据世界的桥梁。本章将深入解析Connector的核心——**SPI（Service Provider Interface）**，重点介绍其关键接口，分析主流Connector的实现特点，并探讨开发自定义Connector的要点。

## 19.1 SPI (Service Provider Interface) 核心接口解析

SPI定义了一套标准的Java接口，任何想要被Presto/Trino查询的数据源都需要提供一个实现了这些接口的Connector插件。

**核心SPI接口:** 这些接口定义了Connector必须提供的核心功能，构成了引擎与数据源交互的基础。

1.  **`Connector`接口:**
    *   **作用:** 这是Connector实现的入口点，用于获取其他核心SPI组件的实例。
    *   **关键方法:**
        *   `getMetadata(...)`: 返回`ConnectorMetadata`实例。
        *   `getSplitManager()`: 返回`ConnectorSplitManager`实例。
        *   `getPageSourceProvider()` / `getRecordSetProvider()` (旧版): 返回`ConnectorPageSourceProvider` / `ConnectorRecordSetProvider`实例。
        *   `getConnectorCapabilities()`: 返回该Connector支持的能力列表（如下推优化等）。
        *   `shutdown()`: 关闭Connector，释放资源。

2.  **`ConnectorFactory`接口:**
    *   **作用:** 用于创建`Connector`实例。Presto/Trino通过Java的ServiceLoader机制发现并加载实现了`ConnectorFactory`的类。
    *   **关键方法:**
        *   `getName()`: 返回Connector的唯一名称（例如`hive`, `mysql`），用于配置文件中。
        *   `create(...)`: 根据配置信息创建并返回`Connector`实例。

**SPI的设计哲学:**
*   **面向接口编程:** 引擎核心代码依赖于SPI接口，而不是具体的Connector实现，实现了引擎与数据源的解耦。
*   **关注点分离:** 将与特定数据源交互的逻辑（元数据读取、数据分片、数据读取）封装在Connector内部。
*   **可插拔性:** 新的数据源支持可以通过开发新的Connector插件来添加，无需修改引擎核心代码。

## 19.2 Metadata API, Data Location API, Data Source API

`Connector`接口返回的几个核心组件分别对应了与数据源交互的不同方面：

### 19.2.1 元数据API (`ConnectorMetadata`)

*   **职责:** 提供关于数据源结构（Schema、Table、Column）的信息，以及执行DDL操作（如果支持）。
*   **关键方法示例:**
    *   `listSchemaNames(...)`: 列出所有可用的Schema（数据库名、库名）。
    *   `getTableHandle(...)`: 根据表名获取表的唯一句柄（`ConnectorTableHandle`），用于后续操作。
    *   `getTableMetadata(...)`: 获取表的元数据（列名、列类型等 - `ConnectorTableMetadata`）。
    *   `listTables(...)`: 列出指定Schema下的所有表名。
    *   `getColumnHandles(...)`: 获取表中所有列的句柄（`ColumnHandle`）。
    *   `getColumnMetadata(...)`: 获取指定列的元数据（`ColumnMetadata`）。
    *   `createTable(...)`, `dropTable(...)`, `renameTable(...)`, `addColumn(...)`等: 执行DDL操作（可选实现）。
    *   `getConnectorCapabilities()`: 返回Connector支持的元数据相关能力。
*   **重要性:** 查询规划（Analysis、Optimization）严重依赖`ConnectorMetadata`提供的信息来验证查询、解析标识符和进行优化（如下推）。

### 19.2.2 数据位置API / 分片管理 (`ConnectorSplitManager`)

*   **职责:** 将一个表（由`ConnectorTableHandle`标识）的数据划分成若干个**分片 (Split)**，并确定每个Split的处理位置（数据本地性信息）。Split是Presto/Trino并行处理数据的基本单元。
*   **关键方法:**
    *   `getSplits(...)`: 核心方法。输入表句柄、分区信息（`TupleDomain<ColumnHandle>`，用于分区裁剪）和约束（`Constraint`），输出一个`ConnectorSplitSource`。
    *   `ConnectorSplitSource`: 一个迭代器或流式的接口，用于获取属于该表的**所有** `ConnectorSplit`。每个`ConnectorSplit`代表一小部分数据。
*   **`ConnectorSplit` 接口:**
    *   **标记接口:** 本身没有方法，具体实现由Connector定义（例如`HiveSplit`包含文件路径、偏移量、长度、文件格式等）。
    *   **关键信息:** 包含足够的信息让`ConnectorPageSourceProvider`能够读取该分片的数据。
    *   **数据本地性 (Node Selection Strategy):** `ConnectorSplit`可以提供关于数据存储位置的提示（`NodeSelectionStrategy` - 如`HARD_AFFINITY`表示数据只在特定节点，`SOFT_AFFINITY`表示优先在某些节点），帮助Coordinator进行任务调度以优化本地读取。
*   **分区裁剪 (Partition Pruning):** `getSplits`方法接收`TupleDomain`参数，其中包含了从查询的`WHERE`子句推断出的分区列的约束。Connector应利用这些约束来**过滤掉不需要扫描的分区**对应的Split，这是性能优化的关键。

### 19.2.3 数据源API (`ConnectorPageSourceProvider` / `ConnectorRecordSetProvider`)

*   **职责:** 根据给定的`ConnectorSplit`和需要读取的列（`List<ColumnHandle>`），创建实际读取数据的执行组件。
*   **两种模式:**
    *   **`ConnectorPageSourceProvider` (推荐，面向列式Page):**
        *   `createPageSource(...)`: 返回一个`ConnectorPageSource`。
        *   `ConnectorPageSource`: 负责从Split中读取数据，并以**Page**对象（Presto/Trino内部的列式内存格式）的形式返回给引擎的`TableScanOperator`。这是与引擎列式执行模型最契合的方式，性能通常更好。
    *   **`ConnectorRecordSetProvider` (旧版，面向行式Record):**
        *   `getRecordSet(...)`: 返回一个`RecordSet`。
        *   `RecordSet`: 返回一个`RecordCursor`，`RecordCursor`按行迭代数据。引擎内部需要将行式数据转换为列式Page，有额外开销。
*   **谓词下推应用:** `createPageSource` / `getRecordSet`方法也可能接收`TupleDomain<ColumnHandle>`（非分区列的谓词），如果Connector有能力在读取数据时应用这些过滤条件（例如，利用数据源的索引、或者在解码时过滤），则可以在此实现，进一步减少返回给引擎的数据量。

**SPI交互流程总结 (查询 SELECT ... FROM table WHERE ...):**

1.  **Coordinator -> `ConnectorMetadata.getTableHandle/getTableMetadata/getColumnHandles`:** 获取表的元数据。
2.  **Coordinator -> `ConnectorSplitManager.getSplits` (传入分区谓词):** 获取表的数据分片列表，进行分区裁剪。
3.  **Coordinator -> (调度Task到Worker):** 将处理特定Split的Task分配给Worker，考虑Split提供的数据本地性信息。
4.  **Worker (Task) -> `ConnectorPageSourceProvider.createPageSource` (传入Split,所需列,非分区谓词):** 创建数据读取器。
5.  **Worker (Task) -> `ConnectorPageSource.getNextPage`:** 读取数据Page。
6.  **Worker (Engine):** 处理Page数据（过滤、投影、聚合、Join等）。

## 19.3 主流Connector实现分析 (Hive, Kafka, RDBMS等)

*   **Hive Connector:**
    *   **核心功能:** 查询存储在HDFS、S3等文件系统上的Hive表（ORC, Parquet, Avro, Text等格式）。
    *   **Metadata:** 通过与**Hive Metastore**服务交互来获取Schema、Table、Partition元数据。
    *   **Splits:** 通常一个HDFS Block或文件的一部分对应一个`HiveSplit`。利用分区信息（`TupleDomain`）进行分区裁剪，只生成需要扫描的分区的Split。
    *   **Data Source:** 根据文件格式（ORC, Parquet等）使用相应的**FileReader**（如`OrcPageSource`, `ParquetPageSource`）读取数据并生成Page。支持谓词下推到文件格式层面（如Parquet/ORC的Row Group/Stripe Skipping）。
    *   **关键优化:** 分区裁剪、文件格式层面的谓词/投影下推。

*   **RDBMS Connector (e.g., MySQL, PostgreSQL):**
    *   **核心功能:** 查询关系型数据库中的表。
    *   **Metadata:** 通过JDBC连接执行SQL（如`SHOW SCHEMAS`, `SHOW TABLES`, `DESCRIBE table`）或查询`information_schema`来获取元数据。
    *   **Splits:** 对于小表，可能只有一个Split。对于大表，可能根据主键、索引或数值列的范围来划分Split（例如，`WHERE id BETWEEN 1 AND 1000`为一个Split）。
    *   **Data Source:** 通过JDBC执行带有下推谓词、投影和Limit的SQL查询 (`SELECT col1, col2 FROM table WHERE filter LIMIT n`) 来获取数据，并将JDBC `ResultSet` 转换为Page。
    *   **关键优化:** 谓词下推（转换为SQL WHERE子句）、投影下推（SELECT子句）、Limit下推、聚合下推（部分聚合函数）、Join下推（如果配置启用且可行）。利用数据库自身的优化能力。

*   **Kafka Connector:**
    *   **核心功能:** 将Kafka Topic视为一张表进行查询（通常用于流批一体或实时ETL场景）。
    *   **Metadata:** 通常将Topic名称映射为表名。Schema可以通过配置、Schema Registry（如Confluent Schema Registry）或消息体自身结构（如JSON）推断。
    *   **Splits:** 一个Kafka Topic Partition通常对应一个`KafkaSplit`，包含Topic名、Partition ID、起始和结束Offset。
    *   **Data Source:** `KafkaPageSource`连接到Kafka Broker，从指定的Partition和Offset范围消费消息，根据定义的Schema和消息格式（JSON, Avro等）解码消息体并生成Page。
    *   **挑战:** Schema管理、消息解码、Exactly-Once语义（如果用于写入）。

## 19.4 Connector开发实践要点

开发自定义Connector以支持新的数据源时，需要注意以下几点：

1.  **理解SPI:** 深入理解`Connector`, `ConnectorFactory`, `ConnectorMetadata`, `ConnectorSplitManager`, `ConnectorPageSourceProvider`等核心接口及其职责。
2.  **元数据映射:** 设计好如何将外部数据源的库、表、列、类型映射到Presto/Trino的概念。
3.  **分片策略 (Splitting):** 设计合理的数据分片策略，目标是生成大小适中、数量合适、能够并行处理的Split。考虑如何利用分区或索引信息进行裁剪。
4.  **数据读取效率:** 实现高效的`ConnectorPageSource`，尽可能利用底层数据源的特性（如列式读取、过滤下推），并以列式Page格式返回数据。
5.  **类型处理:** 正确处理数据类型映射和转换，特别是复杂类型（Array, Map, Struct）和特殊类型（Date, Timestamp, Decimal）。
6.  **下推优化:** 尽可能多地实现各种下推优化（谓词、投影、Limit、聚合），将计算负载推到数据源，这是决定Connector性能的关键。
7.  **数据本地性:** 如果可能，在`ConnectorSplit`中提供准确的数据本地性信息，帮助调度器优化Task放置。
8.  **配置与部署:** 提供清晰的配置选项（如连接URL、认证信息等），并打包成标准插件部署到Presto/Trino集群。
9.  **错误处理与重试:** 实现健壮的错误处理逻辑。
10. **测试:** 编写全面的单元测试和集成测试，覆盖元数据、分片、数据读取和各种下推场景。

**总结:** Connector机制是Presto/Trino架构的基石，赋予其连接万物的能力。通过实现标准的SPI接口，特别是Metadata、Split Management和Data Source三大核心API，Connector将外部数据源无缝对接到Presto/Trino的分布式执行引擎中。主流Connector如Hive、RDBMS、Kafka等展示了不同的实现策略和优化重点。开发高质量的自定义Connector需要深入理解SPI、数据源特性以及各种下推优化技术，这对发挥Presto/Trino联邦查询和交互式分析的威力至关重要。 