# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    dictword = {}
    for i in secretWord: # filling the dictword list of type dict with all unique letters in the secretword
        if i in dictword:
           dictword[i] += 1
        else:
            dictword[i] = 1
    count = 0
    for i in lettersGuessed:
        if i in dictword:
            count += 1
    if len(dictword.keys())<= count:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessdict = {}
    for i in secretWord:
        guessdict[i] = '_ '

    for i in lettersGuessed:
        if i in secretWord:
            guessdict[i] = i

    stringout = ""
    for key in secretWord:
        stringout += guessdict[key]

    return stringout

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = list(string.ascii_lowercase)
    for i in string.ascii_lowercase:
        if i in lettersGuessed:
            available.remove(i)
    return "".join(str(x) for x in available)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed = []
    charguess = ''
    charif = True

    print("Welcome to the game, Hangman!")
    #print('Secret is '+secretWord)
    print("I am thinking of a word that is "+ str(len(secretWord)) + " letters long.")

    while guesses>0:
        charif = True
        print('-----------')
        print("You have "+ str(guesses) +" guesses left.")
        print("Available letters: "+getAvailableLetters(lettersGuessed))

        while charif == True:
            charguess  = str(input("Please guess a letter: ",)).lower()
            if(len(charguess)>1):
                print("Only a single character, please")
            else:
                charif = False
                if charguess in lettersGuessed:
                    print('Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord,lettersGuessed))
                elif charguess not in lettersGuessed:
                    lettersGuessed.append(charguess)
                    if charguess in secretWord:
                        print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                    else:
                        print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                        guesses -= 1

        if isWordGuessed(secretWord,lettersGuessed) == True:
            print('-----------')
            print('Congratulations, you won!')
            break
    if guesses == 0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was '+secretWord+'.')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman('sea')
