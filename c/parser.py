
class ParseError(Exception): pass

def parse(args, short, long = [], *, prefix = '-'):
	l = len(short)
	nd = [prefix + short[i] for i in range(l) if i < l - 1 and short[i] != ':'
		and short[i + 1] == ':']
	op = [prefix + x for x in short if x != ':' and prefix + x not in nd]
	lnd = [x.replace(':', '') for x in long if x.endswith(':')]
	lop = [x for x in long if not x.endswith(':')]
	r = []

	def some(x):
		for y in x:
			if y:
				return True
		return False

	cntd = lambda x, l: some(x in y for y in l)

	for x in args:
		if not x.startswith(prefix):
			continue
		if not cntd(x, (nd, op, lnd, lop)):
			raise ParseError('erro: comando inválido (%s)'%x)
		if cntd(x, (nd, lnd)):
			try:
				r.append((x, args[args.index(x) + 1]))
			except IndexError:
				raise ParseError('erro: a opção %s precisa de um argumento.'%x)
		else:
			r.append((x, True))
	return r