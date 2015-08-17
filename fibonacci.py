def fibonacci(n):
	fib[]
	fib[0]=0
	fib[1]=1
	temp=2
	while temp<n:
		fib[temp]=fib[temp-1]+fib[temp-2]
		temp+=1
	return fib[n-1]

if __name__ == '__main__':
	inp=(int)raw_input(n)
	print(fibonacci(inp))
