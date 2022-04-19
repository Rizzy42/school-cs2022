from ciphers.caesar import CaesarCipherInstance

def main():
	inst1 = CaesarCipherInstance("My name is Shaurya, and I'm 13 years old!", "", 12)
	inst1.encrypt()
	print(inst1.ciphertext)
	inst2 = CaesarCipherInstance("", inst1.ciphertext, inst1.key)
	inst2.decrypt()
	print(inst2.plaintext)

if __name__ == "__main__":
	main()
