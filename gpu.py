"""
Common GPU utilities.
"""

import os
import tensorflow as tf


def allow_growth_config():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return config


def allow_growth_session():
    return tf.Session(config=allow_growth_config())


def select_gpus(devices):
    tp = type(devices)
    if tp == range:
        devices = list(devices)
    elif tp is not None and tp not in (list, tuple):
        devices = [devices]
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    if devices:
        devices = ','.join(str(device) for device in devices)
    else:
        devices = ''
    os.environ['CUDA_VISIBLE_DEVICES'] = devices
