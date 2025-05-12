# YouTube Trending Video Analysis

## Project Overview
This project analyzes trending YouTube videos across multiple countries, including Canada (CA), Germany (DE), France (FR), Great Britain (GB), India (IN), Japan (JP), South Korea (KR), Mexico (MX), Russia (RU), and the United States (US). By leveraging public datasets, the project employs data cleaning, exploratory data analysis (EDA), and visualization to uncover patterns in viewer engagement, content categories, and cross-country trends. The codebase is modular, reproducible, and designed for scalability.

## Objectives
- Identify trending video categories (e.g., Music, Gaming) and top channels by country.
- Analyze engagement metrics (likes, comments, views) to understand viewer behavior.
- Compare content preferences and engagement patterns across countries.
- Provide reusable scripts and notebooks for data processing, analysis, and visualization.

## Dataset
The dataset is sourced from the **Trending YouTube Video Statistics** collection on Kaggle:  
🔗 [https://www.kaggle.com/datasets/datasnaek/youtube-new](https://www.kaggle.com/datasets/datasnaek/youtube-new)

It includes:
- **CSV files** (e.g., `CAvideos.csv`): Video statistics including views, likes, comments, and metadata for each country.
- **JSON files** (e.g., `CA_category_id.json`): Category metadata for videos.

**Setup Instructions**:
1. Download the dataset from the Kaggle link above.
2. Extract the CSV and JSON files.
3. Place them in the `data/` directory, organized by country (e.g., `data/CA/CAvideos.csv`).

**Note**: The dataset is not included in this repository due to its size and licensing. Ensure proper attribution to the dataset source. Refer to `docs/data_dictionary.md` for detailed descriptions of data fields.

## Project Structure
```
YouTube-Trending-EDA/
├── config/                          # Configuration files
│   ├── paths.yaml                  # File paths for data and outputs
│   └── settings.yaml               # Analysis parameters
├── data/                            # Raw datasets (not tracked in Git)
│   ├── CA/                         # Canada data
│   │   ├── CA_category_id.json
│   │   └── CAvideos.csv
│   ├── DE/                         # Germany data
│   │   ├── DE_category_id.json
│   │   └── DEvideos.csv
│   ├── FR/                         # France data
│   │   ├── FR_category_id.json
│   │   └── FRvideos.csv
│   ├── GB/                         # Great Britain data
│   │   ├── GB_category_id.json
│   │   └── GBvideos.csv
│   ├── IN/                         # India data
│   │   ├── IN_category_id.json
│   │   └── INvideos.csv
│   ├── JP/                         # Japan data
│   │   ├── JP_category_id.json
│   │   └── JPvideos.csv
│   ├── KR/                         # South Korea data
│   │   ├── KR_category_id.json
│   │   └── KRvideos.csv
│   ├── MX/                         # Mexico data
│   │   ├── MX_category_id.json
│   │   └── MXvideos.csv
│   ├── RU/                         # Russia data
│   │   ├── RU_category_id.json
│   │   └── RUvideos.csv
│   └── US/                         # United States data
│       ├── US_category_id.json
│       └── USvideos.csv
├── docs/                            # Documentation
│   ├── data_dictionary.md          # Dataset field descriptions
│   ├── methodology.md              # Analysis methodology
│   └── setup_guide.md              # Detailed setup instructions
├── notebooks/                       # Jupyter notebooks for analysis
│   ├── comparative/                # Cross-country analysis
│   │   ├── Cross_Country_Trends.ipynb
│   │   └── Engagement_Analysis.ipynb
│   ├── country_specific/           # Country-specific EDA
│   │   ├── EDA_CA_Youtube.ipynb
│   │   └── EDA_US_Youtube.ipynb
│   └── utilities/                  # Data processing and visualization
│       ├── Data_Cleaning.ipynb
│       └── Visualization_Templates.ipynb
├── outputs/                         # Generated outputs
│   ├── plots/                      # Visualizations
│   │   ├── comparative/           # Cross-country plots
│   │   └── country_specific/      # Country-specific plots
│   │       ├── CA/
│   │       └── US/
│   ├── reports/                    # Analysis reports
│   │   ├── comparative/           # Cross-country reports
│   │   └── country_specific/      # Country-specific reports
│   │       ├── CA/
│   │       └── US/
│   └── tables/                     # Summary tables
│       ├── comparative/           # Cross-country tables
│       └── country_specific/      # Country-specific tables
├── src/                             # Python source code
│   ├── analysis/                   # Analysis modules
│   │   ├── category_trends.py     # Category trend analysis
│   │   ├── engagement.py          # Engagement metrics analysis
│   │   └── __init__.py
│   ├── preprocessing/              # Data cleaning and merging
│   │   ├── clean_data.py          # Data cleaning functions
│   │   ├── merge_datasets.py      # Dataset merging functions
│   │   └── __init__.py
│   └── visualization/              # Visualization modules
│       ├── plot_engagement.py     # Engagement visualization
│       ├── plot_trends.py         # Trend visualization
│       └── __init__.py
├── tests/                           # Unit tests
│   ├── test_analysis.py           # Tests for analysis modules
│   ├── test_preprocessing.py      # Tests for preprocessing modules
│   └── test_visualization.py      # Tests for visualization modules
├── .gitignore                       # Ignored files (e.g., data/, outputs/)
├── LICENSE                          # License file
├── pyproject.toml                   # Project configuration
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

## Installation
**Prerequisites**:
- Python 3.8+
- pip
- Jupyter Notebook or JupyterLab

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mahmoud375/YouTube-Trending-EDA.git
   cd YouTube-Trending-EDA
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Environment**:
   - Update `config/paths.yaml` to reflect data and output paths.
   - Adjust `config/settings.yaml` for analysis parameters (e.g., visualization settings).

## Usage
1. **Data Preparation**:
   - Ensure the dataset is placed in the `data/` directory.
   - Run the data cleaning notebook to preprocess the data:
     ```bash
     jupyter notebook notebooks/utilities/Data_Cleaning.ipynb
     ```

2. **Exploratory Data Analysis**:
   - For country-specific analysis, use notebooks in `notebooks/country_specific/` (e.g., `EDA_CA_Youtube.ipynb`).
   - For cross-country comparisons, use notebooks in `notebooks/comparative/` (e.g., `Cross_Country_Trends.ipynb`).

3. **Visualization**:
   - Generate plots using scripts in `src/visualization/` (e.g., `plot_engagement.py`).
   - Outputs are saved in `outputs/plots/`.
   - Use the visualization templates notebook for reusable designs:
     ```bash
     jupyter notebook notebooks/utilities/Visualization_Templates.ipynb
     ```

4. **Run Tests**:
   - Verify code functionality with unit tests:
     ```bash
     pytest tests/
     ```

## Tools Used
- **Python**: Core programming language for analysis.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations and array operations.
- **Matplotlib**: Data visualization and plotting.
- **Seaborn**: Statistical visualizations.
- **Jupyter Notebook**: Interactive code execution and documentation.

## Key Insights
- **Trending Content Categories**: Identifies dominant video categories (e.g., Music, Gaming) in each country.
- **Top Channels**: Highlights frequently trending YouTube channels by region.
- **Engagement Patterns**: Analyzes correlations between likes, comments, and views to reveal viewer behavior.
- **Cross-Country Trends**: Compares content preferences and engagement metrics across countries (e.g., US, GB, IN).

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

For bug reports or feature requests, please open an issue on the repository.

## License
This project is licensed under the terms specified in the `LICENSE` file.

## Author
Mahmoud Elgendy

## Contact
For questions or support, please contact the project maintainer at [star7ana@gmail.com].# YouTube-Trending-EDA
# YouTube-Trending-EDA
