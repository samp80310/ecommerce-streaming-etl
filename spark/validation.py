from pyspark.sql.functions import col


def validate_orders(df):
    """
    Return only valid ecommerce orders.
    """

    return (
        df.filter(col("order_id").isNotNull())
          .filter(col("customer_id").isNotNull())
          .filter(col("product_id").isNotNull())
          .filter(col("quantity") > 0)
          .filter(col("price") > 0)
    )
def get_invalid_orders(df):
    return (
        df.filter(
            col("order_id").isNull() |
            col("customer_id").isNull() |
            col("product_id").isNull() |
            (col("quantity") <= 0) |
            (col("price") <= 0)
        )
    )