from .config import load_config
from .data_ingestion import fetch_yahoo
from .preprocessing import add_returns, add_volatility
from .features import build_feature_matrix
from .models.hmm_model import RegimeHMM, HMMConfig
from .models.evaluation import attach_states, regime_summary
from .visualization import plot_regimes

def run_pipeline():
    cfg = load_config()

    df = fetch_yahoo(
        symbol=cfg.data["yahoo"]["symbol"],
        start=cfg.data["date_range"]["start"],
        end=cfg.data["date_range"]["end"],
        interval=cfg.data["yahoo"]["interval"],
        auto_adjust=cfg.data["yahoo"]["auto_adjust"],
    )

    df = add_returns(df)
    df = add_volatility(df)

    X, df_feat = build_feature_matrix(df)

    hmm_cfg = HMMConfig(**cfg.model["model"])
    model = RegimeHMM(hmm_cfg).fit(X)
    states = model.predict_states(X)

    df_out = attach_states(df_feat, states)
    summary = regime_summary(df_out)
    fig = plot_regimes(df_out)

    return {
        "data": df_out,
        "summary": summary,
        "transition_matrix": model.transition_matrix,
        "figure": fig,
    }
