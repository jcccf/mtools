import matplotlib.pyplot as plt
from util import *

def pin(output_name, many_xylists, xlabel=None, ylabel=None, title=None,
  color=None, sliding=None, labels=[], average=True):
  xylists = [to_xylists(xylist, sliding=sliding) for xylist in many_xylists]
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  if len(labels) < len(many_xylists):
    for i in range(len(labels), len(many_xylists)):
      labels.append("Plot %d" % i)

  if color is None:
    color = colors(len(many_xylists))

  ax = plt.subplot(111)

  if average is True:
    all = {}
    for xlist, ylist in xylists:
      for x, y in zip(xlist, ylist):
        all.setdefault(x, []).append(y)
    xys = [(x, (sum(y) - 0.0) / len(y)) for x, y in sorted(all.iteritems())]
    xs, ys = zip(*xys)
    ax.plot(xs, ys, linewidth=2, color='k')

  for i, (xlist, ylist) in enumerate(xylists):
    ax.plot(xlist, ylist, marker='o', markeredgecolor='none', color=color[i], label=labels[i])

  ax.legend(loc=0)

  plt.savefig(parse_output_name(output_name))

def p(output_name, many_xylists, xlabel=None, ylabel=None, title=None,
  color=None, sliding=None, labels=[], average=True):
  xylists = [to_xylists(xylist, sliding=sliding) for xylist in many_xylists]
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  if len(labels) < len(many_xylists):
    for i in range(len(labels), len(many_xylists)):
      labels.append("Plot %d" % i)

  if color is None:
    color = colors(len(many_xylists))

  ax = plt.subplot(111)

  if average is True:
    all = {}
    for xlist, ylist in xylists:
      for x, y in zip(xlist, ylist):
        all.setdefault(x, []).append(y)
    xys = [(x, (sum(y) - 0.0) / len(y)) for x, y in sorted(all.iteritems())]
    xs, ys = zip(*xys)
    ax.plot(xs, ys, linewidth=2, color='k')

  for i, (xlist, ylist) in enumerate(xylists):
    ax.plot(xlist, ylist, marker='o', markeredgecolor='none', color=color[i], label=labels[i])

  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fancybox=True, prop={'size':10})

  plt.savefig(parse_output_name(output_name))


def scales3(name, xylists1, xylists2, xylists3, xlabel='', ylabel='', title='',
  linetypes=['b', 'r', 'g', 'k'], sliding=None, labels=['Plot1', 'Plot2', 'Plot3'],
  xlog=None, ylim=None):
  '''Hackish way to get 3 plots with 3 different scales on the same graph'''
  xylists1 = to_xylists(xylists1, sliding=sliding)
  xylists2 = to_xylists(xylists2, sliding=sliding)
  xylists3 = to_xylists(xylists3, sliding=sliding)

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

  ax1 = plt.figure(figsize=(8.5,6)).add_subplot(111)  # Need to set the figure size
  box = ax1.get_position()
  ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height]) # And the box sizze
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
  ax3 = ax1.twinx()
  ax3.plot(xylists3[0], xylists3[1], linetypes[2], label=labels[2])
  for tl in ax3.get_yticklabels():
    tl.set_color(linetypes[2])
    tl.set_position((1.1,0))  # Move the ticks a little bit
  ax3.set_ylabel(labels[2], color=linetypes[2])
  plt.savefig(parse_output_name(name))