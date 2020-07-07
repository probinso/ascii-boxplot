#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

config = {
    'name': 'boxplot',
    'author': 'Evan Wheeler',
    'author_email': 'evanmwheeler@gmail.com',
    'url': 'https://github.com/ewheeler/ascii-boxplot',
    'description': 'ascii boxplot',
    'long_description': open('README', 'r').read(),
    'license': 'Apache Software License v2.0',
    'version': '0.0.1',
    'install_requires': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License v2.0",
        "Development Status :: 1 - Planning",
    ],
    'packages': find_packages(),
    'entry_points':{
        'console_scripts':
        [
            'boxplot = boxplot.main:main'
        ]
    }
}

if __name__ == '__main__':
    setup(**config)
