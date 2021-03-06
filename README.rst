pl-covidnet
================================

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

    python covidnet.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
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


Setup
----

Download Machine learning model from: 
https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md

Make sure to download: COVIDNet-CXR4-B, COVIDNet-SEV-GEO, COVIDNet-SEV-OPC

Then put the downloaded folders in covidnet/models

The folder structure should be:

pl-covidnet/covidnet/models/COVIDNet-CXR4-B


Run
----

.. code:: bash

    cd covidnet
    python covidnet.py inputimage output --imagefile ex-covid.jpeg

inputimage is the input directory

output is the directory you wish the output files to be in

--imagefile ex-covid.jpeg the name of the input image in the input directory





Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "in" directory to ``/incoming`` and an "out" directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Start from the pl-covidnet directory

build the container using 

.. code:: bash

    docker build -t local/pl-covidnet .
    

Now, run the container:

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                       \
            pl-covidnet covidnet.py --imagefile ex-covid.jpeg /incoming /outgoing                       \


This is volume mapping the in and out directory under pl-covidnet. Feel free to create different directories. 

Make sure the input directory contain an image that fits the --imagefile argument, and make sure the incoming and outgoing 
directories used as input are the ones being volume mapped.


You can create different directories using the following command. chmod 777 out just makes out directory writable

.. code:: bash
    
    mkdir in out && chmod 777 out

Examples
--------

docker build -t local/pl-covidnet .

docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing local/pl-covidnet covidnet.py --imagefile ex-covid.jpg /incoming /outgoing
