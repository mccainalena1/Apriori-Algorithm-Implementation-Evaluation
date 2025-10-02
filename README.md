# Apriori Algorithm: Implementation & Evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](requirements.txt)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](./)
[![Association Rules](https://img.shields.io/badge/Algorithm-Apriori-purple)](#-modeling-approach)

A clean, reproducible implementation of **Apriori** for mining frequent itemsets and **association rules**, with experiments on real/synthetic datasets and visual summaries of support, confidence, and lift.

---

## 📚 Table of Contents
- [📖 Project Overview](#-project-overview)
- [📂 Repository Structure](#-repository-structure)
- [⚡ Quickstart](#-quickstart)
- [📊 Data](#-data)
- [🧠 Modeling Approach](#-modeling-approach)
- [🎯 Results](#-results)
- [🌐 Visualizations](#-visualizations)
- [🔁 Reproducibility](#-reproducibility)
- [🚀 Next Steps](#-next-steps)
- [📜 License](#-license)
- [👤 Contact](#-contact)

---

## 📖 Project Overview
This project implements Apriori to discover frequent itemsets and generate association rules. It includes parameter sweeps for **min_support** and **min_confidence**, evaluation metrics (e.g., rule counts, average lift), and visualizations for easy comparison.

**Core features**
- Frequent itemset generation via Apriori
- Association rules with support, confidence, lift
- Parameter grid experiments & timing
- Clear visualizations and tabular summaries

---

## 📂 Repository Structure
```
.
├── src/                    # main source code (Apriori, driver, alternatives/)
│   ├── Apriori.py
│   ├── Driver.py
│   └── alternatives/
│       ├── apriori_with_htree.py
│       └── naive_apriori.py
├── notebooks/              # (optional) Jupyter notebooks
├── data/                   # datasets or samples (CSV/TXT/DAT)
├── results/                # outputs, tables, exports, and reports/slides
│   ├── Final_Paper.docx
│   └── Presentation.pptx
├── figures/                # charts/images
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```
## ⚡ Quickstart
1) **Clone & enter repo**
```bash
git clone https://github.com/mccainalena1/Apriori-Algorithm-Implementation-Evaluation.git
cd apriori-association-rules
```

2) **Install dependencies**
```bash
pip install -r requirements.txt
```

4) **Run script example**
```bash
python src/run_apriori.py --min_support 0.02 --min_confidence 0.3
```

---

## 📊 Data
Place small, non-sensitive CSV/TXT samples in `data/`. If you use large or proprietary datasets, keep them out of version control or use Git LFS.

---

## 🧠 Modeling Approach
- Preprocess transactions to a one-hot (basket) format.
- Mine frequent itemsets using **Apriori**.
- Generate association rules; compute **support**, **confidence**, **lift**.
- Evaluate parameter sweeps and summarize results.

If using **mlxtend**, see: `mlxtend.frequent_patterns.apriori` and `association_rules`.

---

## 🎯 Results
All summary tables/exports go into `results/`. Common artifacts:
- Frequent itemsets (`*_itemsets.csv`)
- Association rules (`*_rules.csv`)
- Timing/benchmark tables

---

## 🌐 Visualizations
Store charts in `figures/` (e.g., bar charts of rule counts vs. min_support; scatter of confidence vs. lift). Reference key images from the README for quick inspection.

---

## 🔁 Reproducibility
- Pin dependencies with `requirements.txt`.
- Keep notebooks/script execution **top-to-bottom**.
- Fix random seeds for synthetic data experiments when applicable.

---

## 🚀 Next Steps
- Add FP-Growth comparison.
- Hyperparameter search utilities.
- Interactive dashboard for rule browsing.

---

## 📜 License
MIT — see [LICENSE](LICENSE).

---

## 👤 Contact
Alena McCain — LinkedIn profile.