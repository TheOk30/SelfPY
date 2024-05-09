def main():
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

    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)

    word = input("Please enter a word: ")
    hidden_word = "_ " * len(word)    
    print(word)
    print(hidden_word)
    letter = input("Please enter a letter: ")
    print(letter.lower())

if __name__ == "__main__":
    main()