from __future__ import print_function, absolute_import, division
from setuptools import setup


version = '0.4.1'
long_description = open('README.md').read()

packages = ['bluebutton']

setup(
    name='BlueButton.py3',
    version=version,
    author='zquangu112z',
    package_dir={'bluebutton': 'bluebutton'},
    packages=packages,
    url='https://github.com/zquangu112z/bluebutton.py3',
    description='A package for parsing CCD data',
    license='Apache License, Version 2.0',
    long_description=long_description,
    zip_safe=False,
    platforms='any',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
