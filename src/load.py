"""
Ce module gère l'étape de chargement (Load) du pipeline ETL.

Il prend les données transformées et les envoie vers la destination finale
(base de données, data warehouse ou fichier final).

Comment il fonctionne :
1. Lecture des données propres depuis `data/processed/`
2. Connexion à la destination finale
3. Insertion ou sauvegarde des données
4. Vérification du succès du chargement

Entrées :
- Fichiers dans data/processed/

Sorties :
- Base de données (tables SQL)
- ou fichiers finaux dans data/final/

Exemple :
    Table SQL : users_final
    ou fichier : data/final/dataset.parquet

Règles importantes :
- Éviter les doublons lors de l'insertion
- Vérifier l'intégrité des données
- Garantir un chargement complet ou rollback

Cas d'utilisation courants :
- Insertion en base SQL
- Export vers data warehouse
- Sauvegarde fichier final

Dépendances possibles :
- pandas
"""