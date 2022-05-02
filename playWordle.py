import wordle as w




def playWordle():

    currentGuesses = 0
    secret_word = w.getWord()
    gameWon = False
    
    while (w.currentGuesses < 6 and not gameWon):
        w.displayGrid()
        w.displayKeyboard()
        guess = input("\n\t   Guess a word: ")
        

        while(w.isGuessValid(guess) is not True):
            w.clearConsole()
            w.displayGrid()
            w.displayKeyboard()
            print(w.isGuessValid(guess))
            guess = input("\t   Guess a word: ")

        w.clearConsole()
            
        w.analyzeGuess(guess)
        #w.displayGrid()
        gameWon = w.isCorrectGuess(guess)

        w.currentGuesses +=1

    w.displayGrid()
    w.displayKeyboard()    
        
    if gameWon:
        print("\nYou win!")
    else:
        print("\nSorry, the answer was: ", w.secret_word)

    replay = w.gameOver()
    if replay:
        w.reset()
        playWordle()

    
    
    
