
[CXL，最强科普](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247749286&idx=1&sn=abbbbf641ff9dd21f9a7a45824c7b048&chksm=ce6e0c51f919854701ad321b572554de18fea32349e938afee1467f14bf4b6df09b91e5c1c8c#rd)
## CXL版本
- CXL1.0
	- PCIe5.0, 32GT/s, only support one host to use the CXL memory
- CXL2.0
	- memory pool,At 1.0/1.1, a device is limited to behaving as a single logical device accessible by only one host at a time. However, a 2.0-level device can be partitioned as multiple logical devices, allowing up to 16 hosts to simultaneously access different portions of the memory.
- CXL3.0
	- PCIe 6.0,64GT/s
	- CXL 3.0 introduces peer-to-peer direct memory access and enhancements to memory pooling where multiple hosts can coherently share a memory space on a CXL 3.0 device
## Core features
- high bandwidth and low latency comapring to Ethnet or infiniband
- memory expansion or pooling
- coherent memory access
	- multiple processors to access shared memory in a coherent manner
	- cache coherence
- Memory semantics

## 参考文献
[Nag - 2023 - CXL (Compute Express Link) Technology](../../../zotero/storage/ZG453YXQ/Nag%20-%202023%20-%20CXL%20(Compute%20Express%20Link)%20Technology.pdf)
