#!/usr/bin/python3


def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return(res)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
