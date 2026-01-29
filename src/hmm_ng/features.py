import polars as pl
import numpy as np

def build_feature_matrix(df: pl.DataFrame) -> tuple[np.ndarray, pl.DataFrame]:
    df_feat = df.drop_nulls(subset=["Returns", "Volatility"])
    X = df_feat.select(["Returns", "Volatility"]).to_numpy()
    return X, df_feat
