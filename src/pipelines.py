from src.extract import extract_data
from src.transform import transform_data
from src.split_data import split_by_time
from src.anomaly_detection import run_anomaly_detection
from src.data_drift import run_data_drift


def run_pipeline():

    # Extraction
    df = extract_data()

    # Transformation
    df = transform_data(df)

    # Découpage
    periods = split_by_time(df, n_splits=6)

    # ======================
    # Boucle périodes
    # ======================

    for i, period in enumerate(periods):

        print(f"\nPériode {i+1}")

        # Anomalies
        anomalies = run_anomaly_detection(period)

        print(f"Anomalies détectées : {len(anomalies)}")

        # Drift
        if i > 0:

            previous_period = periods[i - 1]

            drift_result = run_data_drift(
                previous_period,
                period
            )

            print("Résultat drift :", drift_result)