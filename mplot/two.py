import matplotlib.pyplot as plt
from util import *


def scales(name, two_xylists, xlabel='', ylabel='', title='',
  linetypes=['b', 'r', 'g', 'k'], labels=[], xlog=None, ylim=None):
  plt.clf()
  if len(xlabel) > 0:
    plt.xlabel(xlabel)
  if len(ylabel) > 0:
    plt.ylabel(ylabel)
  if len(title) > 0:
    plt.title(title)
  if xlog:
    plt.xscale('log', basex=xlog)
  if ylim:
    plt.ylim(ylim)

  ax1 = plt.figure().add_subplot(111)
  xylist1, xylist2 = two_xylists
  ax1.plot(xylist1[0], xylist1[1], linetypes[0], label=labels[0])
  for tl in ax1.get_yticklabels():
    tl.set_color(linetypes[0])
  ax1.set_ylabel(labels[0], color=linetypes[0])
  ax2 = ax1.twinx()
  ax2.plot(xylist2[0], xylist2[1], linetypes[1], label=labels[1])
  for tl in ax2.get_yticklabels():
    tl.set_color(linetypes[1])
  ax2.set_ylabel(labels[1], color=linetypes[1])
  plt.savefig(parse_output_name(name))
