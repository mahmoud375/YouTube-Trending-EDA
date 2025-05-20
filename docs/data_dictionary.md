# Data Dictionary for YouTube Trending Dataset

This data dictionary describes the columns included in the dataset used for analyzing trending YouTube videos.

| Column Name                   | Description                                                                          |     |
| ----------------------------- | ------------------------------------------------------------------------------------ | --- |
| **video\_id**                 | Unique identifier for the YouTube video.                                             |     |
| **trending\_date**            | The date the video became trending (in `YY.DD.MM` format).                           |     |
| **title**                     | The title of the YouTube video.                                                      |     |
| **channel\_title**            | The name of the channel that uploaded the video.                                     |     |
| **category\_id**              | Numeric ID representing the category of the video (can be mapped to category\_name). |     |
| **publish\_time**             | The original publish date and time of the video (in ISO 8601 format).                |     |
| **tags**                      | A string of tags associated with the video, separated by \`                          | \`. |
| **views**                     | The number of views the video had at the time of trending.                           |     |
| **likes**                     | The number of likes the video had at the time of trending.                           |     |
| **dislikes**                  | The number of dislikes the video had at the time of trending.                        |     |
| **comment\_count**            | The number of comments the video had at the time of trending.                        |     |
| **thumbnail\_link**           | URL of the video’s thumbnail image.                                                  |     |
| **comments\_disabled**        | Boolean indicating if comments are disabled (`True` or `False`).                     |     |
| **ratings\_disabled**         | Boolean indicating if likes/dislikes are disabled (`True` or `False`).               |     |
| **video\_error\_or\_removed** | Boolean indicating if the video is unavailable due to error or removal.              |     |
| **description**               | The full description of the video as written by the uploader.                        |     |
| **category\_name**            | The name of the category (e.g., Music, Gaming), mapped from `category_id`.           |     |


## Notes and Caveats

- The `trending_date` format is `YY.DD.MM`, which may require conversion to standard format.
- The dataset may contain duplicates for videos trending on multiple days.
- Some videos have missing descriptions or tags.
- `dislikes` column may no longer be accurate due to YouTube hiding public dislike counts after 2021.
