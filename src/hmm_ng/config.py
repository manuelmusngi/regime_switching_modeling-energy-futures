from pathlib import Path
import yaml
from dataclasses import dataclass

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"

def load_yaml(name: str) -> dict:
    with open(CONFIG_DIR / name, "r") as f:
        return yaml.safe_load(f)

@dataclass
class Config:
    base: dict
    data: dict
    model: dict
    experiment: dict

def load_config() -> Config:
    return Config(
        base=load_yaml("base.yaml"),
        data=load_yaml("data.yaml"),
        model=load_yaml("model_hmm.yaml"),
        experiment=load_yaml("experiment_ng1_daily.yaml"),
    )
