import numpy as np
from pyhhmm.gaussian import GaussianHMM

class HMMTrainer:
    def __init__(self, n_states: int = 4, covariance_type: str = "full"):
        self.model = GaussianHMM(
            n_states=n_states,
            covariance_type=covariance_type,
            n_emissions=2
        )

    def fit(self, X: np.ndarray):
        self.model.train([X])

    def predict_states(self, X: np.ndarray):
        return self.model.predict([X])[0]

    def get_params(self):
        return {
            "means": self.model.means,
            "covariances": self.model.covars
        }
