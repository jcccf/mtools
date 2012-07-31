import matplotlib
import re


def colors(length):
  """Return a list of rainbow colors"""
  colors = []
  c = matplotlib.cm.get_cmap('gist_rainbow')
  for i in range(length):
    colors.append(c(1. * i / length))
  return colors


def parse_output_name(output_name):
  """Parse the output name of a file and append PNG by default"""
  if re.search("\.[a-zA-Z0-9]{2,3}$", output_name):
    return output_name
  else:
    return output_name + ".png"


def sliding_window(value_list, window_size=10):
  out_values = []
  cumulative = sum(value_list[:window_size]) - 0.0
  out_values = [cumulative / window_size]
  for i in range(window_size, len(value_list)):
    cumulative += value_list[i]
    cumulative -= value_list[i - window_size]
    out_values.append(cumulative / window_size)
  return out_values


def to_xylists(group, offset=0):
  """Convert a list of numbers into a format suitable for the plot functions
  Offset only applies if a plain numeric list is passed in.
  Formats accepted:
    Dictionaries of x -> y values
    List of (x,y) tuples
    List of ints or floats
    List of x values and y values (left unchanged)
  """
  if isinstance(group, dict):
    xys = sorted(group.iteritems())
    return zip(*xys)
  elif isinstance(group, list):
    if isinstance(group[0], tuple) and len(group[0]) == 2:
      return zip(*group)
    elif isinstance(group[0], int) or isinstance(group[0], float):
      return [range(offset, len(group) + offset), group]
    elif len(group) == 2:
      if reduce(lambda x, y: x and isinstance(y, list), group, True):
        if len(group[0]) == len(group[1]):
          try:
            float(group[0][0]) + float(group[1][0])
            return group
          except:
            pass
  raise Exception("Cannot parse this into xylists format!")

if __name__ == '__main__':
  print sliding_window([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
  print to_xylists([[1, 3], [2, 4]])
