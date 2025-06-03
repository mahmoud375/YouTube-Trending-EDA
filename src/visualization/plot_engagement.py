import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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

def correlation_by_category_before_trend(df: pd.DataFrame) -> pd.Series:
    """
    Compute correlation between views and per-day engagement metrics before trending,
    grouped by video category.

    Args:
        df (pd.DataFrame): Dataset with YouTube video data including 'category_name',
                           'likes', 'dislikes', 'comment_count', 'views', 'days_to_trend'.

    Returns:
        pd.Series: Correlation of each metric (per day before trend) with views.
    """
    df = df.copy()

    # Filter out invalid values
    df = df[df["days_to_trend"] > 0]  # remove invalid zeros to avoid division by zero

    # Estimate engagement per day before trending
    df["likes_per_day"] = df["likes"] / df["days_to_trend"]
    df["dislikes_per_day"] = df["dislikes"] / df["days_to_trend"]
    df["comments_per_day"] = df["comment_count"] / df["days_to_trend"]
    df["views_per_day"] = df["views"] / df["days_to_trend"]

    grouped = df.groupby("category_name").agg(
        avg_views_per_day=("views_per_day", "mean"),
        avg_likes_per_day=("likes_per_day", "mean"),
        avg_dislikes_per_day=("dislikes_per_day", "mean"),
        avg_comments_per_day=("comments_per_day", "mean")
    ).reset_index()

    corr_matrix = grouped[[
        "avg_views_per_day",
        "avg_likes_per_day",
        "avg_dislikes_per_day",
        "avg_comments_per_day"
    ]].corr()

    return corr_matrix["avg_views_per_day"].sort_values(ascending=False)

def plot_engagement_disabled_stats(df: pd.DataFrame) -> plt.Figure:
    """
    Returns a bar plot figure showing average views, likes, and comments 
    grouped by whether comments or ratings are disabled.
    
    Args:
        df (pd.DataFrame): YouTube dataset with 'comments_disabled', 
                           'ratings_disabled', 'views', 'likes', 
                           'comment_count', 'video_id'.

    Returns:
        plt.Figure: The matplotlib figure object.
    """
    # Aggregate average stats by comment/rating disable flags
    engagement_df = (
        df.groupby(['comments_disabled', 'ratings_disabled'], as_index=False)
        .agg(
            avg_views=('views', 'mean'),
            avg_likes=('likes', 'mean'),
            avg_comments=('comment_count', 'mean'),
            count=('video_id', 'count')
        )
    )

    # Create readable labels
    engagement_df["label"] = (
        "Comments: " + engagement_df["comments_disabled"].astype(str) +
        " | Ratings: " + engagement_df["ratings_disabled"].astype(str)
    )

    # Create subplots
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))

    # Plot views
    sns.barplot(data=engagement_df, x="label", y="avg_views", ax=axs[0], hue="label", legend=False, palette="Set2")
    axs[0].set_title("Average Views")
    axs[0].set_ylabel("Views")

    # Plot likes
    sns.barplot(data=engagement_df, x="label", y="avg_likes", ax=axs[1], hue="label", legend=False, palette="Set2")
    axs[1].set_title("Average Likes")
    axs[1].set_ylabel("Likes")

    # Plot comments
    sns.barplot(data=engagement_df, x="label", y="avg_comments", ax=axs[2], hue="label", legend=False, palette="Set2")
    axs[2].set_title("Average Comments")
    axs[2].set_ylabel("Comments")

    # Clean x-axis labels
    for ax in axs:
        ax.tick_params(axis='x', labelrotation=15)
        ax.set_xlabel("")

    plt.tight_layout()
    return fig


