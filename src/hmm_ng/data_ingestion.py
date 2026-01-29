 import polars as pl
import yfinance as yf
from .logging_utils import get_logger

log = get_logger(__name__)

def fetch_yahoo(symbol: str, start: str, end: str | None, interval: str, auto_adjust: bool) -> pl.DataFrame:
    log.info(f"Fetching {symbol} from Yahoo Finance")

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

