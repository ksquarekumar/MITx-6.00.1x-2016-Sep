# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = random.randint(7,13)

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    getword = word.lower() #copy and convert input to lower case
    points = SCRABBLE_LETTER_VALUES  #copy scrabble score table
    tally = 0
    for each in getword:
        tally += points[each]
    tally *= len(getword)
    if len(getword) == n:
        tally += 50

    return tally


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
   # >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    newhand = hand.copy()
    for each in word.lower():
            newhand[each] -= 1
            assert (newhand[each] >= 0), "Index out of range!"
    return newhand



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0                                                            # to count missing instances of letters in hand
    newhand = hand.copy()                                                # no mutation
    #print('Looking for: '+word+' in '+str(newhand))                     # testing
    for each in word.lower():
        if newhand.get(each,0) <= 0:
            count += 1
            #print(each+' not found')                                   # testing
            #print(str(count)+' << count')                              # testing
        elif newhand.get(each,0) >= 1:
            newhand[each] -= 1
            #print(each + ' found ')                                    # testing
            #print('count of '+each+' is '+str(newhand[each]))          # testing


    if word == '' or word == ' ':
        return False
    elif word in wordList:
        if count == 0:
            return True
        elif count > 0:
            return False
    else:
        return False                                                    # word doesnt exist in wordlist

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for each in hand.keys():
            count += hand[each]
    return count



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    score = 0
    tempscore = 0
    handy = hand.copy()
    control = True
    size = 0
    printflag = 0
    while control:
        size = 0
        print('Current Hand: ',end="")
        displayHand(handy)
        userinput = str(input('Enter word, or a "." to indicate that you are finished: ',))
        if userinput == ".":
            control = False
        else:
            if isValidWord(userinput,handy,wordList) == False:
                print('Invalid word, please try again.')
                print()                                                             #empty line
            elif isValidWord(userinput,handy,wordList) == True:
                tempscore = getWordScore(userinput, n)
                print('\"'+userinput+'\" earned '+str(tempscore)+' points.',end=" ")     #remains on same line
                score += tempscore
                print('Total: '+str(score)+' points')
                print()                                                             #empty line
                handy = updateHand(handy, userinput)
                for each in handy:
                    size += handy[each]
                if size == 0:
                    print('Run out of letters. Total score: ' + str(score) + ' points')
                    control = False
                    printflag = 1
            else:
                print('wtf, this is not supposed to happen!')


    if printflag == 0:
        print('Goodbye! Total score: '+str(score)+' points')



#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    #print("playGame not yet implemented.") # <-- Remove this line when you code the function
    hand = {}
    control = True
    runs = 0
    while control:
        gamecondition = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ',))
        if gamecondition == 'e':
            control = False
        elif gamecondition == 'r':
            if runs == 0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand,wordList, HAND_SIZE)
        elif gamecondition == 'n':
            hand = dealHand(HAND_SIZE)
            runs += 1
            playHand(hand, wordList, HAND_SIZE)
        else:
            print('Invalid command.')



   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

#wordList = loadWords()
#print(isValidWord('kwijibo',{'w': 1, 'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1},wordList))
#playHand({'a': 2, 'e': 1, 'p': 2, 'r': 1, 'z': 1}, wordList, 7)