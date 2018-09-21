import sys
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	for  linea  in  open(sys.argv[1]):
		if (('>') == (linea[0])):
			print  (linea)
