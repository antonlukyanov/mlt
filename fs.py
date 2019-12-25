"""
Common file system utilities.
"""

import os


def makedirs(*args, mode=0o700):
    for path in args:
        if isinstance(path, list) or isinstance(path, tuple):
            for dp in path:
                os.makedirs(dp, mode, True)
        else:
            os.makedirs(path, mode, True)
