# YouTube Trending Video Analysis

## Project Overview

| 💡 **Final Insights & Reports** |
|:---|
| The final, summarized insights and detailed country-specific reports are available in the **`reports/`** directory. |

This project analyzes trending YouTube videos across multiple countries, including Canada (CA), Germany (DE), France (FR), Great Britain (GB), India (IN), Japan (JP), South Korea (KR), Mexico (MX), Russia (RU), and the United States (US). By leveraging public datasets, the project employs data cleaning, exploratory data analysis (EDA), and visualization to uncover patterns in viewer engagement, content categories, and cross-country trends. The codebase is modular, reproducible, and designed for scalability.

## Objectives

* Identify trending video categories (e.g., Music, Gaming) and top channels by country.
* Analyze engagement metrics (likes, comments, views) to understand viewer behavior.
* Compare content preferences and engagement patterns across countries.
* Provide reusable scripts and notebooks for data processing, analysis, and visualization.

## Dataset

The dataset is sourced from the **Trending YouTube Video Statistics** collection on Kaggle:
🔗 [https://www.kaggle.com/datasets/datasnaek/youtube-new](https://www.kaggle.com/datasets/datasnaek/youtube-new)

It includes:

* **CSV files** (e.g., `CAvideos.csv`): Video statistics including views, likes, comments, and metadata for each country.
* **JSON files** (e.g., `CA_category_id.json`): Category metadata for videos.

### Setup Instructions

1. Download the dataset from the Kaggle link above.
2. Extract the CSV and JSON files.
3. Place them in the `data/` directory, organized by country (e.g., `data/CA/CAvideos.csv`).

### Directory Setup

After downloading and extracting the dataset, make sure the following directories exist (create them manually if not already present):

```bash
# Create country-specific data directories
mkdir -p data/{CA,DE,FR,GB,IN,JP,KR,MX,RU,US}

# Create output folders for storing results
mkdir -p outputs/plots/comparative
mkdir -p outputs/plots/country_specific/{CA,DE,FR,GB,IN,JP,KR,MX,RU,US}
mkdir -p outputs/tables/comparative
mkdir -p outputs/tables/country_specific/{CA,DE,FR,GB,IN,JP,KR,MX,RU,US}
```

You can run the above commands in a Unix-based shell (e.g., Linux, macOS, or Git Bash on Windows). If you're using Windows CMD or PowerShell, you can create the folders manually or with equivalent commands.

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
│   ├── DE/                          # Germany data
│   ├── ...
│   └── US/                          # United States data
│       ├── US_category_id.json
│       └── USvideos.csv
├── docs/                            # Documentation
│   ├── data_dictionary.md
│   ├── methodology.md
│   └── setup_guide.md
├── notebooks/                       # Jupyter notebooks for analysis
│   ├── comparative/
│   │   ├── Cross_Country_Trends.ipynb
│   │   └── Engagement_Analysis.ipynb
│   └── country_specific/
│       ├── EDA_CA_Youtube.ipynb
│       └── EDA_US_Youtube.ipynb
├── outputs/                         # Generated outputs
│   ├── plots/                       # Visualizations
│   │   ├── comparative/             # Cross-country plots
│   │   └── country_specific/        # Country-specific plots (e.g., CA, US, etc.)
│   └── tables/                      # Summary tables (CSV format)
│       ├── comparative/             # Cross-country summary data
│       └── country_specific/        # Country-specific summary tables
|
├── reports/                         # Final reports and summarized insights
│   ├── CA/
│   │   └── report.md
│   ├── ...
│   └── US/
│       └── report.md
├── src/                             # Python source code
│   ├── analysis/
│   │   ├── category_trends.py
│   │   ├── engagement.py
│   ├── preprocessing/
│   │   ├── data_utils.py
│   │   └── merge_datasets.py
│   └── visualization/
│       ├── plot_engagement.py
│       └── plot_trends.py
├── tests/                           # Unit tests
├── .gitignore                       # Ignored files (e.g., data/, outputs/)
├── LICENSE                          # License file
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
```

## Installation

**Prerequisites**:

* Python 3.8+
* pip
* Jupyter Notebook or JupyterLab

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/mahmoud375/YouTube-Trending-EDA.git
   cd YouTube-Trending-EDA
   ```

2. **Set Up a Virtual Environment** (recommended):

   ```bash
   python -m venv yt_trend_analysis
   source yt_trend_analysis/bin/activate  # On Windows: yt_trend_analysis\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Environment**:

   * Update `config/paths.yaml` to reflect data and output paths.
   * Adjust `config/settings.yaml` for analysis parameters (e.g., visualization settings).

## 📘 Usage

1. **Per-Country Workflow**:

   * For each country, use a **single notebook** that includes:

     * Data cleaning
     * Exploratory data analysis (EDA)
     * Visualizations
   * Located in:
     `notebooks/country_specific/`
     Example notebooks:

     * `EDA_US_Youtube.ipynb`
     * `EDA_EG_Youtube.ipynb`

2. **Cross-Country Comparison**:

   * For multi-country analysis and trends, use:
     `notebooks/comparative/Cross_Country_Trends.ipynb`

3. **Outputs Structure**:

   All generated plots and summary tables are saved in the `outputs/` directory:

   ```
   outputs/
   ├── plots/
   │   ├── comparative/         # Cross-country visualizations
   │   └── country_specific/    # Visualizations per country (e.g., US, EG)
   └── tables/
       ├── comparative/         # Summary data for cross-country analysis
       └── country_specific/    # Per-country summary tables (CSV format)
   ```


4. **Run Tests**:

   * Verify code functionality with unit tests:

     ```bash
     pytest tests/
     ```

## Tools Used

* **Python**: Core programming language for analysis.
* **Pandas**: Data manipulation and analysis.
* **NumPy**: Numerical computations and array operations.
* **Matplotlib**: Data visualization and plotting.
* **Seaborn**: Statistical visualizations.
* **Jupyter Notebook**: Interactive code execution and documentation.

## 🔍 Key Insights

> This project aims to uncover key patterns and insights from YouTube trending video data, focusing on categories, engagement metrics, timing, metadata strategies, creator influence, and video status.

---

**1. Category-Based Insights**

- Which `category_name` has the highest average views or trending frequency?
- How do viewer engagement metrics differ across categories like Music, News, Gaming, etc.?
- What trends can we observe overall?

---

**2. Engagement & Popularity**

- Which engagement metric (likes, dislikes, comments) most strongly correlates with trending success (`views`)?
- Are videos with higher like-to-dislike ratios more likely to have higher view counts?
- Do videos with comments disabled or ratings disabled trend differently than those with full engagement enabled?

---

**3. Temporal Analysis**

- What is the average time delay between `publish_time` and `trending_date` across categories?
- Are there specific days of the week or times of day where videos are more likely to trend?
- How does the trending frequency vary across different months or seasons?

---

**4. Content Metadata & Strategy**

- Do certain tags or patterns in tags appear more frequently in trending videos?
- How does title length or presence of clickbait-style words (e.g., "shocking", "you won’t believe") affect views or engagement?

---

**5. Creator & Channel Influence**

- Which `channel_title` consistently appears on the trending list, and what are their common traits?
- Do channels with repeated trending videos use consistent video formats, or categories?

---

**6. Video Status & Restrictions**

- What is the impact of `comments_disabled`, `ratings_disabled`, or `video_error_or_removed` on engagement?
- Do videos that are later removed or error out tend to have unusually high or low engagement?

---
### 📊 Sample Visualizations

#### Average Views by Category Name
![Average Views by Category Name](https://i.postimg.cc/5ym8FDVM/avg-viows-by-category-name.png)

#### Average Number of Days to Trend by Category
![Average Number of Days to Trend by Category](https://i.postimg.cc/XNg5xMTR/Average-Number-of-Days-to-Trend-by-Category.png)



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

For questions or support, please contact the project maintainer at \[[mahmoud.elgendy.2182003@gmail.com](mailto:mahmoud.elgendy.2182003@gmail.com)].

# YouTube-Trending-EDA
