def findNextPrime(x):
	return findPrimeInRange(n,2*n)

def findPrimeInRange(a,b):
	for p in range(a,b):
		for i in range(2,p):
			if p%i==0:
				break
			else return p
	return None

if __name__ == '__main__':
	main()