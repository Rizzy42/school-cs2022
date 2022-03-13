# Shaurya Rishi at 01/11/2021
# Python SELECTION Problem 2

def main():
	print("Welcome to the Retro Music Recommender!")
	# Declaring variable for later use
	userMusicGenre = "None"
	# Prompt for question; will change if user enters invalid input
	userMusicPrompt = "What is your favourite genre of music? "

	# Continues running if validateInput returns InvalidGenreException
	while True:
		try:
			userMusicGenre = input(userMusicPrompt).lower()
			validateInput(userMusicGenre)
			break
		except Exception:
			userMusicPrompt = "Sorry, we don't support that genre of music yet! Please try again: "
			continue

	# Nice-looking formatting
	print("\n")
	if userMusicGenre == "rock":
		print("We recommend listening to Deep Purple (Smoke on the Water, anyone?)")
	elif userMusicGenre == "metal":
		print("Metallica, all the way")
	elif userMusicGenre == "pop":
		print("Pathetic, go listen to Justin Beiber or whatever")
	elif userMusicGenre == "dance":
		print("Chic (the band, not the genre)")
	elif userMusicGenre == "rap":
		print("Let's go (DaBaby)")

def validateInput(inputGenre):

	if inputGenre in ["rock", "metal", "pop", "dance", "rap"]:
		return True
	else: 
		# Returns an error, triggering the previous try...except block to restart
		# Needed to see docs for this
		raise Exception("Input genre is invalid")

if __name__ == "__main__":
	main()
