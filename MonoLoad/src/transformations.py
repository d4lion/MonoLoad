from os import getcwd, path
from typing import Optional


def transform_config_to_dict(config_path: Optional[str] = None) -> dict:
    """
    Transform a configuration file into a dictionary.
    
    Args:
        config_path: Path to the configuration file. Defaults to src/page.config
        
    Returns:
        Dictionary with configuration keys and values
    """
    if config_path is None:
        # Get the directory of this file, then navigate to page.config
        base_dir = path.dirname(path.abspath(__file__))
        config_path = path.join(base_dir, "page.config")

    config_dict = {}
    
    with open(config_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
                
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            
            # Parse value type without using eval()
            if value.isdigit():
                config_dict[key] = int(value)
            elif value.lower() in ("true", "false"):
                config_dict[key] = value.lower() == "true"
            else:
                config_dict[key] = value

    return config_dict
