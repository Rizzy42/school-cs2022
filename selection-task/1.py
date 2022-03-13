# Shaurya Rishi at 01/11/2021
# Python SELECTION Problem 1
def main():
	numberOne = askUserForNumber("Number one: ")
	numberTwo = askUserForNumber("Number two: ")

	# Formatting
	print("\n")
	if numberOne == numberTwo:
		print("These two numbers are equal")
	if numberOne > numberTwo:
		print(f"The first number, {numberOne}, is greater")
	elif numberOne < numberTwo:
		print(f"The second number, {numberTwo}, is greater")

def askUserForNumber(prompt):
	returnValue = 0.0
	# Failsafe prevents runtime errors when user enters string
	while True:
		try:
			returnValue = float(input(prompt))
			break
		except ValueError:
			continue

	return returnValue

if __name__ == "__main__":
	main()
