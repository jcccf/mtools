

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


if __name__ == '__main__':
  print cumulative({1: 1, 2: 3})
