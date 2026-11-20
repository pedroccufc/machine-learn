# Maintenance and reproducibility notes

This repository is a **historical academic archive**, not a production ML codebase. Its existing notebooks and datasets have been reorganized by purpose while preserving notebook cell outputs and keeping project inputs alongside their notebooks.

## Current organization

| Path | Material |
| :--- | :--- |
| `notebooks/` | Distance measures and classification evaluation |
| `exercises/` | Coursework and practice notebooks |
| `projects/bank-marketing/` | Bank marketing notebooks, dataset and version history |
| `projects/enem/` | ENEM notebook and supporting materials |
| `datasets/` | Datasets and an auxiliary media file |
| `notebooks/presentation.ipynb` | Presentation notebook |

## Reproducibility

- Open each notebook and check imports, Python dependencies, and input paths before running.
- Execute old notebooks in an isolated Python environment; modern package versions may behave differently.
- Notebook outputs may reflect the environment and state at the time of the original work, and should not be interpreted as freshly reproduced results.
- The repository does not currently contain a verified, shared dependency lockfile for every notebook.
- Jupyter-generated `.ipynb_checkpoints` entries were removed; the original notebooks remain.

## Larger assets

- `datasets/movie_data.csv` is approximately **65.9 MB**.
- `datasets/placa-nova-mercosul-tudo-sobre.mp4` is approximately **14.2 MB**.
- `projects/enem/train.csv` is approximately **12 MB**.
- `projects/bank-marketing/bank-additional-full.csv` is approximately **5.8 MB**.

These assets remain tracked in the repository. Before moving or removing them, inspect notebook references, source licenses, and whether each file is required for reproducing the academic work.

## Recommended future modernization

1. Audit notebook imports and file dependencies.
2. Create reproducible, **per-project** dependency specifications after verifying package compatibility.
3. Separate stable datasets from generated model outputs where appropriate.
4. Refactor notebooks into scripts only if that improves reuse and retains their educational value.
5. Add execution tests and sample data to selected projects, without inventing performance results.

This document is an inventory and maintenance guide, **not a claim that all notebooks have been executed or validated**.

[Back to the repository](../README.md)
