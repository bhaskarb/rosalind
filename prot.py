def prot(cstring, codontable):
	l = len(cstring)
	pstring = ""
	for xs in range(0, l, 3):
		codon = cstring[xs:xs + 3]
		if codon not in codontable:
			print "bad codon %s" %codon
			return False
		prot = codontable[codon]
		if prot == "Stop":
			return pstring
		else:
			pstring = pstring + prot
	return pstring

def gencodontable(fname):
	codontable = {}
	with open(fname, 'r') as f:
		for line in f:
			ar = line.rstrip().split(' ')
			codontable[ar[0]] = ar[1]
	return codontable

if __name__ == "__main__":
	f = open('rosalind_prot.txt', 'r')
	cstring = f.readline()
	codontable = gencodontable('codon.txt')
	print cstring
	print prot(cstring, codontable)
			