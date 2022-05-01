import wordle as w



def playWordle():
    currentGuesses = 0
    secret_word = w.getWord()
    gameWon = False
    
    while (currentGuesses < 6 and not gameWon):
        
        guess = input("Guess a word: ")

        while(w.isGuessValid(guess) is not True):
            print(w.isGuessValid(guess))
            guess = input("Guess a word: ")

        w.clearConsole()
            
        w.analyzeGuess(guess)
        w.displayGrid()
        gameWon = w.isCorrectGuess(guess)

        currentGuesses +=1
        
        
    if gameWon:
        print("You win!")
    else:
        print("Sorry, the answer was: ", w.secret_word)

    w.gameOver()
    if w.playAgain:
        playWordle()
