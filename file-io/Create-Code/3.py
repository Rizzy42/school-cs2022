# Shaurya Rishi at 18/01/2022
# Python Text Files "Create your own code" challenge 2

def main():
	# with implicitly closes file
	with open("Sums.txt", "w") as sumsFile:
		repeat = True
		while repeat:
			num1 = getFloat("Number 1: ")
			num2 = getFloat("Number 2: ")
			total = num1 + num2
			print(f"Total: {total}\n")

			# Writes as an f-string for easy formatting
			sumsFile.write(f"{str(num1)} + {str(num2)} = {total}\n")

			# Asks the user if they want to repeat
			repeat = getOption()
	
	with open("Sums.txt", "r") as readeableSums:
		print(readeableSums.read())


# Provides a safe method for getting a float from the user
def getFloat(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("That's not a valid number")
			continue

# Provides a safe way of getting a valid yes-no answer from the user
def getOption():
	while True:
		try:
			opt = input("Repeat? [y/n] ").lower()

			if opt not in ["y", "n"]:
				raise Exception
			
			if opt == "y":
				return True
			else:
				return False
		except Exception:
			print("That's not a valid choice")
			continue

if __name__ == "__main__":
	main()
