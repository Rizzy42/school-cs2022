def getInteger(prompt, numbers):
	while True:
		try:
			return_int = int(input(prompt))
			if return_int not in numbers:
				raise Exception
			
			return return_int
		except ValueError:
			print("\nThat's not an integer.")
		except Exception:
			print(f"\nPlease select from the list of given options [{numbers[0]}-{numbers[len(numbers) - 1]}]")