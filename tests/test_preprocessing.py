import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from pathlib import Path
from src.config_loader import get_paths_config
from src.preprocessing.data_utils import load_data, unique_values_with_counts
from src.preprocessing.merge_datasets import dataset_merger

def test_load_data_csv_and_json():
    paths = get_paths_config()

    csv_path = Path(paths['CA_data']) / 'CAvideos.csv'
    json_path = Path(paths['CA_data']) / 'CA_category_id.json'

    df_csv = load_data(csv_path)
    df_json = load_data(json_path)

    assert isinstance(df_csv, pd.DataFrame)
    assert not df_csv.empty

    assert isinstance(df_json, (dict, list, pd.DataFrame))

    if isinstance(df_json, dict):
        assert "items" in df_json
    elif isinstance(df_json, list):
        assert len(df_json) > 0
    elif isinstance(df_json, pd.DataFrame):
        assert not df_json.empty


def test_dataset_merger_returns_dataframe():
    paths = get_paths_config()

    csv_path = Path(paths['CA_data']) / 'CAvideos.csv'
    json_path = Path(paths['CA_data']) / 'CA_category_id.json'
    merged_df = dataset_merger([str(csv_path), str(json_path)])

    assert isinstance(merged_df, pd.DataFrame)
    assert not merged_df.empty
    assert 'title' in merged_df.columns or 'video_id' in merged_df.columns  # adjust based on structure

def test_unique_values_with_counts():
    df = pd.DataFrame({
        'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Blue', 'Red'],
        'Size': ['S', 'M', 'L', 'S', 'M', 'L', 'M']
    })

    color_counts = unique_values_with_counts(df, 'Color')

    assert isinstance(color_counts, pd.Series)

    assert color_counts['Red'] == 3
    assert color_counts['Blue'] == 3
    assert color_counts['Green'] == 1



if __name__ == '__main__':
    #test_unique_values_with_counts()
    #test_dataset_merger_returns_dataframe()
    test_load_data_csv_and_json()