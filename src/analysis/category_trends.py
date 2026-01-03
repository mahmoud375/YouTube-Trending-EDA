import pandas as pd
import numpy as np
from typing import List, Dict, Optional
import re
from collections import Counter

def extract_categories(data: pd.DataFrame, category_column: str) -> List[str]:
    """
    Extract unique categories from a specified column in the dataset.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        category_column (str): The name of the column that contains category labels.

    Returns:
        List[str]: A list of unique non-null category values.

    Raises:
        KeyError: If the specified column does not exist in the DataFrame.
    """
    return data[category_column].dropna().unique().tolist()

def filter_trends(data: pd.DataFrame, start_date: Optional[str] = None, end_date: Optional[str] = None) -> pd.DataFrame:
    """
    Filter the dataset based on a given date range.

    Args:
        data (pd.DataFrame): The input DataFrame containing a 'date' column.
        start_date (Optional[str]): The start date in 'YYYY-MM-DD' format. Defaults to None.
        end_date (Optional[str]): The end date in 'YYYY-MM-DD' format. Defaults to None.

    Returns:
        pd.DataFrame: Filtered DataFrame containing rows within the specified date range.

    Notes:
        The 'date' column must be in datetime format or convertible to it.
    """
    if start_date:
        data = data[data['date'] >= pd.to_datetime(start_date)]
    if end_date:
        data = data[data['date'] <= pd.to_datetime(end_date)]
    return data

def calculate_category_growth(data: pd.DataFrame, category_column: str, value_column: str, top_n: int = None, freq='M') -> pd.DataFrame:
    """
    Calculate percentage growth with time aggregation (e.g. monthly or weekly).
    
    freq: 'M' for monthly, 'W' for weekly, 'D' for daily (default)
    """
    if 'date' not in data.columns:
        raise KeyError("The column 'date' is not found in the dataset.")

    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data = data.dropna(subset=['date'])

    # Aggregate dates to the freq period (e.g. month start)
    data['period'] = data['date'].dt.to_period(freq).dt.start_time

    if top_n:
        top_categories = data.groupby(category_column)[value_column].sum().nlargest(top_n).index
        data = data[data[category_column].isin(top_categories)]

    grouped = data.groupby([category_column, 'period'])[value_column].sum().reset_index()
    pivoted = grouped.pivot(index='period', columns=category_column, values=value_column)
    growth = pivoted.pct_change(fill_method=None).fillna(0) * 100

    return growth




def identify_top_categories(data: pd.DataFrame, category_column: str, value_column: str, top_n: int = 5) -> List[str]:
    """
    Identify the top N categories based on total value.

    Args:
        data (pd.DataFrame): The input DataFrame.
        category_column (str): The column representing categories.
        value_column (str): The column containing numeric values.
        top_n (int): The number of top categories to return. Defaults to 5.

    Returns:
        List[str]: A list of top N category names sorted by total value in descending order.
    """
    totals = data.groupby(category_column)[value_column].sum()
    return totals.sort_values(ascending=False).head(top_n).index.tolist()

def compare_trends(data: pd.DataFrame, categories: List[str], value_column: str) -> pd.DataFrame:
    """
    Compare the value trends of selected categories over time.

    Args:
        data (pd.DataFrame): The dataset containing date, category, and value columns.
        categories (List[str]): The list of categories to compare.
        value_column (str): The column representing the value to compare.

    Returns:
        pd.DataFrame: A pivoted DataFrame showing values by date and category.
    """
    filtered = data[data['category'].isin(categories)]
    return filtered.pivot_table(index='date', columns='category', values=value_column, aggfunc='sum')

def aggregate_category_data(data: pd.DataFrame, category_column: str, value_column: str) -> pd.DataFrame:
    """
    Aggregate numeric data by category and compute summary statistics.

    Args:
        data (pd.DataFrame): The dataset to analyze.
        category_column (str): The name of the category column.
        value_column (str): The column containing numeric values.

    Returns:
        pd.DataFrame: A DataFrame with aggregated statistics (sum, mean, std, count) per category.
    """
    return data.groupby(category_column)[value_column].agg(['sum', 'mean', 'std', 'count']).reset_index()


