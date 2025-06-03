import pandas as pd
import pytest

from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.analysis.engagement import (
    compute_engagement_rate_df,
    compute_like_dislike_ratio_df,
    summarize_engagement_by_category_df,
    correlation_by_category_before_trend,
    like_dislike_ratio_vs_views,
    engagement_disabled_analysis,
    compare_status_impact,
)

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "video_id": ["a", "b", "c", "d"],
        "category_name": ["Music", "Music", "Gaming", "Gaming"],
        "views": [1000, 2000, 1500, 0],
        "likes": [100, 150, 80, 20],
        "dislikes": [10, 5, 5, 0],
        "comment_count": [20, 30, 10, 5],
        "comments_disabled": [False, True, False, True],
        "ratings_disabled": [False, False, True, True],
        "video_error_or_removed": [False, False, False, True],
        "days_to_trend": [5, 10, 5, 1],
    })

def test_compute_engagement_rate_df(sample_df):
    result = compute_engagement_rate_df(sample_df)
    expected = pd.Series([(100+20)/1000*100, (150+30)/2000*100, (80+10)/1500*100, (20+5)/pd.NA])
    pd.testing.assert_series_equal(result.dropna().reset_index(drop=True), expected.dropna().reset_index(drop=True))

def test_compute_like_dislike_ratio_df(sample_df):
    result = compute_like_dislike_ratio_df(sample_df)
    expected = pd.Series([100/11, 150/6, 80/6, 20/1])
    pd.testing.assert_series_equal(result.round(2), expected.round(2))

def test_summarize_engagement_by_category_df(sample_df):
    result = summarize_engagement_by_category_df(sample_df)
    assert "category_name" in result.columns
    assert set(result["category_name"]) == {"Music", "Gaming"}
    assert result["video_count"].sum() == 4

def test_correlation_by_category_before_trend(sample_df):
    result = correlation_by_category_before_trend(sample_df)
    assert isinstance(result, pd.Series)
    assert "avg_views_per_day" in result.index

def test_like_dislike_ratio_vs_views(sample_df, capsys):
    result = like_dislike_ratio_vs_views(sample_df)
    assert "avg_like_dislike_ratio" in result.columns
    captured = capsys.readouterr()
    assert "Correlation" in captured.out

def test_engagement_disabled_analysis(sample_df):
    result = engagement_disabled_analysis(sample_df)
    assert {"avg_views", "avg_likes", "avg_comments", "count"}.issubset(result.columns)

def test_compare_status_impact(sample_df):
    result = compare_status_impact(sample_df)
    assert isinstance(result, pd.DataFrame)
    assert ("comments_disabled", "views") in result.index
