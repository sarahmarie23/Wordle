# CS232 Spring 2022 Assignment #N
# Sarah Jimenez
# Last modified: May 2, 2022


import wordle as w

# playWordle: upon running this file, the player
# types playWordle() to begin a round. The game
# plays for one round. A future version will include
# the option to replay as many times as the user chooses

def playWordle():
    
    gameWon = False
    
    while(w.currentGuesses < 6 and not gameWon):
        w.showWindow()
        guess = input("\n\t   Guess a word: ")

        while(w.isGuessValid(guess) is not True):
            w.showWindow()
            print(w.isGuessValid(guess))
            guess = input("\n\t   Guess a word: ")

        w.analyzeGuess(guess)
        gameWon = w.isCorrectGuess(guess)

        w.currentGuesses += 1

    w.showWindow()        
        
    if gameWon:
        print("\nYou win!")
    else:
        print("\nSorry, the answer was: ", w.secret_word)


