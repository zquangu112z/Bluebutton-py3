"""
BlueButton.py
"""

import setuptools

setuptools.setup(
    name='bluebutton',
    version='0.4.1.post0',
    packages=setuptools.find_packages(),
    description='The Blue Button Python Library',
    author='Taeber Rapczak',
    author_email='taeber@ufl.edu',
    url='https://github.com/ctsit/bluebutton.py',
    license='Apache License, Version 2.0',
    keywords=[
        "bb",
        "blue button",
        "ccda",
        "c-cda",
        "ehr",
        "emr",
        "health",
        "healthcare",
        "medical",
        "phr",
        "record"
    ],
    setup_requires=[
        "nose >= 1.0",
        "nosexcover >= 1.0.10",
    ],
)
