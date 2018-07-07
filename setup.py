#!/usr/bin/env python

from setuptools import setup, find_packages
from pandna import __version__


setup(
    name='pandna',
    version=__version__,
    description='Pandas-based Data Handlers for DNA-sequencing',
    packages=find_packages(),
    author='Daichi Narushima',
    author_email='dnarsil+github@gmail.com',
    url='https://github.com/dceoy/fract',
    include_package_data=True,
    install_requires=[
        'pandas'
    ],
    entry_points={
        'console_scripts': ['pandna=pandna.main:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    long_description="""\
pandna
--------

Pandas-based Data Handlers for DNA-sequencing
"""
)
