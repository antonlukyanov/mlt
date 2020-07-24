"""
Miscellaneous utilities.
"""
import json
from functools import partial
from time import time
from datetime import datetime, timedelta

import yaml


class Timer:
    def __init__(self, *, name=None, log=None):
        self._started = None
        self._stopped = None
        self._name = name if name else 'timer'
        self._log = log if log else print
        self._log = partial(self._log, '[%s]:' % self._name)

    def start(self):
        self._started = time()
        self._stopped = None
        self._log('started at', datetime.fromtimestamp(self._started))

    def stop(self):
        self._stopped = time()
        self._log('finished at %s, time elapsed %s' % (
                datetime.fromtimestamp(self._stopped),
                timedelta(seconds=self._stopped - self._started)
            )
        )

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def read_json(filepath):
    with open(filepath) as f:
        return json.load(f)


def read_yaml(filepath):
    with open(filepath) as f:
        return yaml.load(f, Loader=yaml.SafeLoader)