# Simple sample doc generator so you start with real files.
from pathlib import Path

SAMPLES = {
    "privacy_policy.txt": """Privacy Policy
This Privacy Policy describes how ExampleOrg collects and uses information. Data retention: We retain user data for up to 3 years unless otherwise required by law. Data sharing: We do not sell personal data. Contact: privacy@example.org.""",
    "academic_paper.txt": """Paper: Responsible AI
Abstract: This paper explores fairness metrics and bias mitigation in language models. We evaluate demographic parity and disparate impact, and propose mitigation techniques.""",
    "policy_brief.txt": """Policy Brief: Data Protection Act
Summary: The Data Protection Act requires organizations to provide transparency on data usage, to enable data subjects to request deletion. Exceptions include legal holds and public safety concerns."""
}

def main(out_dir="data"):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for fn, text in SAMPLES.items():
        p = out / fn
        p.write_text(text)
    print(f"Wrote {len(SAMPLES)} sample documents to {out.resolve()}")

if __name__ == "__main__":
    main()