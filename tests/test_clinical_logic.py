import pytest
from pyspark.sql import SparkSession
from src.clinical_logic import apply_clinical_rules

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("PharmaTests").getOrCreate()

def test_dosage_conversion(spark):
    # Create dummy data: 1 gram dosage
    data = [{"patient_id": "P001", "dosage": 1}]
    df = spark.createDataFrame(data)
    
    # Apply logic
    result_df = apply_clinical_rules(df)
    actual_dosage = result_df.collect()[0]["dosage_mg"]
    
    # Assert
    assert actual_dosage == 1000