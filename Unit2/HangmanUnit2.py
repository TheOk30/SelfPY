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

    letter = input("Please enter a letter: ")
    print(letter)

if __name__ == "__main__":
    main()