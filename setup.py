# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ['click', 'requests']
tests_require = ['pytest', 'pytest-cache', 'pytest-cov']


setup(
    name="cox-usage-cli",
    version='0.0.1',
    description="A CLI to get current data usage from Cox ISP",
    long_description="\n\n".join([open("README.rst").read()]),
    license='MIT',
    author="Anthony Fox",
    author_email="anthonyfox1988@gmail.com",
    url="https://cox-usage-cli.readthedocs.org",
    packages=find_packages(),
    install_requires=requires,
    entry_points={'console_scripts': [
        'cox_usage = cox_usage.cli:main']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython']
)
