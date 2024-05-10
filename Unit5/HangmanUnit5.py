def is_valid_input(letter_guessed):
    # This function checks if the input is valid.
    # It returns True if the input is valid, and False otherwise.
    if len(letter_guessed ) == 1 and letter_guessed.islower():  # Checking if the entered letter matches a pattern
        print(True)  
    elif len(letter_guessed ) > 1 and letter_guessed.islower():
        print(False)   
    elif len(letter_guessed ) > 1 and not letter_guessed.islower():
        print(True)  
    elif len(letter_guessed ) == 1 and not letter_guessed.islower():
        print(False) 
    else:
        print(False) 


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
    print(MAX_TRIES)  

    word = input("Please enter a word: ").lower()  # Prompting the user to enter a word
    hidden_word = "_ " * len(word)  # Creating a hidden word with underscores
    print(word)  #
    print(hidden_word)  

    letter = input("Please enter a letter: ").lower()  # Prompting the user to enter a letter
    print(letter)
            



    if __name__ == "__main__":
        main()  # Calling the main function when the script is executed
