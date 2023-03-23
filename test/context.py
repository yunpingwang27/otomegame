import os
import sys

def abspath(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

_path = abspath('..')
if _path not in sys.path:
    sys.path.insert(0, _path)
