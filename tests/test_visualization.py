import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.visualization.plot_engagement import *
from src.visualization.plot_trends import *

def test_plot_engagement():
    # Generate dummy data for testing
    np.random.seed(0)  # For reproducibility
    data = {
        'Views': np.random.randint(1000, 100000, 100),
        'Likes': np.random.randint(100, 10000, 100),
        'Comments': np.random.randint(10, 1000, 100),
        'Shares': np.random.randint(0, 500, 100)
    }

    df = pd.DataFrame(data)

    # Test average metrics bar plot
    plot_average_metrics(
        df,
        columns=['Views', 'Likes', 'Comments', 'Shares'],
        labels=['Views', 'Likes', 'Comments', 'Shares'],
        title='Average Metrics per Column'
    )

    # Test distribution boxplot
    plot_distribution(
        df,
        columns=['Views', 'Likes', 'Comments', 'Shares'],
        title='Distribution of Metrics'
    )

    # Test correlation scatter plot
    plot_correlation(
        df,
        x_col='Views',
        y_col='Likes',
        title='Correlation between Views and Likes'
    )

def test_plot_trends():
    # Create sample DataFrame with a date column and numeric values
    np.random.seed(1)  # For reproducible results
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    sample_data = {
        'Date': np.random.choice(dates, size=200),  # 200 random entries from those 30 dates
        'Views': np.random.randint(1000, 50000, size=200),
        'Likes': np.random.randint(100, 5000, size=200)
    }

    df = pd.DataFrame(sample_data)

    # Make sure 'Date' is datetime (important for grouping)
    df['Date'] = pd.to_datetime(df['Date'])

    # Test: Daily counts (how many entries per day)
    plot_daily_counts(df, date_col='Date', title='Number of Posts per Day')

    # Test: Daily average of Views
    plot_daily_average(df, date_col='Date', value_col='Views', title='Average Views per Day')

    # Test: Dual-axis plot (count of Likes and average Views per day)
    plot_dual_axis(df, date_col='Date', count_col='Likes', avg_col='Views', title='Likes Count and Average Views per Day')

if __name__ == '__main__':
    #test_plot_engagement()
    test_plot_trends()
