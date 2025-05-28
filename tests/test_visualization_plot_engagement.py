import sys
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt 

# Add parent directory to sys.path to import from src.visualization
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visualization.plot_engagement import (
    customize_engagement_plot_style,
    plot_engagement_per_user,
    plot_engagement_per_post,
    plot_engagement_over_time,
    create_engagement_bar_chart,
    create_engagement_line_chart
)

def create_sample_dataframe():
    """
    Create a sample DataFrame to test the plotting functions.
    
    Returns:
        pd.DataFrame: Sample YouTube-like engagement data.
    """
    data = {
        'channel_title': ['UserA', 'UserB', 'UserA', 'UserC', 'UserB', 'UserA', 'UserD', 'UserC', 'UserE', 'UserD'],
        'video_id': ['vid1', 'vid2', 'vid3', 'vid4', 'vid5', 'vid6', 'vid7', 'vid8', 'vid9', 'vid10'],
        'likes': [100, 150, 200, 50, 300, 120, 80, 60, 90, 40],
        'dislikes': [10, 20, 15, 5, 30, 12, 8, 6, 9, 4],
        'comment_count': [5, 7, 3, 8, 9, 2, 6, 5, 1, 0],
        'trending_date': pd.date_range(start='2023-01-01', periods=10, freq='D')
    }
    return pd.DataFrame(data)

def main():
    # Prepare data
    df = create_sample_dataframe()

    # Set a consistent visual style for all plots
    customize_engagement_plot_style("ggplot")

    print("Generating plots...")

    # Plot top 10 users by likes
    fig1 = plot_engagement_per_user(df, user_col='channel_title', metric='likes')

    # Plot top 10 videos by comment count
    fig2 = plot_engagement_per_post(df, id_col='video_id', metric='comment_count')

    # Plot likes over time (daily frequency)
    fig3 = plot_engagement_over_time(df, datetime_col='trending_date', metric='likes', freq='D')

    # Create a custom bar chart example
    fig4 = create_engagement_bar_chart(
        x=['Category A', 'Category B', 'Category C'],
        y=[10, 20, 15],
        title="Custom Bar Chart",
        xlabel="Category",
        ylabel="Value"
    )

    # Create a custom line chart example
    fig5 = create_engagement_line_chart(
        x=pd.date_range('2023-01-01', periods=3),
        y=[10, 20, 15],
        title="Custom Line Chart",
        xlabel="Date",
        ylabel="Value"
    )

    # Show all figures at once and wait for user to close them
    plt.show()

    print("All plots generated successfully.")

if __name__ == "__main__":
    main()
