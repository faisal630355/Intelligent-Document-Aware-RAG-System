# Utility helpers
import os
from pathlib import Path
import pickle
import numpy as np
import json

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def save_pickle(obj, path):
    ensure_dir(Path(path).parent)
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)