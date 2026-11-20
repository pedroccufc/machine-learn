#!/usr/bin/env python3
"""Static structure checks for the historical academic notebook archive.

Does not run notebook cells or make claims about the results in those notebooks.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "projects/bank-marketing/bank_marketing.ipynb",
    "projects/bank-marketing/bank-additional-full.csv",
    "projects/enem/ENEM.ipynb",
    "projects/enem/train.csv",
    "projects/enem/test.csv",
    "notebooks/metrics-to-classification.ipynb",
    "notebooks/Distancia_Cosseno.ipynb",
    "notebooks/Medidas_de_Distancia.ipynb",
    "notebooks/presentation.ipynb",
    "exercises/list_07.ipynb",
    "exercises/list_08.ipynb",
    "datasets/wdbc.data",
    "datasets/iris.data",
]
# A focused set of relative CSV reads verified during migration.
INPUTS = {
    "projects/bank-marketing/bank_marketing.ipynb": ["bank-additional-full.csv"],
    "projects/bank-marketing/versao-final.ipynb": ["bank-additional-full.csv"],
    "projects/bank-marketing/versao1.ipynb": ["bank-additional-full.csv"],
    "projects/bank-marketing/versao2.ipynb": ["bank-additional-full.csv"],
    "projects/enem/ENEM.ipynb": ["train.csv"],
    "exercises/list_07.ipynb": ["../datasets/wdbc.data"],
    "exercises/list_08.ipynb": ["../datasets/iris.data"],
    "exercises/list_09.ipynb": ["../datasets/iris.data"],
    "exercises/list_10.ipynb": ["../datasets/movie_data.csv"],
    "exercises/list_11.ipynb": ["../datasets/adult.data"],
    "exercises/list_12_1.ipynb": ["../datasets/wdbc.data"],
    "exercises/list_12_2.ipynb": ["../datasets/data_1024.csv"],
}


def check():
    errors = []
    for path in REQUIRED:
        if not (ROOT / path).is_file():
            errors.append(f"Missing expected file: {path}")

    notebooks = sorted(ROOT.rglob("*.ipynb"))
    if not notebooks:
        errors.append("No notebooks were found")

    for path in notebooks:
        rel = path.relative_to(ROOT).as_posix()
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
                errors.append(f"Unexpected notebook structure: {rel}")
                continue
            code = "\n".join(
                "".join(cell.get("source", []))
                if isinstance(cell.get("source"), list)
                else cell.get("source", "")
                for cell in notebook["cells"]
                if cell.get("cell_type") == "code"
            )
            for reference in INPUTS.get(rel, []):
                if reference not in code:
                    errors.append(f"Expected input path missing from code: {rel}: {reference}")
                if not (path.parent / reference).is_file():
                    errors.append(f"Unresolved input path: {rel}: {reference}")
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"Cannot parse {rel}: {exc}")
    if errors:
        for message in errors:
            print("ERROR:", message)
        raise SystemExit(1)
    print(f"OK: {len(notebooks)} notebook files validated; selected data paths resolve.")


if __name__ == "__main__":
    check()
