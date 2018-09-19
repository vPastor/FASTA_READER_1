import sys
if len(sys.argv)>2:
	print ('Numero de argumentos invalidos')
(sys.argv)
field = '/home/victor/Desktop/pdb_seq.txt'
for  linea  in  open(field):
	if (('>') == (inea.split()[0)):
		print  (linea)

