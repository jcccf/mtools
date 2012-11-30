import matplotlib.pyplot as plt
from util import *


def p(output_name, xylists, xlabel=None, ylabel=None, title=None,
  linetype='k', xoffset=0, sliding=None, xlim=None, ylim=None):
  xylists = to_xylists(xylists, sliding=sliding)
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  xlist, ylist = xylists
  plt.plot(xlist, ylist, linetype)

  if xlim is not None:
    plt.xlim(*xlim)
  if ylim is not None:
    plt.ylim(*ylim)

  plt.savefig(parse_output_name(output_name))


def loglog(output_name, xylists, xlabel=None, ylabel=None, title=None,
  linetype='k', xoffset=0, sliding=None):
  xylists = to_xylists(xylists, sliding=sliding)
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)

  xlist, ylist = xylists
  plt.loglog(xlist, ylist, linetype)
  plt.savefig(parse_output_name(output_name))


def hist(output_name, value_list, bins=100, xlabel=None, ylabel=None,
  title=None, linetype='k', normed=False):
  plt.clf()
  if xlabel is not None:
    plt.xlabel(xlabel)
  if ylabel is not None:
    plt.ylabel(ylabel)
  if title is not None:
    plt.title(title)
  plt.hist(value_list, bins=bins, histtype='stepfilled', color='b', alpha=0.5, normed=normed)
  plt.savefig(parse_output_name(output_name))

