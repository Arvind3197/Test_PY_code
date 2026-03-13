from scripts.spark_session import CreateSparkSession
from scripts.transformations import transformation

# Create Spark Session
spark = CreateSparkSession()

# Read raw data
df = spark.read.csv("data/original.csv", header=True, inferSchema=True)

# Apply transformations
clean_df = transformation(df)

# Show clean data
clean_df.show()

# Write cleaned data
clean_df.write.mode("overwrite").csv("output/clean_data", header=True)