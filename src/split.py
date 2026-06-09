import numpy as np
import pandas as pd

def split_by_time(df, n_splits=6):
    # Tri par le temps pour assurer la cohérence chronologique
    df = df.sort_values("time").reset_index(drop=True)

    # np.array_split fonctionne, mais on s'assure de recréer de vrais DataFrames
    # en utilisant les indices générés par NumPy
    indices = np.array_split(df.index, n_splits)
    
    splits = [df.iloc[idx].copy() for idx in indices]

    return splits