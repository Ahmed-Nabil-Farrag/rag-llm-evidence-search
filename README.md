# Blind Spots in AI-Assisted Healthcare Evidence Search

Analysis code for **"Blind Spots in AI-Assisted Healthcare Evidence Search: Retrieval Gaps and Risk of Bias."**

This repository contains the Jupyter notebook used to preprocess the data, run the statistical
analyses, and generate all figures for the study. The analyses were run on the University of
Florida HiperGator cluster.

## Contents

| Path | Description |
|---|---|
| `notebooks/analysis_notebook.ipynb` | Full analysis notebook (25 cells + environment report) |
| `environment_report.py` | First-cell script that records exact Python/package versions |
| `requirements.txt` | Package dependencies |
| `index.html` | Rendered, read-only view of the notebook (GitHub Pages) |

## Reproducing the analysis

1. Create an environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open `notebooks/analysis_notebook.ipynb` and run **Cell 00 — Environment Report** first.
   It prints the Python and package versions and writes `environment.txt`.
3. Run the remaining cells in order.

## Software environment

Analyses were performed on the University of Florida HiperGator cluster in Python 3.9.23 using
pandas 2.3.1, NumPy 2.0.2, SciPy 1.13.1, statsmodels 0.14.5, scikit-learn 1.6.1, Matplotlib 3.9.4,
seaborn 0.13.2, and Plotly 6.3.1. These versions are pinned in `requirements.txt` and `environment.txt`,
and are printed by `environment_report.py`.

## Figures

All figures in the manuscript and supplementary materials are the authors' own original work,
generated directly by this code.

## Citation

Farrag, A. N., Soliman, A., Azubuike, C., Zandbiglari, K., Yadavilli, S., Adkins, L. E.,
Mehrabi, F., Cavallari, L., Goodin, A., & Rouhizadeh, M. *Blind Spots in AI-Assisted
Healthcare Evidence Search: Retrieval Gaps and Risk of Bias.*

## License

Code released under the MIT License (see `LICENSE`).
