"""
Ingest text files (and simple PDFs) from data/ and create a FAISS index.
Saves:
 - indexes/faiss.index (FAISS binary)
 - indexes/metadata.pkl    (list of {doc, chunk, start, end})
 - indexes/embeddings.npy  (numpy array of embeddings)
"""
import os
from pathlib import Path
import pdfplumber
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from src.utils import save_pickle, ensure_dir

DATA_DIR = Path("data")
INDEX_DIR = Path("indexes")
EMBED_MODEL_NAME = "all-mpnet-base-v2"
CHUNK_SIZE = 800  # characters per chunk

def extract_text(p: Path):
    if p.suffix.lower() == ".pdf":
        with pdfplumber.open(p) as pdf:
            pages = [page.extract_text() or "" for page in pdf.pages]
        return "\n".join(pages)
    else:
        return p.read_text(encoding="utf-8", errors="ignore")

def chunk_text(text, size=CHUNK_SIZE):
    text = text.strip()
    if not text:
        return []
    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i:i+size]
        chunks.append(chunk.strip())
        i += size
    return chunks

def main():
    ensure_dir(INDEX_DIR)
    model = SentenceTransformer(EMBED_MODEL_NAME)
    metas = []
    for p in DATA_DIR.glob("*"):
        if p.is_file() and p.suffix.lower() in {".txt", ".pdf", ".html", ".htm"}:
            text = extract_text(p)
            chunks = chunk_text(text)
            for i, c in enumerate(chunks):
                metas.append({"doc": str(p), "chunk": c, "chunk_id": f"{p.name}__{i}"})
    if not metas:
        print("No documents found in data/ — run data/generate_sample_docs.py")
        return
    texts = [m["chunk"] for m in metas]
    print(f"Encoding {len(texts)} chunks with model {EMBED_MODEL_NAME}...")
    emb = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    embeddings = np.array(emb).astype("float32")
    # Build FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, str(INDEX_DIR / "faiss.index"))
    np.save(INDEX_DIR / "embeddings.npy", embeddings)
    save_pickle(metas, INDEX_DIR / "metadata.pkl")
    print(f"Indexed {len(metas)} chunks into {INDEX_DIR.resolve()}")

if __name__ == "__main__":
    main()