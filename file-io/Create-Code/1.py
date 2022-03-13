# Shaurya Rishi at 12/01/2021
# Python Text Files "Create your own code" challenge 1

def main():
	# with implicitly closes file
	with open("Friends.txt", "w") as file:
		# Repeats this process six times
		for i in range(6):
			tempName = input("What is this friend's name? ")
			file.write(f"{tempName}\n")

if __name__ == "__main__":
	main()	