def plot_engagement_correlation_before_trend(df: pd.DataFrame):
    """
    Visualize correlation between pre-trend engagement metrics and views/day.

    Parameters:
        df (pd.DataFrame): YouTube data including engagement and 'days_to_trend'.

    Returns:
        matplotlib.figure.Figure: The resulting bar plot figure.
    """
    corr_series = correlation_by_category_before_trend(df)

    # Drop the self-correlation
    corr_df = corr_series.drop("avg_views_per_day").reset_index()
    corr_df.columns = ["metric", "correlation"]

    # Rename for nicer display
    name_map = {
        "avg_likes_per_day": "Likes/day",
        "avg_dislikes_per_day": "Dislikes/day",
        "avg_comments_per_day": "Comments/day",
    }
    corr_df["metric"] = corr_df["metric"].map(name_map)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=corr_df,
        x="metric",
        y="correlation",
        hue="metric",       
        palette="Set2",
        legend=False,      
        ax=ax
    )

    ax.set_title("Correlation with Views/Day Before Trending")
    ax.set_ylabel("Correlation")
    ax.set_xlabel("")

    min_corr = min(0, corr_df["correlation"].min() - 0.05)
    ax.set_ylim(min_corr, 1)

    ax.axhline(0, color='gray', linestyle='--', linewidth=1)

    plt.xticks(rotation=15)
    plt.tight_layout()

    return fig

def plot_like_dislike_ratio_vs_views(df: pd.DataFrame):
    """
    Visualize avg Like/Dislike ratio vs avg Views per category.

    Parameters:
        df (pd.DataFrame): DataFrame with 'category_name', 'avg_like_dislike_ratio', 'avg_views'.

    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot
    sns.scatterplot(
        data=df,
        x="avg_like_dislike_ratio",
        y="avg_views",
        s=100,
        color="mediumseagreen",
        ax=ax
    )

    # Annotate each point with category name
    for _, row in df.iterrows():
        ax.text(
            row["avg_like_dislike_ratio"] + 0.5,
            row["avg_views"],
            row["category_name"],
            fontsize=9,
            verticalalignment='center'
        )

    ax.set_title("Average Like/Dislike Ratio vs Average Views by Category")
    ax.set_xlabel("Avg Like/Dislike Ratio")
    ax.set_ylabel("Avg Views")
    ax.grid(True)
    plt.tight_layout()
    return fig

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


def plot_category_engagement(df, metric="avg_engagement_rate", top_n=None):
    """
    Visualize engagement metrics by video category and return the figure.

    Args:
        df (pd.DataFrame): Summary DataFrame with category data.
        metric (str): Column name to visualize.
        top_n (int, optional): Show top N categories.

    Returns:
        matplotlib.figure.Figure: The resulting figure object.
    """
    plot_df = df.sort_values(metric, ascending=False)
    if top_n:
        plot_df = plot_df.head(top_n)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        data=plot_df,
        x=metric,
        y="category_name",
        hue="category_name",
        palette="viridis",
        legend=False,
        ax=ax
    )
    ax.set_title(f"{metric.replace('_', ' ').title()} by Category")
    ax.set_xlabel(metric.replace('_', ' ').title())
    ax.set_ylabel("Category")
    fig.tight_layout()
    
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




def visualize_status_impact(df: pd.DataFrame) -> plt.Figure:
    """
    Visualize the impact of video status flags on engagement metrics.
    The function plots a heatmap showing the differences in views, likes, dislikes, and comment_count
    for videos with each flag being ON and OFF.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing the engagement metrics for videos with flags ON and OFF.
        Expected format: MultiIndex with 'Flag' and 'Metric' levels.

    Returns:
    --------
    plt.Figure
        A heatmap visualization of the engagement metrics across different flags.
    """
    # Set up the figure
    plt.figure(figsize=(10, 8))

    # Create a heatmap for visualizing the impact
    heatmap_data = df.unstack(level=1).T
    sns.heatmap(
        heatmap_data,
        annot=True,  # Show values on the heatmap
        fmt=".2e",  # Exponential format for large numbers
        cmap='YlGnBu',  # Choose a color palette
        cbar_kws={'label': 'Engagement Metrics'},
        linewidths=0.5,  # Line width between cells
        linecolor='gray',  # Color of the lines
        vmin=0, vmax=1.5e6  # Set min/max values for the heatmap scale
    )

    # Titles and labels
    plt.title("Impact of Video Status Flags on Engagement", fontsize=16)
    plt.xlabel('Metric', fontsize=12)
    plt.ylabel('Flag', fontsize=12)
    plt.xticks(rotation=45, ha="right")

    # Show the plot
    plt.tight_layout()

    return plt.gcf()

