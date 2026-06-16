import os
import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
# -----------------------------
# Configuration
# -----------------------------

DATA_PATH = "data/Location3Final.csv"
MANUAL_RESULTS_PATH = "drift/drift_results.csv"
OUTPUT_PATH = "output/comparaison/drift_comparaison.csv"

VARIABLES = ["temperature_2m", "relativehumidity_2m", "windspeed_100m", "Power"]


# -----------------------------
# PSI function
# -----------------------------

def calculate_psi(reference, current, bins=10):
    reference = pd.Series(reference).dropna()
    current = pd.Series(current).dropna()

    # Create bins based on reference data
    breakpoints = np.percentile(reference, np.linspace(0, 100, bins + 1))
    breakpoints = np.unique(breakpoints)

    if len(breakpoints) < 2:
        return 0

    ref_counts, _ = np.histogram(reference, bins=breakpoints)
    cur_counts, _ = np.histogram(current, bins=breakpoints)

    ref_percents = ref_counts / len(reference)
    cur_percents = cur_counts / len(current)

    # Avoid division by zero
    ref_percents = np.where(ref_percents == 0, 0.0001, ref_percents)
    cur_percents = np.where(cur_percents == 0, 0.0001, cur_percents)

    psi_values = (cur_percents - ref_percents) * np.log(cur_percents / ref_percents)
    return np.sum(psi_values)


def get_status(psi):
    if psi < 0.1:
        return "Stable"
    elif psi < 0.25:
        return "Moderate drift"
    else:
        return "Significant drift"


# -----------------------------
# Load dataset
# -----------------------------

try:
    df = pd.read_csv(DATA_PATH, sep=";")
except Exception:
    df = pd.read_csv(DATA_PATH)

# Keep only useful variables
df = df[VARIABLES].dropna()

# -----------------------------
# Load manual results
# -----------------------------

manual_df = pd.read_csv(MANUAL_RESULTS_PATH)
manual_df["source"] = "manual_70_30"

# Reorder columns
manual_df = manual_df[["source", "variable", "ks_statistic", "p_value", "psi", "status"]]

# -----------------------------
# Create automated period results
# -----------------------------

# Split dataset into 6 chunks while keeping pandas DataFrames
chunk_size = len(df) // 6
chunks = []

for i in range(6):
    start = i * chunk_size

    if i == 5:
        end = len(df)
    else:
        end = (i + 1) * chunk_size

    chunks.append(df.iloc[start:end].copy())

# First chunk used as reference
reference = chunks[0]

automated_results = []

for i in range(1, len(chunks)):
    current = chunks[i]

    for variable in VARIABLES:
        ks_stat, p_value = ks_2samp(reference[variable], current[variable])
        psi = calculate_psi(reference[variable], current[variable])
        status = get_status(psi)

        automated_results.append({
            "source": f"automated_period_{i + 1}",
            "variable": variable,
            "ks_statistic": ks_stat,
            "p_value": p_value,
            "psi": psi,
            "status": status
        })

automated_df = pd.DataFrame(automated_results)

# -----------------------------
# Combine manual and automated
# -----------------------------

comparison_df = pd.concat([manual_df, automated_df], ignore_index=True)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
comparison_df.to_csv(OUTPUT_PATH, index=False)

print("Comparison file created successfully.")
print(f"Saved in: {OUTPUT_PATH}")
print(comparison_df)