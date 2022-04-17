# Wordle functions


# getWord: int -> string
# purpose: gets a random word from the list
#     of words (from a .txt file) and returns
#     it for gameplay.

def getWord(length):
    pass


# displayKeyboard: dict -> void
# purpose: takes in a dictionary of (char, color)
# and prints to the screen the corresponding
# keys in the correct colors.

def displayKeyboard(keys):
    pass


# displayGrid: list, int -> void
# purpose: takes in a list of the words that
#     have been guessed (which is empty at the
#     beginning of a new game) and prints them
#     to the screen.

def displayGrid(guesses, maxGuess):
    pass


# storeGuesse: list, string -> void
# purpose: takes in the current list of guesses
#     and the string of the current guess and
#     adds it to the list.

def storeGuesses(guesses, currGuess):
    guesses.append(currGuess)


# isCorrectGuess: string -> bool
# purpose: takes in the current guess and
#     returns true if it is the correct
#     guess, false otherwise.

def isCorrectGuess(currGuess):
    pass


# def isGuessValid: string -> bool
# purpose: takes in the current guess and
#     returns true if it is valid, false
#     if it is not.

def isGuessValid():
    # guess is valid if it is exactly
    # the length of wordLength, and it is
    # a valid word (it appears on the list
    # of valid words)
    pass


    
