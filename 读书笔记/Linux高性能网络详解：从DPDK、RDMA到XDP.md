[豆瓣评分 9.1](https://book.douban.com/subject/36322557/)

## 计算机网络
#### 五层协议
- 应用层：http
- 传输层：TCP、UDP
- 网络层：IP
- 链路层：Mac
- 物理层：光电接口

最大传输单元 MTU：数据链路层上能通过的最大负载，标准以太网（对应链路层+物理层）是1500Bytes

## 硬件 

![](attachments/Pasted%20image%2020240909113611.png)

#### 体系结构

![](attachments/Pasted%20image%2020240909113913.png)

#### Cache

cache line 一次从内存取 N 个字节到 Cache 中，N 一般为64Byte

cache 写策略：

1. write-through：同时写 cache 和内存
2. write-back：只写 cache，cache line 标记为 dirty，不同步写内存
#### cache 一致性

![](attachments/Pasted%20image%2020240910090836.png)