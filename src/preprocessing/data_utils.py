import numpy as np
import pandas as pd


def load_data(file_path):
    """
    Load a CSV dataset into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        The path to the CSV file to be loaded.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)


def explore_data(df):
    """
    Display basic information about the DataFrame for exploration.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to explore.
    """
    print("Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nSummary Statistics:\n", df.describe(include='all'))


def unique_values_with_counts(df, column):
    """
    Get unique values in a column along with their counts.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame.
    column : str
        The name of the column to analyze.

    Returns
    -------
    pd.Series
        A Series with unique values as index and their counts as values.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    return df[column].value_counts()



def handle_missing_values(df, strategy="mean"):
    """
    Handle missing values in a DataFrame using a specified strategy.

    Supported strategies:
    - 'mean': Replace missing values with the column mean.
    - 'median': Replace missing values with the column median.
    - 'mode': Replace missing values with the column mode.
    - 'drop': Remove rows that contain any missing values.
    - 'differentiated': For numeric columns, replace missing values with the median;
        for categorical columns, replace with the mode.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame that may contain missing values.
    strategy : str, optional
        Strategy to handle missing values (default is 'mean'). Must be one of
        {'mean', 'median', 'mode', 'drop', 'differentiated'}.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values handled according to the specified strategy.

    Raises
    ------
    ValueError
        If the provided strategy is not one of 'mean', 'median', 'mode', 'drop', or 'differentiated'.
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy in ["mean", "median"]:
        return df.fillna(df.mean() if strategy == "mean" else df.median())
    elif strategy == "mode":
        # Use the first mode in case there are multiple modes
        return df.fillna(df.mode().iloc[0])
    elif strategy == "differentiated":
        df_filled = df.copy()
        numeric_cols = df_filled.select_dtypes(include=[np.number]).columns
        categorical_cols = df_filled.select_dtypes(
            include=["object", "category"]
        ).columns
        for col in numeric_cols:
            df_filled[col] = df_filled[col].fillna(df_filled[col].median())
        for col in categorical_cols:
            df_filled[col] = df_filled[col].fillna(df_filled[col].mode().iloc[0])
        return df_filled
    else:
        raise ValueError(
            "Strategy must be 'mean', 'median', 'mode', 'drop', or 'differentiated'"
        )


def encode_categorical(df):
    """
    Encode categorical columns in a DataFrame using pandas' factorize.

    Each categorical column (columns of type 'object' or 'category') is replaced
    with numerical codes.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with categorical columns.

    Returns
    -------
    pd.DataFrame
        A copy of the original DataFrame with all categorical columns encoded.
    """
    df_encoded = df.copy()
    for col in df_encoded.select_dtypes(include=["object", "category"]).columns:
        df_encoded[col], _ = pd.factorize(df_encoded[col].astype(str))
    return df_encoded


def drop_columns(df, columns):
    """
    Drop specified columns from a DataFrame.

    This function removes the columns listed in 'columns' from the DataFrame. If a column
    is not present, it is ignored.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    columns : list of str
        List of column names to drop.

    Returns
    -------
    pd.DataFrame
        DataFrame with the specified columns removed.
    """
    return df.drop(columns=columns, errors="ignore")


def convert_to_datetime(df, date_col, date_format='%y.%d.%m'):
    """
    Convert a string date column to datetime.

    Args:
        df (pd.DataFrame): The data frame.
        date_col (str): Name of the date column.
        date_format (str): Format of the date strings.
    
    Returns:
        pd.DataFrame: DataFrame with converted date column.
    """
    df[date_col] = pd.to_datetime(df[date_col], format=date_format)
    return df


def save_table(df, filename: str, format: str = "csv"):
    """
    Save a DataFrame table to disk.

    Args:
        df (pd.DataFrame): Table to save.
        filename (str): File path without extension.
        format (str): One of ["csv", "excel", "html"].
    """
    format = format.lower()
    if format == "csv":
        df.to_csv(f"{filename}.csv", index=False)
    elif format == "excel":
        df.to_excel(f"{filename}.xlsx", index=False)
    elif format == "html":
        df.to_html(f"{filename}.html", index=False)
    else:
        raise ValueError("Unsupported format. Choose from 'csv', 'excel', or 'html'.")

