def ask():
	months = int(raw_input("Enter mortgage term (in months): "))
	rate = float(raw_input("Enter annual interest rate: "))
	loan = float(raw_input("Enter loan value: "))

def main():
	time,rate,princi=ask()
	interest=princi*rate*time/12
	installment=(princi+interest)/time
	print installment

if __name__ == '__main__':
	main()
