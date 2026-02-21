import pytest
from src.clinical_logic import apply_clinical_rules

@pytest.mark.parametrize("input_g, expected_mg", [
    (1, 1000),    # Normal case
    (0.5, 500),   # Decimal case
    (0, 0),       # Edge case
])
def test_dosage_conversion_multi(spark, input_g, expected_mg):
    data = [{"patient_id": "P001", "dosage": input_g}]
    df = spark.createDataFrame(data)
    
    result_df = apply_clinical_rules(df)
    actual_dosage = result_df.collect()[0]["dosage_mg"]
    
    assert actual_dosage == expected_mg