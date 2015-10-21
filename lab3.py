# Dylan Leh, Sada Mehari
# Problem 1
def count_mult3_ints(L):
    '''
    returns the number of ints in the list that are multiples of 3
    parameters:
        L - a list (list)
    variables:
        total - counter for the total number of ints that are multiples of 3 (number)
    returns:
        total
    '''
    total = 0
    for x in L:
        if type(x) == int and x%3 == 0:
            total += 1
    return total




# Problem 2
def sum_odd_ints(L):
    '''
    returns the sum of ints in the list that are odd
    parameters:
        L - a list (list)
    variables:
        odd_int_in_list - boolean that is true if there is an odd int in the
            list and false otherwise        (boolean)
        total - counter for sum of the odd integers (number)
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




# Problem 3
def insert_list(list1, string1):
    '''
    Adds a string into a sorted list such that the list remains sorted
    Parameters:
        list1 - a sorted list   (list)
        string1 - string to be inserted into list   (string)
    variables:
        index - tracks the current index while searching the list for various things    (number)
    Chance to return None
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




# Problem 4
def triangle_centroid(x1, y1, x2, y2, x3, y3):
    '''
    Determines the distance from the origin to the centroid of a circle
    Parameters:
        x1 - x coordinate of the first point of the triangle (number)
        y1 - y coordinate of the first point of the triangle (number)
        x2 - x coordinate of the second point of the triangle (number)
        y2 - y coordinate of the second point of the triangle (number)
        x3 - x coordinate of the third point of the triangle (number)
        y3 - y coordinate of the third point of the triangle (number)
    Variables
        stop - boolean that states if parameter testing fails or succeeds (boolean)
        Tx - x coordinate of the centroid of the triangle (number)
        Ty - y coordinate of the centroid of the triangle (number)
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



# Problem 5
def assert_within_tolerance(num1, num2, tolerance):
    '''
    Determines whether two given numbers are close in value of one-another
    Parameters:
        num1 - The first of the two given numbers   (number)
        num2 - the latter of the two given numbers  (number)
        tolerance - The tolerance of the two numbers (number)
    Returns:
        True - if the two numbers pass the tolerance test
        False - If the two numbers fail the tolerance test
        None - if function does not meet necessary parameters
    '''
    if type(num1) != float or type(num2) != float or type(tolerance) != float:
        print('assert_within_tolerance: error - arguments must all be defined as float')
        return None
    if tolerance < 0:
        print('assert_within_tolerance: error - parameter tolerance must be positive')
        return None

    if abs(num1 - num2) <= tolerance:
        return True
    else:
        return False



# Problem 6
def word_separator(string1):
    '''
    Converts a string sentence where all of the words are not separated by spaces and the first letter of each is
    capitalized to a regular sentence
    Parameters:
        string1 - The sentence to be converted (string)
    '''
    list1 = list(string1)
    index = -1
    if len(string1) > 1:
        while index < len(string1):
            index += 1
            if list1[index].isupper() and index != 0:
                list1[index] = list1[index].lower()
                list1.insert(index,' ')
                index += 1
    else:
        return string1.upper()

    return ''.join(list1)




# Problem 7
def word_parser(string1):
    list1 = list(string1)
    list2 = []
    list3 = []
    index = -1

    for x in list1:
        index += 1
        if list1[index] == ' ':
            if list1[index + 1] == ' ':
                list2.append(index)

    index = len(list1)
    for x in reversed(list1):
        index -= 1
        if index in list2:
            list1.pop(index)

    string2 = ''.join(list1)

    tmp = ''
    for c in string2:
        if c == ' ':
            list3.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        list3.append(tmp)

    if list3[0] == '':
        list3.pop(0)

    print(list3)



# Problem 8
def digit_product(string1):
    if type(string1) != str:
        print('digit_product: error - parameter must be defined as str')
        return None

    total = 1
    found = False
    list1 = list(string1)
    for x in list1:
        if x.isdigit():
            found = True
            total *= int(x)

    if (found):
        return total
    else:
        return None





# Problem 9
def valid_password(password):
    length = False
    uppercase = False
    lowercase = False
    numeric = False
    special = False
    invalid_digits = False

    if len(password) >= 8 and len(password) <= 15:
        length = True

    list1 = list(password)
    for x in list1:
        if x.isalpha():
            if x.isupper():
                uppercase = True
            elif x.islower():
                lowercase = True

        elif x.isdigit():
            numeric = True

        elif (x == '@' or x == '$' or x == '%' or x == '^' or x == '&' or
            x == '*' or x == '+' or x == '='):
            special = True

        else:
            invalid_digits = True

    if (length and uppercase and lowercase and numeric and
        special and not(invalid_digits)):
        return True
    else:
        return False
