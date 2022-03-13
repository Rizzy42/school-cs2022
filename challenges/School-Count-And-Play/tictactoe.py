def main():
	char = ""
	playerNum = 0
	i = 0

	grid = [
		["_", "_", "_"],
		["_", "_", "_"],
		["_", "_", "_"]
	]

	tracker = {
		"X": {
			"Rows": {
				0: 0,
				1: 0,
				2: 0
			},
			"Columns": {
				0: 0,
				1: 0,
				2: 0
			},
			"Diagonals": {
				"Bottom-Up": 0,
				"Top-Down": 0
			}
		},
		"O": {
			"Rows": {
				0: 0,
				1: 0,
				2: 0
			},
			"Columns": {
				0: 0,
				1: 0,
				2: 0
			},
			"Diagonals": {
				"Bottom-Up": 0,
				"Top-Down": 0
			}
		}
	}

	r3 = range(3)

	while i < 9:
		if i % 2 == 0:
			char = "X"
			playerNum = 1
		else:
			char = "O"
			playerNum = 2

		coords = [getInt(f"Player {playerNum}, in what row would you like to place your {char}? [1-3] ", [1, 3]) - 1, getInt(f"In what column would you like to place your {char}? [1-3] ", [1, 3]) - 1]
		gridPos = grid[coords[0]][coords[1]]
		if gridPos == "X" or gridPos == "O":
			print("Replacing players' current X's or O's is not allowed")
			continue
		grid[coords[0]][coords[1]] = char
		
		if gridPos == "X":
			if coords == [0, 0]:
				tracker["X"]["Rows"][0] += 1
				tracker["X"]["Columns"][0] += 1
				tracker["X"]["Diagonals"]["Top-Down"] += 1

		for j in r3:
			for k in r3:
				print(f"{grid[j][k]}   ", end="")
			print("\n")
		
				

		i += 1

def getInt(prompt, bounds):
	while True:
		try:
			returnInt = int(input(prompt))
			if returnInt < bounds[0] or returnInt > bounds[1]:
				raise ValueError
			return returnInt
		except ValueError:
			print("That isn't a number")


if __name__ == "__main__":
	main()
