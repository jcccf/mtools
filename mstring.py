import re
import unicodedata


def slugify(value):
  """Slugify a string (i.e. make it usable in either a URL or in a filename, from Django)"""
  value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
  value = re.sub('[^\w\s-]', '', value).strip().lower()
  return re.sub('[-\s]+', '-', value)
