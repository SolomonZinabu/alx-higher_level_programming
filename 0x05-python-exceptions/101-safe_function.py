#!/usr/bin/python3
<<<<<<< HEAD
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
=======
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        return None
