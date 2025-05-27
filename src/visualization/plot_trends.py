import matplotlib.pyplot as plt

# ========== Core Plot Functions ==========

def plot_daily_counts(df, date_col, title='Daily Item Counts'):
    """
    Plot the count of entries per day based on a date column.

    Args:
        df (pd.DataFrame): The input DataFrame.
        date_col (str): The name of the column containing datetime values.
        title (str): The title of the plot.
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
    Plot the average of a specified column per day.

    Args:
        df (pd.DataFrame): The input DataFrame.
        date_col (str): Column containing datetime values.
        value_col (str): Column whose average is to be plotted.
        title (str): Title of the plot.
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
    Plot count and average metrics over time using two Y-axes.

    Args:
        df (pd.DataFrame): The input DataFrame.
        date_col (str): Column with datetime values.
        count_col (str): Column to count (non-null values).
        avg_col (str): Column to average.
        title (str): Title of the plot.
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

# ========== Engagement Specific ==========

def plot_engagement_by_user(df, user_col, value_col, title='Engagement by User'):
    """
    Plot total engagement per user.

    Args:
        df (pd.DataFrame): The input DataFrame.
        user_col (str): Column representing user ID or name.
        value_col (str): Column representing the value to be summed.
        title (str): Title of the plot.
    """
    user_engagement = df.groupby(user_col)[value_col].sum().sort_values(ascending=False)
    user_engagement.plot(kind='bar', figsize=(12, 6), color='green')
    plt.title(title)
    plt.xlabel('User')
    plt.ylabel(f'Total {value_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_engagement_by_post(df, post_col, value_col, title='Engagement by Post'):
    """
    Plot total engagement per post.

    Args:
        df (pd.DataFrame): The input DataFrame.
        post_col (str): Column representing post ID or title.
        value_col (str): Column representing engagement to be summed.
        title (str): Title of the plot.
    """
    post_engagement = df.groupby(post_col)[value_col].sum().sort_values(ascending=False)
    post_engagement.plot(kind='bar', figsize=(12, 6), color='purple')
    plt.title(title)
    plt.xlabel('Post')
    plt.ylabel(f'Total {value_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_engagement_trends(df, date_col, value_col, title='Engagement Trends Over Time'):
    """
    Plot the total engagement over time (daily).

    Args:
        df (pd.DataFrame): The input DataFrame.
        date_col (str): Column containing datetime values.
        value_col (str): Column representing engagement to be summed.
        title (str): Title of the plot.
    """
    trend_data = df.groupby(date_col)[value_col].sum()
    trend_data.plot(kind='line', marker='o', figsize=(12, 6), color='orange')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(f'Total {value_col}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ========== Utility Chart Functions ==========

def create_bar_chart(data, title='Bar Chart', xlabel='', ylabel='', color='blue'):
    """
    Create a simple bar chart.

    Args:
        data (pd.Series): The data to plot.
        title (str): Title of the plot.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
        color (str): Bar color.
    """
    data.plot(kind='bar', figsize=(10, 5), color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def create_line_chart(data, title='Line Chart', xlabel='', ylabel='', color='black'):
    """
    Create a simple line chart.

    Args:
        data (pd.Series): The data to plot.
        title (str): Title of the plot.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
        color (str): Line color.
    """
    data.plot(kind='line', marker='o', figsize=(10, 5), color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ========== Customization Functions ==========

def customize_plot_style(style='ggplot'):
    """
    Apply a Matplotlib style to all plots.

    Args:
        style (str): Name of the matplotlib style (e.g., 'ggplot', 'seaborn').
    """
    plt.style.use(style)


def add_plot_labels(xlabel='', ylabel='', title=''):
    """
    Add labels and title to the current plot.

    Args:
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        title (str): Plot title.
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

# ========== Output Functions ==========

def save_engagement_plot(filename='engagement_plot.png'):
    """
    Save the current figure to an image file.

    Args:
        filename (str): The name of the file to save the plot to.
    """
    plt.savefig(filename, bbox_inches='tight')
    print(f'Plot saved as {filename}')

