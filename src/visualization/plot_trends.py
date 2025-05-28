import matplotlib.pyplot as plt
import pandas as pd

def add_plot_trends_labels(ax, title="", xlabel="", ylabel=""):
    """
    Add common plot labels and layout adjustments.

    Parameters:
        ax (matplotlib.axes.Axes): The axes object to label.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    
def plot_category_trends(dataframe, category_col='category_name', value_col='views', freq='D'):
    """
    Visualize the trend of a specific metric (e.g., views) over time for each content category.

    Parameters:
        dataframe (pd.DataFrame): Dataset containing YouTube video data.
        category_col (str): Column name that represents the video category.
        value_col (str): Column name of the metric to track over time (e.g., 'views').
        freq (str): Frequency for time grouping ('D' daily, 'W' weekly, 'M' monthly).

    Returns:
        matplotlib.figure.Figure: A line plot showing trends per category.
    """
    df = dataframe.copy()
    df['trending_date'] = pd.to_datetime(df['trending_date'])
    df.set_index('trending_date', inplace=True)
    grouped = df.groupby(category_col).resample(freq)[value_col].sum().unstack(0)
    fig, ax = plt.subplots()
    grouped.plot(ax=ax)
    add_plot_trends_labels(ax, f"{value_col.capitalize()} Trend by Category", "Date", value_col.capitalize())
    return fig


def plot_time_series_trends(dataframe, datetime_col='trending_date', value_col='views', freq='D'):
    """
    Plot the aggregate value of a metric over time (e.g., daily total views).

    Parameters:
        dataframe (pd.DataFrame): Dataset containing YouTube video data.
        datetime_col (str): Name of the datetime column (usually 'trending_date').
        value_col (str): Name of the metric column to aggregate and plot.
        freq (str): Frequency for time grouping ('D' daily, 'W' weekly, 'M' monthly).

    Returns:
        matplotlib.figure.Figure: A time series line plot.
    """
    df = dataframe.copy()
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df.set_index(datetime_col, inplace=True)
    grouped = df[value_col].resample(freq).sum()
    fig, ax = plt.subplots()
    grouped.plot(ax=ax)
    add_plot_trends_labels(ax, f"{value_col.capitalize()} Over Time", "Date", value_col.capitalize())
    return fig



def plot_trend_comparison(dataframe, group_col='category_name', value_col='likes'):
    """
    Compare the average value of a metric (e.g., likes) across different groups (e.g., categories).

    Parameters:
        dataframe (pd.DataFrame): Dataset containing YouTube video data.
        group_col (str): Column name to group by (e.g., 'category_name').
        value_col (str): Metric column to average (e.g., 'likes').

    Returns:
        matplotlib.figure.Figure: Bar chart comparing average metrics across groups.
    """
    df = dataframe.copy()
    grouped = df.groupby(group_col)[value_col].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    add_plot_trends_labels(ax, f"Average {value_col.capitalize()} by {group_col}", group_col, value_col.capitalize())
    return fig


def create_scatter_plot(x, y, title="", xlabel="", ylabel=""):
    """
    Generate a scatter plot for any two numerical variables.

    Parameters:
        x (array-like): Values for the x-axis.
        y (array-like): Values for the y-axis.
        title (str): Plot title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.

    Returns:
        matplotlib.figure.Figure: The resulting scatter plot.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    add_plot_trends_labels(ax, title, xlabel, ylabel)
    return fig


def create_pie_chart(labels, sizes, title=""):
    """
    Create a pie chart showing proportions of different categories.

    Parameters:
        labels (list): Labels for the pie chart slices.
        sizes (list): Numeric sizes corresponding to each label.
        title (str): Title for the chart.

    Returns:
        matplotlib.figure.Figure: The resulting pie chart.
    """
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)
    return fig


def highlight_trend_peaks(ax, data_series):
    """
    Annotate the highest value(s) in a data series on a plot.

    Parameters:
        ax (matplotlib.axes.Axes): The axes object to annotate.
        data_series (pd.Series): Series containing the values with datetime index.
    """
    peaks = data_series[data_series == data_series.max()]
    for date, value in peaks.items():
        ax.annotate(f"Peak: {value}", xy=(date, value), xytext=(date, value * 1.1),
                    arrowprops=dict(arrowstyle="->", color='red'))


def annotate_trend_changes(ax, change_points):
    """
    Annotate specific change points on a plot.

    Parameters:
        ax (matplotlib.axes.Axes): Axes object to annotate.
        change_points (list of tuples): Each tuple contains (x, y, label).
    """
    for (x, y, label) in change_points:
        ax.annotate(label, xy=(x, y), xytext=(x, y * 1.1),
                    arrowprops=dict(arrowstyle="->", color='blue'))


def export_trend_plot(fig, filepath):
    """
    Export a matplotlib figure to a file.

    Parameters:
        fig (matplotlib.figure.Figure): The figure to save.
        filepath (str): Path to save the file.
    """
    fig.savefig(filepath)


def adjust_plot_scale(ax, scale_type="linear"):
    """
    Adjust the y-axis scale of a plot.

    Parameters:
        ax (matplotlib.axes.Axes): The axes to modify.
        scale_type (str): Scale type ('linear', 'log', etc.).
    """
    ax.set_yscale(scale_type)


def reset_plot_settings():
    """
    Reset all matplotlib style settings to default.
    """
    plt.rcdefaults()

