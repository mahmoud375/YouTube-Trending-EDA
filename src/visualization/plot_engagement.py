import matplotlib.pyplot as plt
import pandas as pd

def add_plot_engagement_labels(ax, title="", xlabel="", ylabel=""):
    """
    Add labels and title to the plot.

    Parameters:
        ax (matplotlib.axes.Axes): Axes object to label.
        title (str): Plot title.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
    """
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


def plot_engagement_per_user(dataframe, user_col='channel_title', metric='likes'):
    """
    Plot total engagement metric (e.g., likes) by user/channel.

    Parameters:
        dataframe (pd.DataFrame): YouTube dataset.
        user_col (str): Column representing the user/channel.
        metric (str): Engagement metric to sum (e.g., 'likes', 'dislikes').

    Returns:
        matplotlib.figure.Figure: Bar chart of top users by engagement metric.
    """
    df = dataframe.copy()
    grouped = df.groupby(user_col)[metric].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    add_plot_engagement_labels(ax, f"Top {user_col} by {metric.capitalize()}", user_col, metric.capitalize())
    return fig


def plot_engagement_per_post(dataframe, id_col='video_id', metric='comment_count'):
    """
    Plot engagement metric by individual post/video.

    Parameters:
        dataframe (pd.DataFrame): YouTube dataset.
        id_col (str): Column representing video ID.
        metric (str): Metric to plot (e.g., 'comment_count').

    Returns:
        matplotlib.figure.Figure: Bar chart of videos by engagement.
    """
    df = dataframe.copy()
    grouped = df.groupby(id_col)[metric].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    add_plot_engagement_labels(ax, f"Top Videos by {metric.capitalize()}", id_col, metric.capitalize())
    return fig


def plot_engagement_over_time(dataframe, datetime_col='trending_date', metric='likes', freq='D'):
    """
    Plot the trend of an engagement metric over time.

    Parameters:
        dataframe (pd.DataFrame): YouTube dataset.
        datetime_col (str): Column representing the date.
        metric (str): Engagement metric to aggregate over time.
        freq (str): Frequency for time grouping ('D' daily, 'W' weekly, 'M' monthly).

    Returns:
        matplotlib.figure.Figure: Line plot of metric over time.
    """
    df = dataframe.copy()
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df.set_index(datetime_col, inplace=True)
    grouped = df[metric].resample(freq).sum()
    fig, ax = plt.subplots()
    grouped.plot(ax=ax)
    add_plot_engagement_labels(ax, f"{metric.capitalize()} Over Time", "Date", metric.capitalize())
    return fig


def create_engagement_bar_chart(x, y, title="", xlabel="", ylabel=""):
    """
    Create a bar chart from provided data.

    Parameters:
        x (array-like): Labels/categories for x-axis.
        y (array-like): Corresponding values.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.

    Returns:
        matplotlib.figure.Figure: The resulting bar chart.
    """
    fig, ax = plt.subplots()
    ax.bar(x, y)
    add_plot_engagement_labels(ax, title, xlabel, ylabel)
    return fig


def create_engagement_line_chart(x, y, title="", xlabel="", ylabel=""):
    """
    Create a line chart from provided data.

    Parameters:
        x (array-like): X-axis values (e.g., time).
        y (array-like): Corresponding metric values.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.

    Returns:
        matplotlib.figure.Figure: The resulting line chart.
    """
    fig, ax = plt.subplots()
    ax.plot(x, y)
    add_plot_engagement_labels(ax, title, xlabel, ylabel)
    return fig


def customize_engagement_plot_style(style="ggplot"):
    """
    Apply a visual style to all engagement plots.

    Parameters:
        style (str): Matplotlib style name (e.g., 'ggplot', 'seaborn').
    """
    plt.style.use(style)


def save_engagement_plot(fig, filepath):
    """
    Save a plot figure to file.

    Parameters:
        fig (matplotlib.figure.Figure): Figure object to save.
        filepath (str): Destination file path.
    """
    fig.savefig(filepath)

