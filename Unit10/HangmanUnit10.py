from random import randint

def check_valid_input(letter_guessed, old_letters_guessed):
    # This function checks if the input is valid.
    # It returns True if the input is valid, and False otherwise.

    # Checking if the entered letter matches a pattern
    return len(letter_guessed ) == 1 and letter_guessed.islower()

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # The function tries to update the letter_guessed list.

    old_letters_guessed.append(letter_guessed)  # Adding the letter to the list of guessed letters
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True
    
    print("X")
      # Printing the list of guessed letters
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    # The function tries to update the hidden_word string.
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word.strip()

def check_win(secret_word, old_letters_guessed):
    # This function checks if the user has won the game.
    # It returns True if the user has won, and False otherwise.
    
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    # This function prints the Hangman ASCII art.

    HANGMAN_PHOTOS = {
        0:
        """
        x-------x""",

        1:
        """
        x-------x
        |
        |
        |
        |
        """,

        2:
        """
        x-------x
        |       |
        |       O
        |
        |
        """,

        3:
        """
        x-------x
        |       |
        |       0
        |       |
        |
        """,

        4:
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        """,

        5:
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        """,

        6:
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,

        7:
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """}
    
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path = "Unit10\words.txt", index=0):
    # This function returns a word from the file at the given index.

    with open(file_path, "r") as file:
        words = file.read().lower().split()
        words = list(dict.fromkeys(words)) # remove duplicates
        return words[index]
    
def main():
    
    # This function is the entry point of the Hangman game.
    # It displays the game's ASCII art, prompts the user for a word,
    # and allows the user to guess letters until they either win or lose.
    
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
    """

    MAX_TRIES = 6  # Maximum number of tries allowed in the game

    print(HANGMAN_ASCII_ART)  
    print("Max tries", MAX_TRIES)  

    file_name = input("Enter file path") #"Unit10\words.txt"
    index = int(input("Enter index"))
    word = choose_word(file_name, index)    # Prompting the user to enter a word
    num_of_tries = 1
    old_letters_guessed = []  # A list of letters that the user has guessed

    # play the game until win or until the user has lost
    while not check_win(word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        print_hangman(num_of_tries) # print the hangman
        print(" -> ".join(old_letters_guessed))  # Printing the list of guessed letters
        print(show_hidden_word(word, old_letters_guessed)) # Print the hidden word

        letter = input("\nPlease enter a letter: ").lower()  # Prompting the user to enter a letter
        while not try_update_letter_guessed(letter, old_letters_guessed):
            letter = input("Please enter a letter: ").lower()  # Prompting the user to enter a letter

        if letter not in word:
            num_of_tries += 1

    # Check if user has won the game
    if num_of_tries < MAX_TRIES:
        print(show_hidden_word(word, old_letters_guessed)) # print the original word
        print("You won!")
    else:
        print("You lost!") # if the user has lost the game


if __name__ == "__main__":
    main()  
