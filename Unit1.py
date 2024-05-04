import random

tries = random.randint(5, 10)
print("Welcome to the game Hangman")
print(""" 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
""")

print(tries)

#picture 1:
print("""
    x-------x""")

#picture 2:
print("""
    x-------x
    |
    |
    |
    |
    |""")

#picture 3:
print("""
    x-------x
    |       |
    |       O
    |
    |
    |""")

#picture 4:
print("""
    x-------x
    |       |
    |       0
    |       |
    |
    |""")

#picture 5:
print("""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")

#picture 6:

print("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")

#picture 7:

print("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
