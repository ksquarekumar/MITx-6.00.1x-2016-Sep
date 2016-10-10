def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    temp = 1
    count = 0
    while abs(num-temp) > abs(num-temp*base):
        temp *= base
        count += 1
    return count

#print(closest_power(4,1))

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    comp = min (len(listA),len(listB))
    prod = 0
    for i in range (0,comp):
        prod += listA[i] * listB[i]
    return prod

#print(dotProduct([1,2,3],[4,5,6]))


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """

    def reverse(L):
        size = len(L)
        for i in range(0, size // 2):
            L[i], L[size - i - 1] = L[size - i - 1], L[i]
        return L

    L = reverse(L)
    element = []
    for i in range(0,len(L)):
        L[i] = reverse(L[i])
    print(L)


L = [[1, 2], [3, 4], [5, 6, 7]]
#deep_reverse(L)

#def f(a, b):
    #return a + b  -- ex7

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d1keys = set(d1.keys())
    d2keys = set(d2.keys())
    commonsets = d1keys.intersection(d2keys)
    uncomsets = d1keys.symmetric_difference(d2keys)

    listf = {}
    listnull = {}
    for keys in commonsets:
        listf[keys] = (f(d1[keys],d2[keys]))
    for keys in uncomsets:
        try:
            listnull[keys] = (d1[keys])
        except:
            listnull[keys] = (d2[keys])

    return (listf,listnull)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#print(dict_interdiff(d1, d2))


#ex 8

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here

    L2 = L[:]

    for e in L2:
        if g(f(e)) == False:
            L.remove(e)
    if(len(L)==0):
        return -1
    else:
        return max(L)

L = [0, -10, 5, 6, -4, -4]
print(applyF_filterG(L, f, g))
print(L)