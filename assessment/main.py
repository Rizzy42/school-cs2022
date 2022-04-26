# This main program brings all the components together and does the actual heavy work of encryption

# Initialises colorama to convert ANSI codes to win32 so that the display correctly on Windows
from colorama import init as colorama_init 

from utils.files import importLines, writeLines, appendLines

# Interface programs
from interface.input_source import getInputSource

from ciphers.caesar import CaesarCipherInstance
from ciphers.atbash import AtbashCipherInstance

colorama_init()

def main():
	# All the abstraction paid off, this looks great!
	user_source_option = getInputSource()
	user_cipher_option = 0
	user_crypt_option = 0

	
if __name__ == "__main__":
	main()
