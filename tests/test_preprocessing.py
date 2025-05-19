import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config_loader import get_paths_config
from src.preprocessing.clean_data import load_data

paths = get_paths_config()
CA_data_path = Path(paths['CA_data'])/ 'CAvideos.csv'
CA_data = load_data(CA_data_path)

print(CA_data.head())