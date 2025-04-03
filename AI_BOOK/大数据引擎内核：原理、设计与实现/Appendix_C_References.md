# 附录C: 参考文献与推荐阅读 (References & Further Reading)

本书的撰写参考了大量官方文档、技术博客、社区分享、会议演讲以及相关领域的经典论文和书籍。由于篇幅限制，无法一一列举所有参考来源，在此仅列出部分核心资源和推荐的进一步阅读材料，希望能为读者提供深入探索的起点。

## 官方文档 (Official Documentation)

官方文档是了解引擎特性、配置、API和最佳实践最权威、最及时的来源。

*   **Apache Spark:** [https://spark.apache.org/docs/latest/](https://spark.apache.org/docs/latest/)
*   **Apache Flink:** [https://nightlies.apache.org/flink/flink-docs-stable/](https://nightlies.apache.org/flink/flink-docs-stable/)
*   **Trino (formerly PrestoSQL):** [https://trino.io/docs/current/](https://trino.io/docs/current/)
*   **PrestoDB:** [https://prestodb.io/docs/current/](https://prestodb.io/docs/current/)
*   **Apache Hadoop:** [https://hadoop.apache.org/docs/current/](https://hadoop.apache.org/docs/current/)
*   **Apache Kafka:** [https://kafka.apache.org/documentation/](https://kafka.apache.org/documentation/)
*   **Delta Lake:** [https://docs.delta.io/latest/index.html](https://docs.delta.io/latest/index.html)
*   **Apache Iceberg:** [https://iceberg.apache.org/docs/latest/](https://iceberg.apache.org/docs/latest/)
*   **Apache Hudi:** [https://hudi.apache.org/docs/overview](https://hudi.apache.org/docs/overview)

## 核心论文与设计文档 (Key Papers & Design Docs)

理解引擎设计的根源和思想，阅读核心论文和设计文档至关重要。

*   **MapReduce:** Dean, Jeffrey, and Ghemawat, Sanjay. "MapReduce: simplified data processing on large clusters." Communications of the ACM 51.1 (2008): 107-113.
*   **Spark RDD:** Zaharia, Matei, et al. "Resilient distributed datasets: A fault-tolerant abstraction for in-memory cluster computing." NSDI'12.
*   **Spark SQL:** Armbrust, Michael, et al. "Spark SQL: Relational data processing in Spark." SIGMOD'15.
*   **Structured Streaming:** Zaharia, Matei, et al. "Structured Streaming: A Declarative API for Real-Time Applications in Apache Spark." SIGMOD'18.
*   **Flink (Stream Processing):** Carbone, Paris, et al. "Apache Flink: Stream and batch processing in a single engine." Bulletin of the IEEE Computer Society Technical Committee on Data Engineering 36.4 (2015).
*   **Flink Checkpointing (Asynchronous Barrier Snapshotting):** Carbone, Paris, et al. "Lightweight asynchronous snapshots for distributed dataflows." arXiv preprint arXiv:1506.08603 (2015).
*   **Presto:** Sethi, Dain, et al. "Presto: SQL on everything." ICDE'19.
*   **Google File System (GFS):** Ghemawat, Sanjay, Gobioff, Howard, and Leung, Shun-Tak. "The Google file system." SOSP'03.
*   **Bigtable:** Chang, Fay, et al. "Bigtable: A distributed storage system for structured data." OSDI'06.
*   **Dynamo:** DeCandia, Giuseppe, et al. "Dynamo: Amazon's highly available key-value store." SOSP'07.
*   *(更多相关论文，可在引擎官网、主要会议如 SIGMOD, VLDB, NSDI, OSDI, ICDE 等查找)*

## 推荐书籍 (Recommended Books)

*   **《Designing Data-Intensive Applications》 by Martin Kleppmann:** (中文版《数据密集型应用系统设计》) 分布式系统领域的经典之作，强烈推荐阅读，有助于理解底层原理和权衡。
*   **《Spark: The Definitive Guide》 by Bill Chambers and Matei Zaharia:** (中文版《Spark权威指南》) 全面介绍Spark生态和用法的权威书籍。
*   **《Learning Spark, 2nd Edition》 by Jules S. Damji, Brooke Wenig, Tathagata Das, and Denny Lee:** 适合入门和进阶学习Spark。
*   **《Stream Processing with Apache Flink》 by Fabian Hueske and Vasiliki Kalavri:** (中文版《Flink流处理编程》) 由Flink核心开发者撰写，深入讲解Flink流处理。
*   **《Flink Basis》 by Zhu Zhu:** (中文版《Flink原理、实战与性能优化》) 国内作者撰写的Flink实战书籍。
*   **《Trino: The Definitive Guide》 by Matt Fuller, Manfred Moser, and Martin Traverso:** Trino官方出品的权威指南。
*   **《Database System Concepts》 by Abraham Silberschatz, Henry F. Korth, and S. Sudarshan:** 数据库领域的经典教材，有助于理解SQL优化、事务等基础。
*   **《Distributed Systems》 by Maarten van Steen and Andrew S. Tanenbaum:** 分布式系统领域的经典教材。

## 技术博客与社区资源 (Tech Blogs & Community Resources)

*   **Databricks Blog:** [https://databricks.com/blog](https://databricks.com/blog) (大量Spark和Delta Lake深度文章)
*   **Flink Official Blog:** [https://flink.apache.org/blog/](https://flink.apache.org/blog/)
*   **Ververica Blog (Flink商业公司):** [https://www.ververica.com/blog](https://www.ververica.com/blog)
*   **Trino Blog:** [https://trino.io/blog/](https://trino.io/blog/)
*   **Confluent Blog (Kafka):** [https://www.confluent.io/blog/](https://www.confluent.io/blog/)
*   **各大云厂商博客 (AWS, Azure, GCP):** 包含大量关于在其平台上使用这些引擎的最佳实践。
*   **InfoQ, Hacker News, Reddit (r/bigdata, r/apachespark, etc.):** 获取最新资讯和讨论。
*   **Stack Overflow:** 解决具体问题。

## 会议演讲 (Conference Talks)

*   **Spark Summit / Data + AI Summit:** Spark领域的顶级会议。
*   **Flink Forward:** Flink领域的顶级会议。
*   **Trino Summit:** Trino社区会议。
*   **Strata Data Conference (已停办，但历史资料仍有价值)**
*   **SIGMOD, VLDB, NSDI, OSDI, ICDE 等学术会议:** 关注前沿研究。
*   *(可在YouTube等视频平台搜索相关会议演讲)*

**致谢:** 感谢所有为这些开源项目和技术社区做出贡献的研究人员、工程师和布道者，他们的工作是本书得以完成的基础。 