def main():
    # Tracks if the user input is a pangram or not
    input_is_pangram = False

    with open("myPangrams.txt", "a") as user_pangrams:
        while True:
            # Convert to lower to account for all "case" cases :)
            user_string = input("Input a possible pangram [or Quit]: ").lower()
    
            if user_string == "quit":
                print("Bye!")
                break
            else:
                input_is_pangram = checkPangram(user_string)

                if input_is_pangram == True:
                    print("Hooray! It's a pangram!")
                    user_pangrams.write(f"{user_string}\n")
                else:
                    print("Oh no! Your input is not a pangram! Please try again!")
            

def checkPangram(input):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Will count the number of letters of the alphabet present in a line
    line_alphabet_count = 0

    # If each character is present in the input update the number of alphabet characters present
    for char in alphabet:
        if char in input:
            line_alphabet_count += 1

    if line_alphabet_count == 26:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
