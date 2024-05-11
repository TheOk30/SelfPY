def check_valid_input(letter_guessed, old_letters_guessed):
    # This function checks if the input is valid.
    # It returns True if the input is valid, and False otherwise.

    # Checking if the entered letter matches a pattern
    return len(letter_guessed ) == 1 and letter_guessed.islower()  and letter_guessed in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # The function tries to update the letter_guessed list.

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)  # Adding the letter to the list of guessed letters
        return True
    
    print("X")
    print(" -> ".join(old_letters_guessed))  # Printing the list of guessed letters
    return False

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
