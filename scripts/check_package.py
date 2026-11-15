from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
for suffix, expected in [("", 16), ("-v2", 33)]:
    raw = (root / f"evidence/synthetic-events{suffix}.jsonl").read_bytes()
    rows = [json.loads(line) for line in raw.splitlines()]
    assert len(rows) == expected
    assert all(r["EvidenceType"] == "synthetic" for r in rows)
    provenance = json.loads((root / f"evidence/provenance{suffix}.json").read_text())
    assert hashlib.sha256(raw).hexdigest() == provenance["sha256"]
result = json.loads((root / "reports/validation-v2.json").read_text())
assert (result["cases"], result["passed"], result["failed"]) == (16, 16, 0)
patterns = [r"gh[pousr]_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{40,}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
for path in root.rglob("*"):
    if path.is_file() and path.suffix in {".md", ".kql", ".json", ".jsonl", ".txt"}:
        text = path.read_text()
        assert not any(re.search(pattern, text) for pattern in patterns), path
        if path.suffix == ".md":
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                if "://" not in link and not link.startswith("#"):
                    assert (path.parent / link.split("#")[0]).exists(), (path, link)
print("Package checks passed: fixture hashes, labels, result counts, links and credential patterns")
