def diffs(listy):
  """Return the differences between elements in a list"""
  diffitems = []
  previtem = listy[0]
  for l in listy:
    diffitems.append(l - previtem)
    previtem = l
  return diffitems[1:]


def diffs_first(listy):
  """Return the differences between the first and rest of elements in the list"""
  if len(listy) > 0:
    origin = listy[0]
  else:
    origin = 0
  return [l - origin for l in listy]
