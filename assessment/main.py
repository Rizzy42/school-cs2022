from ciphers.caesar import CaesarCipherInstance
from ciphers.atbash import AtbashCipherInstance

def main():
	inst = AtbashCipherInstance("abcdefghijklmnopqrstuvwxyz", "")
	inst.encrypt()
	print(inst.ciphertext)
	inst.plaintext = ""
	inst.decrypt()
	print(inst.plaintext)
	
if __name__ == "__main__":
	main()
