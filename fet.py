#!/usr/bin/python
from c.parser import parse, ParseError
from c.fetch import fetch
from sys import argv

u = '''Veja o conteúdo no namespace de módulos python.
Uso:
 %s [opções]
opções:
 -m, --module  Aponta para o módulo.
 -f, --find    Expressão regular para filtrar resultado
'''.rstrip()%argv[0]

try:
	a = parse(argv[1:], 'm:f:h', ['--module:', '--find:', '--help'])
except ParseError as e:
	print(e)
	exit(1)

m = None
f = None

for k, v in a:
	if k in ('-m', '--module'):
		m = v
	elif k in ('-f', '--find'):
		f = v
	elif k in ('-h', '--help'):
		print(u)
		exit(0)

if m is None:
	print('Uso inválido. use -h ou --help para mostrar a ajuda.')
	exit(1)

try:
	r = fetch(m, f)
except Exception as e:
	print(e)
	exit(2)

for n, m in r:
	print('%s: %s'%(n, m))