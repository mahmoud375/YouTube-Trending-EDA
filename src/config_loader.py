from pathlib import Path
import yaml


def find_project_root(marker_files=('README.md', 'requirements.txt', '.git')) -> Path:
    """
    Find the project root directory by looking for marker files/directories.
    
    Args:
        marker_files: Tuple of filenames/directories that indicate the project root.
    
    Returns:
        Path: Absolute path to the project root directory.
    """
    current = Path(__file__).resolve()
    # Check current file's directory and all parent directories
    for parent in [current] + list(current.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent
    # Fallback: assume config_loader.py is in src/, so project root is parent.parent
    return current.parent.parent


# Global constant for project root
PROJECT_ROOT = find_project_root()


def load_yaml(relative_path: str) -> dict:
    """
    Load a YAML file relative to the project root and return its content as a dictionary.
    
    Args:
        relative_path: Path to YAML file relative to project root.
    
    Returns:
        dict: Parsed YAML content.
    
    Raises:
        FileNotFoundError: If the YAML file doesn't exist.
        ValueError: If the YAML file is malformed.
    """
    abs_path = PROJECT_ROOT / relative_path

    try:
        with abs_path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found at path: {abs_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file at path: {abs_path}\n{str(e)}")


def get_paths_config() -> dict:
    """
    Load paths configuration from config/paths.yaml and convert all relative paths to absolute Path objects.
    
    Returns:
        dict: Configuration dictionary with all path strings converted to absolute Path objects.
    
    Note:
        This ensures paths work regardless of the current working directory when scripts/notebooks are executed.
    """
    raw_config = load_yaml("config/paths.yaml")
    paths_config = {}
    
    for key, value in raw_config.items():
        if isinstance(value, str) and (value.startswith('./') or value.startswith('../')):
            # Convert relative paths to absolute Path objects
            # Strip leading './' to avoid double resolution
            clean_path = value.lstrip('./')
            paths_config[key] = PROJECT_ROOT / clean_path
        elif isinstance(value, str):
            # For paths that don't start with ./ or ../, treat as relative to project root
            paths_config[key] = PROJECT_ROOT / value if not Path(value).is_absolute() else Path(value)
        else:
            # Non-string values (shouldn't happen in paths.yaml, but handle gracefully)
            paths_config[key] = value
    
    return paths_config


def get_settings_config() -> dict:
    """
    Load settings configuration from config/settings.yaml
    
    Returns:
        dict: Settings configuration dictionary.
    """
    return load_yaml("config/settings.yaml")



