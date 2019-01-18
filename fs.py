"""
Common file system utilities.
"""

import os


def makedirs(dirpath):
    os.makedirs(dirpath, 0o700, True)
