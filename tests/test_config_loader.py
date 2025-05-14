import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from config_loader import *

paths = get_paths_config()
print(paths)

print('##' * 40)

def test_settings_config_loading():
    settings = get_settings_config()
    print(settings)

test_settings_config_loading()