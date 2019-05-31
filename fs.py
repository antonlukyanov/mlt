"""
Common file system utilities.
"""

import os


def makedirs(dirpath, mode=0o700):
    os.makedirs(dirpath, mode, True)
