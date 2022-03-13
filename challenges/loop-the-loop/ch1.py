# Shaurya Rishi started this at 16/11/2021
# Loop the loop challenge 1

# Sleep execution delays execution for a given number of seconds
from time import sleep

def main():
	stop = 0
	# Tries until user enters a valid number
	while True:
		try:
			# abs takes care of negative numbers
			stop = abs(int((input("STOP number: "))))
			break
		except:
			print("Please enter a valid number")

	stopwatch(stop)

def stopwatch(stop):
	for i in range(stop):
		sleep(1)
		print(i + 1)

if __name__ == "__main__":
	main()

