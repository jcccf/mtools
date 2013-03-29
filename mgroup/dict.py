

def cumulative(dicty):
  """Return the cumulative sum of values in a dictionary,
  where the sum is ordered by key"""
  sorts = sorted(dicty.iteritems(), key=lambda x: x[0])
  sum = 0
  dict_sort = {}
  for k, v in sorts:
    sum += v
    dict_sort[k] = sum
  return dict_sort


def percentage(dicty):
  maxv = max(dicty.itervalues())
  return dict([(k, (v - 0.0) / maxv) for k, v in dicty.iteritems()])


def percentage_sum(dicty):
  total = sum(dicty.itervalues())
  return dict([(k, (v - 0.0) / total) for k, v in dicty.iteritems()])


class DictDictList:
  '''Useful for generating feature vectors for objects where each object has an incomplete list of keyed features'''
  def __init__(self):
    self.d = {}
    self.counter = 0
    self.key_to_index = {}

  def add(self, obj, key, val):
    if key not in self.key_to_index:
      self.key_to_index[key] = self.counter
      self.counter += 1
    if obj not in self.d:
      self.d[obj] = {}
    self.d[obj][key] = val - 0.0

  def to_dictlist(self):
    newd = {}
    for k, vdict in self.d.iteritems():
      newl = [0.0] * self.counter
      for k2, v2 in vdict.iteritems():
        newl[self.key_to_index[k2]] = v2
      newd[k] = newl
    return newd

if __name__ == '__main__':
  print cumulative({1: 1, 2: 3})
  ddl = DictDictList()
  ddl.add("j", 4, 44)
  ddl.add("j", 5, 3)
  ddl.add("k", 6, 4)
  ddl.add("k", 4, 45)
  print ddl.to_dictlist()