def primeFactors(n):
	while n%2==0:
		n=n/2
		print 2
	i=3
	while i<sqrt(n):
		while n%i==0:
			n=n/i
			i+=2
			print i
	if n>2:
		print n

if __name__ == '__main__':
	input=(int)raw_input(n)
	primeFactors(n)