# YouTube Trending EDA – Setup Guide

This guide explains how to install and run the YouTube Trending Data Analysis project step-by-step.

---

## 1. Prerequisites

Make sure you have the following installed:

* Python 3.10+
* Git
* pip (Python package manager)
* (Optional) `virtualenv` or `conda` for environment management

---

## 2. Clone the Repository

```bash
git clone https://github.com/mahmoud375/YouTube-Trending-EDA.git
cd YouTube-Trending-EDA
```

---

## 3. Create a Virtual Environment

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

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Project Settings

Ensure the following files exist and are correctly configured in the `config/` directory:

* `paths.yaml`: File paths for input data and output directories
* `settings.yaml`: General project options (e.g., countries to analyze, visualization parameters)

Edit these files as needed to match your environment.

---

## 6. Setup Directory Structure

Ensure your directories are correctly set up before running analysis:

```bash
# Create required directories (if not already present)
mkdir -p data/CA data/DE data/FR data/GB data/IN data/JP data/KR data/MX data/RU data/US
mkdir -p outputs/plots/comparative
mkdir -p outputs/plots/country_specific/CA
mkdir -p outputs/plots/country_specific/US
mkdir -p outputs/tables/comparative
mkdir -p outputs/tables/country_specific
```

Place the CSV and JSON files inside each respective country directory, e.g.,:

* `data/US/USvideos.csv`
* `data/US/US_category_id.json`

---

## 7. Run Scripts

### Data Cleaning & Merging

```bash
python src/preprocessing/clean_data.py
python src/preprocessing/merge_datasets.py
```

### Analysis

```bash
python src/analysis/category_trends.py
python src/analysis/engagement.py
```

### Visualization

```bash
python src/visualization/plot_trends.py
python src/visualization/plot_engagement.py
```

---

## 8. Launch Jupyter Notebooks

To explore and visualize the data interactively:

```bash
jupyter notebook
```

Then open relevant notebooks:

* `notebooks/country_specific/EDA_US_Youtube.ipynb`
* `notebooks/country_specific/EDA_CA_Youtube.ipynb`
* `notebooks/comparative/Cross_Country_Trends.ipynb`
* `notebooks/comparative/Engagement_Analysis.ipynb`

---

## ✅ Done!

You’re all set to analyze YouTube trending videos across multiple countries!

For any issues or contributions, refer to the README or open a GitHub issue.