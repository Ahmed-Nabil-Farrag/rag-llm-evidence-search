# Blind Spots in AI-Assisted Healthcare Evidence Search

Analysis code and data for "Blind Spots in AI-Assisted Healthcare Evidence Search:
Multiplatform Evaluation of Clinical Retrieval Gaps and Risk-of-Bias," published in
*npj Digital Medicine*.

**DOI:** [10.1038/s41746-026-03277-y](https://doi.org/10.1038/s41746-026-03277-y)

This repository contains the Jupyter notebook used to preprocess the data, run the
statistical analyses, and generate all figures for the study, together with the raw
and processed retrieval outputs and the complete candidate-level matching dataset.
The analyses were run on the University of Florida HiPerGator cluster.

## Citation

> Farrag, A. N., Soliman, A., Azubuike, C., Zandbiglari, K., Yadavilli, S.,
> Adkins, L. E., Mehrabi, F., Cavallari, L., Goodin, A., & Rouhizadeh, M. (2026).
> Blind Spots in AI-Assisted Healthcare Evidence Search: Multiplatform Evaluation of
> Clinical Retrieval Gaps and Risk-of-Bias. *npj Digital Medicine*.
> https://doi.org/10.1038/s41746-026-03277-y

```bibtex
@article{Farrag2026BlindSpots,
  author  = {Farrag, Ahmed N. and Soliman, Ahmed and Azubuike, Chidimma and
             Zandbiglari, Kimia and Yadavilli, Surya and Adkins, Lauren E. and
             Mehrabi, Fatemeh and Cavallari, Larisa and Goodin, Amie and
             Rouhizadeh, Masoud},
  title   = {Blind Spots in {AI}-Assisted Healthcare Evidence Search:
             Multiplatform Evaluation of Clinical Retrieval Gaps and Risk-of-Bias},
  journal = {npj Digital Medicine},
  year    = {2026},
  doi     = {10.1038/s41746-026-03277-y}
}
```

GitHub's "Cite this repository" button reads `CITATION.cff` in this repository and
returns the same reference.

## Authors

Ahmed N. Farrag<sup>1\*</sup>, Ahmed Soliman<sup>1,2</sup>, Chidimma Azubuike<sup>1</sup>,
Kimia Zandbiglari<sup>1</sup>, Surya Yadavilli<sup>1,3</sup>, Lauren E. Adkins<sup>4</sup>,
Fatemeh Mehrabi<sup>1</sup>, Larisa Cavallari<sup>5,6</sup>, Amie Goodin<sup>1,7</sup>,
Masoud Rouhizadeh<sup>1,7,8\*</sup>

1. Department of Pharmaceutical Outcomes and Policy, College of Pharmacy, University of Florida, Gainesville, FL, USA
2. Department of Health Outcomes & Biomedical Informatics, University of Florida, Gainesville, FL, USA
3. Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, FL, USA
4. Health Science Center Libraries, University of Florida, Gainesville, FL, USA
5. Department of Pharmacotherapy and Translational Research, College of Pharmacy, University of Florida, Gainesville, FL, USA
6. Center for Pharmacogenomics and Precision Medicine, University of Florida, Gainesville, FL, USA
7. Center for Drug Evaluation and Safety (CoDES), University of Florida, Gainesville, FL, USA
8. Division of Health Sciences Informatics, Johns Hopkins University, Baltimore, MD, USA

\* Corresponding authors: Masoud Rouhizadeh (mrou@cop.ufl.edu, ORCID
[0000-0002-9006-6112](https://orcid.org/0000-0002-9006-6112)); Ahmed N. Farrag
(ahmed.farrag@ufl.edu, ORCID [0000-0001-9241-0127](https://orcid.org/0000-0001-9241-0127))

## Study at a glance

Five publicly accessible retrieval-augmented and LLM-based evidence-search platforms
(Ai2 Paper Finder, Consensus, ChatGPT-4.1, Gemini-2.5-Pro, Claude-Sonnet-4.0) were
evaluated against a prospectively assembled, PRISMA-guided gold standard of 83 studies
that was not publicly released as a curated benchmark at the time of evaluation. Each
platform was queried with 15 prompt formulations (5 strategies x 3 wording variations),
each executed in triplicate, for 225 total executions.

## Contents

| Path | Description |
|------|-------------|
| `notebooks/analysis_notebook.ipynb` | Full analysis notebook (26 cells, including the environment report) |
| `matching/01_primary_matches_analysis.csv` | Candidate-level adjudication, primary matches at or above the 60% screen (n = 2,344 pairs) |
| `matching/02_sensitivity_analysis_20to60.csv` | Candidate-level adjudication, 20-60% threshold-sensitivity sweep (n = 9,815 pairs) |
| `environment_report.py` | First-cell script that records exact Python/package versions |
| `requirements.txt` | Package dependencies |
| `environment.txt` | Pinned environment as recorded at run time |
| `docs/index.html` | Rendered, read-only view of the notebook (GitHub Pages) |
| `Raw Run Files.zip` | Raw, unprocessed platform outputs (see Data) |
| `Pooled Std Raw and Recall Files 28 Sep.zip` | Standardized and gold-standard-matched outputs (see Data) |
| `LICENSE` | MIT License |

## Data

Two archives capture the full pipeline from platform response to analysis-ready data:

- **`Raw Run Files.zip`** - the raw, verbatim outputs returned by each of the five
  platforms across all 15 prompt formulations and 3 independent runs, before any
  cleaning or normalization.

- **`Pooled Std Raw and Recall Files 28 Sep.zip`** - the processed, pooled data in two
  stages: (1) **standardized** files, parsed and normalized from the raw platform
  outputs into a consistent citation schema; and (2) **recall (matched)** files, in
  which the standardized citations were matched against the 83-study gold-standard
  corpus. These matched files are the direct input to `analysis_notebook.ipynb`.

The `matching/` directory holds the candidate-level adjudication dataset in full: every
candidate pair of a platform-returned title and a gold-standard study, with the
title-overlap score and the adjudication outcome. This is the dataset reported as
Supplementary Data 1 in the published article.

### How matching works

Platform outputs were matched to the gold standard by title overlap, quantified as the
Jaccard similarity of normalized title-word sets. An initial 60% screen generated
candidate pairs; exact matches were accepted automatically and non-identical candidates
were adjudicated for study identity by consensus. Because the score compares literal
words, a record that abbreviates part of a title scores below 100% even when it names
the same study, so recognized abbreviations were expanded before the titles were
compared again at adjudication. Candidate pairs were then re-examined down to 20%
overlap; no confirmed match fell below 42.9%, and 40% was adopted as the operational
threshold.

## Reproducing the analysis

```bash
git clone https://github.com/Ahmed-Nabil-Farrag/rag-llm-evidence-search.git
cd rag-llm-evidence-search
python -m pip install -r requirements.txt
jupyter lab notebooks/analysis_notebook.ipynb
```

Unzip both data archives into the directory the notebook reads from, then run the cells
in order. The first cell writes `environment.txt` with the exact versions in use.

Figure export requires `kaleido==0.2.1`. Later releases of kaleido expect a separately
installed Google Chrome; version 0.2.1 ships its own renderer and needs nothing else.

## Environment

Python 3.9.23 with pandas 2.3.1, NumPy 2.0.2, SciPy 1.13.1, statsmodels 0.14.5,
scikit-learn 1.6.1, Matplotlib 3.9.4, seaborn 0.13.2, Plotly 6.3.1 and kaleido 0.2.1.
Exact pins are in `requirements.txt`.

## License

Released under the MIT License. See `LICENSE`.
