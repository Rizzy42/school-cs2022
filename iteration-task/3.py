# Shaurya Rishi started this at 11/11/2021
# Iteration Task Problem 3

def main():
	# Declare variables at the start for readability
	totalPrice = 0
	units = ""
	# Decides whether program should stop asking for prices
	end = False
	# Iterator for specifying item number
	i = 1

	# Repeats until program tells loop to end using end variable
	while end == False:
		price = getPriceOfItem(i)
		if price == 0:
			end = True
		else:
			totalPrice = totalPrice + price
			# Sets iterator so that next item is different
			i += 1
	
	units = getUnits()
	if len(units) > 1:
		print(f"The total price is {totalPrice} {units}")
		# If unit is for example $ put in front of price
	else:
		# If unit is for example AED or USD put behind price
		print(f"The total price is {units}{totalPrice}")

# Provides a mechanism to get the price of an item
# Keeps code readable and concise
def getPriceOfItem(itemNum):
	# Repeats until user enters a valid float
	while True:
		try:
			return float(input(f"What is the price of item {itemNum}? "))
		except:
			print("Please type in a valid price")

# Provides mechanism to get valid currency
# Keeps code concise
def getUnits():
	# Repeats until user enters a non-blank currency
	while True:
		try:
			units = input("What is the currency (e.g. $, AED)? ")
			if units == "":
				raise ValueError
			else:
				return units
		except ValueError:
			print("Please enter a valid currency")

if __name__ == "__main__":
	main()
