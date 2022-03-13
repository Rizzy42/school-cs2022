# Shaurya Rishi started this at 11/11/2021
# Iteration Task Problem 4

# Creates a custom error for more readability
# Needed to consult docs for this
class InvalidInputException():
	pass

def main():
	playerPoints = 101
	# To inform player of new game
	print(f"You're starting a new game with 101 points")

	# Runs while the player's score is above 0
	while playerPoints >= 0:
		# Decrements playerPoints based on the result of dartThrow()
		playerPoints = playerPoints - dartThrow()
		# Informs player of current score
		print(f"You now have {playerPoints} points")

	# Informs player of end of the game and their final score
	print(f"\nThe game has ended, you ended with {playerPoints} points")

def dartThrow():
	# Multiline string is easier to read
	prompt = """
Where did the dart land?
-----------------------------
1. Bullseye [-20 points]
2. Inner Circle [-10 points]
3. Outer Circle [-5 points]
-----------------------------
""" 
	# Repeats until the user enters a valid choice
	while True:
		try:
			landed = int(input(prompt))
			# Raises previously-declared error to start except block
			if landed not in [1,2,3]:
				raise InvalidInputException("Input does not satisfy conditions")

			# Returns the points to decrement based on where the dart landed
			if landed == 1:
				return 20
			elif landed == 2:
				return 10
			elif landed == 3:
				return 5
		except:
			print("Please enter a valid choice")
			prompt = "Where did the dart land? [1/2/3] "

if __name__ == "__main__":
	main()
