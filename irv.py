def irv(c):
	pr = [ 1 ,1, 1, 0.75, 0.5, 0 ]
	val = 2*sum(i*j for i, j in zip(pr, c))
	return val
	
if __name__=="__main__":
	f = open('rosalind_iev.txt', 'r')
	l = f.readline()
	ar = map(int, l.split(' '))
	print irv(ar)
