import yaml
import os

def load_yaml(relative_path: str) -> dict:
    """
    Load a YAML file relative to the project root and return its content as a dictionary.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # جذر المشروع
    abs_path = os.path.join(base_dir, relative_path)

    try:
        with open(abs_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found at path: {abs_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file at path: {abs_path}\n{str(e)}")
    
def get_paths_config() -> dict:
    """
    Load paths configuration from config/paths.yaml
    """
    return load_yaml("config/paths.yaml")

def get_settings_config() -> dict:
    """
    Load settings configuration from config/settings.yaml
    """
    return load_yaml("config/settings.yaml")


