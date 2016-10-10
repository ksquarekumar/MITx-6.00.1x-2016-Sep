import random
import string

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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
        guessdict[i] = ' _ '

    for i in lettersGuessed:
        if i in secretWord:
            guessdict[i] = ' '+i+' '

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



print(getAvailableLetters(lettersGuessed))