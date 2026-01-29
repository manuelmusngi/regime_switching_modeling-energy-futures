from .config import load_config
from .data_ingestion import fetch_yahoo
from .preprocessing import add_returns, add_volatility
from .features import build_feature_matrix
from .models.hmm_model import RegimeHMM, HMMConfig
from .models.evaluation import attach_states, regime_stats
from .visualization import plot_regimes

def run_pipeline():
    cfg = load_config()

    yahoo = cfg.data["yahoo"]
    dates = cfg.data["date_range"]

    df = fetch_yahoo(
        symbol=yahoo["symbol"],
        start=dates["start"],
        end=dates["end"],
        interval=yahoo["interval"],
        auto_adjust=yahoo["auto_adjust"],
    )

    df = add_returns(df)
    df = add_volatility(df)

    X, df_feat = build_feature_matrix(df)

    hmm_cfg = HMMConfig(**cfg.model["model"])
    model = RegimeHMM(hmm_cfg).fit(X)
    states = model.predict_states(X)

    df_out = attach_states(df_feat, states)
    stats = regime_stats(df_out)
    fig = plot_regimes(df_out)

    return {
        "df": df_out,
        "stats": stats,
        "transition_matrix": model.transition_matrix,
        "figure": fig,
    }
