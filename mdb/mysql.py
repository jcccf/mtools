import MySQLdb


class MMySQL(object):
  def __init__(self, database, host='localhost', username='root', password=''):
    self.conn = MySQLdb.connect(host, username, password, database)
    self.conn.text_factory = str
    self.c = self.conn.cursor()

  class MDbTable():
    '''Helper class for ActiveRecord-style database access'''
    def __init__(self, mdb, table_name):
      self.mdb = mdb
      self.table_name = table_name
      self.limit = None  # Or a number
      self.order = None  # Or an array of orderings
      self.selects = None  # Or an array of things to select
      self.wheres = None  # Or an array of wheres

    def __iter__(self):
      query, stuple = self.__build_query()
      self.result = self.mdb.i(query, stuple)
      return self

    def next(self):
      row = self.result.fetchone()
      if row is None:
        self.result.close()
        raise StopIteration
      return row

    def query_plan(self):
      return self.__build_query()

    def all(self):
      self.__iter__()
      res = self.result.fetchall()
      self.result.close()
      return res

    def first(self):
      self.__iter__()
      return self.result.fetchone()

    def __build_query(self):
      query = ""

      # Build select part
      if self.selects is not None:
        query = "SELECT "
        for selected in self.selects:
          query += selected + ", "
        query = query[:-2] + " FROM " + self.table_name
      else:
        query = "SELECT * FROM " + self.table_name

      # Build where
      svals, stuple = self.__process_where()
      query += svals

      # Build order limit
      query += self.__process_order_limit()

      return (query, stuple)

    def __process_where(self):
      if self.wheres is not None:
        svals, stuple = ' WHERE ', ()
        for k, v in self.wheres.items():
          if v is not None:
            if isinstance(v, tuple) and len(v) == 0:
              svals += k + " IS NOT NULL AND "
            else:
              svals += k + '=%s AND '
              stuple += (v,)
          else:
            svals += k + " IS NULL AND "
        svals = svals[:-5]
        return (svals, stuple)
      else:
        return ("", None)

    def __process_order_limit(self):
      addition = ""
      if self.order is not None:
        addition += " ORDER BY "
        for ordering in self.order:
          addition += ordering + ", "
        addition = addition[:-2]
      if self.limit is not None:
        addition += " LIMIT " + self.limit
      return addition

    def select(self, *selects):
      if self.selects is None:
        self.selects = []
      self.selects += selects
      return self

    def count(self, what=None):
      if self.selects is None:
        self.selects = []
      if what is not None:
        self.selects += ['COUNT(' + what + ') AS numfound']
      else:
        self.selects += ['COUNT(*) AS numfound']
      return self

    def where(self, **vals):
      if self.wheres is None:
        self.wheres = {}
      for k, v in vals.items():
        self.wheres[k] = v
      return self

    def order_by(self, *orderings):
      if self.order is None:
        self.order = []
      self.order += orderings
      return self

    def limit(self, limit):
      self.limit = limit
      return self

    def insert(self, **vals):
      snames, svals, stuple = '(', 'VALUES(', ()
      for k, v in vals.items():
        if v is not None:
          snames += k + ', '
          svals += '%s, '
          stuple += (v,)
      snames = snames[:-2] + ')'
      svals = svals[:-2] + ')'
      return self.mdb.q('INSERT INTO ' + self.table_name + snames + ' ' + svals, stuple)

  def __getattr__(self, name):
    if len(self.q('SHOW TABLES LIKE %s', name)) == 0:
      raise AttributeError(name)
    return MMySQL.MDbTable(self, name)

  def q(self, query, tuples=None):
    c = self.conn.cursor()
    '''Make a database query and return all rows'''
    try:
      if tuples:
        c.execute(query, tuples)
      else:
        c.execute(query)
      res = c.fetchall()
      c.close()
      return res
    except MySQLdb.IntegrityError as err:
      print "Integrity Error | %s" % err
      return -2

  def i(self, query, tuples=None):
    c = self.conn.cursor()
    '''Make a database query and return the cursor (useful for iterating)'''
    if tuples:
      c.execute(query, tuples)
    else:
      c.execute(query)
    return c

  def commit(self):
    self.conn.commit()

  def rollback(self):
    self.conn.rollback()

  def close(self):
    self.c.close()
