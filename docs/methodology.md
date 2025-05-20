# Methodology

This document outlines the step-by-step process followed during the analysis of the YouTube Trending dataset.

---

## 1. Objective

The objective is to explore and analyze trending YouTube videos to identify factors that contribute to virality, such as video category, publish time, and engagement metrics like views, likes, and comments.

---

## 2. Data Collection

The dataset was sourced from Kaggle: [YouTube Trending Video Dataset](https://www.kaggle.com/datasnaek/youtube-new). Each CSV file represents trending video data from a specific region (e.g., US, GB).

---

## 3. Data Preprocessing

* Removed duplicate records (same video trending on multiple days).
* Converted `trending_date` to standard `YYYY-MM-DD` format.
* Parsed `publish_time` to extract publish date and hour.
* Handled missing values in `description` and `tags`.
* Converted boolean-like columns (`comments_disabled`, `ratings_disabled`, `video_error_or_removed`) to actual boolean types.
* Mapped `category_id` to human-readable `category_name` using the category mapping JSON.

---

## 4. Exploratory Data Analysis (EDA)

* Analyzed distribution of videos across categories.
* Identified top channels by average and total views.
* Plotted trends between views, likes, dislikes, and comments.
* Generated word clouds for video titles and tags.
* Explored timing patterns of publishing and trending.

---

## 5. Visualization Tools

The following tools and libraries were used:

* `pandas` and `numpy` for data manipulation
* `matplotlib` and `seaborn` for visualizations
* `wordcloud` for textual analysis

---

## 6. Limitations

* Dataset includes only trending videos, not the complete set of uploaded videos.
* Metrics like dislikes may be affected due to YouTube’s policy changes.
* No access to watch time, impressions, or user retention.
* Some text fields contain missing or non-English content.

---

## 7. Future Work

* Use YouTube API to collect real-time or more granular data.
* Build predictive models to estimate a video’s likelihood of trending.
* Perform sentiment analysis on video comments (if data available).
* Study longitudinal trends across multiple regions and years.
