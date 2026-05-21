import pandas as pd
from src.processing import load_and_clean_data
from src.model import (
    train_isolation_forest,
    train_lof
)

from src.visualisation import plot_algorithm

# Chargement
df = load_and_clean_data("data/Location3Final.csv")

# Colonnes utiles
all_features = [
    'windspeed_100m',
    'Power',
    'temperature_2m',
    'windspeed_10m',
    'windgusts_10m'
]

# Vérifie les colonnes existantes
features = [col for col in all_features if col in df.columns]

# Supprime les lignes vides
df = df.dropna(subset=features)

# Isolation Forest
df = train_isolation_forest(df, features) # Maintenant df est bien un DataFrame
print("Isolation Forest anomalies :", df['anomaly_iforest'].sum())

# LOF
df = train_lof(df, features)
print("LOF anomalies :", df['anomaly_lof'].sum())


# Graphiques

print("Génération des graphiques comparatifs...")

plot_algorithm(
    df, 
    'anomaly_iforest', 
    'Détection par Isolation Forest', 
    'graphique_iforest.png'
)

plot_algorithm(
    df, 
    'anomaly_lof', 
    'Détection par Local Outlier Factor', 
    'graphique_lof.png'
)

print("Terminé ! Regarde les fichiers .png dans ton dossier.")


# 1. CLASSIFICATION SELON L'ALGORITHME (PROVENANCE)
is_iforest = (df['anomaly_iforest'] == 1)
is_lof = (df['anomaly_lof'] == 1)

df['Provenance'] = "Normal"
df.loc[is_iforest & is_lof, 'Provenance'] = "(IF + LOF)"
df.loc[is_iforest & ~is_lof, 'Provenance'] = "IForest"
df.loc[~is_iforest & is_lof, 'Provenance'] = "LOF"

# On ne garde que les lignes qui contiennent une anomalie pour la suite
df_anomalies = df[df['Provenance'] != "Normal"].copy()

# 2. CLASSIFICATION SELON LA PHYSIQUE (DIAGNOSTIC)

def diagnostiquer_anomalie(row):
    vent = row['windspeed_100m']
    puissance = row['Power']
    temp = row['temperature_2m']
    
    if temp <= 2.0:
        return "Icing Risk"
    elif vent > 3.5 and puissance < 0.05:
        return "Total Shutdown / Failure"
    elif vent > 8.0 and puissance < 0.5:
        return "Underperformance"
    else:
        return "Other Atypical Behavior"

df_anomalies['Diagnostic'] = df_anomalies.apply(diagnostiquer_anomalie, axis=1)

# 3. LE MIX PARFAIT : TABLEAU CROISÉ GÉNÉRÉ PAR PANDAS
print("--- TABLE ---")

# Cette ligne magique croise les diagnostics (lignes) et la provenance (colonnes)
tableau_mixte = pd.crosstab(
    df_anomalies['Diagnostic'], 
    df_anomalies['Provenance'], 
    margins=True,          # Ajoute les totaux "All" à la fin
    margins_name="TOTAL"   # Renomme la ligne/colonne du total
)

print(tableau_mixte)

# Sauvegarde de ce tableau croisé unique
tableau_mixte.to_csv("data/bilan_mixte_anomalies.csv", sep=";")
print("Le fichier combiné 'bilan_mixte_anomalies.csv' a été enregistré.")