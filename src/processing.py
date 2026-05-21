import pandas as pd
import numpy as np

def load_and_clean_data(file_path, separator=";"):
    """
    Fonction universelle pour charger et nettoyer un dataset.
    Elle gère les séparateurs, les doublons et les valeurs aberrantes.
    """
    # 1. Chargement flexible
    df = pd.read_csv(file_path, sep=separator)
    
    # 2. Nettoyage des doublons (Indispensable pour la qualité)
    df = df.drop_duplicates()
    
    # 3. Gestion des dates (Si une colonne 'Time' ou 'Date' existe)
    # On cherche une colonne qui ressemble à du temps pour la convertir
    for col in df.columns:
        if 'time' in col.lower() or 'date' in col.lower():
            # La version ultime pour gérer les changements de format de date
            df[col] = pd.to_datetime(df[col], dayfirst=True, format='mixed', errors='coerce')    

    df:set        
    return df

def remove_outliers(df, column_name, min_val, max_val):
    """
    Supprime les lignes où les valeurs sont physiquement impossibles.
    Ex: Température > 60°C ou < -50°C
    """
    df_cleaned = df[(df[column_name] >= min_val) & (df[column_name] <= max_val)]
    return df_cleaned

