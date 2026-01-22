# Retriever that loads FAISS index + metadata and returns top-k passages
from pathlib import Path
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from src.utils import load_pickle

INDEX_DIR = Path("indexes")
EMBED_MODEL_NAME = "all-mpnet-base-v2"

class Retriever:
    def __init__(self):
        idx_path = INDEX_DIR / "faiss.index"
        meta_path = INDEX_DIR / "metadata.pkl"
        emb_path = INDEX_DIR / "embeddings.npy"
        if not idx_path.exists():
            raise FileNotFoundError("Index not found. Run src/ingest_and_index.py first.")
        self.index = faiss.read_index(str(idx_path))
        self.metas = load_pickle(meta_path)
        self.embeddings = np.load(emb_path)
        self.embedder = SentenceTransformer(EMBED_MODEL_NAME)

    def retrieve(self, query: str, top_k: int = 3):
        qvec = self.embedder.encode([query], convert_to_numpy=True).astype("float32")
        D, I = self.index.search(qvec, top_k)
        res = []
        for idx, score in zip(I[0], D[0]):
            meta = self.metas[int(idx)].copy()
            meta["score"] = float(score)
            res.append(meta)
        return res