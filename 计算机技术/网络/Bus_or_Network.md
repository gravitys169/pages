[AI fabric is a bus or a network？](https://jx.huawei.com/community/comgroup/postsDetails?postId=55e9eaaa78a04284bf3b5b0efa361943&noTop=true&type=freePost&zoneId=3)


网红大咖Zarbot

![](https://raw.githubusercontent.com/gravitys169/images_upload/master/202406251116514.jpg?token=ACGIA7WF3ZVEIQMPBFLB4RTGPI3LE)

- 从 bus 的角度扩展，提升 BW/IOPS 容易, 扩展规模受限，代表为 HCCS/Nvlink
- 从网络的角度扩展，通过多层解耦，提升 BW 代价高，代表为 IB、RoCE , [UEC](https://www.sdnlab.com/26274.html) ，以及[中国版 UEC 高通量以太网联盟](https://mp.weixin.qq.com/s/VUQeIuygP7XaBwaPTShEhA)

![](attachments/Pasted%20image%2020240625113715.png)

站在计算的角度，点评一下过去网党征伐计算的战绩 ：） 也就是RDMA这个战车啦，这仗真心说打得挺烂的，靠IB在HPC领域撑住了场子，但DCN领域的空间一直没打开。

RDMA最大的困境，在于如何解决Lossy和Out-of-Order的主要问题（后者包括多路径和重传），以及上下文爆炸的次级问题