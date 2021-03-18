"""
Miscellaneous utilities.
"""
import json
from functools import partial
from time import time
from datetime import datetime, timedelta

import yaml


class Timer:
    def __init__(self, *, name=None, log=print):
        self._started = None
        self._stopped = None
        self._name = name if name else 'timer'
        self._log = partial(log, '[%s]:' % self._name) if log is not None else log

    def start(self):
        self._started = time()
        self._stopped = None
        self.log('started at', datetime.fromtimestamp(self._started))
        return self._started

    def stop(self):
        self._stopped = time()
        finished = datetime.fromtimestamp(self._stopped)
        elapsed_sec = self._stopped - self._started
        elapsed = timedelta(elapsed_sec)
        self.log(f'finished at {finished}, time elapsed {elapsed}')
        return self._stopped, elapsed_sec

    def log(self, *args, **kwargs):
        if self._log is not None:
            self._log(*args, **kwargs)

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
        return yaml.load(f, Loader=yaml.FullLoader)
