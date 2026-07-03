from pyspark.sql.functions import col

def add_total_amount(df):
    return df.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )