import yfinance as yf
import numpy as np
import pandas as pd

class FuturesProduct:
    def __init__(self, symbol: str, start_date: str, end_date: str):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def load(self) -> pd.DataFrame:
        df = yf.download(self.symbol, self.start_date, self.end_date)
        df.rename(columns={"Adj Close": "price"}, inplace=True)
        df["log_returns"] = np.log(df["price"] / df["price"].shift(1))
        df.dropna(inplace=True)
        self.data = df
        return df
