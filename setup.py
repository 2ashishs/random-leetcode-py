# Copyright (c) 2024 Ashish Sadhwani
# This software is released under the Mozilla Public License Version 2.0.
# See the LICENSE file for details.

from setuptools import setup, find_packages

setup(
    name='random_leetcode',
    version='0.1',
    packages=find_packages(),
    package_data={
        'random_leetcode': ['lc_master.txt'],
    },
    entry_points={
        'console_scripts': [
            'random_leetcode=random_leetcode.random_leetcode:main',
        ],
    },
)
