def fasta(fname):
	fasta_dict = {}
	badfasta = False
	with open(fname, 'r') as f:
		newString = False
		name = None
		for line in f:
			if line[0] == '>':
				if name != None:
					fasta_dict[name] = fastaval
				name = line[1:].rstrip()
				newString = True
				fastaval = ""
			elif newString:
				fastaval = fastaval + line.rstrip() 
			else:
				badfasta = True
				print "bad fasta string: %s" %(line)
	if name != None and newString:
		fasta_dict[name] = fastaval
	return (fasta_dict, badfasta)
	
if __name__ == "__main__":
	print fasta('testfasta.txt')
