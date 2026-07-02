from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

from schemas import order_schema

spark = (
    SparkSession.builder
    .appName("EcommerceStreamingETL")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "ecommerce_orders")
    .option("startingOffsets", "latest")
    .load()
)

json_df = (
    df.selectExpr("CAST(value AS STRING) AS json")
      .select(from_json(col("json"), order_schema).alias("data"))
      .select("data.*")
)

query = (
    json_df.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", False)
    .start()
)

query.awaitTermination()