import pytest
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.visualization.plot_engagement import *

@pytest.fixture
def basic_df():
    return pd.DataFrame({
        "video_id": ["v1", "v2", "v3", "v4"],
        "category_name": ["Music", "Gaming", "Education", "Music"],
        "views": [1000, 2000, 1500, 2500],
        "likes": [100, 200, 150, 250],
        "dislikes": [10, 20, 15, 25],
        "comment_count": [30, 50, 40, 60],
        "comments_disabled": [False, True, False, True],
        "ratings_disabled": [False, False, True, True],
        "days_to_trend": [1, 2, 3, 4],
        "channel_title": ["Channel A", "Channel B", "Channel A", "Channel C"],
        "trending_date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"])
    })


def test_plot_engagement_disabled_stats(basic_df):
    fig = plot_engagement_disabled_stats(basic_df)
    assert isinstance(fig, plt.Figure)


def test_plot_engagement_correlation_before_trend(basic_df):
    fig = plot_engagement_correlation_before_trend(basic_df)
    assert isinstance(fig, plt.Figure)


def test_plot_like_dislike_ratio_vs_views():
    df = pd.DataFrame({
        "category_name": ["Music", "Gaming", "Education"],
        "avg_like_dislike_ratio": [10, 8, 12],
        "avg_views": [2000, 1500, 1800]
    })
    fig = plot_like_dislike_ratio_vs_views(df)
    assert isinstance(fig, plt.Figure)


def test_plot_engagement_per_user(basic_df):
    fig = plot_engagement_per_user(basic_df, metric="likes")
    assert isinstance(fig, plt.Figure)


def test_plot_engagement_per_post(basic_df):
    fig = plot_engagement_per_post(basic_df, metric="comment_count")
    assert isinstance(fig, plt.Figure)


def test_plot_engagement_over_time(basic_df):
    fig = plot_engagement_over_time(basic_df, metric="likes")
    assert isinstance(fig, plt.Figure)


def test_create_engagement_bar_chart():
    x = ["A", "B", "C"]
    y = [10, 20, 15]
    fig = create_engagement_bar_chart(x, y, "Test Chart", "X", "Y")
    assert isinstance(fig, plt.Figure)


def test_create_engagement_line_chart():
    x = pd.date_range(start="2024-01-01", periods=3)
    y = [10, 15, 12]
    fig = create_engagement_line_chart(x, y, "Line Chart", "Time", "Value")
    assert isinstance(fig, plt.Figure)


def test_plot_category_engagement():
    df = pd.DataFrame({
        "category_name": ["Music", "Gaming", "Education"],
        "avg_engagement_rate": [0.2, 0.3, 0.25]
    })
    fig = plot_category_engagement(df, metric="avg_engagement_rate")
    assert isinstance(fig, plt.Figure)


def test_visualize_status_impact():
    # Simulated MultiIndex DataFrame
    index = pd.MultiIndex.from_product(
        [["comments_disabled", "ratings_disabled"], ["views", "likes", "dislikes", "comment_count"]],
        names=["Flag", "Metric"]
    )
    df = pd.DataFrame([1e5, 2e4, 1e3, 5e2, 9e4, 1.5e4, 800, 400], index=index)
    fig = visualize_status_impact(df)
    assert isinstance(fig, plt.Figure)
