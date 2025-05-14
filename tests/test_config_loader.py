from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.config_loader import get_paths_config, get_settings_config

paths = get_paths_config()
settings = get_settings_config()

data_dir = Path(paths['data_directory'])
countries = settings['analysis_settings']['country_list']

print(f"Working with countries: {countries}")
print(f"Data path: {data_dir.resolve()}")
