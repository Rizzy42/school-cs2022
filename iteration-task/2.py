# Shaurya Rishi started this at 10/11/2021
# Iteration Task 2

def main():
	# Sets variable for tracking goals
	goals = 0
	# Repeats the asking of goals for each match until the number of matches is reached
	for i in range(getMatches()):
		# Increments goal by number of matches
		# Puts i+1 as i starts on 0
		goals = goals + getGoals(i + 1)
	print(f"In total, {goals} goals were scored in the tournament.")

# Gets the number of matches played in the tournament from the user
def getMatches():
	# Repeats until user enters a valid integer
	while True: 
		try:
			return int(input("How many matches were played? "))
		except:
			print("Please enter a valid integer")

# Function to request goals from the user for a match
def getGoals(matchNum):
	# Repeats until user enters a valid integer
	while True:
		try:
			return int(input(f"How many goals were scored in match {matchNum}? "))
		except:
			print("Please enter a valid integer")

if __name__ == "__main__":
	main()
