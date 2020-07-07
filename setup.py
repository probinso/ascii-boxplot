#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

config = {
    'name': 'boxplot',
    'author': 'Evan Wheeler',
    'author_email': 'evanmwheeler@gmail.com',
    'url': 'https://github.com/ewheeler/ascii-boxplot',
    'license'='Apache License 2.0',
    'description': 'ascii boxplot',
    'long_description': open('README', 'r').read(),
    'license': 'MIT',
    'version': '0.0.1',
    'install_requires': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
    ],
    'packages': find_packages(),
}

if __name__ == '__main__':
    setup(**config)
