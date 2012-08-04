import matplotlib.pyplot as plt
from util import *


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
    ax.plot(xlist, ylist, color=color[i], label=labels[i])

  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

  plt.savefig(parse_output_name(output_name))
