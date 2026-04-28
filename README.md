
# Table of Contents

1.  [What?](#orgb69adda)
2.  [Installing](#orgd46109b)
    1.  [Create a python environment](#org513266c)
    2.  [Install the python package](#org0414010)
    3.  [Access to the path of the package](#org9eb5b85)
3.  [Check Test](#orge480c64)
    1.  [In the path:](#org49f38f4)
    2.  [Execute all tests:](#orga382a4f)
    3.  [Execute one file:](#org38d200b)


<a id="orgb69adda"></a>

# What?

That's a package to run tests about scikit library of Python.
For example, create models, vectorizer


<a id="orgd46109b"></a>

# Installing


<a id="org513266c"></a>

## Create a python environment

    $ mkdir venv3.14
    $ python3 -m venv venv3.14
    $ cd venv3.14
    $ source bin/activate  


<a id="org0414010"></a>

## Install the python package

    $ pip3 install damescikit


<a id="org9eb5b85"></a>

## Access to the path of the package

    $ cd lib/python3.14/site-packages/damescikit


<a id="orge480c64"></a>

# Check Test


<a id="org49f38f4"></a>

## In the path:

    $ cd damescikit


<a id="orga382a4f"></a>

## Execute all tests:

    $ pytest tests


<a id="org38d200b"></a>

## Execute one file:

    $ pytest tests/test_models.py

