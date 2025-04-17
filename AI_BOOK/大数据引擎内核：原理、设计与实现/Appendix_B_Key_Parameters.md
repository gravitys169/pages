# 附录B: 主要配置参数解读 (Key Configuration Parameters)

**注意:** 以下列表并非详尽无遗，仅列出部分对性能、资源、行为影响较大的常用配置参数。具体参数和默认值可能随引擎版本变化，请参考官方文档。

## Spark

### 资源与执行内存 (Resource & Execution Memory)
*   `spark.driver.memory`: Driver进程内存大小。
*   `spark.driver.cores`: Driver进程使用的CPU核心数 (Standalone/K8s模式)。
*   `spark.executor.memory`: 每个Executor进程的内存大小。
*   `spark.executor.cores`: 每个Executor进程使用的CPU核心数。
*   `spark.executor.instances`: (可选) 初始或固定启动的Executor数量。
*   `spark.dynamicAllocation.enabled`: 是否启用动态资源分配 (自动增减Executor)。
*   `spark.dynamicAllocation.minExecutors`: 动态分配时最小Executor数。
*   `spark.dynamicAllocation.maxExecutors`: 动态分配时最大Executor数。
*   `spark.memory.fraction`: (统一内存管理) 用于执行内存和存储内存的总内存在JVM堆中的比例 (默认0.6)。
*   `spark.memory.storageFraction`: (统一内存管理) 分配给存储内存的比例 (相对于`spark.memory.fraction`部分，默认0.5)。执行内存和存储内存可相互借用。
*   `spark.memory.offHeap.enabled`: 是否启用堆外内存。
*   `spark.memory.offHeap.size`: 堆外内存的大小 (字节)。

### Shuffle相关
*   `spark.shuffle.service.enabled`: 是否启用External Shuffle Service (ESS)。在YARN/K8s上强烈推荐启用，支持动态伸缩。
*   `spark.shuffle.manager`: Shuffle管理器类型 (默认`sort`)。
*   `spark.shuffle.sort.bypassMergeThreshold`: 分区数小于此阈值时，对于无Map端聚合的Shuffle，可以绕过排序，提高效率。
*   `spark.sql.shuffle.partitions`: Spark SQL中Shuffle操作（如Join, Aggregation）的默认分区数。非常关键的性能参数，需要根据数据量和集群规模调整。

### SQL与AQE
*   `spark.sql.autoBroadcastJoinThreshold`: 小于此大小（字节）的表在Join时会自动执行Broadcast Join (默认10MB)。设置为-1禁用。
*   `spark.sql.adaptive.enabled`: 是否启用AQE (Adaptive Query Execution)。(Spark 3.0+ 默认通常为true)
*   `spark.sql.adaptive.coalescePartitions.enabled`: AQE是否启用动态合并Shuffle分区。
*   `spark.sql.adaptive.skewJoin.enabled`: AQE是否启用倾斜Join优化。
*   `spark.sql.codegen.wholeStage`: 是否启用Whole-Stage Code Generation。

### Structured Streaming
*   `spark.sql.streaming.checkpointLocation`: Structured Streaming Checkpoint的存储路径。
*   `spark.sql.streaming.minBatchesToRetain`: 保留的最小完成批次数 (用于容错和元数据清理)。

## Flink

### 资源与内存 (Resource & Memory)
*   `jobmanager.memory.process.size`: JobManager进程总内存大小。
*   `taskmanager.memory.process.size`: TaskManager进程总内存大小 (推荐配置此项，Flink会自动推导其他内存部分)。
*   `taskmanager.numberOfTaskSlots`: 每个TaskManager提供的Task Slot数量 (通常配置为CPU核数)。
*   `jobmanager.execution.failover-strategy`: 作业失败恢复策略 (如`region` - 推荐, `full`)。
*   `execution.attached`: 作业是否附加到提交客户端 (影响客户端退出时作业的行为)。

