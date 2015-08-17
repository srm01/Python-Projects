from math import e

def make_precise_e(n):
	return '%.*f' % (n,e)

if __name__ == '__main__':
	val=False
	while not val:
		precision=(int)raw_input(n)
		if precision>=1 and precision<51:
			val=True
	print(make_precise_e(precision))