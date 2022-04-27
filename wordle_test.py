# wordle.py
# text-based wordle game
# Sarah Jimenez
# CS 232
# Final project


from random import randrange
from string import *
import os

from hangman_template import WORDLIST_FILENAME

os.chdir("C/Users/User/Desktop/CPH/CS 232 - Python/")

WORDLIST_FILENAME = "5letterwords.txt"

secret_word = "start"


def load_words():

    inFile = open(WORDLIST_FILENAME, "rt")
    line = inFile.readline()
    wordlist = line.split()

    return wordlist

list_of_words = load_words()

