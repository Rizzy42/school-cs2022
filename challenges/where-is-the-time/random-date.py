from datetime import date
from random import randint

# Custom errors that will make sense later
class InputValueTooHighError(Exception):
	pass
class InputValueTooLowError(Exception):
	pass

def main():
	user_date = createNewDate()

	user_date["year"]= getBoundedInteger("Enter a year [yyyy between 0 and 10000 inclusive]: ", [0, 10000])
	user_date["month"]= getBoundedInteger("Enter a month [mm between 1 and 12 inclusive]: ", [0, 12])
	user_date["day"] = getBoundedInteger("Enter a day [mm number relevant to the month]: ", getBounds(user_date["month"], user_date["year"]))

	today_generated = date.today()
	
	today_date = createNewDate()
	today_date["year"] = getFormattedDateInteger("%Y", today_generated)
	today_date["month"] = getFormattedDateInteger("%m", today_generated)
	today_date["day"] = getFormattedDateInteger("%d", today_generated)

	random_date = createNewDate()
	comparedAssignment("year", user_date, today_date, random_date)
	comparedAssignment("month", user_date, today_date, random_date)

	#* If the user's date and today are the same, then the random date be the same as well
	if user_date["year"] == today_date["year"] and user_date["month"] == today_date["month"]:
		random_date["day"] = today_date["day"]
	else:
		# Ensures that the day makes sense relative to the month
		random_date_day_bounds = getBounds(random_date["month"], random_date["year"])
		random_date["day"] = randint(random_date_day_bounds[0], random_date_day_bounds[1])

	print(f"Here's a random date between your date and today: {random_date['day']}/{random_date['month']}/{random_date['year']}")

#* Provides a simple way to create an object storing a date's attributes
def createNewDate():
	return {
		"year": 0,
		"month": 0,
		"day": 0
	}

# randint()'s first argument is always lesser than the second, so this function accounts for both cases of a user's date being greater than or lesser than today
def comparedAssignment(aspect, user_date, today_date, random_date):
	if user_date[aspect] < today_date[aspect]:
		random_date[aspect] = randint(user_date[aspect], today_date[aspect])
	elif user_date[aspect] > today_date[aspect]:
		random_date[aspect] = randint(today_date[aspect], user_date[aspect])
	else:
		# Duplicate the date if user's 
		random_date[aspect] = today_date[aspect]

#* Conveniently provides wanted aspect of today's date in integer form
today = date.today()
def getFormattedDateInteger(format, date):
	return int(date.strftime(format))

#* Provides a safe way of getting an integer between two user-defined bounds
def getBoundedInteger(prompt, bounds):
	bound_lower = bounds[0]
	bound_upper = bounds[1]
	user_int = 0

	while True:
		try:
			user_int = int(input(prompt))

			if user_int < bound_lower:
				raise InputValueTooLowError
			if user_int > bound_upper:
				raise InputValueTooHighError
			
			return user_int
		# Different errors help to inform the user of different errors in their input
		except ValueError:
			print("That isn't a valid integer.")
		except InputValueTooLowError:
			print("Your number was too low")
		except InputValueTooHighError:
			print("Your number was too high")

#* Returns the allowed bounds for a given month
# Also accounts for leap years
def getBounds(month, year):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return [1, 31]
	elif month == 2:
		if year % 400 == 0:
			return [1, 29]
		elif year % 4 == 0 and year % 100 != 0:
			return [1, 29]
		else:
			return [1, 28]
	else:
		return [1, 30]

if __name__ == "__main__":
	main()
