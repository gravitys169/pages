随着大数据的发展，大数据平台从单一服务于BI类业务，转而向AI类业务服务，一套大数据平台架构解决BI&AI的业务成为趋势
在meta内部presto早已不仅仅是担任adhoc的场景

This space  
Test

他说的

水电费

啊防守打法


## 数据清洗算子
#### 去重MinHash
- Jaccard Similarity：集合的交集除以集合的并集，1为完全相同，0为完全不同
- 集合的矩阵表示与行列变换

考虑集合 S1 = {1， 2， 5} S2 = {3} S3 = {2， 3， 4， 6} S4 = {1， 4， 6}，集合可矩阵表示为


![](attachments/Pasted%20image%2020240605092838.png)


经过一次随机行列变换


![](attachments/Pasted%20image%2020240605093252.png)


每次变换取最小的不为1的下标值作为签名，故两次变换后S1={1,1}，S2={3,6}。。。
- 基于Hash的签名矩阵：**将上述矩阵变换操作改为Hash操作**，并使用Fast Min hashing算法可求得每个集合的hash signature集合
- ![](attachments/Pasted%20image%2020240605094122.png)


其中N为set个数，k为hash函数个数
- 在表示element时，往往不以原始的值做运算，而是对值取sha1

## 参考文献

[BigCode 背后的大规模数据去重](https://huggingface.co/blog/zh/dedup)


[Data Preprocessing — Deduplication with MinHash and LSH | Medium](https://wenjingzhan.medium.com/data-preprocessing-deduplication-with-minhash-and-lsh-99c5e10703d)


[Python的datasketch库中的MinHashLSH-CSDN博客](https://blog.csdn.net/IOT_victor/article/details/104044453)
