# Validation status

## Audited source

The supplied `EAR.ipynb` loads `n7i5x9/driver-drowsiness-dataset`. Its saved, successful output reports:

| Split | Images |
|---|---:|
| Train | 18,492 |
| Validation | 2,321 |
| Test | 2,313 |
| Total | 23,126 |

The notebook's later 90% plot is generated from formulas and a manually constructed confusion matrix. It is **not measured model accuracy** and is intentionally excluded as proof. The notebook also trains on synthetic data in cells 13 and 15; those scores are not real-world validation.

## Reproducible proof requirement

Run inference on the untouched 2,313-image test split and save `y_true,y_pred` to CSV. Then run:

```bash
python scripts/evaluate.py predictions.csv --out artifacts/metrics.json
```

Only the resulting test metrics should be described as accuracy. A 100,000+ claim requires a separately identified, license-compatible dataset and a documented split; augmentation must not be represented as 100,000 unique source images.
