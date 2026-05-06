def run_anomaly_detection(df_period):

    # Code du collègue ici
    anomalies = df_period[df_period["value"] > 100]

    return anomalies