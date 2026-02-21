# scripts/ingest_data.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Configurable paths
source_url = "abfss://raw-data@stlakehousedev.dfs.core.windows.net/uploads/"
checkpoint_url = "abfss://checkpoints@stlakehousedev.dfs.core.windows.net/ingest/"

print(f"Reading from: {source_url}")

# Auto Loader logic
(spark.readStream
  .format("cloudFiles")
  .option("cloudFiles.format", "csv")
  .option("cloudFiles.schemaLocation", checkpoint_url)
  .load(source_url)
  .writeStream
  .option("checkpointLocation", checkpoint_url)
  .trigger(availableNow=True)
  .toTable("main.default.ingested_raw_data"))