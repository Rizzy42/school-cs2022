# Shaurya Rishi at 11/01/2022
# Python Text Files "Explaining Code"

def main():
	# with implicitly closes files
	with open("Ages.txt", "w") as file:
		again = True
		while again == True:
			name = input("Enter name: ")
			age = getAge()
			# Format string formats the name and age correctly and as the programmer expected
			file.write(f"{name}, {age}\n")
			more = getChoice()
			# Can compare against "n" since getChoice takes care of correct choice and converting to lowercase
			if more == "n":
				again = False

	with open("Ages.txt", "r") as file:
		print(file.read())

# Defines a function for safely getting the choice
def getChoice():
	while True:	
		try:
			# Converts to lowercase to account for Y and N cases
			userChoice = input("Enter another? [y/n] ").lower()
			# Array comparison is more concise than (if userChoice == "y" and userChoice = ...)
			if userChoice not in ["y", "n"]:
				raise Exception
			return userChoice
		except Exception:
			print("That's not a valid choice")
			continue

# Defines a method for safely getting an integer age
def getAge():
	while True:
		try:
			userAge = int(input("Enter age: "))
			return userAge
		except ValueError:
			print("That's not a valid age")
			continue

if __name__ == "__main__":
	main()