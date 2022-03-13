# Shaurya Rishi started this at 29/11/2021
# Loop the loop challenge 3

# Will be used later
from random import randint

# Global variable used in a lot of functions
# Tracks user's guesses
guesses = 1

def main():
	global guesses
	# Tracks user's guess
	userGuess = 0

	# Generates random number for guesing
	number = randint(1, 100)

	# Repeats until user gets it right
	while userGuess != number:
		userGuess = getGuess()
		if userGuess > number:
			print("Your guess was too high")
			incrementGuesses()
		elif userGuess < number:
			print("Your guess was too low")
			incrementGuesses()
		else:
			break

	print(f"\nCongrats! The answer was {number}; you guessed it in {guesses} guesses")

# Operation is large so function looks better
def getGuess():
	global guesses
	while True:
		try:
			return int(input(f"Guess my number [Guess {guesses}]! "))
		except ValueError:
			print("Please enter a valid integer")

# Used repeatedly
def incrementGuesses():
	global guesses
	guesses += 1

if __name__ == "__main__":
	main()
