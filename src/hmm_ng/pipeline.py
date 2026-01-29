from .config import load_config
from .data_ingestion import fetch_yahoo
from .preprocessing import add_returns, add_volatility
from .features import build_feature_matrix
from .models.hmm_model import RegimeHMM, HMMConfig

def run_pipeline():
    cfg = load_config()

    yahoo_cfg = cfg.data["yahoo"]["tickers"]["ng1"]

    df = fetch_yahoo(
        symbol=yahoo_cfg["symbol"],
        start=cfg.data["start"],
        end=cfg.data["end"],
        interval=yahoo_cfg["interval"],
        auto_adjust=yahoo_cfg["auto_adjust"],
    )

    df = add_returns(df)
    df = add_volatility(df)

    X, df_feat = build_feature_matrix(df)

    model = RegimeHMM(HMMConfig(**cfg.model)).fit(X)
    states = model.predict_states(X)

    return df_feat.with_columns(states=states)
