from dataclasses import dataclass
import numpy as np
from hmmlearn.hmm import GaussianHMM

@dataclass
class HMMConfig:
    n_components: int
    covariance_type: str
    n_iter: int
    tol: float
    random_state: int | None = None

class RegimeHMM:
    def __init__(self, cfg: HMMConfig):
        self.model = GaussianHMM(
            n_components=cfg.n_components,
            covariance_type=cfg.covariance_type,
            n_iter=cfg.n_iter,
            tol=cfg.tol,
            random_state=cfg.random_state,
        )

    def fit(self, X: np.ndarray):
        self.model.fit(X)
        return self

    def predict_states(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)

    @property
    def transition_matrix(self):
        return self.model.transmat_
