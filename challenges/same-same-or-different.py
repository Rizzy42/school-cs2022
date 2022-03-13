# Shaurya Rishi at 10/11/2021
# Challenge - Same Same or Different

def main():
	userName = input("What is your name? ")
	while True:
		try:
			userAge = int(input("How old are you? "))
			break
		except ValueError:
			print("Please enter an integer age")

	if userName == "Shaurya" or userName == "Shaurya Rishi" and userAge == 13:
		print("Same Same!")
	elif userAge == 13 and len(userName) == 7 or len(userName) == 13:
		print("Same age buddy and that name of yours has an awesome number of characters")
	elif userName != "Shaurya" and userAge > 13:
		print("Yo oldie your name stinks")
	elif userName != "Shaurya" and userAge < 13:
		print("Hey kid, nice name but mine's better.")
	else:
		print("Different!")

if __name__ == "__main__":
	main()
