import wordle as w

# defineGlobals: int, int/string -> null
# purpose: keeps track of the game's settings
#     if the user changes the default

secretWord = "start"
global guesses
guesses = []
global maxGuesses
maxGuesses = 6

def defineGlobals(wordLen = 5, diff = 1):
    global wordLength
    wordLength = wordLen
    global difficulty
    difficulty = diff
    global maxGuesses
    maxGuesses = 6
    global secretWord
    secretWord = ""
    global guesses
    guesses = []
    global gameOver
    gameOver = False
    global numGuesses
    numGuesses = 0



def playWordle():

    
    while (len(guesses) < maxGuesses):
        curr_row = w.emptyRow()
        print(curr_row)
        guess = input("Guess a word: ")
        w.storeGuesses(guesses, guess)
        w.displayGrid(guesses, maxGuesses)
