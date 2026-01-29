import polars as pl

def add_returns(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.col("Close").log().diff().alias("Returns")
    )

def add_volatility(df: pl.DataFrame, window: int = 21) -> pl.DataFrame:
    return df.with_columns(
        pl.col("Returns")
        .pow(2)
        .rolling_mean(window)
        .sqrt()
        .alias("Volatility")
    )
