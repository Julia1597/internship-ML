"""
Ce module est responsable de l'étape d'extraction (Extract) du pipeline ETL.
Son rôle est de récupérer les données depuis une source externe
(fichier CSV, API, base de données, etc.) et de les stocker dans
un format brut dans le dossier `data/raw/`.

son but :
1. Connexion ou lecture de la source de données
2. Chargement des données sans modification
3. Sauvegarde des données dans leur format brut

Entrées :
- Fichier CSV (ex: data/source/input.csv)

Sorties :
- Fichiers bruts dans : data/raw/

Exemple de sortie :
    data/raw/dataset_raw.csv

Règles importantes :
- Aucune transformation ne doit être effectuée ici
- Les données doivent rester fidèles à la source
- Cette étape doit être reproductible

Dépendances possibles :
- pandas
"""
_________________________________________


from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/location3Final.csv")


def extract_data():
    df = pd.read_csv(DATA_PATH)
    return df

