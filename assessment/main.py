from colorama import init as colorama_init 
from colorama import Fore, Back, Style
from utils.files import importLines, writeLines, appendLines
from interface.interactions import getInteger
from ciphers.caesar import CaesarCipherInstance
from ciphers.atbash import AtbashCipherInstance

colorama_init()

def main():
	user_source_option = 0
	user_cipher_option = 0
	user_crypt_option = 0

	print("Welcome to the Encryptor.")

	user_source_option = getInteger('''
Please select an input source:
1. External file
2. Direct input string
''', [1, 2])

	
if __name__ == "__main__":
	main()
