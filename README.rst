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

Description
-----------

``covidnet.py`` is a ChRIS-based application that...

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


.. code:: bash

    python covidnet/covidnet.py covidnet/inputimage/ex-covid.jpeg  output

covidnet/inputimage/ex-covid.jpeg is the input image directory
output is the directory you wish the output files to be in

Here are 3 optional parameters to specify the location of AI model and the default value is on the right  

--weightspath : "../COVID-Net/models/COVIDNet-CXR-Large"  

--metaname      : "model.meta"  

--ckptname      : "model-8485"  





Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing                             \
            fnndsc/pl-covidnet covidnet.py                        \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-covidnet covidnet.py                        \
            --man                                                       \
            /incoming /outgoing

Examples
--------





