mtools
======

A collection of Python convenience functions

Usage
-----
    from mtools import *
    depth = mgraph.directed.depth(my_networkx_graph)

mplot, mlang and mdb must be manually imported

    from random import random
    from mtools import mplot
    mplot.one.p("test.eps", [random() for i in range(0, 100)], sliding=10)

Modules
-------
* mdb - MySQL convenience functions (depends on python-mysqldb)
* mgraph - Graph functions to use with networkx (depends on networkx)
* mgroup - List and dictionary convenience functions
* mlang - NLP convenience functions (depends on nltk)
* mplot - Chart plotting convenience functions (depends on matplotlib)

MDb
---
Supports ActiveRecord-style chained queries

    from mtools import mdb
    db = mdb.mysql.MMySQL('my_database', host='my_host', username='my_username', password='my_password')
    
    # Get a single row
    print db.users_table.select('name').where(id=10).first()
    
    # Get multiple rows
    for user in db.users_table.select('id', 'location').where(location='SF').order_by('age DESC').limit(100):
      print user
    
    # Get everything
    for user in db.users_table:
      print user

    # Count the number of distinct ids in a table
    print db.users_table.count('DISTINCT id').where(location='NY').first()

    # Chain whichever way you want
    db.users_table.limit(2).select('id').order_by('name', 'id DESC').where(location='SF').select('name', 'location')

Regular queries are also supported

    # Use db.q if you want to get everything at once
    users = db.q('SELECT * FROM users WHERE location = %s AND age > %s', (some_location, some_age))

    # Use db.i if you want an iterator instead
    for user in db.i('SELECT * FROM users'):
      print user

Remember to commit your changes if you modify the database!

    db.commit()

MPlot
-----
Plot two lines with different scales

    from mtools import mplot
    xylist1 = [0, 1, 2]
    xylist2 = [100, 200, 300]
    mplot.two.scales('my_output_file.eps', xylist1, xylist2, xlabel='X Axis', ylabel='Y Axis', labels['First Plot', 'Second Plot'])

MPlot understands several input formats

    xylist = [0, 1, 2, 3]  # MPlot assumes these are y values and will add indices for the x values
    xylist = {1: 500, 2: 600, 3: 900}
    xylist = [(1, 500), (2, 600), (3, 900)]
    xylist = [[1, 2, 3], [500, 600, 900]]

MPlot can also do sliding window averages

    mplot.one.loglog('my_output_file.png', xylist, sliding=10)
