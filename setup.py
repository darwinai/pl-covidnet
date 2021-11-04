from os import path

from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name='covidnet',
    # for best practices make this version the same as the VERSION class variable
    # defined in your ChrisApp-derived Python class
    version='0.1',
    description='Plugin to ChRIS for covidnet functionalities',
    long_description=readme,
    author='Jeffer Peng',
    author_email='jeffer.peng@darwinai.ca',
    url='https://github.com/darwinai/pl-covidnet',
    packages=['covidnet'],
    install_requires=['chrisapp', 'pudb'],
    test_suite='nose.collector',
    tests_require=['nose'],
    license='AGPL',
    python_requires='>=3.6',
    entry_points={'console_scripts': ['covidnet = covidnet.__main__:main']},
    zip_safe=False)