### Checkpoint与状态 (Checkpoint & State)
*   `execution.checkpointing.interval`: Checkpoint的时间间隔。
*   `execution.checkpointing.mode`: Checkpoint模式 (默认 `EXACTLY_ONCE`)。
*   `execution.checkpointing.timeout`: Checkpoint允许的最大超时时间。
*   `execution.checkpointing.max-concurrent-checkpoints`: 允许同时进行的Checkpoint数量 (默认1)。
*   `state.backend`: 状态后端的类型 (如 `hashmap` - Memory, `filesystem` - FS, `rocksdb`)。
*   `state.checkpoints.dir`: Checkpoint数据持久化的目录 (必需，如 `hdfs:///flink/checkpoints` 或 `s3://...`)。
*   `state.backend.rocksdb.localdir`: RocksDB状态后端存储本地文件的目录。
*   `state.backend.rocksdb.memory.managed`: 是否让Flink管理RocksDB的内存 (推荐true)。

### 网络与Shuffle (Networking & Shuffle)
*   `taskmanager.memory.network.fraction`: TaskManager总进程内存中用于网络缓冲的比例。
*   `taskmanager.memory.network.min`: 网络缓冲的最小内存。
*   `taskmanager.memory.network.max`: 网络缓冲的最大内存。
*   `taskmanager.network.blocking-shuffle.type`: 批处理Blocking Shuffle使用的类型 (如 `file`, `yarn`)。

### Table API/SQL
*   `table.optimizer.join-reorder-enabled`: 是否启用Join Reorder优化。
*   `table.optimizer.agg-phase-strategy`: 聚合策略 (如 `AUTO`, `TWO_PHASE`, `ONE_PHASE`)。
*   `table.exec.source.idle-timeout`: 源空闲超时时间 (用于Watermark生成等)。

## Presto/Trino

### Coordinator配置 (`config.properties`)
*   `query.max-memory`: 单个查询在整个集群中允许使用的最大**用户内存** (如`50GB`)。关键防OOM参数。
*   `query.max-total-memory`: 单个查询在整个集群中允许使用的最大**总内存** (用户+系统内存)。
*   `query.max-memory-per-node`: 单个查询在**单个Worker节点**上允许使用的最大用户内存 (如`1GB`)。
*   `query.max-history`: 保留的查询历史记录数量。
*   `query.queue-config-file`: 查询队列(Resource Group)配置文件的路径。
*   `optimizer.join-reordering-strategy`: CBO Join重排序策略 (如 `AUTOMATIC`, `ELDER`, `NONE`)。
*   `optimizer.join-distribution-type`: CBO Join分布类型选择策略 (如 `AUTOMATIC`, `PARTITIONED`, `BROADCAST`)。

### Worker配置 (`config.properties`)
*   `query.max-memory-per-node`: (同Coordinator配置，Worker也需感知此限制)。

### JVM配置 (`jvm.config` - Coordinator & Worker)
*   `-Xmx...`: JVM最大堆内存。需要为堆外内存留出足够空间。
*   `-XX:+UseG1GC`: 推荐使用G1垃圾回收器。
*   `-XX:G1HeapRegionSize`: G1区域大小。
*   `-XX:+ExplicitGCInvokesConcurrent`: 允许并发执行System.gc()。
*   `-XX:+ExitOnOutOfMemoryError`: 内存溢出时退出进程。
*   `-XX:-UseBiasedLocking`: 禁用偏向锁可能有助于性能。

### 资源组配置 (e.g., `resource-groups.json`)
*   `maxQueued`: 此组允许排队的最大查询数。
*   `hardConcurrencyLimit`: 此组允许同时运行的最大查询数。
*   `softMemoryLimit`: 查询内存使用的软限制 (百分比或绝对值)，超限可能导致查询排队或优先级降低。
*   `hardCpuLimit`: CPU时间硬限制。
*   `schedulingPolicy`: 组内查询调度策略 (如 `fair`, `weighted_fair`, `query_priority`)。

### Connector配置 (e.g., `etc/catalog/hive.properties`)
*   `connector.name`: Connector类型 (如`hive`, `mysql`, `kafka`)。
*   `hive.metastore.uri`: Hive Metastore地址。
*   `hive.config.resources`: Hive配置文件路径。
*   (特定Connector的配置，如JDBC URL, 用户名密码，Kafka Broker地址等) 