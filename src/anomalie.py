from src.model import train_isolation_forest


def run_anomaly_detection(df):
    """
    Détection des anomalies avec Isolation Forest.
    """

    features = [
        "temperature_2m",
        "relativehumidity_2m",
        "windspeed_100m",
        "power"
    ]

    df = train_isolation_forest(
        df=df,
        features=features,
        contamination=0.01
    )

    anomalies = df[
        df["anomaly_iforest"] == 1
    ]

    return anomalies