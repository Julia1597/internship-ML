import pandas as pd
import matplotlib.pyplot as plt
import os

# Load drift results
results_df = pd.read_csv("drift/drift_results.csv")

# Normalize variable names
results_df["variable"] = results_df["variable"].str.lower()

# Create graph
plt.figure(figsize=(9, 5))
plt.bar(results_df["variable"], results_df["psi"])

# Threshold lines
plt.axhline(y=0.1, linestyle="--", label="Moderate drift threshold (0.1)")
plt.axhline(y=0.25, linestyle="--", label="Significant drift threshold (0.25)")

plt.xlabel("Variables")
plt.ylabel("PSI value")
plt.title("Population Stability Index by Variable")
plt.xticks(rotation=30)
plt.yticks([0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5])
plt.legend()
plt.tight_layout()

# Save image where dashboard expects it
os.makedirs("drift", exist_ok=True)
plt.savefig("drift/psi_by_variable.png", dpi=300)
plt.close()

print("Graph created: drift/psi_by_variable.png")
