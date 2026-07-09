# Blind Spots in AI-Assisted Healthcare Evidence Search

Analysis code and data for "Blind Spots in AI-Assisted Healthcare Evidence
Search: Multiplatform Evaluation of Clinical Retrieval Gaps and Risk-of-Bias."

This repository contains the Jupyter notebook used to preprocess the data,
run the statistical analyses, and generate all figures for the study, together
with the raw and processed retrieval outputs. The analyses were run on the
University of Florida HiperGator cluster.

## Authors

Ahmed N. Farrag¹*, Ahmed Soliman¹˒², Chidimma Azubuike¹, Kimia Zandbiglari¹,
Surya Yadavilli¹˒³, Lauren E. Adkins⁴, Fatemeh Mehrabi¹, Larisa Cavallari⁵˒⁶,
Amie Goodin¹˒⁷, Masoud Rouhizadeh¹˒⁷˒⁸*

1. Department of Pharmaceutical Outcomes and Policy, College of Pharmacy, University of Florida, Gainesville, FL, USA
2. Department of Health Outcomes & Biomedical Informatics, University of Florida, Gainesville, FL, USA
3. Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, FL, USA
4. Health Science Center Libraries, University of Florida, Gainesville, FL, USA
5. Department of Pharmacotherapy and Translational Research, College of Pharmacy, University of Florida, Gainesville, FL, USA
6. Center for Pharmacogenomics and Precision Medicine, University of Florida, Gainesville, FL, USA
7. Center for Drug Evaluation and Safety (CoDES), University of Florida, Gainesville, FL, USA
8. Division of Health Sciences Informatics, Johns Hopkins University, Baltimore, MD, USA

\* Corresponding authors: Masoud Rouhizadeh (mrou@cop.ufl.edu, ORCID 0000-0002-9006-6112); Ahmed N. Farrag (ahmed.farrag@ufl.edu, ORCID 0000-0001-9241-0127)

## Contents

| Path | Description |
|------|-------------|
| `notebooks/analysis_notebook.ipynb` | Full analysis notebook (25 cells + environment report) |
| `environment_report.py` | First-cell script that records exact Python/package versions |
| `requirements.txt` | Package dependencies |
| `index.html` | Rendered, read-only view of the notebook (GitHub Pages) |
| `Raw Run Files.zip` | Raw, unprocessed platform outputs (see Data) |
| `Pooled Std Raw and Recall Files 28 Sep.zip` | Standardized and gold-standard-matched outputs (see Data) |

## Data

Two archives capture the full pipeline from platform response to analysis-ready data:

- **`Raw Run Files.zip`** - the raw, verbatim outputs returned by each of the five
  platforms (Ai2 Paper Finder, Consensus, ChatGPT-4.1, Gemini-2.5-Pro,
  Claude-Sonnet-4.0) across all 15 prompt formulations and 3 independent runs, before
  any cleaning or normalization.

- **`Pooled Std Raw and Recall Files 28 Sep.zip`** - the processed, pooled data in two
  stages: (1) **standardized** files, parsed and normalized from the raw platform
  outputs into a consistent citation schema; and (2) **recall (matched)** files, in
  which the standardized citations were matched against the 83-study gold-standard
  corpus. These matched files are the direct input to `analysis_notebook.ipynb`.

## Citation

If you use this code or data, please cite:

> Farrag AN, Soliman A, Azubuike C, Zandbiglari K, Yadavilli S, Adkins LE,
> Mehrabi F, Cavallari L, Goodin A, Rouhizadeh M. Blind Spots in AI-Assisted
> Healthcare Evidence Search: Multiplatform Evaluation of Clinical Retrieval
> Gaps and Risk-of-Bias. *[Journal]*. [Year]. [DOI]

A machine-readable `CITATION.cff` can be added so GitHub renders a
"Cite this repository" button; update the journal, year, and DOI once available.

## License

Released under the [MIT License](LICENSE) (or specify your preferred license).
