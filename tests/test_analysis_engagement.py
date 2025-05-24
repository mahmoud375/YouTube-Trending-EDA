import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analysis.engagement import *

videos = [
    {
        "video_id": "x1",
        "title": "First Video",
        "likes": 100,
        "dislikes": 5,
        "comment_count": 20,
        "views": 2000,
    },
    {
        "video_id": "x2",
        "title": "Second Video",
        "likes": 150,
        "dislikes": 3,
        "comment_count": 30,
        "views": 3000,
    }
]

from pprint import pprint

# Calculate engagement metrics for the first video
metrics = calculate_engagement_metrics(videos[0])
print("Engagement metrics for first video:")
pprint(metrics)
# {'likes': 100, 'dislikes': 5, 'comments': 20, 'total_engagement': 125}

# Compute engagement rate for second video
rate = compute_engagement_rate(videos[1])
print(f"\nEngagement rate for second video: {rate:.2f}%")
# Engagement rate for second video: 6.00%

# Compare engagement between first and second video
diff = compare_video_engagement(videos[0], videos[1])
print("\nEngagement difference (video 1 - video 2):")
pprint(diff)
# {'likes_diff': -50, 'dislikes_diff': 2, 'comments_diff': -10, 'total_engagement_diff': -58}

# Generate summary for all videos
summary = generate_engagement_summary(videos)
print("\nEngagement summary:")
pprint(summary)
# [
#   {'video_id': 'x1', 'title': 'First Video', 'likes': 100, 'comments': 20, 'views': 2000, 'engagement_rate': 6.0},
#   {'video_id': 'x2', 'title': 'Second Video', 'likes': 150, 'comments': 30, 'views': 3000, 'engagement_rate': 6.0}
# ]

# Track a new like and comment on first video
track_like(videos[0])
track_comment(videos[0], 2)
print("\nUpdated engagement for first video after tracking:")
pprint(videos[0])
# 'likes': 101, 'comment_count': 22

# Reset engagement stats on second video
reset_engagement(videos[1])
print("\nSecond video after resetting engagement:")
pprint(videos[1])
# 'likes': 0, 'dislikes': 0, 'comment_count': 0

