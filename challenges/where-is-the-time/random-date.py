# Shaurya Rishi @ 19/01/2022
# "Where is the time?" Challenge 2

def main():

	def monthLogic(userInt):
		if userMonth == 2 and userInt > 28:
			raise Exception
		elif userMonth < 8 and userMonth % 2 == 0 and userInt > 30:
			raise Exception
		elif userMonth >= 8 and userMonth % 2 == 1 and userInt > 30:
			raise Exception
	
	def dayConvenienceLogic(userInt):
		if userMonth == 2:
			return [1, 28]
		elif (userMonth < 8 and userMonth % 2 == 1) or (userMonth >= 8 and userMonth % 2 == 0):
			return [1, 31]
		else:
			return [1, 30]

	userYear = getBoundedInteger("Enter year [yyyy]: ", [0, 10000], "That's not a valid year")[0]
	
	userMonthData = getBoundedInteger("Enter month [1-12]", [0, 13], "That month does not exist", monthLogic, dayConvenienceLogic)
	userMonth, dayLower, dayHigher = userMonthData[0], userMonthData[1][0], userMonthData[1][1]

	userDay = getBoundedInteger(f"Enter day [{dayLower}-{dayHigher}]: ", [dayLower - 1, dayHigher])


# Provides a safe method for getting an integer within defined exclusive bounds from the user
def getBoundedInteger(prompt, bounds, validityErrorMsg, extraLogic=lambda none : return none, metaLogic=lambda a: return a):
	# Easier than repeating bounds[n]
	lower = bounds[0]
	upper = bounds[1]
	while True:
		try:
			userInt = int(input(prompt))
			# First parameter of range() is always inclusive
			if userInt not in range(lower + 1, upper):
				raise Exception

			extraLogic(userInt)
			meta = metaLogic(userInt)

			return (userInt, meta)
		except ValueError:
			# If there are letters in the input
			print(validityErrorMsg)
		except Exception:
			# Informs user of bounds
			print(f"Out of bounds. Must be between {lower} and {upper}")

if __name__ == "__main__":
	main()
