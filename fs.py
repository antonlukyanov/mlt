"""
Common file system utilities.
"""

import os


def makedirs(dirpaths, mode=0o700):
    if isinstance(dirpaths, str):
        dirpaths = [dirpaths]
    for dp in dirpaths:
        os.makedirs(dp, mode, True)
