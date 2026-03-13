from pyspark.sql.functions import col, regexp_replace

def transformation(df):

    # Remove $ from Salary
    df = df.withColumn(
        "Salary",
        regexp_replace(col("Salary"), "\\$", "").cast("double")
    )

    # Fill missing City
    df = df.fillna({"City": "Unknown"})

    # Fill missing JobTitle
    df = df.fillna({"JobTitle": "Not Specified"})

    # Drop rows where Latitude or Longitude is null
    df = df.dropna(subset=["Latitude", "Longitude"])

    return df
