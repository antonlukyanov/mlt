"""
Common file system utilities.
"""

import os


def makedirs(*args, mode=0o755, exist_ok=True):
    for path in args:
        if isinstance(path, list) or isinstance(path, tuple):
            for dp in path:
                os.makedirs(dp, mode, exist_ok)
        else:
            os.makedirs(path, mode, exist_ok)
