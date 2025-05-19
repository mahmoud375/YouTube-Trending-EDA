import matplotlib.pyplot as plt
import pandas as pd


def plot_daily_counts(df, date_col, title='Daily Item Counts'):
    """
    Plot the count of entries per date.

    Args:
        df (pd.DataFrame): The data frame.
        date_col (str): Name of the date column (must be datetime).
        title (str): Plot title.
    """
    daily_counts = df.groupby(date_col).size()

    plt.figure(figsize=(12, 6))
    daily_counts.plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()


def plot_daily_average(df, date_col, value_col, title='Daily Average'):
    """
    Plot average of a column per date.

    Args:
        df (pd.DataFrame): The data frame.
        date_col (str): Name of the datetime column.
        value_col (str): Column to average.
        title (str): Plot title.
    """
    avg_per_day = df.groupby(date_col)[value_col].mean()

    plt.figure(figsize=(12, 6))
    avg_per_day.plot(kind='line', marker='o', color='red')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(f'Average {value_col}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_dual_axis(df, date_col, count_col, avg_col, title='Count and Average Over Time'):
    """
    Plot two metrics (count and average) over time using dual axes.

    Args:
        df (pd.DataFrame): The data frame.
        date_col (str): Date column name.
        count_col (str): Column to count per date (any non-null field).
        avg_col (str): Column to average per date.
        title (str): Plot title.
    """
    count_series = df.groupby(date_col)[count_col].count()
    avg_series = df.groupby(date_col)[avg_col].mean()

    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(count_series.index, count_series.values, alpha=0.6, color='skyblue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Count', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(avg_series.index, avg_series.values, color='red', marker='o')
    ax2.set_ylabel(f'Average {avg_col}', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title(title)
    fig.tight_layout()
    plt.show()
