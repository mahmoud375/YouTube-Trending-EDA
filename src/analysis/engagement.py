import pandas as pd

# =============================================================
# Engagement & Trend Analysis by Category - YouTube Dataset
# =============================================================
# This module analyzes YouTube trending video data by category.
# It includes functions to:
#   - Compute engagement metrics (engagement rate, like/dislike ratio)
#   - Analyze correlation between views and likes/dislikes/comments
#   - Examine the impact of disabling comments or ratings
#   - Summarize category-level statistics
# =============================================================

# ------------------------------
# Engagement Rate Calculation
# ------------------------------

def compute_engagement_rate_df(df: pd.DataFrame) -> pd.Series:
    """
    Compute engagement rate for each video in the DataFrame.
    Engagement Rate = (likes + comment_count) / views * 100

    Args:
        df (pd.DataFrame): Dataset containing 'likes', 'comment_count', and 'views'.

    Returns:
        pd.Series: Engagement rate per video (as a percentage).
    """
    safe_views = df["views"].replace(0, pd.NA)
    return ((df["likes"] + df["comment_count"]) / safe_views) * 100


def compute_like_dislike_ratio_df(df: pd.DataFrame) -> pd.Series:
    """
    Compute like-to-dislike ratio per video.
    To avoid division by zero, adds +1 to denominator.

    Args:
        df (pd.DataFrame): Dataset containing 'likes' and 'dislikes'.

    Returns:
        pd.Series: Like/dislike ratio.
    """
    return df["likes"] / (df["dislikes"] + 1)

# ------------------------------
# Category-Level Engagement Summary
# ------------------------------

def summarize_engagement_by_category_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize total and average engagement metrics grouped by category.

    Args:
        df (pd.DataFrame): Dataset with 'category_name', 'likes', 'comment_count', and 'views'.

    Returns:
        pd.DataFrame: Summary with total/average metrics for each category.
    """
    df = df.copy()
    df["engagement_rate"] = compute_engagement_rate_df(df).fillna(0)

    grouped = df.groupby("category_name").agg(
        video_count=("video_id", "count"),
        total_likes=("likes", "sum"),
        total_comments=("comment_count", "sum"),
        total_views=("views", "sum"),
        avg_engagement_rate=("engagement_rate", "mean")
    ).reset_index()

    return grouped

# ------------------------------
# Correlation Analysis
# ------------------------------

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



def print_engagement_correlation_before_trend(df: pd.DataFrame) -> None:
    """
    Print correlation summary between daily engagement metrics (before trending) and views.

    This version considers only engagement that happened between publish time and
    trending date, by normalizing metrics over 'days_to_trend'.

    Args:
        df (pd.DataFrame): YouTube data with engagement and days_to_trend.

    Returns:
        None
    """
    corr_series = correlation_by_category_before_trend(df)
    mapping = {
        "avg_comments_per_day": "Comments/day",
        "avg_dislikes_per_day": "Dislikes/day",
        "avg_likes_per_day": "Likes/day",
        "avg_views_per_day": "Views/day"
    }

    corr_df = corr_series.drop("avg_views_per_day").reset_index()
    corr_df.columns = ["Metric", "Correlation with Views/day"]
    corr_df["Metric"] = corr_df["Metric"].map(mapping)

    print("\n Correlation Between Pre-Trend Daily Engagement and Trending Success (Views/day)\n")
    for _, row in corr_df.iterrows():
        print(f"- {row['Metric']:<15}: {row['Correlation with Views/day']:.3f}")


# ------------------------------
# Like/Dislike Ratio vs Views
# ------------------------------

def like_dislike_ratio_vs_views(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze relationship between average like/dislike ratio and views across categories.

    Args:
        df (pd.DataFrame): Dataset containing 'likes', 'dislikes', 'views', 'category_name'.

    Returns:
        pd.DataFrame: Grouped by category with ratio and average views, sorted by views.
    """
    df = df.copy()
    df["like_dislike_ratio"] = compute_like_dislike_ratio_df(df)

    grouped = df.groupby("category_name").agg(
        avg_like_dislike_ratio=("like_dislike_ratio", "mean"),
        avg_views=("views", "mean")
    ).reset_index()

    corr = grouped["avg_like_dislike_ratio"].corr(grouped["avg_views"])
    print(f"Correlation between like/dislike ratio and average views: {corr:.3f}")
    return grouped.sort_values(by="avg_views", ascending=False)

# ------------------------------
# Disabled Engagement Features
# ------------------------------

def engagement_disabled_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare performance of videos with disabled comments or ratings.

    Args:
        df (pd.DataFrame): Dataset with boolean columns 'comments_disabled', 'ratings_disabled'.

    Returns:
        pd.DataFrame: Grouped statistics showing average views, likes, comments.
    """
    return df.groupby(["comments_disabled", "ratings_disabled"]).agg(
        avg_views=("views", "mean"),
        avg_likes=("likes", "mean"),
        avg_comments=("comment_count", "mean"),
        count=("video_id", "count")
    ).reset_index()



def compute_engagement_rate_df(df: pd.DataFrame) -> pd.Series:
    """
    Compute engagement rate for a DataFrame of videos.
    Engagement rate = (likes + comment_count) / views * 100
    """
    safe_views = df["views"].replace(0, pd.NA)
    return ((df["likes"] + df["comment_count"]) / safe_views) * 100

def summarize_engagement_by_category_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize engagement metrics grouped by category_name.

    Args:
        df (pd.DataFrame): Full video dataset with category_name, likes, comment_count, and views columns.

    Returns:
        pd.DataFrame: Summary with category_name, video_count, total_likes, total_comments,
                      total_views, avg_engagement_rate.
    """
    df = df.copy()
    df["engagement_rate"] = compute_engagement_rate_df(df).fillna(0)

    grouped = df.groupby("category_name").agg(
        video_count=("video_id", "count"),
        total_likes=("likes", "sum"),
        total_comments=("comment_count", "sum"),
        total_views=("views", "sum"),
        avg_engagement_rate=("engagement_rate", "mean")
    ).reset_index()

    return grouped


def compare_status_impact(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare the impact of video status flags on engagement metrics.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing YouTube trending video data. Must include the following columns:
        - 'comments_disabled'
        - 'ratings_disabled'
        - 'video_error_or_removed'
        - 'views', 'likes', 'dislikes', 'comment_count'

    Returns:
    --------
    pd.DataFrame
        A multi-index DataFrame showing average engagement metrics when each flag is ON vs OFF.
        Rows are a MultiIndex of (Flag, Metric), and columns are 'Flag OFF', 'Flag ON'.
    """
    status_flags = ['comments_disabled', 'ratings_disabled', 'video_error_or_removed']
    engagement_metrics = ['views', 'likes', 'dislikes', 'comment_count']

    results = []

    for flag in status_flags:
        grouped = (
            df.groupby(flag)[engagement_metrics]
            .mean()
            .rename(index={False: 'Flag OFF', True: 'Flag ON'})
            .T
        )
        # Reshape for neat MultiIndex
        grouped['Flag'] = flag
        grouped = grouped.set_index('Flag', append=True).reorder_levels([1, 0])
        results.append(grouped)

    summary_df = pd.concat(results)
    return summary_df
