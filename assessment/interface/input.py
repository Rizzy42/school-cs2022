from interface.data import name, version
from interface.interactions import getInteger

def getInputSource():
	print(f"Welcome to {name} (Version: {version})")

	return getInteger('''
Please select an input source:
1. External file
2. Direct input string
''', [1, 2])
