def main():
	userName = input("Name: ")
	# Convenient to use later
	nameLength = len(userName)
	# Handles runtime errors if user types in string or float
	while True:
		try:
			userNumber = int(input("Number: "))
			break
		except ValueError:
			continue

	# Neat divider
	print("\n-- DATA --")

	# Question labels at the beginning of each data value
	print(f"3. {userNumber + nameLength}")
	print(f"4. {userName * nameLength}")
	print(f"5. {userNumber / nameLength}")
	print(f"6. {userNumber % nameLength}")
	# Ensures that the difference remains positive in case nameLength * 2 is less than userNumber
	print(f"7. {abs((nameLength * 2) - userNumber)}")
	print(f"8. {userNumber ** nameLength}")

if __name__ == "__main__":
	main()
