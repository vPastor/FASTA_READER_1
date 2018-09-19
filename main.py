
field = '/home/victor/Desktop/pdb_seq.txt'
for  linea  in  open(field):
	if '>' in linea:
		print  (linea)

