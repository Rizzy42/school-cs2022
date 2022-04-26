def importLines(input_file):
	try:
		with open(input_file, "r") as file:
			return file.readlines
	except FileNotFoundError:
		raise Exception("Input file does not exist")

def writeLines(input_file, input_lines):
	with open(input_file, "w") as file:
		file.writelines(input_lines)

def appendLines(input_file, input_lines):
	with open(input_file, "a") as file:
		file.writelines(input_lines)
