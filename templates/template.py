#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" template.py

Usage: python -m ...
___
--help | -h Display documentation

Module title

Description 

This file can also be imported as a module and contains the following functions:
    * foo: returns str.

TO DO:  
    *
"""

from __future__ import absolute_import, division, print_function
import argparse

__author__ = "Fernando Pozo"
__copyright__ = "Copyright 2020"
__license__ = "GNU General Public License"
__version__ = "1.0.1"
__maintainer__ = "Fernando Pozo"
__email__ = "fpozoc@cnio.es"
__status__ = "Production"

### Python and 3rd party libraries 
import os, sys
import warnings

### Custom packages 
# sys.path.append('./')
# from src import utils


# Global variables
warnings.filterwarnings('ignore')


# Class declarations


# Function declarations
def foo(arg1:list, arg2:str = 'a', arg3:int = 2) -> str:
    """[summary]
    
    Arguments:
        arg1 {list} -- [description]
    
    Keyword Arguments:
        arg2 {str} -- [description] (default: {'a'})
        arg3 {int} -- [description] (default: {2})
    
    Returns:
        str -- [description]
    """    
    foo = 'abc'
    return foo.capitalize()


# Main body
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

if __name__ == '__main__':
    main()