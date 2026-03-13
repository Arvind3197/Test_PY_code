from pyspark.sql import SparkSession

def CreateSparkSession():
    spark = SparkSession.builder \
        .appName("PySpark Data Pipeline") \
        .getOrCreate()

    return spark
