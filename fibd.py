def fibd(n ,m):
	permonth = [0]*m;
	permonth[0] = 1
	for i in range(1, n):
		print i, permonth
		nn = sum(permonth[1:n])
		nd = permonth.pop();
		permonth.insert(0, nn)
	print permonth
	return sum(permonth)

if __name__ == "__main__":
	f = open('rosalind_fibd.txt', 'r')
	l = f.readline()
	ar = map(int, l.split(' '))
	print fibd(ar[0], ar[1])