def average_days_to_trend_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the average number of days it takes for a video to trend after publishing, grouped by category.

    Returns:
        pd.DataFrame: category_name and average days_to_trend
    """
    return (
        df[df["days_to_trend"] > 0]
        .groupby("category_name")["days_to_trend"]
        .mean()
        .sort_values()
        .reset_index(name="avg_days_to_trend")
    )

def trending_day_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Counts how many videos trended on each day of the week.

    Parameters:
        df (pd.DataFrame): Must contain 'publish_weekday' column with day names (e.g., 'Monday').

    Returns:
        pd.DataFrame: A DataFrame with 'weekday' and 'count', sorted from Monday to Sunday.
    """
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['publish_weekday'] = pd.Categorical(df['publish_weekday'], categories=weekday_order, ordered=True)

    return (
        df['publish_weekday']
        .value_counts()
        .sort_index()
        .reset_index(name='count')
        .rename(columns={'index': 'weekday'})
    )


def trending_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the number of trending videos per month.

    Returns:
        pd.DataFrame: month and count of trending videos
    """
    df["trending_month"] = pd.to_datetime(df["trending_date"]).dt.month
    return (
        df["trending_month"]
        .value_counts()
        .sort_index()
        .reset_index(name="count")
        .rename(columns={"index": "month"})
    )

def analyze_top_tags_by_category(df: pd.DataFrame, top_n: int = 10) -> dict:
    """
    Analyzes top tags per category from trending videos.

    Args:
        df (pd.DataFrame): DataFrame containing 'tags' and 'category_name' columns.
        top_n (int): Number of top tags to return per category.

    Returns:
        dict: Dictionary where keys are categories and values are DataFrames of top tags.
    """
    tag_by_category = {}

    # Ensure correct format
    df = df.dropna(subset=['tags', 'category_name']).copy()
    df['tags'] = df['tags'].str.lower().str.replace('"', '').str.replace('|', ',')

    # Group by category
    for category, group in df.groupby('category_name'):
        all_tags = [
            tag.strip() for tags in group['tags']
            for tag in tags.split(',') if tag and tag != '[none]'
        ]
        tag_counts = Counter(all_tags)
        tag_df = pd.DataFrame(tag_counts.most_common(top_n), columns=['tag', 'count'])
        tag_by_category[category] = tag_df

    return tag_by_category



def analyze_clickbait_effect_by_category(df: pd.DataFrame, keywords=None) -> pd.DataFrame:
    """
    Analyze how clickbait-style keywords in video titles impact engagement within each category.

    Args:
        df (pd.DataFrame): Must include 'title', 'category', 'views', 'likes', and 'comment_count'.
        keywords (list, optional): Custom list of clickbait keywords or phrases.

    Returns:
        pd.DataFrame: Mean views, likes, and comments grouped by category and clickbait presence.
    """
    if keywords is None:
        keywords = ['shocking', 'unbelievable', 'you won’t believe', 'amazing', 'insane', 'gone wrong']

    required_cols = ['title', 'category_name', 'views', 'likes', 'comment_count']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in DataFrame: {missing}")

    pattern = '|'.join(re.escape(word.lower()) for word in keywords)

    df = df.copy()
    df['clickbait_in_title'] = df['title'].str.lower().str.contains(pattern, na=False)

    result = (
        df.groupby(['category_name', 'clickbait_in_title'])[['views', 'likes', 'comment_count']]
        .mean()
        .reset_index()
    )
    return result


def summarize_top_trending_channels(df, top_n=10):
    """
    Returns the top N most consistently trending channels and their common traits.
    """
    top_channels = df['channel_title'].value_counts().head(top_n).index
    subset = df[df['channel_title'].isin(top_channels)]

    summary = (
        subset.groupby('channel_title')
        .agg(trending_count=('video_id', 'count'),
             unique_videos=('video_id', 'nunique'),
             avg_views=('views', 'mean'),
             avg_likes=('likes', 'mean'),
             most_common_category=('category_name', lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A'))
        .reset_index()
        .sort_values(by='trending_count', ascending=False)
    )

    return summary


def analyze_channel_format_category_consistency(df, min_trending=10):
    """
    Checks if high-trending channels tend to stick to consistent categories or varied ones.
    """
    # Filter to channels with many trending videos
    channel_stats = (
        df.groupby('channel_title')
        .agg(
            trending_count=('video_id', 'count'),
            unique_categories=('category_name', 'nunique'),
            common_category=('category_name', lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A'),
            avg_tags_per_video=('tags', lambda x: x.apply(lambda t: len(str(t).split('|'))).mean())
        )
        .query('trending_count >= @min_trending')
        .sort_values(by='trending_count', ascending=False)
    )

    # Add a metric for "category consistency"
    channel_stats['category_consistency'] = 1 - (channel_stats['unique_categories'] / channel_stats['trending_count'])

    return channel_stats.reset_index()
