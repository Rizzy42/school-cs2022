# Shaurya Rishi at 10/11/2021
# Iteration Task 1

# Global variable for use in multiple functions
totalPay = 0
def main():
	# Could find no other way to do this more efficiently, so had to call functions seven times
	incrementPayWith("Sunday")
	incrementPayWith("Monday")
	incrementPayWith("Tuesday")
	incrementPayWith("Wednesday")
	incrementPayWith("Thursday")
	incrementPayWith("Friday")
	incrementPayWith("Saturday")
	# Had to see docs for this one (currency formatting)
	print("Total pay: ${:,.2f}".format(totalPay / 100))

# Defined function to avoid repetition
def incrementPayWith(day):
	# Need to work with global variable
	global totalPay
	# Repeats until user enters an integer
	while True:
		try:
			totalPay += int(input(f"How many newspapers were sold on {day}? ")) * 10
			break
		except ValueError:
			print("Please enter a valid integer")

if __name__ == "__main__":
	main()
