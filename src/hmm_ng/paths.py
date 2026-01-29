from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def data_dir() -> Path:
    return ROOT / "data"

def interim_dir() -> Path:
    return data_dir() / "interim"

def processed_dir() -> Path:
    return data_dir() / "processed"
