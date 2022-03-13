# There are no new features
# The main improvements here are more well-written code, as this was rewritten from scratch with one year more of experience (and a healthy dose of docs)

#* - IMPROVEMENTS -

# [IMPORTS]
#* Imports are more concise

# [LOGGER]
#* Logger puts logs into a "logs" directory instead of a massive log.txt file
#* The logger is now completely self-contained and useable outside this programs

# [GAME LOOP]
#* Program now actually exits at the end of the game

# Writing date in logfile
from datetime import datetime
# Creating the log files
from os import mkdir, getcwd
# Formatting an exception for logging
from traceback import format_exc

# Generating random numbers
from random import randint

# Nicely introducing the game
from art import tprint

# WOOOOO COLOURED TEXTTTTTT
from colorama import init, Fore, Style

# Code creates logger for use later
class Logger:
	now = datetime.now()

	# Initliases a log directory for storing logs
	# Initialises a log file for the current session
	def __init__(self):
		try:
			mkdir("logs")
		except FileExistsError:
			pass

		now = self.now
		self.logFile = open(f"{getcwd()}/logs/{now.strftime('%Y-%m-%d')}--{now.strftime('%H-%M-%S')}.log", "a")

		self.logFile.write(f"Log for run on {now.strftime('%d/%m/%Y %H:%M:%S')}\n\n")

	# Method for logging user input errors
	def writeInputError(self):
		self.logFile.write(f"User Error\n----------\n{format_exc()}\n")

	# Method for explicitly ending the log file and closing it
	def end(self):
		logFile = self.logFile

		logFile.write("End log")
		logFile.close()

# Initalises the logger for use later
logger = Logger()

# Declares some utility variables for use later
reset = Style.RESET_ALL
config = Fore.CYAN
error = Fore.RED
information = Fore.GREEN

lightcyan = Fore.LIGHTCYAN_EX


def main():
	# Variables essential for the functioning of the game
	players = 0
	difficulty = 0
	guess = 0

	# Stores guesses for each player
	store = {}

	# If the os is Windows colorama will use Win32 colour codes instead of ANSI colour codes
	init()

	# Cache for storing current player's current guess
	answerCache = -1

	# Introduces the game
	print(Fore.LIGHTCYAN_EX)
	tprint("PyNum++")

	# Creates an array for tracking the number of players
	# Converted into a list as we will be using .pop() on it later
	players = list(range(getIntFromUser(f"{config}CONFIG{reset} How many players will be playing? [1-100] {config}", "Please enter a valid number of players\n", 1, 100)))

	# Initalises store
	for player in players:
		store[player] = 0

	difficulty = getIntFromUser(f"{config}CONFIG{reset} How difficult should the game be? [{Fore.GREEN}1{reset}, {Fore.YELLOW}2{reset}, {Fore.RED}3{reset}] {config}", f"Please enter a valid option.\n", 1, 3)

	# Affects the upper bound of the number generator depending on difficulty
	if difficulty == 1:
		upto = 100
	elif difficulty == 2:
		upto = 1000
	elif difficulty == 3:
		upto = 10000

	guess = randint(0, upto)

	while answerCache != guess:
		# Gets a guess from each player
		for player in players:
			# Displaying the correct player number (Would Player 0 look right?)
			playerNum = player + 1

			answerCache = getIntFromUser(f"\n{Fore.YELLOW}GUESS{reset} {lightcyan}Player {playerNum}{reset}, what is your guess? {lightcyan}", "Your guess was invalid or out of bounds", 0, upto)
			# Increments player's guess (only when they enter a valid input)
			store[player] += 1

			if answerCache > guess:
				print(f"\n{information}INFORMATION{reset} {lightcyan}Player {playerNum}{reset}, your guess was too high")
			elif answerCache < guess:
				print(f"\n{information}INFORMATION{reset} {lightcyan}Player {playerNum}{reset}, your guess was too low")
			else:
				# Displays player's guess
				print(f"\n{Fore.GREEN}CORRECT{reset} {lightcyan}Player {playerNum}{reset}, you guessed correctly! It took you {store[player]} guesses.")
				# Gets rid of player from the list and store
				store.pop(player)
				players.pop(players.index(player))
				# Breaks out of the loop only when there are no players remaining
				if len(players) != 0:
					answerCache = -1
				else:
					break
	
	# End of the program, end of the log
	logger.end()

# Method for safely getting an integer from the user as defined in lower and upper bounds
def getIntFromUser(prompt, errPrompt, min, max):
	while True:
		try:
			# Customisable prompt
			returnVal = int(input(prompt))
			if returnVal < min or returnVal > max:
				raise ValueError
			return returnVal
		except ValueError:
			# Customisable error message
			print(f"\n{error}{Style.BRIGHT}ERROR{reset} {errPrompt}")
			logger.writeInputError()

# Useful for debugging functions
if __name__ == "__main__":
	main()
