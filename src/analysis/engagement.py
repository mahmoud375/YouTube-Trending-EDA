from typing import List, Dict, Union, Optional

VideoRecord = Dict[str, Union[int, float, str, bool]]


def calculate_engagement_metrics(video: VideoRecord) -> Dict[str, int]:
    """
    Calculate basic engagement counts from a video record.

    Args:
        video (VideoRecord): Dictionary representing a video's data.

    Returns:
        Dict[str, int]: Dict with keys: likes, dislikes, comments, total_engagement.
    """
    likes = int(video.get("likes", 0))
    dislikes = int(video.get("dislikes", 0))
    comments = int(video.get("comment_count", 0))
    total_engagement = likes + comments + dislikes
    return {
        "likes": likes,
        "dislikes": dislikes,
        "comments": comments,
        "total_engagement": total_engagement
    }


def compute_engagement_rate(video: VideoRecord) -> float:
    """
    Compute engagement rate as (likes + comments) / views * 100.

    Args:
        video (VideoRecord): Video data dict.

    Returns:
        float: Engagement rate percentage (0-100).
    """
    likes = video.get("likes", 0)
    comments = video.get("comment_count", 0)
    views = video.get("views", 0)
    if views == 0:
        return 0.0
    return ((likes + comments) / views) * 100


def compare_video_engagement(video_a: VideoRecord, video_b: VideoRecord) -> Dict[str, int]:
    """
    Compare engagement between two videos.

    Args:
        video_a (VideoRecord): First video's data.
        video_b (VideoRecord): Second video's data.

    Returns:
        Dict[str, int]: Differences in likes, dislikes, comments, total engagement.
    """
    metrics_a = calculate_engagement_metrics(video_a)
    metrics_b = calculate_engagement_metrics(video_b)

    diff = {
        "likes_diff": metrics_a["likes"] - metrics_b["likes"],
        "dislikes_diff": metrics_a["dislikes"] - metrics_b["dislikes"],
        "comments_diff": metrics_a["comments"] - metrics_b["comments"],
        "total_engagement_diff": metrics_a["total_engagement"] - metrics_b["total_engagement"]
    }
    return diff


def generate_engagement_summary(videos: List[VideoRecord]) -> List[Dict[str, Union[str, int, float]]]:
    """
    Generate a summary of engagement for multiple videos.

    Args:
        videos (List[VideoRecord]): List of video records.

    Returns:
        List[Dict]: Each dict contains video_id, title, likes, comments, views, engagement_rate.
    """
    summary = []
    for video in videos:
        video_id = video.get("video_id", "N/A")
        title = video.get("title", "")
        likes = int(video.get("likes", 0))
        comments = int(video.get("comment_count", 0))
        views = int(video.get("views", 0))
        engagement_rate = compute_engagement_rate(video)
        summary.append({
            "video_id": video_id,
            "title": title,
            "likes": likes,
            "comments": comments,
            "views": views,
            "engagement_rate": engagement_rate
        })
    return summary


def track_like(video: VideoRecord, count: int = 1) -> None:
    """
    Increment likes count in the video record.

    Args:
        video (VideoRecord): Video record to update.
        count (int): Number of likes to add.

    Returns:
        None
    """
    video["likes"] = video.get("likes", 0) + count


def track_comment(video: VideoRecord, count: int = 1) -> None:
    """
    Increment comment_count in the video record.

    Args:
        video (VideoRecord): Video record to update.
        count (int): Number of comments to add.

    Returns:
        None
    """
    video["comment_count"] = video.get("comment_count", 0) + count


def reset_engagement(video: VideoRecord) -> None:
    """
    Reset engagement metrics (likes, dislikes, comments) to zero.

    Args:
        video (VideoRecord): Video record to reset.

    Returns:
        None
    """
    video["likes"] = 0
    video["dislikes"] = 0
    video["comment_count"] = 0
