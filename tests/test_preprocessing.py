import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pathlib import Path
import yaml
with open(os.path.join('config', 'paths.yaml'), 'r') as f:
    paths = yaml.safe_load(f)

from src.preprocessing.clean_data import load_data, split_data

CA_data_pass = os.path.join(paths['CA_data'], 'CAvideos.csv')
CA_data = load_data(CA_data_pass)

print(CA_data.head())
