# Maintenance, Reproducibility and Data Provenance

This repository is an **academic archive**. The November 2026 refactor standardized names and paths without re-running historic ML experiments.

## Conventions

- All project, study, and notebook names use `snake_case`.
- Independent projects live in `projects/<project>/` with their own `notebooks/`, `data/`, documentation and README.
- Course lists share data in `coursework/data/` and use `coursework/notebooks/`.
- General concept notebooks live in `studies/notebooks/`.
- Non-ML reference media is stored separately in `assets/media/`.
- Source datasets and notebook outputs are not silently regenerated or removed.
- Each notebook's working directory is its own `notebooks/` folder.

## Historical migrations

| Old location | New location |
| --- | --- |
| `final_job/` | `projects/bank_marketing/` |
| `competition-kaggle/` | `projects/enem/` |
| `exercise_lists/`, `exercises/` | `coursework/notebooks/` |
| `datasets/` | `coursework/data/` |
| `notebooks/` | `studies/notebooks/` |

Some source files have been renamed. Git preserves their original versions in the commit history.

## Files with special considerations

- `coursework/data/movie_data.csv` is approximately 65.9 MB.
- `assets/media/mercosul_license_plate.mp4` is approximately 14.2 MB, and is not a training dataset.
- `projects/enem/data/train.csv` is approximately 12 MB.
- `projects/bank_marketing/data/bank_marketing.csv` is approximately 5.8 MB.

No legal rights are inferred from the fact that these files were historically committed. Check their provenance and licenses before redistribution.

## Validation and limitations

Run `python scripts/validate_repository.py` or inspect the GitHub Actions checks. The standard-library script parses every notebook and checks expected source/data files and selected relative input paths. It **does not execute notebook cells** or claim modern Python, scikit-learn, or pandas compatibility.

If you later modernize notebooks, introduce versioned per-project environment specifications, write small repeatable smoke tests, and document new experiments separately from historical results.

[Return to main README](../README.md)
