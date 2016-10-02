import math as m        # builtin python math library, namespace is "m"

def polysum(n,s): #function definition for polysum function
    '''
    prints the sum of areas and the square of perimeter of a regular polygon. EDx CH 2 EX OPT "POLYSUM"
    https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2016/courseware/0de4fecc5a9a4749923133fcf4de181f/344d02eadf134621a1f17f473ef14514/
    :param n: the number of sides of the polygon, Integer ONLY
    :param s: the length of it's sides
    :return:
    '''
    return round(area(n,s)+(perimeter(n,s)**2),4) #returns the sums of the area and the square of perimeter, rounded to 4 digits

def area(n,s): #function definition for area calculator
    '''
    AREA CALCULATOR
    :param n: the number of sides of the polygon, Integer ONLY
    :param s: the length of it's sides
    :return: the area
    '''
    return ((0.25*int(n)*(s**2))/(m.tan(m.pi/int(n)))) #returns the area #unrounded
def perimeter(n,s):  #function definition for perimeter calculator
    '''
    PERIMETER CALCULATOR
    :param n: the number of sides of the polygon, Integer ONLY
    :param s: the length of it's sides
    :return: the perimeter
    '''
    return (int(n)*s) #returns the perimeter #unrounded

print(polysum(23,3) ) #testing