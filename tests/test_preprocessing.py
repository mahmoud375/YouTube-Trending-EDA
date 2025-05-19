import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config_loader import get_paths_config
from src.preprocessing.clean_data import load_data
from src.preprocessing.merge_datasets import dataset_merger

paths = get_paths_config()

def test_clean_data():
    CA_data_csv_path = Path(paths['CA_data'])/ 'CAvideos.csv'
    CA_data_CSV = load_data(CA_data_csv_path)

    CA_data_json_path = Path(paths['CA_data'])/ 'CA_category_id.json'
    CA_data_json = load_data(CA_data_json_path)
    #print(CA_data_CSV.head())
    #print(CA_data_json)

    return [CA_data_csv_path, CA_data_json_path]

def test_marge_data():
    files_paths = test_clean_data()
    string_paths = [str(p) for p in files_paths]
    
    marged_df = dataset_merger(string_paths)
    print(marged_df.columns)

   


if __name__ == '__main__':
    #test_clean_data()
    test_marge_data()