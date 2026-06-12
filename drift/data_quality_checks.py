import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/Location3Final.csv", sep=";")

# Variables used in the project
variables = [
    "temperature_2m",
    "relativehumidity_2m",
    "windspeed_100m",
    "Power"
]

results = []

for variable in variables:
    series = df[variable]

    # Missing values
    missing_values = series.isna().sum()
    missing_percentage = (missing_values / len(series)) * 100

    # Outlier detection using IQR method
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = series[(series < lower_bound) | (series > upper_bound)].count()
    outlier_percentage = (outliers / len(series)) * 100

    results.append({
        "variable": variable,
        "missing_values": missing_values,
        "missing_percentage": round(missing_percentage, 2),
        "outliers": outliers,
        "outlier_percentage": round(outlier_percentage, 2),
        "lower_bound": round(lower_bound, 2),
        "upper_bound": round(upper_bound, 2)
    })

# Duplicate rows
duplicate_rows = df.duplicated().sum()

quality_df = pd.DataFrame(results)

os.makedirs("drift", exist_ok=True)
quality_df.to_csv("drift/data_quality_results.csv", index=False)

print("Data quality checks completed.")
print("Duplicate rows:", duplicate_rows)
print("Results saved in drift/data_quality_results.csv")
print(quality_df)