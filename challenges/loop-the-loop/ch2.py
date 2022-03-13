# Shaurya Rishi started this at 16/11/2021
# Loop the loop challenge 2
from time import sleep

def main():
	start = 0
	while True:
		try:
			start = abs(int(input("START number: ")))
			break
		except:
			print("Please enter a valid number")

def countdown(start):
	while start > 0:
		print (Start)
		sleep(1)
		start -= 1
