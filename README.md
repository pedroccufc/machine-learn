# Machine Learning — Academic Portfolio

> Academic coursework and experiments from Computer Science studies. **These are not production systems.**

[![Archive validation](https://github.com/pedroccufc/machine-learn/actions/workflows/validate.yml/badge.svg)](https://github.com/pedroccufc/machine-learn/actions/workflows/validate.yml)

## Repository structure

```text
projects/
  bank_marketing/
    notebooks/          # Exploration and historical iterations, numbered
    data/               # Input dataset
    README.md
  enem/
    notebooks/          # ENEM analysis
    data/               # Train and test inputs
    docs/               # Supporting dictionaries
    README.md
coursework/
  notebooks/            # Numbered exercise submissions
  data/                 # Shared coursework datasets
  README.md
studies/
  notebooks/            # Concept notebooks and presentation
  README.md
assets/
  media/                # Historical reference material, not model training data
docs/
  MAINTENANCE.md
scripts/
  validate_repository.py
.github/workflows/
  validate.yml
```

## Explore the material

| Area | Description |
| --- | --- |
| [Bank Marketing](projects/bank_marketing/README.md) | Academic modeling notebooks and dataset |
| [ENEM](projects/enem/README.md) | Academic competition study and data dictionaries |
| [Coursework](coursework/README.md) | Numbered machine-learning exercises |
| [Concept studies](studies/README.md) | Classification metrics, distances and presentation |
| [Maintenance guide](docs/MAINTENANCE.md) | Reproducibility, data provenance and validation |

## Validation

Run `python scripts/validate_repository.py` from the repository root. This static check validates notebook JSON, required files, naming conventions, and local data references. GitHub Actions runs it automatically.

**This is not a notebook execution test.** These historical notebooks may require legacy Python/scikit-learn versions; their output cells are preserved and their model results have not been reproduced.

## Working with notebooks

Use each notebook's directory as its working directory, because data paths are relative to that location. For example:

```bash
cd projects/bank_marketing/notebooks
jupyter notebook 01_exploration.ipynb
```

Dependency installation, dataset licensing, and full reproducibility must be verified per project; no unsupported performance claims are made.

---

**Pedro Jr. · pedrojr.ds** — [GitHub profile](https://github.com/pedroccufc)
