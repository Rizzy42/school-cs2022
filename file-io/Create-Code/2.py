# Shaurya Rishi at 18/01/2021
# Python Text Files "Create your own code" challenge 2

def main():
	# with implicitly closes file
	with open("Friends.txt", "a") as file:
		userName = input("Enter name: ")
		# Adds newline in case program is run again, so that name is put on new line
		file.write(f"{userName}\n")
	
	with open("Friends.txt", "r") as file:
		print(file.read())


if __name__ == "__main__":
	main()
