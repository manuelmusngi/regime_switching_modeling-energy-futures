import pandas as pd
from src.data.futures_product import FuturesProduct
from src.features.feature_engineering import add_features
from src.models.hmm_trainer import HMMTrainer
from src.visualization.plotting import plot_price, plot_returns, plot_regimes

class HMMESPipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        fp = FuturesProduct(
            symbol=self.config["symbol"],
            start_date=self.config["start_date"],
            end_date=self.config["end_date"]
        )

        df = fp.load()
        X = add_features(df)

        hmm = HMMTrainer(
            n_states=self.config["hmm"]["n_states"],
            covariance_type=self.config["hmm"]["covariance_type"]
        )

        hmm.fit(X.values)
        states = hmm.predict_states(X.values)

        plot_price(df, self.config["symbol"])
        plot_returns(df, self.config["symbol"])
        plot_regimes(df, states)

        return {
            "df": df,
            "states": states,
            "params": hmm.get_params()
        }
