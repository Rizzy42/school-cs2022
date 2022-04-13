from ciphers.caesar import CaesarCipherInstance

def main():
	inst = CaesarCipherInstance("Test", "", 1)
	inst.encrypt()
	print(inst.ciphertext)

if __name__ == "__main__":
	main()
