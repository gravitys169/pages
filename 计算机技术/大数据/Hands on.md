## Dev Env

spark-sql --deploy-mode client --master yarn --driver-cores 1  --driver-memory 1g --num-executors 2  --executor-cores 2  --executor-memory 2g  --database tpcds_1g --conf spark.memory.offHeap.enabled=true  --conf spark.memory.offHeap.size=1g  --conf spark.task.cpus=1 

