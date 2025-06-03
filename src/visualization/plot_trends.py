import matplotlib.pyplot as plt
import seaborn as sns
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


import matplotlib.pyplot as plt
import pandas as pd

def plot_category_growth(growth_df: pd.DataFrame, title: str = "Category Growth Over Time") -> plt.Figure:
    """
    Plots the monthly growth of YouTube video categories over time.

    Args:
        growth_df (pd.DataFrame): A DataFrame where the index is datetime and 
                                  columns represent different categories with their growth values.
        title (str, optional): Title of the plot. Defaults to "Category Growth Over Time".

    Returns:
        plt.Figure: The matplotlib figure object, which can be saved or further customized.

    Notes:
        - The function automatically converts the index to datetime if not already.
        - It plots a multi-line graph showing percentage growth over time for each category.
        - The legend is placed outside the main plot area on the right.
        - The function does NOT display the plot directly using `plt.show()` to allow saving.
    """
    # Ensure the index is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(growth_df.index):
        growth_df.index = pd.to_datetime(growth_df.index, errors='coerce')
        growth_df = growth_df[~growth_df.index.isna()]

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    growth_df.plot(ax=ax, marker='o')
    
    # Customize axes
    ax.set_title(title)
    ax.set_ylabel("Growth (%)")
    ax.set_xlabel("Date")
    ax.grid(True)
    
    # Position legend
    ax.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
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


def plot_avg_days_to_trend_by_category(df: pd.DataFrame):
    """
    Plots the average number of days it takes for videos to trend by category.

    Parameters:
    -----------
    df : pd.DataFrame
        A DataFrame with two columns:
        - 'category_name': The name of the video category.
        - 'avg_days_to_trend': Precomputed average number of days to trend.

    Returns:
    --------
    matplotlib.figure.Figure
        A matplotlib figure object representing the bar plot.
    """
    df_sorted = df.sort_values('avg_days_to_trend')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=df_sorted,
        x='avg_days_to_trend',
        y='category_name',
        hue='category_name',  # Explicitly set hue
        palette="viridis",
        legend=False,         # Hide legend since hue is just for coloring
        ax=ax
    )

    ax.set_title("Average Number of Days to Trend by Category")
    ax.set_xlabel("Average Days")
    ax.set_ylabel("Video Category")
    plt.tight_layout()

    return fig



def plot_trending_day_distribution(df: pd.DataFrame):
    """
    Nicely plots the count of trending videos by weekday without title clutter or palette warnings.
    """
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['publish_weekday'] = pd.Categorical(df['publish_weekday'], categories=weekday_order, ordered=True)

    count_df = df['publish_weekday'].value_counts().reindex(weekday_order).reset_index()
    count_df.columns = ['Weekday', 'Count']

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=count_df,
        x='Weekday',
        y='Count',
        hue='Weekday',  # add hue to satisfy Seaborn
        palette='crest',
        ax=ax,
        legend=False  # hide the legend since hue duplicates x
    )

    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Number of Videos")
    ax.set_title("Distribution of Trending Videos by publish Weekday") 
    plt.xticks(rotation=15)
    sns.despine()
    plt.tight_layout()

    return fig



def plot_trending_by_month(df):
    """
    Plots the number of trending videos by month.

    Args:
        df (pd.DataFrame): DataFrame with columns ['trending_month', 'count'].

    Returns:
        matplotlib.figure.Figure: Bar plot of trending videos by month.
    """
    # Map month numbers to names
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    df['month_name'] = df['trending_month'].map(month_names)
    df = df.sort_values('trending_month')

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x='month_name', y='count', hue='month_name', dodge=False, palette='Blues', ax=ax, legend=False)

    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Trending Videos')
    ax.set_title('Trending Videos by Month')  # ← added title
    ax.tick_params(axis='x', rotation=45)

    return fig



def visualize_top_tags_per_category(tag_data: dict, max_categories: int = 6, tags_per_category: int = 10) -> plt.Figure:
    """
    Visualizes the most frequent tags for each video category.

    Args:
        tag_data (dict): Dictionary where keys are category names and values are DataFrames 
                         with columns ['tag', 'count'] representing tag frequency.
        max_categories (int): Maximum number of categories to visualize (default is 6).
        tags_per_category (int): Number of top tags to show per category (default is 10).

    Returns:
        matplotlib.figure.Figure: The figure object containing subplots for each category.
    
    Notes:
        - Designed for output from `analyze_top_tags_by_category()`.
        - Uses a single color to avoid Seaborn's future warning about palettes without hue.
    """
    sns.set(style="whitegrid")
    num_categories = min(len(tag_data), max_categories)
    fig, axes = plt.subplots(nrows=num_categories, figsize=(12, 4 * num_categories), constrained_layout=True)

    # Ensure axes is iterable
    if num_categories == 1:
        axes = [axes]

    for ax, (category, df) in zip(axes, list(tag_data.items())[:num_categories]):
        # Sort and select top tags
        top_tags = df.nlargest(tags_per_category, 'count').sort_values(by='count')
        sns.barplot(
            x='count',
            y='tag',
            data=top_tags,
            ax=ax,
            color=sns.color_palette('viridis', n_colors=1)[0],  # consistent color
        )
        ax.set_title(f"Top {tags_per_category} Tags in '{category}'", fontsize=14)
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Tag")

    return fig


def plot_clickbait_effect_alternative(df: pd.DataFrame):
    """
    Plots side-by-side comparisons of clickbait vs. non-clickbait engagement using grouped bar charts.

    Args:
        df (pd.DataFrame): Must contain 'category_name', 'clickbait_in_title', 'views', 'likes', 'comment_count'.

    Returns:
        matplotlib.figure.Figure: The resulting matplotlib figure object.
    """
    import matplotlib.pyplot as plt
    import pandas as pd

    # Convert clickbait boolean to string for labeling
    df = df.copy()
    df['clickbait_in_title'] = df['clickbait_in_title'].map({True: 'Clickbait', False: 'No Clickbait'})

    metrics = ['views', 'likes', 'comment_count']
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 12), sharex=True)

    for i, metric in enumerate(metrics):
        pivot_df = df.pivot(index='category_name', columns='clickbait_in_title', values=metric)
        pivot_df.plot(kind='bar', ax=axes[i], colormap='Set2')
        axes[i].set_title(f'Average {metric.capitalize()} by Category and Clickbait')
        axes[i].set_ylabel(metric.capitalize())
        axes[i].grid(True)

    axes[-1].set_xlabel("Category")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    return fig



def plot_channel_category_heatmap(df, top_n=10):
    """
    Heatmap showing how often each top channel appears under each category.
    Returns the figure object.
    """
    top_channels = df['channel_title'].value_counts().head(top_n).index
    filtered = df[df['channel_title'].isin(top_channels)]

    pivot = (
        filtered.groupby(['channel_title', 'category_name'])
        .size()
        .unstack(fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu', ax=ax)

    ax.set_title('Trending Category Distribution Across Top Channels')
    ax.set_ylabel('Channel')
    ax.set_xlabel('Category')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig