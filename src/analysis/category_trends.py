import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict, Optional

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

def calculate_category_growth(data: pd.DataFrame, category_column: str, value_column: str) -> pd.DataFrame:
    """
    Calculate the percentage growth of values for each category over time.

    Args:
        data (pd.DataFrame): The input DataFrame containing time-series data.
        category_column (str): The column name identifying different categories.
        value_column (str): The numeric column to measure growth.

    Returns:
        pd.DataFrame: A pivot table showing percentage growth of each category by date.

    Notes:
        Growth is computed as the percent change between consecutive time points.
        Missing values are filled with zero.
    """
    grouped = data.groupby([category_column, 'date'])[value_column].sum().reset_index()
    pivoted = grouped.pivot(index='date', columns=category_column, values=value_column)
    growth = pivoted.pct_change().fillna(0) * 100
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

