# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
from locust_runner.version import __version__

try:
    with open(path.join(path.dirname(__file__), 'README.md')) as f:
        long_description = f.read()
except Exception:
    # XXX: Intentional pokemon catch to prevent this read from breaking setup.py
    long_description = None

setup(
    name='locust-runner',
    version=__version__,
    author='Peter Han',
    author_email='git@peterhan.me',
    description='Runner for Locust.io load testing tool',
    long_description=long_description,
    url='https://github.com/hanpeter/locust-runner',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # TODO: Test and support more versions of Python
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[
        'locustio'
    ],
    # TODO: Test and support more versions of Python
    python_requires='==2.7.*',
    # Make sure the license file is packaged up too
    include_package_data=True,
)
