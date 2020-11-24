#!/usr/bin/env python3

import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
        requirements = f.read().split('\n')
except:
    requirements = []

setup(
    name='mlt',
    version='0.1a0',
    description='Machine learning tools.',
    url='http://github.com/antonlukyanov/mlt',
    author='Anton Lukyanov',
    author_email='anton.lukyanov@gmail.com',
    license='MIT',
    python_requires='>=3.7.0',
    packages=['mlt'],
    package_dir={'mlt': '.'},
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements
)
