import matplotlib.pyplot as plt
from util import *


def p(output_name, xylists, xlabel=None, ylabel=None, title=None,
  linetype='k', xoffset=0, sliding=None):
  if sliding is not None:
    xylists = sliding_window(xylists)
    xylists = to_xylists(xylists, offset=sliding / 2)
  else:
    xylists = to_xylists(xylists)
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  xlist, ylist = xylists
  plt.plot(xlist, ylist, linetype)
  plt.savefig(parse_output_name(output_name))


def hist(output_name, value_list, bins=100, xlabel=None, ylabel=None,
  title=None, linetype='k'):
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  plt.hist(value_list, bins=bins)
