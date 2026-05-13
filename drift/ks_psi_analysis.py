import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

# Charger le dataset
# Load dataset
df = pd.read_csv("data/Location3Final.csv", sep=";")

# Afficher les premières lignes
# Display first rows
print(df.head())

# Séparation en 70% / 30%
# Split into 70% / 30%
split_index = int(len(df) * 0.7)

# Données de référence
# Reference data
df_A = df[:split_index].copy()

# Nouvelles données
# New data
df_B = df[split_index:].copy()

print("Taille A :", len(df_A))
print("Taille B :", len(df_B))

# Simulation de drift sur certaines variables
# Drift simulation on some variables
df_B["windspeed_100m"] = df_B["windspeed_100m"] + 2
df_B["temperature_2m"] = df_B["temperature_2m"] + 1

print("Drift simulé sur certaines variables")
print("Drift simulated on some variables")


# Fonction PSI
# PSI function
def calculate_psi(expected, actual, bins=10):

    # Création des intervalles
    # Create bins
    breakpoints = np.linspace(min(expected), max(expected), bins + 1)

    # Comptage des valeurs dans chaque intervalle
    # Count values in each bin
    expected_counts = np.histogram(expected, bins=breakpoints)[0]
    actual_counts = np.histogram(actual, bins=breakpoints)[0]

    # Conversion en proportions
    # Convert counts to proportions
    expected_percents = expected_counts / len(expected)
    actual_percents = actual_counts / len(actual)

    # Éviter division par zéro
    # Avoid division by zero
    expected_percents = np.where(expected_percents == 0, 0.0001, expected_percents)
    actual_percents = np.where(actual_percents == 0, 0.0001, actual_percents)

    # Calcul du PSI
    # PSI calculation
    psi = np.sum(
        (expected_percents - actual_percents)
        * np.log(expected_percents / actual_percents)
    )

    return psi


# Fonction de détection du drift
# Drift detection function
def detect_drift(df_reference, df_new, variable):

    # Sélection des données
    # Select data
    A = df_reference[variable]
    B = df_new[variable]

    # Application du KS-test
    # Apply KS-test
    stat, p_value = ks_2samp(A, B)

    # Calcul du PSI
    # PSI calculation
    psi_value = calculate_psi(A, B)

    # Détermination du statut du drift
    # Drift status determination
    if psi_value < 0.1:
        drift_status = "Stable"

    elif psi_value < 0.25:
        drift_status = "Moderate drift"

    else:
        drift_status = "Significant drift"

    # Retour des résultats
    # Return results
    return {
        "variable": variable,
        "ks_statistic": stat,
        "p_value": p_value,
        "psi": psi_value,
        "status": drift_status
    }


# Variables à analyser
# Variables to analyze
variables = [
    "temperature_2m",
    "relativehumidity_2m",
    "windspeed_100m",
    "Power"
]

# Liste des résultats
# Results list
results = []

# Boucle sur toutes les variables
# Loop through all variables
for variable in variables:

    result = detect_drift(
        df_A,
        df_B,
        variable
    )

    results.append(result)

# Création du tableau final
# Create final dataframe
results_df = pd.DataFrame(results)

# Affichage des résultats
# Display results
print("\n==============================")
print("DRIFT ANALYSIS RESULTS")
print("==============================\n")

print(results_df)

# Sauvegarde des résultats dans un fichier CSV
# Save results into CSV file
results_df.to_csv(
    "drift/drift_results.csv",
    index=False
)

print("\nResults saved in drift/drift_results.csv")