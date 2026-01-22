# Minimal FastAPI server providing query endpoint
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.retriever import Retriever
from src.agent import make_extractive_answer, make_generative_answer
from src.verifier import check_entities_in_sources

app = FastAPI(title="Document-Aware RAG Demo")

class Query(BaseModel):
    query: str
    top_k: int = 3
    mode: str = "extractive"  # or "generative"

@app.on_event("startup")
def startup_event():
    global RETRIEVER
    RETRIEVER = Retriever()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/query")
def query(q: Query):
    try:
        hits = RETRIEVER.retrieve(q.query, top_k=q.top_k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if q.mode == "generative":
        try:
            answer = make_generative_answer(hits, q.query)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        answer = make_extractive_answer(hits)
    verification = check_entities_in_sources(answer, hits)
    return {"answer": answer, "sources": hits, "verification": verification}