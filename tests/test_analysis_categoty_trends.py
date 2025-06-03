import pytest
import pandas as pd

from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.analysis import category_trends

def test_extract_categories():
    df = pd.DataFrame({'category': ['A', 'B', 'A', None]})
    result = category_trends.extract_categories(df, 'category')
    assert sorted(result) == ['A', 'B']

def test_filter_trends():
    df = pd.DataFrame({'date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01'])})
    filtered = category_trends.filter_trends(df, start_date='2023-02-01', end_date='2023-03-01')
    assert len(filtered) == 2
    assert all(filtered['date'] >= pd.Timestamp('2023-02-01'))

def test_calculate_category_growth():
    df = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=4, freq='M'),
        'category': ['A', 'A', 'B', 'B'],
        'views': [100, 200, 300, 400]
    })
    growth = category_trends.calculate_category_growth(df, 'category', 'views', freq='M')
    assert isinstance(growth, pd.DataFrame)
    assert 'A' in growth.columns
    assert 'B' in growth.columns

def test_identify_top_categories():
    df = pd.DataFrame({'cat': ['x', 'y', 'x', 'y', 'z'], 'val': [1, 2, 3, 4, 5]})
    top = category_trends.identify_top_categories(df, 'cat', 'val', top_n=2)
    assert top == ['y', 'z']  # y: 6, z:5

def test_compare_trends():
    df = pd.DataFrame({
        'date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02']),
        'category': ['A', 'B', 'A'],
        'views': [100, 200, 150]
    })
    pivot = category_trends.compare_trends(df, ['A', 'B'], 'views')
    assert pivot.shape[1] == 2  # A and B columns

def test_aggregate_category_data():
    df = pd.DataFrame({
        'cat': ['x', 'x', 'y', 'z'],
        'val': [1, 2, 3, 4]
    })
    agg = category_trends.aggregate_category_data(df, 'cat', 'val')
    assert 'sum' in agg.columns
    assert 'mean' in agg.columns

def test_average_days_to_trend_by_category():
    df = pd.DataFrame({
        'category_name': ['a', 'a', 'b'],
        'days_to_trend': [1, 3, 2]
    })
    avg = category_trends.average_days_to_trend_by_category(df)
    assert 'avg_days_to_trend' in avg.columns

def test_trending_day_distribution():
    df = pd.DataFrame({'publish_weekday': ['Monday', 'Tuesday', 'Monday', 'Sunday']})
    dist = category_trends.trending_day_distribution(df)
    assert 'weekday' in dist.columns
    assert dist.loc[dist['weekday'] == 'Monday', 'count'].values[0] == 2

def test_trending_by_month():
    df = pd.DataFrame({'trending_date': ['2023-01-10', '2023-01-15', '2023-02-01']})
    result = category_trends.trending_by_month(df)
    assert set(result['month']) == {1, 2}

def test_analyze_top_tags_by_category():
    df = pd.DataFrame({
        'tags': ['fun|wow', 'fun|crazy', 'wow|cool', None],
        'category_name': ['A', 'A', 'A', 'B']
    })
    result = category_trends.analyze_top_tags_by_category(df, top_n=2)
    assert 'A' in result
    assert isinstance(result['A'], pd.DataFrame)

def test_analyze_clickbait_effect_by_category():
    df = pd.DataFrame({
        'title': ['Amazing video', 'normal video'],
        'category_name': ['x', 'x'],
        'views': [1000, 500],
        'likes': [100, 50],
        'comment_count': [20, 10]
    })
    result = category_trends.analyze_clickbait_effect_by_category(df)
    assert set(result.columns).issuperset({'views', 'likes', 'comment_count'})

def test_summarize_top_trending_channels():
    df = pd.DataFrame({
        'channel_title': ['a', 'a', 'b', 'b', 'b'],
        'video_id': [1, 2, 3, 3, 4],
        'views': [100, 200, 300, 300, 500],
        'likes': [10, 20, 30, 30, 50],
        'category_name': ['x', 'x', 'y', 'y', 'y']
    })
    summary = category_trends.summarize_top_trending_channels(df, top_n=2)
    assert 'channel_title' in summary.columns
    assert 'trending_count' in summary.columns

def test_analyze_channel_format_category_consistency():
    df = pd.DataFrame({
        'channel_title': ['a'] * 5 + ['b'] * 5,
        'video_id': list(range(1, 11)),
        'category_name': ['x', 'x', 'y', 'x', 'y', 'z', 'z', 'z', 'z', 'z'],
        'tags': ['tag1|tag2'] * 10
    })
    result = category_trends.analyze_channel_format_category_consistency(df, min_trending=5)
    assert 'channel_title' in result.columns
    assert 'category_consistency' in result.columns
