.. highlight:: shell

Build from source
=================

{{project.name}} package
------------------------

Debian
++++++

Setup virtual environment:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

Build sdist and wheel:

.. code-block:: console

    $ python setup.py sdist
    $ python setup.py bdist_wheel


Windows
+++++++

Setup an virtual environment:

.. code-block:: doscon

    > py -3 -m venv venv
    > venv\Scripts\activate

Build sdist and wheel

.. code-block:: doscon

    > python setup.py sdist
    > python setup.py bdist_wheel

Docs
----

Debian
++++++

Install requirements

.. code-block:: console

    # requirements for pdf
    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

    # requirements for pdf multi language
    $ sudo apt-get install texlive-lang-european texlive-lang-english

Setup virtual environment:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

Build docs:

.. code-block:: console

    $ cd docs
    $ make html
    $ make latexpdf
