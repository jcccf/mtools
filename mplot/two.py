import matplotlib.pyplot as plt
from util import *

def p(output_name, xylists1, xylists2, xlabel=None, ylabel=None, title=None,
  linetypes=['r', 'b'], xoffset=0, sliding=None, labels=['Plot1', 'Plot2']):
  xylists1 = to_xylists(xylists1, sliding=sliding)
  xylists2 = to_xylists(xylists2, sliding=sliding)
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  xlist1, ylist1 = xylists1
  xlist2, ylist2 = xylists2
  plt.plot(xlist1, ylist1, linetypes[0], label=labels[0])
  plt.plot(xlist2, ylist2, linetypes[1], label=labels[1])

  plt.legend()

  plt.savefig(parse_output_name(output_name))


def scales(name, xylists1, xylists2, xlabel='', ylabel='', title='',
  linetypes=['b', 'r', 'g', 'k'], sliding=None, labels=['Plot1', 'Plot2'],
  xlog=None, ylim=None):
  xylists1 = to_xylists(xylists1, sliding=sliding)
  xylists2 = to_xylists(xylists2, sliding=sliding)

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
  ax1.plot(xylists1[0], xylists1[1], linetypes[0], label=labels[0])
  for tl in ax1.get_yticklabels():
    tl.set_color(linetypes[0])
  ax1.set_ylabel(labels[0], color=linetypes[0])
  ax2 = ax1.twinx()
  ax2.plot(xylists2[0], xylists2[1], linetypes[1], label=labels[1])
  for tl in ax2.get_yticklabels():
    tl.set_color(linetypes[1])
  if len(xlabel) > 0:
    ax1.set_xlabel(xlabel)
  ax2.set_ylabel(labels[1], color=linetypes[1])
  plt.savefig(parse_output_name(name))
