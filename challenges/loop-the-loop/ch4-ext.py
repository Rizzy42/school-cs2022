# Shaurya Rishi at 07/12/2021
# Loop the loop challenge 4

def main():
	# 10 rows
	for i in range(1, 11):
		# 10 columns
		for j in range(1, 11):
			# We obtain the number from multiplying the column and row position
			mul = i * j

			# Prints an extra space to push single-digit numbers to the end of the column
			if mul / 10 < 1:
				print(end=" ")

			# Prints the actual number
			print(mul, end="")

			# Only puts a one-space divider between the number and the next number, so that 100 can fit into the last column
			# There is one more 90 (the one above 100), but this won't show any visible difference
			if mul == 90:
				print(end=" ")
			# Apply a regular two-space divider
			else:
				print(end="  ")
		# Newline
		print()

if __name__ == "__main__":
	main()
