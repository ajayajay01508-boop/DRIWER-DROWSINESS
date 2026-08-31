"""Evaluate predictions without inventing metrics: CSV columns must be y_true,y_pred."""
import argparse, csv, json
from pathlib import Path


def evaluate(rows):
    tp = tn = fp = fn = 0
    for row in rows:
        y, p = int(row["y_true"]), int(row["y_pred"])
        if y not in (0, 1) or p not in (0, 1):
            raise ValueError("labels must be 0 or 1")
        tp += y == 1 and p == 1; tn += y == 0 and p == 0
        fp += y == 0 and p == 1; fn += y == 1 and p == 0
    n = tp + tn + fp + fn
    if not n: raise ValueError("no evaluation rows")
    return {"samples": n, "accuracy": (tp+tn)/n, "precision": tp/(tp+fp) if tp+fp else 0,
            "recall": tp/(tp+fn) if tp+fn else 0, "confusion_matrix": [[tn, fp], [fn, tp]]}


if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--out", default="artifacts/metrics.json")
    a=ap.parse_args()
    with open(a.csv, newline="") as f: result=evaluate(csv.DictReader(f))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True); Path(a.out).write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
