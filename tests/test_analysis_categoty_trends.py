import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
from src.analysis.category_trends import (
    extract_categories,
    filter_trends,
    calculate_category_growth,
    identify_top_categories,
    compare_trends,
    aggregate_category_data
)
from datetime import datetime, timedelta

def test_extract_categories():
    df = pd.DataFrame({'category': ['A', 'B', 'A', None, 'C']})
    result = extract_categories(df, 'category')
    assert set(result) == {'A', 'B', 'C'}

def test_filter_trends():
    today = datetime.today()
    dates = [today - timedelta(days=i) for i in range(5)]
    df = pd.DataFrame({'date': dates, 'value': range(5)})
    result = filter_trends(df, start_date=(today - timedelta(days=2)).strftime('%Y-%m-%d'))
    assert all(result['date'] >= pd.to_datetime(today - timedelta(days=2)))

def test_calculate_category_growth():
    today = datetime.today()
    df = pd.DataFrame({
        'date': [today - timedelta(days=i) for i in range(2)] * 2,
        'category': ['A', 'A', 'B', 'B'],
        'value': [10, 20, 5, 10]
    })
    growth = calculate_category_growth(df, 'category', 'value')
    assert isinstance(growth, pd.DataFrame)
    assert 'A' in growth.columns and 'B' in growth.columns

def test_identify_top_categories():
    df = pd.DataFrame({
        'category': ['A', 'A', 'B', 'B', 'C'],
        'value': [5, 5, 20, 10, 1]
    })
    top = identify_top_categories(df, 'category', 'value', top_n=2)
    assert top == ['B', 'A']

def test_compare_trends():
    today = datetime.today()
    df = pd.DataFrame({
        'date': [today - timedelta(days=i) for i in range(3)] * 2,
        'category': ['A'] * 3 + ['B'] * 3,
        'value': [1, 2, 3, 4, 5, 6]
    })
    result = compare_trends(df, ['A', 'B'], 'value')
    assert isinstance(result, pd.DataFrame)
    assert 'A' in result.columns and 'B' in result.columns

def test_aggregate_category_data():
    df = pd.DataFrame({
        'category': ['A', 'A', 'B', 'B', 'B'],
        'value': [10, 20, 5, 15, 30]
    })
    result = aggregate_category_data(df, 'category', 'value')
    assert all(col in result.columns for col in ['sum', 'mean', 'std', 'count'])


if __name__ == '__main__':

    #test_extract_categories()
    #test_filter_trends()
    #test_calculate_category_growth()
    test_identify_top_categories()
    # test_compare_trends()
    # test_aggregate_category_data()