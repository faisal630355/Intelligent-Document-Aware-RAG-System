# Agent that composes extractive answers (and optional generative path using OpenAI)
import os
import textwrap
from typing import List
import openai

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

def make_extractive_answer(retrieved: List[dict]) -> str:
    # Build an extractive answer: concatenate top passages and mark sources
    parts = []
    for i, r in enumerate(retrieved, 1):
        header = f"[Source {i}] {r.get('doc')}"
        body = textwrap.fill(r.get("chunk")[:1000], width=100)
        parts.append(f"{header}\n{body}")
    answer = "\n\n".join(parts)
    return answer

def make_generative_answer(retrieved: List[dict], query: str) -> str:
    # Requires OPENAI_API_KEY
    if not OPENAI_KEY:
        raise RuntimeError("OpenAI key not found. Set OPENAI_API_KEY to use generative mode.")
    openai.api_key = OPENAI_KEY
    context = "\n\n".join([r["chunk"] for r in retrieved])
    prompt = f"You are a helpful assistant. Answer the user query using ONLY the provided context. If the context doesn't contain the answer, say 'I don't know based on the provided documents.'\n\nContext:\n{context}\n\nQuery: {query}\n\nAnswer:"
    # Use a stable model name; change if you have a specific model.
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role":"user","content":prompt}],
        max_tokens=400,
        temperature=0.0,
    )
    return resp["choices"][0]["message"]["content"].strip()