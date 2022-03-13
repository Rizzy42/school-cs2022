# Shaurya Rishi at 05/01/2021 (Happy New Year!)
# File I/O Task 1
from os.path import isfile

def main():
	# Checks if file exists so as to not waste resources on truncating it (needed to refer to docs to get method, idea was my own)
	if isfile("pe.txt") == False:
		# with block implicitly closes file at the end (needed to refer to docs for this awesome idea!)
		with open("pe.txt", "w") as writeablePe:
			# Writes a list of five sports
			# \n makes sure code remains concise without being unreadeable
			writeablePe.write("Rugby\nFootball\nSwimming\nBasketball\nHandball")

	# Need to open file for reading again
	with open("pe.txt", "r") as readeablePe:
		print(readeablePe.read())
		# Oddly enough input() was not needed as the text printed just fine!

if __name__ == "__main__":
	main()
