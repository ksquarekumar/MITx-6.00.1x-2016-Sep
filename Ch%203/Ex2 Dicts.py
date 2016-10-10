animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    num = 0
    keys = aDict.keys()
    for i in keys:
        num += len(aDict[i])
    return num

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    num = []
    keys = aDict.keys()
    newdict = {}
    for i in keys:
        num.append(len(aDict[i]))
        newdict[len(aDict[i])] = i
    return newdict[max(num)]

print(how_many(animals))
print(biggest(animals))