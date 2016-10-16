'''
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
'''

'''
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
'''

'''
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
'''
'''
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
'''

'''
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
'''

'''
def fancy_divide(list_of_numbers, index):
   try:
       denom = list_of_numbers[index]
       return [simple_divide(item, denom) for item in list_of_numbers]
   except IndexError:
       fancy_divide(list_of_numbers, index-1)
'''

'''
def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0
'''

#print(fancy_divide([0, 2, 4], 5))

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')