```markdown
# Intelligent Document-Aware RAG System (Beginner-friendly)

Overview
- Local demo of a Retrieval‑Augmented system that answers questions strictly from provided documents.
- Works out-of-the-box using local SentenceTransformers embeddings + FAISS.
- Two modes:
  - extractive (default): answer is strictly composed of retrieved passages (no external LLM).
  - generative (optional): uses OpenAI to synthesize an answer from retrieved passages (requires OPENAI_API_KEY).

What’s included
- sample data generator (creates a few policy/academic/legal-style text files)
- ingestion & chunking pipeline -> FAISS index + metadata
- FastAPI server providing /query and /health endpoints
- verifier module to detect likely hallucinations (basic NER-check)
- bias-evaluation script with templated prompts
- Dockerfile and docker-compose for local deployment

Quickstart (local, recommended for beginners)
1. Clone or create a directory and copy the repository files into it.
2. Create a Python virtual environment:
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows PowerShell
3. Install dependencies:
   pip install -r requirements.txt
4. (Optional) download spaCy model:
   python -m spacy download en_core_web_sm
5. Generate sample documents and build index:
   python data/generate_sample_docs.py
   python src/ingest_and_index.py
6. Run the API:
   uvicorn src.server:app --reload --host 0.0.0.0 --port 8000
7. Query (example):
   curl -X POST "http://localhost:8000/query" -H "Content-Type: application/json" -d '{"query":"What does the privacy policy say about data retention?", "top_k":3}'
8. To use generative mode (OpenAI):
   export OPENAI_API_KEY=sk-...
   set OPENAI_API_KEY=sk-...  # Windows
   Then restart the server. The server will detect OPENAI_API_KEY and use the generative path.

Files and structure
- data/
  - generate_sample_docs.py            # creates simple sample docs
- indexes/
  - (created by ingestion step)
- src/
  - ingest_and_index.py                # ingestion + FAISS building
  - retriever.py                       # retrieval helper
  - agent.py                           # generation wrappers (extractive + optional generative)
  - verifier.py                        # hallucination check (basic)
  - bias_eval.py                       # bias tests (templated)
  - server.py                          # FastAPI server
  - utils.py                           # helpers
- Dockerfile
- docker-compose.yml
- requirements.txt

What the demo guarantees
- In extractive mode the “answer” is built only from the retrieved text passages; this avoids LLM hallucination because no new facts are invented.
- Verifier does a quick NER-based check to detect claims about entities not present in retrieved sources (basic sanity check).
- Bias evaluator runs templated prompts and records whether answers include explicit demographic stereotyping (starter set; extendable).

Next steps after you’re comfortable
- Replace sample docs with your own corpus (PDFs/HTML/TXT). The ingestion script supports text and simple PDF extraction.
- Swap FAISS to a managed vector DB like Pinecone or Weaviate if scaling beyond a single machine.
- Plug in a different embedding model (OpenAI or a larger SentenceTransformers model).
- For production, add authentication, logging, monitoring, CI, and rate limits.

If you want, I can:
- Prepare CI workflows and GitHub Actions (you requested this earlier) — add secrets in repo Settings when ready.
- Implement advanced bias metrics, AIF360 integration, and a web frontend.
- Set up a small Kubernetes manifest and Helm chart for cloud deployment.

If you need anything simplified further, say “Make it simpler” and I will reduce the steps even more.
```