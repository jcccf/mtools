def diffs(listy):
  """Return the differences between elements in a list"""
  diffitems = []
  previtem = listy[0]
  for l in listy:
    diffitems.append(l - previtem)
    previtem = l
  return diffitems[1:]
