# Shaurya Rishi started this at 29/11/2021
# Loop the loop challenge 3

# Will be used later
from random import randint

# Global variable used in a lot of functions
# Tracks user's guesses
guesses = 1

def main():
	play = True
	while play == True:
		global guesses
		# Tracks user's guess
		userGuess = 0

		# Generates random number for guesing
		number = randint(getIntFromUser("Enter the lower bound of the generator: "), getIntFromUser("Enter the higher bound of the generator: "))

		# Repeats until user gets it right
		while userGuess != number:
			userGuess = getGuess()
			if userGuess > number:
				print("your number is too high, please try again")
				incrementGuesses()
			elif userGuess < number:
				print("your number is too low, please try again")
				incrementGuesses()
			else:
				break
			
		print(f"\nyou guessed correctly, it took you {guesses} guesses")

		# Asks user if they want to play again
		try:
			userPlayAgain = input("\nwould you like to play again? (y/n): ").lower()

			# Validates Input
			if userPlayAgain != "y" and userPlayAgain != "yes" and userPlayAgain != "n" and userPlayAgain != "no":
				raise Exception

			# If user wants to play again, reset guesses and restart main()
			if userPlayAgain == "y" or userPlayAgain == "yes":
				play = True
				guesses = 1
			# If user doesn't want to play again, set play to exit the program on the next if block
			if userPlayAgain == "n" or userPlayAgain == "no":
				play = False
		except Exception:
			print("Please enter a valid choice")
		
		# Breaks out of the loop if user doesn't want to play again
		if play == False:
			print("Goodbye")
			break

# Operation is large so function looks better
def getGuess():
	global guesses
	while True:
		try:
			return int(input(f"Guess my number [Guess {guesses}]! "))
		except ValueError:
			print("Please enter a valid integer")

# A function for safely getting an integer from the user
def getIntFromUser(prompt):
	# Keeps asking user for number until they enter a valid integer and enda the loop
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid integer")

# Used repeatedly
def incrementGuesses():
	global guesses
	guesses += 1

if __name__ == "__main__":
	main()
