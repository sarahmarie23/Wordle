# Wordle functions

from random import randrange
from string import *
import os

os.chdir("C:/Users/User/Desktop/CPH/CS 232 - Python/Wordle")
words_5_letters = "5letterwords.txt"
valid_words = "validwords.txt"



guesses = []
maxGuesses = 6
currentGuesses = 0
wordLength = 5
playAgain = False


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
    #randWord = wordlist[randrange(0, len(wordlist))]
    
    return wordlist[randrange(0, len(wordlist))]

secret_word = getWord()

# displayKeyboard: dict -> void
# purpose: takes in a dictionary of (char, color)
# and prints to the screen the corresponding
# keys in the correct colors.

def displayKeyboard():
    
    for k, v in keyboard.items():
        print(v, end =" ")
        if k in ['p', 'l']:
            print('\n')


# displayGrid: list -> void
# purpose: takes in a list of the words that
#     have been guessed (which is empty at the
#     beginning of a new game) and prints them
#     to the screen.

def displayGrid():
    for line in range(len(guesses)):
        print("         ", end = "")
        print(guesses[line])
    for i in range(0, maxGuesses-currentGuesses):
        emptyRow()
    

# storeGuesse: list -> null
# purpose: takes in the current guess in a list
#     that consists of lists of letters and 
#     colors and converts it into 3 strings
#     that will print nicely. The 3 strings
#     get added to the global guesses list.

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
# purpose: takes in the current guess and
#     returns true if it is the correct
#     guess, false otherwise.

def isCorrectGuess(currGuess):
    
    if currGuess == secret_word:
        gameWon = True
        return True
    else:
        return False


# def isGuessValid: string -> bool
# purpose: takes in the current guess and
#     returns true if it is valid, false
#     if it is not.

def isGuessValid(guess):
    # guess is valid if it is exactly
    # the length of wordLength, and it is
    # a valid word (it appears on the list
    # of valid words)

    if len(guess) is not wordLength:
        return "\n   Guess must be {} letters long!".format(wordLength)
    
    file = open(valid_words)
    checklist = file.read()
    if guess not in checklist:
        return "\n\tNot a valid word!"
    file.close()

    return True

def emptyRow():

    print("         +---+---+---+---+---+")
    print("         |   |   |   |   |   |")
    print("         +---+---+---+---+---+")

    


def analyzeGuess(guess):
    guess_list = [[char, "---+"] for char in guess]
    
    for i in range(0, len(guess)):
        if guess_list[i][0] is secret_word[i]:
            guess_list[i][1] = "###+"
            curr = (guess_list[i][0]).capitalize()
            keyboard[guess_list[i][0]] = "[{}]".format(curr)
            
        check_index = guess.find(secret_word[i])
        if check_index > -1 and guess_list[check_index][1] == "---+":
            guess_list[check_index][1] = "===+"
            
            curr = (guess_list[check_index][0]).capitalize()
            keyboard[guess_list[check_index][0]] = "[{}]".format(curr)

    for i in range(0, len(guess)):
        if guess_list[i][1] == "---+":
            keyboard[guess_list[i][0]] = "[ ]"
            
    storeGuesses(guess_list)


def gameOver():
    # display their stats (guess distribution, win percent)
    # ask if they want to play again
    # if so, activate playWordle()

    guesses.clear()
    currentGuesses = 0
    replay = input("\nPlay again? y/n ")
    if replay == "y":
        return True
    else:
        print("\nThanks for playing!")


def clearConsole():
    print("\n" * 45)  

def reset():
    currentGuesses = 0
    secret_word = getWord()
    keyboard = {'q':'[q]', 'w':'[w]', 'e':'[e]', 'r':'[r]', 't':'[t]',
            'y':'[y]', 'u':'[u]', 'i':'[i]', 'o':'[o]', 'p':'[p]',
            '2':'', 'a':'[a]', 's':'[s]', 'd':'[d]', 'f':'[f]',
            'g':'[g]','h':'[h]', 'j':'[j]', 'k':'[k]', 'l':'[l]',
            '3':'  ', 'z':'[z]', 'x':'[x]', 'c':'[c]', 'v':'[v]',
            'b':'[b]', 'n':'[n]','m':'[m]'}

