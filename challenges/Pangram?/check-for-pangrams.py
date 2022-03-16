def main():
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	# Will count the number of letters of the alphabet present in a line
	line_alphabet_count = 0

	# Will be used to give the line number
	line_index = 1

	with open("pangrams.txt", "r") as pangrams:
		pangram_lines = pangrams.readlines()
		for line in pangram_lines:
			# Converting to lower means that we don't also have to compare capital letters
			line = line.lower()
			for char in alphabet:
				if char in line:
					line_alphabet_count += 1
			if line_alphabet_count == 26:
				print(f"[TRUE] Line {line_index} is a pangram")
			else:
				print(f"[FALSE] Line {line_index} is not a pangram")

			# Reset and update variables for the next cycle
			line_alphabet_count = 0
			line_index += 1

if __name__ == "__main__":
	main()
