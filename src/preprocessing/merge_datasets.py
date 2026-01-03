import pandas as pd
import os
import json
from pathlib import Path

def dataset_merger(file_paths, how='inner', on=None):
    """
    Merge multiple datasets (CSV and structured JSON) into a single DataFrame.

    Parameters:
    - file_paths (list): List of file paths (CSV or JSON).
    - how (str): Type of merge: 'inner', 'outer', 'left', or 'right'.
    - on (str or list): Column(s) to join on. If None, auto-detects common columns.

    Returns:
    - pd.DataFrame: Merged DataFrame.
    """
    dataframes = []

    for file in file_paths:
        # Convert Path objects to strings for compatibility
        file_str = str(file) if isinstance(file, Path) else file
        
        if not os.path.exists(file_str):
            raise FileNotFoundError(f"File not found: {file_str}")
        
        if file_str.endswith('.csv'):
            df = pd.read_csv(file_str)

        elif file_str.endswith('.json'):
            with open(file_str, 'r') as f:
                data = json.load(f)
                if "items" in data and isinstance(data["items"], list):
                    # Extract 'id' and 'snippet.title'
                    extracted = []
                    for item in data["items"]:
                        if "id" in item and "snippet" in item and "title" in item["snippet"]:
                            extracted.append({
                                "category_id": int(item["id"]),
                                "category_name": item["snippet"]["title"]
                            })
                    df = pd.DataFrame(extracted)
                else:
                    raise ValueError("Unsupported JSON structure.")
        else:
            raise ValueError(f"Unsupported file type: {file}")

        dataframes.append(df)

    # Start with the first DataFrame
    merged_df = dataframes[0]

    for df in dataframes[1:]:
        if on is None:
            common_cols = merged_df.columns.intersection(df.columns).tolist()
            if not common_cols:
                raise ValueError("No common columns to join on. Please specify 'on' parameter.")
        else:
            common_cols = on

        merged_df = pd.merge(merged_df, df, how=how, on=common_cols)

    return merged_df
