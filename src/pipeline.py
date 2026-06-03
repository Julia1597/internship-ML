from src.extract import extract_data
from src.transform import transform_data
from src.split import split_by_time
from src.anomalie import run_anomaly_detection
from src.data_drift import run_data_drift

from src.load import (
    save_anomalies,
    save_drift
)

def run_pipeline():

    # Extraction
    df = extract_data()

    # Transformation
    df = transform_data(df)

    # Découpage
    periods = split_by_time(df, n_splits=6)



    for i, period in enumerate(periods):

        print(f"\nPériode {i+1}")
        
        # Anomalies
        anomalies = run_anomaly_detection(period)

        print(f"Anomalies détectées : {len(anomalies)}")

        save_anomalies(anomalies, i+1)
        
        # Drift
        if i > 0:

            previous_period = periods[i - 1]
            current_period = period
            
            drift_result = run_data_drift(
                previous_period,
                current_period
            )
            
            save_drift(
                drift_result,
                i + 1
            )

            print("Résultat drift :", drift_result)