#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='houdini',
    version='0.1.0',
    author='Mihir Singh (@citruspi)',
    author_email='pypi.service@mihirsingh.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'paramiko',
    ]
)
