# 🧠 Intelligent Document-Aware RAG System  
*A Beginner-Friendly, Production-Adjacent Retrieval-Augmented Generation Demo*

[![Demo](https://img.shields.io/badge/demo-local-orange)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.9+-green)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-ready-teal)]()

---

## 🚀 Elevator Pitch

**Intelligent Document-Aware RAG System** is a polished, practical **Retrieval-Augmented Generation (RAG)** demo that answers user questions **strictly from provided documents**, actively **minimizes hallucinations**, and includes **bias-evaluation tooling**.

Designed to be **production-adjacent and recruiter-friendly**, this project demonstrates:
- real-world NLP system design  
- ML engineering best practices  
- ethical and responsible AI workflows  

—all in a single, demo-ready repository.

---

## ❓ Why This Project Matters

Large Language Models can sound confident while being wrong.  
This project shows how to build a **trustworthy RAG system** that:

- 📌 Grounds answers in **explicit document passages**
- 🔎 Provides **source provenance** for every response
- 🛡️ Detects **unsupported claims**
- ⚖️ Includes **bias & fairness evaluation**
- 💻 Runs **fully locally** (no paid APIs required)

> This is how real-world RAG systems are built — not just prompt demos.

---

## ⭐ Key Features (What Recruiters Notice)

- 📄 Document ingestion pipeline (TXT / policy / academic-style docs)
- ✂️ Intelligent chunking with metadata tracking
- 🧠 Local **Sentence-Transformer embeddings**
- ⚡ **FAISS** vector index for fast semantic retrieval
- 🔀 Dual RAG modes:
  - **Extractive** (default, hallucination-resistant)
  - **Generative** (optional OpenAI, strict grounding)
- 🧾 Source-aware answers with citations
- 🛡️ Lightweight hallucination verifier (NER-based)
- ⚖️ Bias evaluation module (templated prompts)
- 🐳 Dockerized for one-command local deployment
- 🧼 Clean, modular, interview-ready codebase

---

## 📁 Project Structure

```text
rasg/
├── data/
│   ├── academic_paper.txt
│   ├── policy_brief.txt
│   ├── privacy_policy.txt
│   └── generate_sample_docs.py
│
├── indexes/
│   ├── embeddings.npy        # Stored embedding vectors
│   ├── faiss.index           # FAISS vector index
│   └── metadata.pkl          # Chunk metadata (source, text, ids)
│
├── src/
│   ├── __init__.py
│   ├── agent.py              # RAG orchestration logic
│   ├── retriever.py          # Vector retrieval (FAISS)
│   ├── ingest_and_index.py   # Ingestion + embedding + indexing
│   ├── server.py             # FastAPI application
│   ├── verifier.py           # Hallucination verification (NER-based)
│   ├── bias_eval.py          # Bias evaluation templates
│   ├── utils.py              # Helper utilities
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
````

---

## 🖥️ Quick Demo (What It Looks Like)

1. Start the FastAPI server
2. Send a query to `/query`
3. Receive:

   * ✅ **Answer** (grounded text)
   * 📚 **Sources** (document chunks + similarity scores)
   * 🛡️ **Verification report** (entity support check)

> 📸 
<img width="1241" height="756" alt="Screenshot 2026-01-22 170634" src="https://github.com/user-attachments/assets/7fbb777d-4dae-4f97-a95d-0740acfe9c40" />
<img width="1193" height="857" alt="Screenshot 2026-01-22 170704" src="https://github.com/user-attachments/assets/03a75183-e44c-48ff-9f25-cc302a1346e7" />






---

## 🛠️ Tech Stack & Skills Demonstrated

**Languages & Frameworks**

* Python, FastAPI

**ML & NLP**

* SentenceTransformers
* FAISS
* spaCy (NER)
* Dense embeddings & semantic search

**RAG Patterns**

* Retrieval-first QA
* Grounded generation
* Context-aware prompting
* Verification loops

**Ethics & Evaluation**

* Bias templating
* Hallucination detection
* AIF360-ready design

**DevOps**

* Docker
* docker-compose
* CI-ready project structure

---

## ⚡ Quickstart — Run Locally (30–60 Minutes)

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd rasg
```

### 2️⃣ Create & Activate Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ (Optional) Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5️⃣ Generate Sample Documents

```bash
python data/generate_sample_docs.py
```

### 6️⃣ Build FAISS Index

```bash
python src/ingest_and_index.py
```

### 7️⃣ Start the Server

```bash
uvicorn src.server:app --reload --host 0.0.0.0 --port 8000
```

### 8️⃣ Query the System

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query":"What is the data retention period?","top_k":2}'
```

---

⚠️ The model is **strictly instructed to use retrieved context only**.

---

## 🧩 How It Works (High-Level)

1. **Ingest** – Parse documents, chunk text, store metadata
2. **Embed** – Convert chunks into dense vectors
3. **Index** – Store vectors in FAISS
4. **Retrieve** – Fetch top-k relevant passages
5. **Answer**

   * Extractive → direct grounded text
   * Generative → controlled synthesis
6. **Verify** – Detect unsupported named entities
7. **Evaluate** – Run bias templates and log outputs

---
Made by Faisal Durrani
