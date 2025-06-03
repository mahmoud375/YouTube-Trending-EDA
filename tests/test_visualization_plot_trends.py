import pytest
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.visualization import plot_trends

@pytest.fixture
def sample_df():
    data = {
        'trending_date': pd.date_range('2024-01-01', periods=10),
        'category_name': ['Music', 'Gaming'] * 5,
        'views': [100, 200, 150, 180, 210, 160, 170, 220, 140, 190],
        'likes': [10, 20, 15, 18, 21, 16, 17, 22, 14, 19],
        'comment_count': [1, 2, 1, 2, 3, 2, 1, 3, 1, 2],
        'clickbait_in_title': [True, False] * 5,
        'channel_title': ['Channel A', 'Channel B'] * 5,
        'avg_days_to_trend': [3, 4, 3, 5, 4, 2, 5, 3, 4, 3],
        'publish_weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                            'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
    }
    df = pd.DataFrame(data)
    df['trending_month'] = df['trending_date'].dt.month
    return df

def test_plot_category_trends(sample_df):
    fig = plot_trends.plot_category_trends(sample_df)
    assert isinstance(fig, plt.Figure)

def test_plot_category_growth(sample_df):
    # simulate growth dataframe
    df = sample_df.copy()
    df = df.set_index('trending_date')
    growth_df = df.groupby([pd.Grouper(freq='D'), 'category_name'])['views'].sum().unstack().pct_change().fillna(0) * 100
    fig = plot_trends.plot_category_growth(growth_df)
    assert isinstance(fig, plt.Figure)

def test_plot_time_series_trends(sample_df):
    fig = plot_trends.plot_time_series_trends(sample_df)
    assert isinstance(fig, plt.Figure)

def test_plot_trend_comparison(sample_df):
    fig = plot_trends.plot_trend_comparison(sample_df)
    assert isinstance(fig, plt.Figure)

def test_create_scatter_plot(sample_df):
    fig = plot_trends.create_scatter_plot(sample_df['views'], sample_df['likes'], "Views vs Likes", "Views", "Likes")
    assert isinstance(fig, plt.Figure)

def test_create_pie_chart():
    labels = ['Music', 'Gaming', 'News']
    sizes = [40, 35, 25]
    fig = plot_trends.create_pie_chart(labels, sizes, "Category Distribution")
    assert isinstance(fig, plt.Figure)

def test_plot_avg_days_to_trend_by_category(sample_df):
    df = sample_df[['category_name', 'avg_days_to_trend']].groupby('category_name', as_index=False).mean()
    fig = plot_trends.plot_avg_days_to_trend_by_category(df)
    assert isinstance(fig, plt.Figure)

def test_plot_trending_day_distribution(sample_df):
    fig = plot_trends.plot_trending_day_distribution(sample_df)
    assert isinstance(fig, plt.Figure)

def test_plot_trending_by_month(sample_df):
    count_df = sample_df.groupby('trending_month').size().reset_index(name='count')
    fig = plot_trends.plot_trending_by_month(count_df)
    assert isinstance(fig, plt.Figure)

def test_visualize_top_tags_per_category():
    tag_data = {
        "Music": pd.DataFrame({'tag': ['pop', 'rock'], 'count': [100, 80]}),
        "Gaming": pd.DataFrame({'tag': ['fps', 'rpg'], 'count': [90, 70]})
    }
    fig = plot_trends.visualize_top_tags_per_category(tag_data)
    assert isinstance(fig, plt.Figure)

def test_plot_clickbait_effect_alternative(sample_df):
    fig = plot_trends.plot_clickbait_effect_alternative(sample_df)
    assert isinstance(fig, plt.Figure)

def test_plot_channel_category_heatmap(sample_df):
    fig = plot_trends.plot_channel_category_heatmap(sample_df)
    assert isinstance(fig, plt.Figure)

def test_export_trend_plot(tmp_path, sample_df):
    fig = plot_trends.plot_time_series_trends(sample_df)
    file_path = tmp_path / "trend_plot.png"
    plot_trends.export_trend_plot(fig, str(file_path))
    assert file_path.exists()
