import os
import glob
import pandas as pd

# Configuration
MANUAL_RESULTS_PATH = "drift/drift_results.csv"
AUTOMATED_RESULTS_DIR = "output/drift"
OUTPUT_PATH = "output/comparaison/drift_comparaison.csv"
COLUMNS = ["source", "variable", "ks_statistic", "p_value", "psi", "status"]

# Load manual results (already computed by ks_psi_analysis.py)

manual_df = pd.read_csv(MANUAL_RESULTS_PATH)
manual_df["source"] = "manual_70_30"
manual_df = manual_df[COLUMNS]

# Load automated period results (already computed by the automated pipeline)
period_files = sorted(
    glob.glob(os.path.join(AUTOMATED_RESULTS_DIR, "drift_period_*.csv"))
)

automated_dfs = []
for path in period_files:
    # Extract period number from filename, e.g. drift_period_2.csv -> 2
    period_number = int(os.path.splitext(os.path.basename(path))[0].split("_")[-1])
    period_df = pd.read_csv(path, sep=";")
    period_df["source"] = f"automated_period_{period_number}"
    # Harmonise variable naming (some files use 'power', others 'Power')
    period_df["variable"] = period_df["variable"].str.replace(
        "^power$", "Power", regex=True
    )
    automated_dfs.append(period_df[COLUMNS])

# Combine manual and automated results
comparison_df = pd.concat([manual_df] + automated_dfs, ignore_index=True)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
comparison_df.to_csv(OUTPUT_PATH, index=False)

print("Comparison file created successfully.")
print(f"Saved in: {OUTPUT_PATH}")
print(comparison_df)