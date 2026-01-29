import yfinance as yf
import polars as pl

def fetch_yahoo(
    symbol: str,
    start: str,
    end: str | None,
    interval: str,
    auto_adjust: bool,
) -> pl.DataFrame:
    df = yf.download(
        symbol,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=auto_adjust,
        progress=False,
    )

    if df.empty:
        raise ValueError(f"No data returned for {symbol}")

    return (
        pl.from_pandas(df.reset_index())
        .rename({"Date": "Date", "Close": "Close"})
        .with_columns(pl.col("Date").cast(pl.Date))
        .sort("Date")
    )
