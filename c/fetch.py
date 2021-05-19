from re import match

def getModule(n):
	try:
		return __import__(n)
	except ImportError as e:
		raise ImportError('Módulo não encontrado: %s.'%n) from e

def fetch(n, find = None):
	d = getModule(n).__dict__
	return [(x, d[x]) for x in d if match(find, x)] if find else [(x, d[x]) for x in d]