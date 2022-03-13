# Main function can be used in other files
def main():
    # Imports, randint for random number, format_exc for making tracebacks into strings, datetime for logging the date, tprint for ASCII art, and init and Fore for colours
    from random import randint
    from traceback import format_exc
    from datetime import datetime
    from art import tprint
    from colorama import init, Fore

    #* Improvement: declare random number and lower and upper bounds variables which will be used later
    rand = 0
    lower = 0
    higher = 0

    # Create point store for players
    store = {}

    # Variable for number of players
    playerNum = 0

    #* Improvement: declare difficulty level variable which will be used later
    diffNum = 0

    #* Improvement: choose level number
    levelNum = 0
    
    #* Level iterator will be used to make level harder and harder depending on difficulty
    levelIterator = 0

    #* Improvement: display emoji, used to show level difficulty
    emoji = ""

    # Player's guess
    playerGuess = 0

    # Open log
    logFile = open('log.txt', 'a', encoding='UTF-8')

    # Assign dates and times to variables
    now = datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    nowDay = now.strftime('%D')

    # Write date of run in log
    logFile.write(f'\nLog for run at {nowTime} on {nowDay}\n')

    # Initialise colorama for prompt colours
    init()

    # Create reset variable for resetting prompt colour
    reset = Fore.RESET

    # Player cursor is color of players input number
    player = Fore.CYAN

    #* Improvement: colours
    green = Fore.GREEN
    yellow = Fore.YELLOW
    red = Fore.RED
    cyan = Fore.CYAN

    # Introduce PyNum as game name
    print(Fore.CYAN)
    tprint("PyNum")

    # Reset
    print(reset)

    # Get number of players, while true loop so that it will keep asking until it gets a valid answer
    while True:
        # Try except block to check for errors, if there is a valid answer break out of while true loop and if not a valid answer, log error and ask again
        try: 
            playerNum = int(input(f"{Fore.BLUE + 'CONFIG'}{reset} How many players will play? {player}"))
            break
        except:
            # format_exc converts exception to string
            logFile.write(f'\nException\n{format_exc()}')

    #* Improvement: added difficulty levels for determining random number
    # go function starts the game with an introductory message
    def go():
        print(f"\n{emoji} A number between {lower} and {higher}? Let's go!")

    while True:
        # Try except block to check for errors, if there is a valid answer break out of while true loop and if not a valid answer, log error and ask again
        try: 
            diffNum = int(input(f"{Fore.BLUE + 'CONFIG'}{reset} What is the difficulty level? [{green}1{reset}, {green}2{reset}, {yellow}3{reset}, {yellow}4{reset}, {red}5{reset}] {player}"))
            # Each option changes the go function slightly
            if diffNum == 1:
                rand = randint(1, 100)
                lower = 1
                higher = 100
                levelIterator = 50

                emoji = "😁"
            elif diffNum == 2:
                rand = randint(1, 500)
                lower = 1
                higher = 500
                levelIterator = 100
                
                emoji = "😁"
            elif diffNum == 3:
                rand = randint(1, 2500)
                lower = 1
                higher = 2500
                levelIterator = 500
                
                emoji = "😎"
            elif diffNum == 4:
                rand = randint(1, 10000)
                lower = 1
                higher = 10000
                levelIterator = 10000

                emoji = "😎"
            elif diffNum == 5:
                rand = randint(1, 100000)
                lower = 1
                higher = 100000
                levelIterator = 10000
                
                emoji = "🔥"
            else:
                raise Exception
            break
        except:
            # format_exc converts exception to string
            logFile.write(f'\nException\n{format_exc()}')

    #* Improvement: added level numbers
    while True:
        # Try except block to check for errors, if there is a valid answer break out of while true loop and if not a valid answer, log error and ask again
        try: 
            levelNum = int(input(f"{Fore.BLUE + 'CONFIG'}{reset} How many levels would you like to play? {player}"))
            break
        except:
            # format_exc converts exception to string
            logFile.write(f'\nException\n{format_exc()}')

    # Initialises number of players in playerNum in store
    for i in range(playerNum):
        store[f'player{i}'] = {
            'points': 0,
            'attemptCounter': 0
        }
    
    breaker = False
    # First while true loop ensures it keeps asking each player
    #* Improvement: Levels, increments the upper bound each time
    for i in range(levelNum):
        if i == 0:
            pass
        else:
            rand = randint(lower, higher + levelIterator)
            go()
        
        while True:
            if breaker:
                break
            # Breaker will be used to break out of the first loop if all players have guessed the number
            # Starts to ask each player, determines player number through length of store
            for i in range(len(store)):
                while True:
                    # Wraps in a try except block, if player does not exist goes to next player
                    try:
                        store[f'player{i}']['attemptCounter'] += 1
                    except KeyError:
                        i += 1
                        # Checks if no players are left in store, sets breaker to true and breaks out of for loop
                        if len(store) == 0:
                            breaker = True
                            break
                        else:
                            # Continues if players are still left in the store
                            continue
                    # This try except block keeps asking the player until it gets a valid answer, if not valid it logs the error, informs player answer is not valid and tries again
                    try: 
                        playerGuess = int(input(f"\n{Fore.YELLOW + 'QUESTION'}{reset} {player}Player {i + 1}{reset}, what is your guess? {player}"))
                        break
                    except ValueError:
                        logFile.write(f'\nError{format_exc()}')
                        print(f"\n{Fore.RED + 'ERROR'}{reset} Your guess was not valid")
                        continue
                
                # Checks if player's guess is equal to, above, or below the random number. It informs the player in all three cases
                if playerGuess > rand:
                    print(f"\n{Fore.GREEN + 'INFORMATION'}{reset} The random number is lower")
                elif playerGuess < rand:
                    print(f"\n{Fore.GREEN + 'INFORMATION'}{reset} The random number is greater")
                else:
                    # attemptCounter variable is to ensure code is still readable in congratulations message
                    attemptCounter = store[f'player{i}']['attemptCounter']
                    # Increments player's points
                    store[f'player{i}']['points'] += 5
                    print(f"{Fore.CYAN} 💫 Congratulations Player {i + 1}! You got the number in {attemptCounter} attempts! 💫")
                    # Removes player from store as they have already guessed, allows other players to keep playing
                    store.pop(f'player{i}')

# Runs main if this is the file being run
if __name__ == "__main__":
    main()