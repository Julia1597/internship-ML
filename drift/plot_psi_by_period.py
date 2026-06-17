import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import re

# Find automated drift period files anywhere inside output/
files = sorted(glob.glob("output/**/drift_period_*.csv", recursive=True))

if not files:
    raise FileNotFoundError("No drift_period files found inside the output folder.")

print("Files found:")
for file in files:
    print(file)

all_results = []

for file in files:
    # Extract period number from filename
    match = re.search(r"drift_period_(\d+)", file)
    period = int(match.group(1)) if match else None

    df = pd.read_csv(file)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Normalize variable names
    df["variable"] = df["variable"].str.lower()

    # Add period column
    df["period"] = period

    all_results.append(df)

# Combine all period results
period_df = pd.concat(all_results, ignore_index=True)

# Create pivot table
pivot_df = period_df.pivot_table(
    index="period",
    columns="variable",
    values="psi",
    aggfunc="mean"
)

# Create graph
plt.figure(figsize=(10, 6))

for variable in pivot_df.columns:
    plt.plot(
        pivot_df.index,
        pivot_df[variable],
        marker="o",
        label=variable
    )

# Threshold lines
plt.axhline(y=0.1, linestyle="--", label="Moderate drift threshold (0.1)")
plt.axhline(y=0.25, linestyle="--", label="Significant drift threshold (0.25)")

plt.xlabel("Automated period")
plt.ylabel("PSI value")
plt.title("PSI Evolution Across Automated Periods")
plt.xticks(pivot_df.index)
plt.legend()
plt.tight_layout()

# Save graph
os.makedirs("drift", exist_ok=True)
plt.savefig("drift/psi_by_period.png", dpi=300)
plt.close()

print("Automated period graph created: drift/psi_by_period.png")