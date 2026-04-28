import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

df = pd.read_csv("data/Location3Final.csv", sep=";")

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

# Simulation de drift sur windspeed
#Simulation of drift on windspeed
df_B["windspeed_100m"] = df_B["windspeed_100m"] + 2

print("Drift simulé sur windspeed_100m")


A = df_A["windspeed_100m"]
B = df_B["windspeed_100m"]

stat, p_value = ks_2samp(A, B)

print("p-value :", p_value)
print("KS Statistic :", stat)
print("p-value :", p_value)

# Calcul du PSI
# PSI calculation

def calculate_psi(expected, actual, bins=10):
    # Créer les intervalles (bins)
    # Create bins
    breakpoints = np.linspace(min(expected), max(expected), bins + 1)

    # Compter les valeurs dans chaque bin
    # Count values in each bin
    expected_counts = np.histogram(expected, bins=breakpoints)[0]
    actual_counts = np.histogram(actual, bins=breakpoints)[0]

    # Convertir en proportions
    # Convert counts to proportions
    expected_percents = expected_counts / len(expected)
    actual_percents = actual_counts / len(actual)

    # Éviter division par 0
    # Avoid division by zero
    expected_percents = np.where(expected_percents == 0, 0.0001, expected_percents)
    actual_percents = np.where(actual_percents == 0, 0.0001, actual_percents)

    # Calcul du PSI
    # PSI calculation
    psi = np.sum((expected_percents - actual_percents) * np.log(expected_percents / actual_percents))

    return psi


# Appliquer PSI sur windspeed
# Apply PSI on windspeed
psi_value = calculate_psi(A, B)

print("PSI :", psi_value)