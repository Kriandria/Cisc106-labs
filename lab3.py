L = [1.0, '1', 1.0, 0, -21.0, '3', 18]
L2 = ['a','b','d']
L3 = ['aardvark']
L4 = []

def count_mult3_ints(L):
    '''
    returns the number of ints in the list that are multiples of 3
    parameters:
        L - a list
    variables:
        total - counter for the total number of ints that are multiples of 3
    returns:
        total
    '''
    total = 0
    for x in L:
        if type(x) == int and x%3 == 0:
            total += 1
    return total





def sum_odd_ints(L):
    '''
    returns the sum of ints in the list that are odd
    parameters:
        L - a list
    variables:
        odd_int_in_list - boolean that is true if there is an odd int in the
            list and false otherwise
        total - counter for sum of the odd integers
    returns:
        total
        None (if no odd integers can be found)
    '''
    total = 0
    odd_int_in_list = False
    for x in L:
        if type(x) == int and x%2 == 1:
            total += x
            odd_int_in_list = True
    if (odd_int_in_list):
        return total
    else:
        return None





def insert_list(list1, string1):        #doesnt work for empty list
    '''
Adds a string into a sorted list such that the list remains sorted
Parameters:
    list1 - a sorted list
    string1 - string to be inserted into list
variables:
    index - tracks the current index while searching the list for various things
    '''
    index = -1
    for x in list1:
        if type(x) != str:
            print('insert_list: error - list parameter contains more types \
than str')
            return None    
    for x in list1:
        index += 1
        if index != 0:
            if list1[index] < list1[index - 1]:
                print('insert_list: error - list parameter is not in increasing order')
                return None
    if type(string1) != str:
        print('insert_list: error - string parameter is not defined as str')
        return None

    index = -1
    for x in list1:
        index += 1
        if string1 <= list1[index]:
            list1.insert(index, string1)
            break
        elif string1 > list1[-1]:
            list1.append(string1)
            break
        
    if list1 == []:
        list1.append(string1)



def triangle_centroid(x1, y1, x2, y2, x3, y3):
    '''
Determines the distance from the origin to the centroid of a circle
Parameters:
    x1 - x coordinate of the first point of the triangle
    y1 - y coordinate of the first point of the triangle
    x2 - x coordinate of the second point of the triangle
    y2 - y coordinate of the second point of the triangle
    x3 - x coordinate of the third point of the triangle
    y3 - y coordinate of the third point of the triangle
    '''
    stop = False
    if type(x1) != int and type(x1) != float:
        stop = True
    elif type(y1) != int and type(y1) != float:
        stop = True
    elif type(x2) != int and type(x2) != float:
        stop = True
    elif type(y2) != int and type(y2) != float:
        stop = True
    elif type(x3) != int and type(x3) != float:
        stop = True
    elif type(y3) != int and type(y3) != float:
        stop = True

    if stop == True:
        print('triangle_centroid: error - arguments must all be numbers')
        return None

    Tx = (x1 + x2 + x3) / 3
    Ty = (y1 + y2 + y3) / 3

    return (Tx ** 2 + Ty ** 2)**(1/2)




def assert_within_tolerance(num1, num2, tolerance):
    stop = False
    

