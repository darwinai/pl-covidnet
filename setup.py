from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             =   'covidnet',
    version          =   '0.2.0',
    description      =   'Plugin to ChRIS for covidnet functionalities',
    long_description =   readme,
    author           =   'Jeffer Peng',
    author_email     =   'jeffer.peng@darwinai.ca',
    url              =   'https://github.com/FNNDSC/pl-covidnet#pl-covidnet',
    packages         =   ['covidnet'],
    license          =   'AGPL',
    zip_safe         =   False,
    python_requires  =   '>=3.6',
    entry_points     = {
        'console_scripts': [
            'covidnet = covidnet.__main__:main'
            ]
        }
)
