class CaesarCipherInstance:
	# Initialises the two components of the cipher
	def __init__(self, plaintext, ciphertext, key):
		self.plaintext = plaintext
		self.ciphertext = ciphertext
		self.key = key

	alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	def encrypt(self):
		# Aliasing variables to prevent repetition of "self"
		alphabet_lower = self.alphabet_lower
		alphabet_upper = self.alphabet_upper

		for letter in self.plaintext:
			# Spaces should not be shifted
			if letter == " ":
				continue
			elif letter in alphabet_lower or letter in alphabet_upper:
				if letter in alphabet_lower:
					alphabet_local = alphabet_lower
				elif letter in alphabet_upper:
					alphabet_local = alphabet_upper

				letter_index = alphabet_local.index(letter)
				letter_shifted_index = letter_index + self.key
				# If the shifted index is greater than accessing the array with it will give an out of range error
				if letter_shifted_index > 25:
					letter_shifted_index = letter_shifted_index - 26

				# Constructs the ciphertext 
				self.ciphertext = self.ciphertext + alphabet_local[letter_shifted_index]
			# Symbols shouldn't be shifted
			else:
				continue