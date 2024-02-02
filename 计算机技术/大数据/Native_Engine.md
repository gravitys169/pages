## Why
- JVM 内存管理开销大：GC，底噪
	- C++精细化管理内存
- JVM隔离了硬件，难以应用直接SIMD Intrinsic
	- C++可直接调用intel AVX、ARM Neon/SVE指令

## What
- Huawei OmniOperator
- Databricks Photon
- Apache Arrow Datafusion 
- Apache Velox
-