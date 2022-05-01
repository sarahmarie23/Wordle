import wordle as w

# defineGlobals: int, int/string -> null
# purpose: keeps track of the game's settings
#     if the user changes the default

##secretWord = "panda"
##global guesses
##guesses = []
##global maxGuesses
##maxGuesses = 6
##
##def defineGlobals(wordLen = 5, diff = 1):
##    global wordLength
##    wordLength = wordLen
##    global difficulty
##    difficulty = diff
##    global maxGuesses
##    maxGuesses = 6
##    global secretWord
##    secretWord = ""
##    global guesses
##    guesses = []
##    global gameOver
##    gameOver = False
##    global numGuesses
##    numGuesses = 0



def playWordle():
    currentGuesses = 0
    w.guesses.clear()
    while (currentGuesses < 6):
        
        guess = input("Guess a word: ")

        while(w.isGuessValid(guess) is not True):
            print(w.isGuessValid(guess))
            guess = input("Guess a word: ")
            
        w.analyzeGuess(guess)
        w.displayGrid()
        
        if w.isCorrectGuess(guess):
            print("You win!")
            replay = input("Play again? y/n ")
            if replay is "y":
                playWordle()
            break
        currentGuesses +=1

    print("Sorry, the answer was: ", w.secretWord)
        
