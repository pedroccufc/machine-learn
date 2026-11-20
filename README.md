<div align="center">

# Machine Learning · Academic Portfolio

**Academic projects · Exercises · Jupyter notebooks · Data exploration**

A curated archive of coursework and learning experiments from my Computer Science studies. These notebooks document exploration and learning, not production-ready models.

[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white)](notebooks)
[![Python](https://img.shields.io/badge/Python-Studies-3776AB?style=flat-square&logo=python&logoColor=white)](.)

</div>

---

## Repository structure

```text
machine-learn/
├── projects/
│   ├── bank-marketing/         # Academic project, notebooks and CSV
│   └── enem/                   # ENEM study, notebook, CSVs and dictionaries
├── exercises/                  # Course assignments
├── notebooks/                  # Foundational studies and presentation
├── datasets/                   # Shared reference data and media
├── docs/
│   └── MAINTENANCE.md          # Reproducibility notes
├── scripts/
│   └── validate_repository.py  # Static repository checks
└── .github/workflows/          # Automated static checks
```

## Explore

| Category | Material |
| :--- | :--- |
| [Bank Marketing](projects/bank-marketing/README.md) | Coursework, historical notebook versions, input CSV |
| [ENEM](projects/enem/README.md) | ENEM study notebook, inputs, dictionaries |
| [Course exercises](exercises) | Lists 07–12, classification and modeling exercises |
| [Concept notebooks](notebooks) | Distance measures, cosine similarity, classification metrics |
| [Reference datasets](datasets/README.md) | Shared data and auxiliary media |
| [Maintenance guide](docs/MAINTENANCE.md) | Compatibility, dataset notes and reproducibility |

## Selected notebooks

- [Classification metrics](notebooks/metrics-to-classification.ipynb)
- [Cosine distance](notebooks/Distancia_Cosseno.ipynb)
- [Distance measures](notebooks/Medidas_de_Distancia.ipynb)
- [Bank marketing](projects/bank-marketing/bank_marketing.ipynb)
- [ENEM](projects/enem/ENEM.ipynb)
- [Presentation](notebooks/presentation.ipynb)

## Reproducibility

The notebook files and data are preserved, with historical outputs untouched. Relative paths typically assume the notebook's own directory as working directory. Execute individual notebooks in isolated environments and verify dependencies before running.

The [automated checks](scripts/validate_repository.py) verify **file structure, notebook JSON and selected input-path references**. They do not execute notebook cells, install historical ML libraries or validate model performance.

## Academic context

This portfolio preserves historical coursework. Some material may follow third-party exercises or contain externally sourced datasets; consult the individual assignments and verify dataset licenses before reuse.

---

<div align="center">

**Pedro Jr. · Data Science & Machine Learning**

[GitHub profile](https://github.com/pedroccufc)

</div>
