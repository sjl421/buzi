#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'buzi is a simple microservice architecture'

setup(
    name='buzi',
    version=VERSION,
    description=DESCRIPTION,
    author='ybrs',
    license='MIT',
    url="http://github.com/ybrs/buzi",
    author_email='aybars.badur@gmail.com',
    packages=['buzi'],
    install_requires=['redis'],
    entry_points={
        'console_scripts': [
            'buzi = buzi.main:main',
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)