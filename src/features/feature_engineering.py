import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Returns"] = df["price"].pct_change()
    df["Volatility"] = (df["High"] / df["Low"]) - 1
    df.dropna(inplace=True)
    return df[["Returns", "Volatility"]]
