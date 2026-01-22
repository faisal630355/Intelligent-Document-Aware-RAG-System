# Basic hallucination detector: checks that named entities in the answer appear in retrieved passages.
# This is a starter heuristic (not a proof). For production, use stronger fact verification.
import spacy
from collections import Counter

try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None

def extract_entities(text):
    if nlp:
        doc = nlp(text)
        return [ent.text for ent in doc.ents]
    # fallback: naive capitalized token extraction
    tokens = [t for t in text.split() if t and t[0].isupper()]
    return tokens[:50]

def check_entities_in_sources(answer: str, sources: list):
    ans_ents = set(extract_entities(answer))
    source_text = " ".join([s["chunk"] for s in sources])
    source_ents = set(extract_entities(source_text))
    missing = [e for e in ans_ents if e not in source_ents]
    return {
        "answer_entities": list(ans_ents),
        "source_entities": list(source_ents),
        "missing_entities": missing,
        "is_supported": len(missing) == 0
    }