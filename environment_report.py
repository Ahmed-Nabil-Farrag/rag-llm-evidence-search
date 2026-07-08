# ============================================================================
# ENVIRONMENT REPORT  —  run this as the FIRST cell of the notebook
# Records the exact Python and package versions used, prints a version table,
# writes environment.txt, and prints a ready-to-paste Code Availability
# sentence for the manuscript.
# ============================================================================
import sys, platform
from importlib import metadata

# Packages actually imported by the analysis notebook
PACKAGES = [
    "pandas", "numpy", "scipy", "statsmodels",
    "scikit-learn", "matplotlib", "seaborn", "plotly",
]
# import name -> distribution name (only where they differ)
DIST = {"scikit-learn": "scikit-learn"}

def _ver(pkg):
    try:
        return metadata.version(DIST.get(pkg, pkg))
    except Exception:
        return "not installed"

py = platform.python_version()
rows = [(p, _ver(p)) for p in PACKAGES]

print("=" * 60)
print("ENVIRONMENT REPORT")
print("=" * 60)
print(f"Python           {py}")
print(f"Platform         {platform.platform()}")
print("-" * 60)
for name, ver in rows:
    print(f"{name:<16} {ver}")
print("=" * 60)

# Write a pinned environment file for the repository
with open("environment.txt", "w") as fh:
    fh.write(f"python=={py}\n")
    for name, ver in rows:
        fh.write(f"{name}=={ver}\n")
print("Wrote environment.txt")

# Ready-to-paste Code Availability sentence (versions filled in automatically)
pkg_str = ", ".join(f"{n} {v}" for n, v in rows)
print("\n--- paste into the Code Availability statement ---\n")
print(
    f"All analyses were performed in Python {py} using {pkg_str}. "
    "The complete analysis code is openly available at "
    "https://github.com/<your-username>/rag-llm-evidence-search."
)
