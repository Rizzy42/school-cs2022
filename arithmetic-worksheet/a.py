def main():
	userNumber1 = askUserForNumber("First number: ")
	userNumber2 = askUserForNumber("Second number: ")

	print("-- DATA --")
	print(f"Total: {userNumber1 + userNumber2}")
	print(f"Difference: {abs(userNumber1 - userNumber2)}")
	print(f"Product: {userNumber1 * userNumber2}")
	print(f"Division: {userNumber1 / userNumber2}")
	print(f"Floor division {userNumber1 // userNumber2}")
	print(f"Modulo {userNumber1 % userNumber2}")

# We need to ask for two numbers, so this function prevents the logic from being written twice 
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
