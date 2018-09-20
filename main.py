import sys
if len(sys.argv)>2 || len(sys.argv)<1:
	print ('Numero de argumentos invalidos')
else:
	field = sys.argv[1]
	for  linea  in  open(field):
		if (('>') == (inea.split()[0])):
			print  (linea)

