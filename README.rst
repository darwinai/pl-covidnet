pl-covidnet
===========

.. image:: https://badge.fury.io/py/covidnet.svg
    :target: https://badge.fury.io/py/covidnet

.. image:: https://travis-ci.org/FNNDSC/covidnet.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/covidnet

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-covidnet

.. contents:: Table of Contents


Abstract
--------

Plugin to ChRIS for covidnet functionalities


Synopsis
--------

.. code::

    python covidnet.py
        [-v <level>] [--verbosity <level>]
        [--version]
        [--man]
        [--meta]
        <inputDir>
        <outputDir>
        [--imagefile] <imagefile>

Description
-----------

``covidnet.py`` is a ChRIS-based application that integrates COVID-Net to ChRIS

Agruments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.

    [--meta]
    If specified, print plugin meta data.

    [--imagefile]
    The name of the input image in the input directory, this is required


Models
------

The COVIDNet-CXR4-B, COVIDNet-SEV-GEO, and COVIDNet-SEV-OPC models are downloaded from
https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md



Local Build
-----------

.. code:: bash

    DOCKER_BUILDKIT=1 docker build -t local/pl-covidnet .

Run
----

.. code:: bash

    docker run --rm -v $PWD/in:/incoming -v $PWD/out:/outgoing    \
        darwinai/covidnet-pl covidnet                             \
                --imagefile ex-covid.jpeg /incoming /outgoing
