"""
Common file system utilities.
"""

import os


def makedirs(dirpaths):
    for dirpath in dirpaths:
        os.makedirs(dirpath, 0o700, True)
