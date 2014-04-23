import fasta

def gccontent(fastastr):
	num = sum((c == 'G' or c == 'C') for c in fastastr)
	return (100*num)/float(len(fastastr))

def gc(gc_dict):
	max_score = 0
	max_string = ""
	for key in gc_dict:
		score = gccontent(gc_dict[key])
		#print key, score
		if score > max_score:
			max_score = score
			max_string = key
	return (max_score, max_string)

if __name__ == "__main__":
	(gc_dict, invalid) = fasta.fasta('rosalind_gc.txt')
	if not invalid:
		(max, maxstr) = gc(gc_dict)
		print maxstr
		print max
		
