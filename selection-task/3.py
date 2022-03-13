# Shaurya Rishi started this at 02/11/2021
# Python SELECTION Problem 3

numQuestionsCorrect = 0 
numQuestionsAsked = 0

def main():
	# Functions have been composed together to make the code more readable
	intro()
	newQuestion("Who wrote the original Linux kernel?", "Dennis Ritchie", "Linus Torvalds", "Alan Turing", "B")
	newQuestion("What distro is Ubuntu 20.04 LTS based on?", "Debian", "Slackware", "RHEL", "A")
	newQuestion("What is arguably Arch Linux's most useful feature?", "Arch User Repository (AUR)", "GNOME", "apt", "A")
	newQuestion("What was Linux based on?", "EFIX", "RUFIX", "UNIX", "C")
	newQuestion("Linux, Windows, or macOS?", "Linux (Nice choice)", "macOS (Looks good ngl)", "Windows (pathetic)", "A")

	# Prints the final score and rating
	if numQuestionsCorrect >= 4:
		print(f"A score of {numQuestionsCorrect}/5, you're a genius!")
	elif numQuestionsCorrect >= 2:
		print(f"Got {numQuestionsCorrect}/5? Not bad...")
	else:
		print(f"{numQuestionsCorrect}/5. Maybe time to brush up on your computer skills, don't you think?")


def validateInput(input, possibleInputChoices, compareInputsAgainst):
		if input in compareInputsAgainst:
			pass
		else:
			# Raises an error in preparation for the except block
			raise Exception(f"Input does not satisfy choices: {possibleInputChoices}")

# Function to print the intro to the quiz
def intro():
	returnVal = None
	prompt = "Welcome to the Linux quiz, ready to start? [Y/N] "

	# Repeats until user enters a valid input (i.e. only Y or N)
	while True:
		try:
			# Conversion to upper case to make it easier to compare
			returnVal = input(prompt).upper()
			validateInput(returnVal, "[Y, N]", ["Y", "N"])
			# Cheeky comment :)
			if returnVal == "N":
				print("Too bad.")
			break
		except:
			# Changes prompt to reflect the error
			prompt = "Sorry, please try again"
			continue

# Provides an interface to create a new question
def newQuestion(prompt, opt1, opt2, opt3 , corrOpt):
	# Changes global values as they are used in main()
	global numQuestionsAsked
	global numQuestionsCorrect
	# Declares these variables at the start to make it easier to read and understand
	userAnswer = ""
	answerPrompt = ""

	# Increments the number of questions asked, so as to show it in the prompt
	numQuestionsAsked += 1
	# Inserts the question prompt into the prompt string
	print(f"\nQ{numQuestionsAsked}) {prompt} [A, B, C]")
	# Inserts the options into the option strings
	print(f"A) {opt1}")
	print(f"B) {opt2}")
	print(f"C) {opt3}")
	# Neat division of the prompt/options and the answer
	print("------------")

	# Repeats until user enters a valid input (i.e. only A, B, or C)
	while True:
		try: 
			# Obtains the user's answer to pass into validateInput()
			# Could chain but it would make the code less readable
			userAnswer = input(answerPrompt).upper()
			validateInput(userAnswer, "A, B, C", ["A", "B", "C"])
			break
		except Exception:
			# Changes prompt to reflect the error
			answerPrompt = "Sorry, please try again [A, B, C]: "
			continue

	# Informs the user if they were correct or not
	if userAnswer == corrOpt:
		print("CORRECT! :D\n")
		numQuestionsCorrect += 1
	else:
		print("WRONG :(\n")

# Calls the main function
# Can be used in other files to run the quiz
if __name__ == "__main__":
	main()
