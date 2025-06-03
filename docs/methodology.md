# Methodology for YouTube Trending Video Analysis

This document outlines the step-by-step process followed during the analysis of the YouTube Trending dataset.

---

## 1. Objective

The objective is to explore and analyze trending YouTube videos to identify factors that contribute to virality, such as video category, publish time, and engagement metrics like views, likes, and comments.

---

## 2. Data Collection

The dataset was sourced from Kaggle: [YouTube Trending Video Dataset](https://www.kaggle.com/datasnaek/youtube-new). Each CSV file represents trending video data from a specific region (e.g., US, GB).

---

## 3. Data Preprocessing

* Removed duplicate video entries by grouping on `video_id` and retaining the first trending instance.
* Standardized `trending_date` to `YYYY-MM-DD` format.
* Extracted `publish_date`, `publish_hour`, and `day_of_week` from `publish_time`.
* Filled missing or empty fields in `description`, `tags` with placeholders (e.g., "No Description").
* Converted categorical flags:

  * `comments_disabled`, `ratings_disabled`, `video_error_or_removed` → Boolean (`True/False`)
* Mapped `category_id` to `category_name` using the corresponding `*_category_id.json` file for each country.

---

## 4. Exploratory Data Analysis (EDA)

* Examined frequency and average views across video categories.
* Ranked top channels by total and average views.
* Analyzed engagement distribution: likes, dislikes, comments.
* Correlated engagement metrics with views to assess predictors of popularity.
* Created time-based features to examine publishing vs. trending delay.
* Used heatmaps, bar plots, and KDE plots for visualization.

---

## 5. Cross-Country Comparative Analysis

* Merged cleaned datasets from multiple countries (US, CA, GB, etc.) into a unified format.
* Compared content preferences across regions (e.g., top categories in US vs. India).
* Studied variation in engagement patterns (e.g., like-to-dislike ratios, comments) between countries.

---

## 6. Tools and Libraries

* **Pandas**, **NumPy**: data preprocessing and aggregation
* **Matplotlib**, **Seaborn**: statistical and temporal visualizations
* **WordCloud**: tag and title frequency visualizations
* **Jupyter Notebook**: exploratory analysis and documentation

---

## 7. Limitations

* Dataset includes only trending videos, not the complete set of uploaded videos.
* Metrics like dislikes may be affected due to YouTube’s policy changes.
* No access to watch time, impressions, or user retention.
* Some text fields contain missing or non-English content.

---

## 8. Future Work

* Use YouTube API to collect real-time or more granular data.
* Build predictive models to estimate a video’s likelihood of trending.
* Perform sentiment analysis on video comments (if data available).
* Study longitudinal trends across multiple regions and years.

---

## 9. Reproducibility and Automation

* Modular scripts ensure reproducible data cleaning, analysis, and visualization.
* Configuration files (`config/paths.yaml`, `config/settings.yaml`) make the pipeline flexible and adaptable to new datasets.

---

This methodology ensures a scalable and interpretable approach to understanding what makes YouTube videos trend globally.
