def decToBinary(dec_no):
	binary=''
	while dec_no>0:
		binary=str(dec_no%2)
		dec_no/=2
	return binary[::-1]

def binToDecimal(binary_no):
	rev=str(number)[::-1]
	decimal=0
	counter=0
	while counter<len(rev):
		if rev[counter]=='1':
			decimal+=2**counter
		counter+=1
	return decimal

if __name__ == '__main__':
	x=raw_input()
	print 'If decimal to binary enter 1'
	print 'Else if binary to decimal enter 2'
	i=raw_input()
	if i==1:
		decToBinary(x)
	if i==2:
		binToDecimal(x)


