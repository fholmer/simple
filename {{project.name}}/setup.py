# -*- coding: utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html


To build sdist:
    python3 setup.py sdist

To build wheel:
    install wheel:
      python3 -m pip install wheel
    build wheel:
      python3 setup.py bdist_wheel

Update requirements:
    python3 -m pip freeze -r requirements.txt > requirements.txt

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from {{ project.package }} import __version__ as app_version

here = path.abspath(path.dirname(__file__))

NAME = "{{ project.name }}"
MAIN_PACKAGE = "{{ project.package }}"

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

def get_list_from_file(*fullfilepath):
    return open(path.join(*fullfilepath), "r").read().splitlines()

setup(

    # default setuptools options:
    name=NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=app_version,

    description="{{ project.short_description }}",
    long_description=long_description,

    # The project's main homepage.
    url='',

    # Author details
    author="{{ project.author_name }}",
    author_email='{{ project.author_email }}',

    # Choose your license
    license='Proprietary',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    
    packages=find_packages(include=['{{ project.package }}*']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    
    install_requires=get_list_from_file(here, "requirements.txt"),

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},
    
    #package_dir={NAME: NAME},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],
    
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
)
