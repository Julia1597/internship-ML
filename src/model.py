from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor


def train_isolation_forest(df, features, contamination=0.01):
    """
    Entraîne un modèle Isolation Forest et détecte les anomalies.
    """
    X = df[features]

    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    # 1. On crée la colonne 'anomaly_iforest'
    df['anomaly_iforest'] = model.fit_predict(X)
    
    # 2. On transforme cette MÊME colonne (on n'utilise plus le nom 'anomaly')
    df['anomaly_iforest'] = df['anomaly_iforest'].map({1: 0, -1: 1})

    return df


def train_lof(df, features, contamination=0.01):

    X = df[features]

    lof = LocalOutlierFactor(
        n_neighbors=20,
        contamination=contamination
    )

    predictions = lof.fit_predict(X)

    df['anomaly_lof'] = [1 if x == -1 else 0 for x in predictions]

    return df