import decimal

def pi_decimal(n):
	D=decimal.Decimal
	decimal.getcontext().prec=	n+10
	pi=D(0)
	k=0
	prev_k=''

	while True:
		pi+=D(4)/D(8*k+1)-D(2)/D(8*k+4)-D(1)/D(8*k+5)-D(1)/D(8*k+6)
		ans=str(pi)[n+1:-1]
		k+=1
		if ans==prev_k:
			break
		prev_k=ans
	decimal.getcontext().prec=n

	return str(pi*D(1))

if __name__=='__main__':
	import doctest
	doctest.testmod()