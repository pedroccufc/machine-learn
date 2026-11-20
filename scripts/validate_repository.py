#!/usr/bin/env python3
"""Static integrity checks for this historical academic ML archive.

Uses only the Python standard library. Does not execute notebook cells or
claim to reproduce historical ML results.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS = [
    "projects/bank_marketing/notebooks/01_exploration.ipynb",
    "projects/bank_marketing/notebooks/02_iteration.ipynb",
    "projects/bank_marketing/notebooks/03_iteration.ipynb",
    "projects/bank_marketing/notebooks/04_final.ipynb",
    "projects/enem/notebooks/enem_analysis.ipynb",
    "coursework/notebooks/exercise_07.ipynb",
    "coursework/notebooks/exercise_08.ipynb",
    "coursework/notebooks/exercise_09.ipynb",
    "coursework/notebooks/exercise_10.ipynb",
    "coursework/notebooks/exercise_11.ipynb",
    "coursework/notebooks/exercise_12_part_1.ipynb",
    "coursework/notebooks/exercise_12_part_2.ipynb",
    "studies/notebooks/classification_metrics.ipynb",
    "studies/notebooks/cosine_distance.ipynb",
    "studies/notebooks/distance_measures.ipynb",
    "studies/notebooks/presentation.ipynb",
]

DATA_FILES = [
    "projects/bank_marketing/data/bank_marketing.csv",
    "projects/enem/data/train.csv",
    "projects/enem/data/test.csv",
    "projects/enem/docs/enem_2016_dictionary.ods",
    "projects/enem/docs/enem_2016_dictionary.xlsx",
    "coursework/data/adult.data",
    "coursework/data/adult.names",
    "coursework/data/iris.data",
    "coursework/data/wdbc.data",
    "coursework/data/data_1024.csv",
    "coursework/data/movie_data.csv",
    "assets/media/mercosul_license_plate.mp4",
]

DATA_REFERENCES = {
    "projects/bank_marketing/notebooks/01_exploration.ipynb": ["../data/bank_marketing.csv"],
    "projects/bank_marketing/notebooks/02_iteration.ipynb": ["../data/bank_marketing.csv"],
    "projects/bank_marketing/notebooks/03_iteration.ipynb": ["../data/bank_marketing.csv"],
    "projects/bank_marketing/notebooks/04_final.ipynb": ["../data/bank_marketing.csv"],
    "projects/enem/notebooks/enem_analysis.ipynb": ["../data/train.csv"],
    "coursework/notebooks/exercise_07.ipynb": ["../data/wdbc.data"],
    "coursework/notebooks/exercise_08.ipynb": ["../data/iris.data"],
    "coursework/notebooks/exercise_09.ipynb": ["../data/iris.data"],
    "coursework/notebooks/exercise_10.ipynb": ["../data/movie_data.csv"],
    "coursework/notebooks/exercise_11.ipynb": ["../data/adult.data"],
    "coursework/notebooks/exercise_12_part_1.ipynb": ["../data/wdbc.data"],
    "coursework/notebooks/exercise_12_part_2.ipynb": ["../data/data_1024.csv"],
}

OTHER_FILES = [
    "README.md",
    "projects/bank_marketing/README.md",
    "projects/enem/README.md",
    "coursework/README.md",
    "coursework/data/README.md",
    "studies/README.md",
    "docs/MAINTENANCE.md",
    ".editorconfig",
    ".github/workflows/validate.yml",
]

# Keep historical binary assets, but enforce consistent names for notebooks
# and selected directories without falsely assuming the source datasets are ours.
SNAKE_CASE_NAME = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*\.ipynb$")
OLD_DIRECTORIES = {"datasets", "exercises", "exercise_lists", "final_job", "competition-kaggle"}


def validate():
    problems = []
    for path in NOTEBOOKS + DATA_FILES + OTHER_FILES:
        if not (ROOT / path).is_file():
            problems.append("Missing file: " + path)

    for directory in OLD_DIRECTORIES:
        if (ROOT / directory).exists():
            problems.append("Legacy directory still present: " + directory)

    existing = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.ipynb")}
    expected = set(NOTEBOOKS)
    for unexpected in sorted(existing - expected):
        problems.append("Unexpected notebook not documented in inventory: " + unexpected)

    for rel in NOTEBOOKS:
        path = ROOT / rel
        if not path.is_file():
            continue
        if not SNAKE_CASE_NAME.fullmatch(path.name):
            problems.append("Notebook name does not follow snake_case: " + rel)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("nbformat") != 4 or not isinstance(data.get("cells"), list):
                problems.append("Invalid Jupyter v4 structure: " + rel)
                continue
            code = "\n".join(
                "".join(c.get("source", [])) if isinstance(c.get("source"), list)
                else c.get("source", "")
                for c in data["cells"] if c.get("cell_type") == "code"
            )
            for link in DATA_REFERENCES.get(rel, []):
                if link not in code:
                    problems.append(f"Code input reference missing: {rel} -> {link}")
                if not (path.parent / link).is_file():
                    problems.append(f"Broken local data reference: {rel} -> {link}")
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            problems.append(f"Could not parse notebook {rel}: {exc}")

    if problems:
        print("\n".join("ERROR: " + p for p in problems))
        raise SystemExit(1)

    print(f"OK: {len(NOTEBOOKS)} notebooks and {len(DATA_FILES)} data/media files checked.")
    print("Note: no notebook cells were executed.")


if __name__ == "__main__":
    validate()
