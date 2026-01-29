import matplotlib.pyplot as plt
import polars as pl

def plot_regimes(df: pl.DataFrame):
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(df["Date"], df["Close"], color="black", lw=1)

    for state in df["State"].unique().sort():
        mask = df["State"] == state
        ax.scatter(
            df.filter(mask)["Date"],
            df.filter(mask)["Close"],
            s=8,
            label=f"Regime {state}",
        )

    ax.set_title("NG1 Hidden Markov Model Regimes")
    ax.legend()
    fig.autofmt_xdate()
    return fig
