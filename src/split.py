import numpy as np


def split_by_time(df, n_splits=6):

    df = df.sort_values("date")

    splits = np.array_split(df, n_splits)

    return splits