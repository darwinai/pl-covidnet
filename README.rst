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


Run
----

Download Machine learning model from: 
https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md

By default, the app uses COVIDNet-CXR3-B.

Then put the downloaded folder in covidnet/models

.. code:: bash

    cd covidnet
    python covidnet.py inputimage output --imagefile ex-covid.jpeg

inputimage is the input directory

output is the directory you wish the output files to be in

--imagefile ex-covid.jpeg the name of the input image in the input directory





Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/in:/inputimage -v $(pwd)/out:/output                       \
            pl-covidnet covidnet.py --imagefile ex-covid.jpeg /inputimage /output                       \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-covidnet covidnet.py                        \
            --man                                                       \
            /incoming /outgoing

sudo docker run -v $(pwd)/in:/inputimage -v $(pwd)/out:/output pl-covidnet covidnet.py --imagefile ex-covid.jpeg /inputimage /output

Examples
--------





