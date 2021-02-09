pl-covidnet
================================

.. image:: https://img.shields.io/github/license/FNNDSC/pl-covidnet
    :target: https://github.com/FNNDSC/pl-covidnet/blob/master/LICENSE
    :alt: License AGPL-3.0

.. image:: https://img.shields.io/docker/v/fnndsc/pl-covidnet?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-covidnet


.. contents:: Table of Contents


Abstract
--------

A ChRIS plugin to do predictive analysis on chest x-ray for COVID-19 diagnostics.


Synopsis
--------

.. code::

    python covidnet.py                                              \
        [--imagefile <imagefile>]                                   \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>                                                  \
        <outputDir>                                                 


Description
-----------

``covidnet.py`` is a ChRIS-based application that integrates the COVID-Net inference engine in a ChRIS plugin.

Agruments
---------

.. code::

    [--imagefile <imageFile>]
    The name of the input image in the input directory. 

    If not specified, the first ``png`` image file will be analyzed.
    
    If no ``png`` images are found, the first ``jpg/jpeg`` image will
    be analyzed. 

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.


Local Build
-----------

.. code:: bash

    DOCKER_BUILDKIT=1 docker build -t local/pl-covidnet .

Run
----

.. code:: bash

    docker run --rm -v $PWD/in:/incoming -v $PWD/out:/outgoing    \
        fnndsc/pl-covidnet:0.2.0 covidnet                         \
               --imagefile ex-covid.jpeg /incoming /outgoing


Links
-----

Models are rehosted for the sake of convenience, opposed to using Google Drive
as a CDN. They were originally sourced from
https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md

A custom UI was developed for a workflow which this plugin is a part of.
https://github.com/FNNDSC/covidnet_ui


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co/plugin/28
