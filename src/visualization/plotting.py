import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")

def plot_price(df: pd.DataFrame, symbol: str):
    df["price"].plot(figsize=(12, 6), title=f"Price Chart: {symbol}")

def plot_returns(df: pd.DataFrame, symbol: str):
    df["log_returns"].plot(figsize=(12, 6), title=f"Log Returns: {symbol}")

def plot_regimes(df: pd.DataFrame, states):
    plt.figure(figsize=(14, 6))
    plt.scatter(df.index, df["price"], c=states, cmap="viridis", s=10)
    plt.title("Regime States Over Price")
