from pathlib import Path
import yaml
from dataclasses import dataclass

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"

def _load(name: str) -> dict:
    with open(CONFIG_DIR / name) as f:
        return yaml.safe_load(f)

@dataclass
class Config:
    base: dict
    data: dict
    model: dict

def load_config() -> Config:
    return Config(
        base=_load("base.yaml"),
        data=_load("data.yaml"),
        model=_load("model_hmm.yaml"),
    )

