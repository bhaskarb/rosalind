def calcprob(k, m, n):
	pH_HH = float(k)/(k + m + n)
	pH_Hh = float(m)*(k + 0.75*m - 0.75 + 0.5*n)/((k+m+n)*(k+m+n-1))
	pH_hh = float(n)*(k + 0.5*m)/((k+m+n)*(k+m+n-1))
	return pH_HH + pH_Hh + pH_hh

if __name__ == "__main__":
	f = open('rosalind_iprb.txt', 'r')
	l = f.readline()
	ar = l.split(' ')
	print calcprob(int(ar[0]), int(ar[1]), int(ar[2]))
