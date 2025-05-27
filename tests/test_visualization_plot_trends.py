import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import traceback
from src.visualization.plot_trends import *


df = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'user': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'post': ['Post1', 'Post2', 'Post1', 'Post3', 'Post2'],
    'engagement': [10, 20, 15, 30, 25],
    'likes': [5, 10, 8, 15, 12]
})


def test_func(func, *args, **kwargs):
    try:
        print(f"Running {func.__name__}...")
        func(*args, **kwargs)
        print(f"{func.__name__} ran successfully.\n")
    except Exception:
        print(f"{func.__name__} failed:")
        traceback.print_exc()
        print()


if __name__ == '__main__':

    test_func(plot_daily_counts, df, 'date', title='Daily Count')
    test_func(plot_daily_average, df, 'date', 'likes', title='Daily Avg Likes')
    test_func(plot_dual_axis, df, 'date', 'engagement', 'likes', title='Count vs Avg')


    test_func(plot_engagement_by_user, df, 'user', 'engagement', title='Engagement by User')
    test_func(plot_engagement_by_post, df, 'post', 'engagement', title='Engagement by Post')
    test_func(plot_engagement_trends, df, 'date', 'engagement', title='Engagement Trends')


    series_sample = df.groupby('user')['engagement'].sum()
    test_func(create_bar_chart, series_sample, title='Test Bar Chart', xlabel='User', ylabel='Engagement')
    test_func(create_line_chart, series_sample, title='Test Line Chart', xlabel='User', ylabel='Engagement')

    test_func(add_plot_labels, xlabel='X Test', ylabel='Y Test', title='Label Test')

    test_func(save_engagement_plot, filename='test_plot.png')
