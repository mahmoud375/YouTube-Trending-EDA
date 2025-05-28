import sys
import os
import pandas as pd
import matplotlib.pyplot as plt 

# Add parent directory to sys.path to import from src.visualization
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visualization.plot_trends import *

def create_sample_data():
    """
    Create sample data resembling YouTube video stats for testing.
    """
    data = {
        'category_name': ['Music', 'Gaming', 'Music', 'Education', 'Gaming', 'Education', 'Music', 'Education', 'Gaming', 'Music'],
        'views': [1000, 1500, 1200, 800, 2000, 700, 1100, 900, 1300, 1400],
        'likes': [100, 120, 110, 80, 150, 75, 105, 90, 130, 115],
        'trending_date': pd.date_range(start='2023-01-01', periods=10, freq='D')
    }
    return pd.DataFrame(data)

def main():
    # Create the sample dataframe
    df = create_sample_data()

    print("Testing plot_category_trends...")
    fig1 = plot_category_trends(df, category_col='category_name', value_col='views', freq='D')

    print("Testing plot_time_series_trends...")
    fig2 = plot_time_series_trends(df, datetime_col='trending_date', value_col='views', freq='D')

    print("Testing plot_trend_comparison...")
    fig3 = plot_trend_comparison(df, group_col='category_name', value_col='likes')

    print("Testing create_scatter_plot...")
    fig4 = create_scatter_plot(df['views'], df['likes'], title="Views vs Likes Scatter Plot", xlabel="Views", ylabel="Likes")

    print("Testing create_pie_chart...")
    category_counts = df['category_name'].value_counts()
    fig5 = create_pie_chart(labels=category_counts.index.tolist(), sizes=category_counts.values, title="Category Distribution")

    # Test highlight_trend_peaks and annotate_trend_changes on a simple plot
    fig6, ax6 = plt.subplots()
    series = df.groupby('trending_date')['views'].sum()
    series.plot(ax=ax6, title="Views Over Time")
    highlight_trend_peaks(ax6, series)
    annotate_trend_changes(ax6, [(series.index[3], series.iloc[3], "Special Event"), (series.index[7], series.iloc[7], "Trend Shift")])
    add_plot_trends_labels(ax6, "Views Over Time with Annotations", "Date", "Views")

    # Show all plots together (blocking)
    plt.show()

if __name__ == "__main__":
    main()
