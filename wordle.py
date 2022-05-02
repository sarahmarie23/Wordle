# CS232 Spring 2022 Assignment #N
# Sarah Jimenez
# Last modified: May 2, 2022

# wordle.py contains all the functions that will be called
#     by play_wordle.py


from random import randrange
from string import *
import os

os.chdir("C:/Users/Sarah/Desktop/Wordle")
words_5_letters = "5letterwords.txt"
valid_words = "validwords.txt"

guesses = []        # stores all the ascii-decorated guess rows
maxGuesses = 6      # this could be changed for a different difficulty
currentGuesses = 0  # keeps track of how many guesses have been made
wordLength = 5      # future version could use different length words

keyboard = {'q':'[q]', 'w':'[w]', 'e':'[e]', 'r':'[r]', 't':'[t]',
            'y':'[y]', 'u':'[u]', 'i':'[i]', 'o':'[o]', 'p':'[p]',
            '2':'', 'a':'[a]', 's':'[s]', 'd':'[d]', 'f':'[f]',
            'g':'[g]','h':'[h]', 'j':'[j]', 'k':'[k]', 'l':'[l]',
            '3':'  ', 'z':'[z]', 'x':'[x]', 'c':'[c]', 'v':'[v]',
            'b':'[b]', 'n':'[n]','m':'[m]'}


# getWord: void -> void
# purpose: gets a random word from the list
#     of words (from a .txt file) and returns
#     it for gameplay.

def getWord():
    
    file = open(words_5_letters, "rt")
    line = file.read()
    wordlist = line.split()
    file.close()
    
    return wordlist[randrange(0, len(wordlist))]

secret_word = getWord()


# displayKeyboard: void -> void
# purpose: prints the keyboard dictionary to the
#     screen, in a manner that represents a
#     real keyboard.   

def displayKeyboard():
    
    for k, v in keyboard.items():
        print(v, end =" ")
        if k in ['p', 'l']:
            print('\n')


# displayGrid: void -> void
# purpose: prints the title and grid with
#     guesses, and prints empty rows if 
#     not all guesses have been made  

def displayGrid():
    
    print("                 Wordle")
    for line in range(len(guesses)):
        print("         ", end = "")
        print(guesses[line])
    for i in range(0, maxGuesses-currentGuesses):
        emptyRow()


# storeGuesse: list -> null
# purpose: takes in the guess_list, which holds
#     the current guess with the corresponding
#     borders, and puts it into strings that are     
#     appended to the guesses list, which makes
#     it easy to display.

def storeGuesses(guess_list):
    
    plus = ["+"]
    border = [text for pair in guess_list for text in pair if len(text) > 1 ]
    pb = plus + border
    borderFinal = "".join([str(text) for text in pb])

    word = [char for pair in guess_list for char in pair if len(char) == 1]
    wordStr = " | ".join([str(char) for char in word])
    wordFinal = "| " + wordStr + " |"
    
    guesses.append(borderFinal)
    guesses.append(wordFinal)
    guesses.append(borderFinal)


# isCorrectGuess: string -> bool
# purpose: takes in the current guess and returns true if
#     it is the correct guess, false otherwise.

def isCorrectGuess(currGuess):
    
    if currGuess == secret_word:
        gameWon = True
        return True
    else:
        return False


# isGuessValid: string -> string or bool
# purpose: takes in the current guess and returns true if
#     it is valid, or an error message if it is not.

def isGuessValid(guess):
    
    # guess is valid if it is exactly the length of wordLength,
    # and it is a valid word (it appears on the list of valid words)

    if len(guess) is not wordLength:
        return "\n   Guess must be {} letters long!".format(wordLength)
        
    file = open(valid_words)
    checklist = file.read()
    
    if guess not in checklist:
        return "\n\tNot a valid word!"
        
    file.close()

    return True


# emptyRow: void -> void
# purpose: prints to the screen a row of blank tiles

def emptyRow():

    print("         +---+---+---+---+---+")
    print("         |   |   |   |   |   |")
    print("         +---+---+---+---+---+")


# analyzeGuess: string -> void
# purpose: takes in the current guess, turns it into a list
#     that is added to the storeGuesses list, with info about
#     the color it gets. At the same time, the keyboard is
#     updated as each letter is checked.

def analyzeGuess(guess):
    
    guess_list = [[char, "---+"] for char in guess]

    # check for green letters
    
    for i in range(0, len(guess)):
        if guess_list[i][0] is secret_word[i]:
            guess_list[i][1] = "###+"
            
            curr = (guess_list[i][0]).capitalize()
            keyboard[guess_list[i][0]] = "[{}]".format(curr)

    # check for yellow letters
    
        else:      
            check_index = guess.find(secret_word[i])
            if check_index > -1 and guess_list[check_index][1] == "---+":
                guess_list[check_index][1] = "===+"
            
                curr = (guess_list[check_index][0]).capitalize()
                keyboard[guess_list[check_index][0]] = "[{}]".format(curr)

    # check for keys that need to go blank
    
    for i in range(0, len(guess)):
        if guess_list[i][1] == "---+":
            check = ''.join(i for i in keyboard[guess_list[i][0]] if i.isalpha())
            if check.islower():
                keyboard[guess_list[i][0]] = "[ ]"
            
    storeGuesses(guess_list)




        
# clearConsole: void -> void
# purpose: this is called each time to simulate clearning
#     the screen and displaying updated info.

def clearConsole():
    
    print("\n" * 45)


# showWindow: void -> void
# purpose: to make the code less cluttered on the playWordle.py
#     file, this function is called which in turn calls
#     other functions.

def showWindow():
    
    clearConsole()
    displayGrid()
    displayKeyboard()
    

#################################################
# Functions to be added for an upgraded version #
#################################################    

def gameOver():
    # display their stats (guess distribution, win percent)
    # ask if they want to play again
    # if so, activate playWordle()
    # needs to deal with resetting everything
    pass
    guesses.clear()
    currentGuesses = 0
    replay = input("Play again? y/n ")
    if replay == "y":
        playAgain = True
    else:
        print("Thanks for playing!")    
