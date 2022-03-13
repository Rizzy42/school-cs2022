import math
def main():
	userNumber1 = input("Number 1: ")
	userNumber2 = input("Number 2: ")
	userNumber3 = input("Number 3: ")
	userNumber4 = input("Number 4: ")
	userNumber5 = input("Number 5: ")
	
	total = m(userNumber1, userNumber2, userNumber3, userNumber4, userNumber5)
	print(f"Total: {total}")
	print(f"Mean Average: {total / 5}")

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