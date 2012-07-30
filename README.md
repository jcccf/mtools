mtools
======

A collection of Python convenience functions

Usage
-----
    from * import mtools
    depth = mgraph.directed.depth(my_networkx_graph)

mplot must be manually imported as mplot significantly slows loading times

    from random import random
    from mtools import mplot
    mplot.one.p("test.eps", [random() for i in range(0, 100)], sliding=10)

Modules
-------
* mgraph - Graph functions to use with networkx
* mgroup - List and dictionary convenience functions
* mplot - Matplotlib convenience functions
