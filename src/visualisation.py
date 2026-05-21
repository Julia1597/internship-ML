import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def plot_algorithm(df, anomaly_column, title, filename):
    fig, ax = plt.subplots(figsize=(12,6))

    normal = df[df[anomaly_column] == 0]
    anomalies = df[df[anomaly_column] == 1]

    # Sécurité : Si 'Time' est l'index, on le remet en colonne pour l'affichage
    if 'Time' not in df.columns:
        df = df.reset_index()

    # On force la conversion de la colonne 'Time' en vraies dates de manière robuste
    times_normal = pd.to_datetime(normal['Time'], dayfirst=True, format='mixed', errors='coerce')
    times_anomalies = pd.to_datetime(anomalies['Time'], dayfirst=True, format='mixed', errors='coerce')

    # Affichage des points avec la vraie dimension temporelle
    ax.scatter(times_normal, normal['Power'], label='Normal', s=10, alpha=0.3)
    ax.scatter(times_anomalies, anomalies['Power'], label='Anomaly', s=25, color='red')

    # Configuration de l'axe X
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # Format : Année-Mois-Jour
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))    # Un repère tous les 2 mois

    fig.autofmt_xdate() # Incline les dates

    ax.set_xlabel("Date")
    ax.set_ylabel("Power")
    ax.set_title(title)
    ax.legend()
    
    plt.savefig(filename, bbox_inches="tight")
    plt.close() 
    print(f"Graphique corrigé sauvegardé : {filename}")