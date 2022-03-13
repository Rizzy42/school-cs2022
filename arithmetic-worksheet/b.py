def main():
	length = askUserForNumber("Length: ")
	width = askUserForNumber("Width: ")
	height = askUserForNumber("Height: ")

	print(f"Volume: {length * width * height}")

# We need to ask for three numbers, so this function prevents the logic from being written multiple times 
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
