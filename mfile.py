import os
import os.path


def make_dir(dir):
  '''Create a directory (recursively) if it doesn't exist'''
  if not os.path.exists(dir):
    os.makedirs(dir)
