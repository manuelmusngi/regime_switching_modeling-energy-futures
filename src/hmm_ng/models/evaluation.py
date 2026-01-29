import polars as pl
import numpy as np

def attach_states(df: pl.DataFrame, states: np.ndarray) -> pl.DataFrame:
    return df.with_columns(pl.Series("State", states))

def regime_stats(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.groupby("State")
        .agg([
            pl.col("Returns").mean().alias("mean_return"),
            pl.col("Volatility").mean().alias("mean_vol"),
            pl.count().alias("n_obs"),
        ])
        .sort("State")
    )
