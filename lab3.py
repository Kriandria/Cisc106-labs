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
assertEqual(count_mult3_ints([9, 12]), 2)
assertEqual(count_mult3_ints([9, 12, 16, 18, 24]), 3)
assertEqual(count_mult3_ints([3, 15, 7, 18, 27]), 4)
assertEqual(count_mult3_ints([9, 12, 7, 24, 39]), 4)
assertEqual(count_mult3_ints([15, 36, 23, 22, 27]), 8)
assertEqual(count_mult3_ints([12, 15, 7, 18, 27]), 5)




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
assertEqual(sum_odd_ints([9, 12, 7]), 16)
assertEqual(sum_odd_ints([9, 12]), 2)
assertEqual(sum_odd_ints([11, 15]), 26)
assertEqual(sum_odd_ints([2, 1, 7,]), 8)
assertEqual(sum_odd_ints([6, 3, 2, 8, 10]), 9)
assertEqual(sum_odd_ints([8, 12, 66, 58]), None)




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
assertEqual(insert_list(['a', 'b', 'c'], 'd'), ['a', 'b', 'c','d'])



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
assertEqual(triangle_centroid(0, 2, 3, 4, 6, 7), 5.27)
assertEqual(triangle_centroid('s', '2', 3, 4, 6, 7), None)
assertEqual(triangle_centroid(5, 8, 8, 12, 12.0, 8), 12.512216252748974 )
assertEqual(triangle_centroid(2, 2, 6, 4, 9, 2.0), 6.262764742685312)
assertEqual(triangle_centroid(0, '2', 3, 4, '6', 7), None)
assertEqual(triangle_centroid('1', 2, 3, 7, '12', 7), None)





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
assertEqual(assert_within_tolerance(0, 2, 3), None)
assertEqual(assert_within_tolerance(1.0, 2.0, -1.0), None)
assertEqual(assert_within_tolerance(6, 9, 2), None)
assertEqual(assert_within_tolerance(7.0, 12.0, 5.0), True)
assertEqual(assert_within_tolerance(19.0, 24.0, 3.0), False)
assertEqual(assert_within_tolerance(11.0, 19.0, 10.0), True)



# Problem 6
def word_separator(string1):
    '''
    Converts a string sentence where all of the words are not separated by spaces and the first letter of each is
    capitalized to a regular sentence
    Parameters:
        string1 - The sentence to be converted (string)
    Variables:
        list1 - a list made by splitting string1 into characters (list)
        index - a counter for the current index of the loop in the function (number)
    Returns:
        ''.join(list1) - combines the list into a single string and returns it (string)
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
assertEqual(word_separator('HelloBob'), 'Hello bob')
assertEqual(word_separator(''), '')
assertEqual(word_separator('LikeWater'), 'Like water')





# Problem 7
def word_parser(string1):
    '''
    Takes a sentence with any amount of whitespace between words and turns it into a list of words (without
    whitespace)
    Parameters:
        string1 - the sentence with whitespace to be separated (string)
    Variables:
        list1 - list made up of the characters of string1 (list)
        list2 - List of indicies to be removed from list1 (list)
        list3 - Final list to be retured, contains only words in list1 (list)
        index - a counter for the current index of the loop in the function (number)
        temp - temporary holder for a word lin list1    (string)
        string2 - string1 with only 1 whitespace between each word  (string)
    Returns:
        list3
    '''
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

    temp = ''
    for x in string2:
        if x == ' ':
            list3.append(tmp)
            tmp = ''
        else:
            temp += c
    if temp:
        list3.append(temp)

    if list3[0] == '':      # Removes any whitespace before the first word in list3
        list3.pop(0)

    print(list3)



# Problem 8
def digit_product(string1):
    '''
    Returns the product of every digit that occurs in the given string
    Parameters:
        string1 - the string that possibly contains digits for the programs output (string)
    Variables:
        total - keeps track of the product of the digits in string1 (number)
        found - boolean that states if there is a digit in the string   (boolean)
        list1 - list comprised of the characters of string1 (list)
    Returns:
        total
        None - if there are no digits in string1, or if string1 is not defined as a string
    '''
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
assertEqual(digit_product('Hi12'), 2)
assertEqual(digit_product('Hi6p5'), 30)
assertEqual(digit_product('Lo8o8'), 64)
assertEqual(digit_product(98), None)
assertEqual(digit_product(9), None)
assertEqual(digit_product(18), None)




# Problem 9
def valid_password(password):
    '''
    Determines if a given password meets a set of given criteria
    Parameters:
        password - the given password to check using the given criteria (string)
    Variables:
        length - True if password meets length requirements, false otherwise (boolean)
        uppercase - true if password contains an uppercase letter, false otherwise (boolean)
        lowercase - True if password contains a lowercase letter, false otherwise (boolean)
        numeric - True if password contains a number, false otherwise (boolean)
        special - True if password contains a special character from the given list, false otherwise (boolean)
        invalid_digits - True if there are any invalid digits found in the password, false otherwise (boolean)
        list1 - list of characters found in password
    Returns:
        True - If password meets all requirements
        False - If password does not meet all requirements
    '''
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
        if not(length):
            print('Password must be between 8 and 15 characters long')
        if not(uppercase):
            print('Password must contain at least one uppercase letter')
        if not(lowercase):
            print('Password must contain at least one lowercase letter')
        if not(numeric):
            print('Password must  contain at leaast one number')
        if not(special):
            print('Password must contain at least one of the following: @, $, %, ^, &, *, +, =')
        if invalid_digits:
            print('Password may only contain letters, numbers, and the following special \
            characters: @, $, %, ^, &, *, +, =')
        return False
assertEqual(valid_password('29374@Dp'), True)
assertEqual(valid_password('79304@Lo'), True)
assertEqual(valid_password('388494@mp'), False)
assertEqual(valid_password('097@Dp'), False)
assertEqual(valid_password('17283M45p'), False)
assertEqual(valid_password('98304$RB'), False)
