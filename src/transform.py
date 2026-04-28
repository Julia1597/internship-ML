"""
Description :
Ce module gère l'étape de transformation (Transform) du pipeline ETL.

Il prend les données brutes issues de `data/raw/` et les transforme
en données propres, cohérentes et exploitables.

Comment il fonctionne :
1. Chargement des données brutes
2. Nettoyage des données (valeurs nulles, doublons, erreurs)
3. Transformation des formats (dates, types, colonnes)
4. Export des données propres

Entrées :
- Fichiers dans data/raw/

Sorties :
- Fichiers nettoyés dans data/processed/

Exemple de sortie :
    data/processed/dataset_clean.csv

Opérations courantes de transformation: 
- Suppression des doublons
- Gestion des valeurs manquantes
- Normalisation des colonnes
- Conversion des types de données
- Filtrage des lignes inutiles

Règles importantes :
- Ne jamais modifier les données brutes
- Toute transformation doit être traçable
- Les résultats doivent être reproductibles

Dépendances possibles :
- pandas
- numpy
"""