def cost():
	cost=float(raw_input(Cost per m^2:))
	breadth=float(raw_input(Width :))
	length=float(raw_input(Length:))
	return cost,breadth,length

def main():
	a,b,c=cost()
	print "The cost is: %.2f Rupees" % (float)(a*b*c)

if __name__ == '__main__':
	main()