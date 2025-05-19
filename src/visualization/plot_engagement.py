import matplotlib.pyplot as plt
import pandas as pd

def plot_average_metrics(df, columns, labels=None, title='Average Metrics'):
    """
    Plot the average of given numeric columns.
    
    Args:
        df (pd.DataFrame): The data frame.
        columns (list): List of column names to include in the plot.
        labels (list): Optional list of display labels for the columns.
        title (str): Title for the plot.
    """
    if labels is None:
        labels = columns

    avg_values = [df[col].mean() for col in columns]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, avg_values, color=plt.cm.Set2.colors)
    plt.title(title)
    plt.ylabel('Average Value')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05 * yval, f'{int(yval):,}', ha='center')

    plt.show()


def plot_distribution(df, columns, title='Metric Distribution'):
    """
    Plot boxplot distributions for specified columns.
    
    Args:
        df (pd.DataFrame): The data frame.
        columns (list): List of numeric column names to plot.
        title (str): Title for the plot.
    """
    df_subset = df[columns]

    plt.figure(figsize=(12, 6))
    df_subset.boxplot()
    plt.title(title)
    plt.ylabel('Value')
    plt.show()


def plot_correlation(df, x_col, y_col, title='Correlation Plot'):
    """
    Plot scatter plot between two columns to see correlation.
    
    Args:
        df (pd.DataFrame): The data frame.
        x_col (str): Column name for x-axis.
        y_col (str): Column name for y-axis.
        title (str): Plot title.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.5, c='orange')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.show()
