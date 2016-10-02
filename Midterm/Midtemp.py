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

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    