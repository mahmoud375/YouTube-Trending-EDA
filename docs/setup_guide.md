# YouTube Trending EDA – Setup Guide

This guide explains how to install and run the YouTube Trending Data Analysis project step-by-step.

---

## 1 Prerequisites

Make sure you have the following installed:

* Python 3.10+
* Git
* pip (Python package manager)
* (Optional) `virtualenv` or `conda` for environment management

---

## 2 Clone the Repository

```bash
git clone https://github.com/mahmoud375/YouTube-Trending-EDA.git
cd YouTube-Trending-EDA
```

---

## 3 Create a Virtual Environment

### Using `venv`:

```bash
python -m venv yt_trend_analysis
source yt_trend_analysis/bin/activate    # On Linux/macOS
yt_trend_analysis\Scripts\activate       # On Windows
```

### Or using `conda`:

```bash
conda create -n yt_trend_analysis python=3.11
conda activate yt_trend_analysis
```

---

## 4 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5 Configure Project Settings

Make sure the following files exist in the `config/` folder:

* `paths.yaml` – contains paths for data input/output
* `settings.yaml` – contains general project options (e.g., countries to analyze)

Edit these files as needed before running the pipeline.

---

## 6 Run Scripts

### Data Cleaning & Merging:

```bash
python src/preprocessing/clean_data.py
python src/preprocessing/merge_datasets.py
```

### Analysis:

```bash
python src/analysis/category_trends.py
python src/analysis/engagement.py
```

### Visualization:

```bash
python src/visualization/plot_trends.py
python src/visualization/plot_engagement.py
```

---

## 7 Launch Jupyter Notebooks

To explore and visualize the data interactively:

```bash
jupyter notebook
```

Then open the notebooks in the `notebooks/` folder:

* `notebooks/country_specific/EDA_US_Youtube.ipynb`
* `notebooks/comparative/Cross_Country_Trends.ipynb`

---

## Done!

You’re all set to start analyzing YouTube trending videos across the globe! 
