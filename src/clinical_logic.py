from pyspark.sql.functions import col

def apply_clinical_rules(df):
    return df.withColumn("dosage_mg", col("dosage") * 1000)

    """
    Standardizes dosage and flags records for review.
    """
    return df.with_column(
        "dosage_mg", 
        col("dosage") * 1000  # Example: Converting grams to milligrams
    )