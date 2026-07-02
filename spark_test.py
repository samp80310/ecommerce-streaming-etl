from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SparkTest")
    .master("local[*]")
    .getOrCreate()
)

print(f"Spark Version: {spark.version}")

spark.range(5).show()

spark.stop()