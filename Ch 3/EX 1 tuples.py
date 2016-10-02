'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
where every other element of the input tuple is copied, starting with the first one.

So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

aTup = ("nnumon", 6, "2kki0", 3, 0, 11, 17, 8, 10) # -- for testing

def oddTuples(aTup):
    '''

    :param aTup: the tuple to split
    :return: the new tuple with even elements
    '''
    bTup = () # empty tuple to append to..
    for i in range(0,len(aTup)):
        if(i%2==0):
            bTup += tuple([(aTup[i])]) #can only concatenate tuple (not "str/int...") to tuple
    return bTup

print(oddTuples(aTup))