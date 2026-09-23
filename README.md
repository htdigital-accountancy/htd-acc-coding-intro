# Accountants for Coding

A place to find useful scripts for starting your coding experiments.

This repo is primarily Python-based and is intended as a shared resource for exploring data, automating tasks, and building analytical skills through code. We'll continue adding scripts, notebooks, and non-private mock data to help you get started.

## Contents

| Folder | Description |
|--------|-------------|
| `00_python_fundamentals` | Python basics — variables, lists, dicts, loops, functions; notebook + `.py` scripts ([cheat sheet](00_python_fundamentals/CHEATSHEET.md)) |
| `01_intro_to_jupyter_and_pandas` | Introduction to Jupyter notebooks and data manipulation with pandas |
| `02_intro_to_APIs` | Introduction to APIs — fetching exchange, blockchain, and price data programmatically |

## Getting Started

### Option 1: conda (recommended for beginners)

Install [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), then create a new environment and install the required packages:

```bash
# Create a new environment
conda create -n acc-coding python=3.12

# Activate it
conda activate acc-coding

# Install all dependencies from requirements.txt
pip install -r requirements.txt

# Launch Jupyter
jupyter-lab
```

### Option 2: uv (fast, modern — preferred)

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
# Create a new virtual environment
uv venv .venv

# Activate it
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Install dependencies from requirements.txt
uv pip install -r requirements.txt

# Launch Jupyter
jupyter-lab
```

### Option 3: Poetry

Install [Poetry](https://python-poetry.org/docs/#installation), then:

```bash
# Initialise a new project (or use an existing pyproject.toml)
poetry init

# Install dependencies from requirements.txt
poetry add $(cat requirements.txt)

# Launch Jupyter inside the Poetry environment
poetry run jupyter-lab
```

## Contributing

Scripts, notebooks, and mock data are welcome. Keep any data non-private and anonymised before committing.
