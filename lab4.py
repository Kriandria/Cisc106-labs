# Dylan Leh (Working alone, don't dock points for missing partner's name)
import hashlib
import base64
import matplotlib.pyplot as plt
from cisc106_34 import *




print('Problem 1')
def compute_md5_hash(passphrase):
    '''
    Take a string and encrypt it using an MD5 encryption
    Parameters:
        passphrase - the string to be encrypted (string)
    Variables:
        tmp - the holding spot for the string while it is being encrypted (hashlib.HASH)
    Returns:
        tmp.hexdigest - the final step in encrypting the string (string)
    '''
    tmp = hashlib.md5()
    tmp.update(bytes(passphrase, 'UTF-8'))
    return tmp.hexdigest()

assertEqual(compute_md5_hash('Porcupine'), '1af356d147244cdd18e7af284c4ff652')
assertEqual(compute_md5_hash('Elephant'),'f6cf83978d6a8e7ac57444bb38a540a7')
assertEqual(compute_md5_hash('What are words?'), '555131db548d2a4602be54a63504539d')





print()
print('Problem 2')
def convert_to_base64(uncoded_string):
    '''
    Take a string and encrypt it using an base64 encryption
    Parameters:
        uncoded_string - The string to be encrypted (string)
    Variables:
        coded_string - The encrypted version of the string in base64 (bytes)
    Returns:
        coded_string    (bytes)
    '''
    coded_string = bytes(uncoded_string, 'UTF-8')
    coded_string = base64.b64encode(coded_string)
    return coded_string

assertEqual(convert_to_base64('Porcupine'),b'UG9yY3VwaW5l')
assertEqual(convert_to_base64('Elephant'),b'RWxlcGhhbnQ=')
assertEqual(convert_to_base64('What are words?'),b'V2hhdCBhcmUgd29yZHM/')






print()
print('Problem 3')
def convert_from_base64(coded_string):
    '''
    Decode a string encrypted with base64
    Parameters:
        coded_string - the encrypted string to be decoded (bytes)
    Variables:
        decoded_string - The decoded version of the string(bytes)
    Returns:
        decoded_string - the string version of decoded_string variable (string)
    '''
    decoded_string = base64.b64decode(coded_string)
    return str(decoded_string.decode('UTF-8'))

assertEqual(convert_from_base64(b'UG9yY3VwaW5l'),'Porcupine')
assertEqual(convert_from_base64(b'RWxlcGhhbnQ='),'Elephant')
assertEqual(convert_from_base64(b'V2hhdCBhcmUgd29yZHM/'),'What are words?')





print()
print('Problem 4')
def quadratic_roots(a,b,c):
    '''
    Determine the roots from the quadratic equation determined by the users
        parameters
    Parameters:
        a - The 'a' from the quadratic equation (number)
        b - The 'b' from the quadratic equation (number)
        c - The 'c' from the quadratic equation (number)
    Variables:
        roots - list holding all of the valid roots from the quadratic equation (list)
        valid - Bool that is used to in parameter checking (boolean)
        answer1 - holds the first root of the quadratic equation, if it exists (string)
        answer2 - holds the second root of the quadratic equation, if it exists (string)
    Returns:
        roots   (list)
        None    (if parameter testing fails)
    '''
    roots = []
    valid = True            #parameter testing phase
    if type(a) != float and type(a) != int:
        valid = False
    elif type(b) != float and type(b) != int:
        valid = False
    elif type(c) != float and type(c) != int:
        valid = False
    if not(valid):
        print('quadratic_roots: error - all parameters must be defined as float or int')
        return None

    if b**2 - 4*a*c < 0:    #if the sqrt is negative
        return roots
    elif a == 0 and b == 0:
        return roots
    elif a == 0:
        answer1 = 'x - {}'.format(-c/b)
        roots.append(answer1)
        return roots
    else:
        answer1 = 'x - {}'.format((-b + (b**2 - 4*a*c)**0.5)/(2*a))
        answer2 = 'x - {}'.format((-b - (b**2 - 4*a*c)**0.5)/(2*a))

        roots.append(answer1)
        if answer1 != answer2:
            roots.append(answer2)
        return roots

assertEqual(quadratic_roots('1','2','3'), None)
assertEqual(quadratic_roots('4',0,0), None)
assertEqual(quadratic_roots(0,0,'3'), None)
assertEqual(quadratic_roots(0,0,3), [])
assertEqual(quadratic_roots(0,4,3), ['x - -0.75'])
assertEqual(quadratic_roots(3,-10,3), ['x - 3.0', 'x - 0.3333333333333333'])





print()
print('Problem 5')
def convert_10_to_16(decimal):
    '''
    Converts a decimal number of base 10 to its hexadecimal form
    Parameters:
        decimal - the decimal number to be converted to a hexadecimal (int)
    Variables:
        hexdec - list that holds all of the characters of the hexadecimal number (list)
        charList - list tht holds all of the possible hexadecimal letters (list)
        recall - new parameter for every recursion (int)
        hexChar - holds the value of the current hexadecimal character (int/string)
    Returns:
        ''.join(hexdec) - combines the hexdec list into the hexadecimal number (string)

    '''
    if type(decimal) != int:    #parameter testing phase
        print('convert_10_to_16: error - parameter must be defined as int')
        return None
    elif decimal < 0:
        print('convert_10_to_16: error - parameter must be positive')
        return None

    hexdec = []
    charList = ['A', 'B', 'C', 'D', 'E', 'F']
    if decimal != 0:
        recall = decimal // 16
        hexChar = decimal % 16
        if hexChar >= 10:       #number to letter conversion
            hexChar = charList[(hexChar - 10)]
        else:
            hexChar = str(hexChar)

        hexdec.insert(0,hexChar)
        hexdec.insert(0,convert_10_to_16(recall))

    return ''.join(hexdec)

assertEqual(convert_10_to_16('this is a string'), None)
assertEqual(convert_10_to_16('this is also a string'), None)
assertEqual(convert_10_to_16(-24), None)
assertEqual(convert_10_to_16(483), '1E3')
assertEqual(convert_10_to_16(255), 'FF')
assertEqual(convert_10_to_16(1997), '7CD')





print()
print('Probem 6')
def plot_chem_eng_101_grades(student_grades):
    '''
    Take a classes grades on an exam and plot them in a pie chart and in a histogram
    Parameters:
        student_grades - Contains the exam grades of all students in the class (list)
    Variables:
        A, B, C, D F - Contains the number of grades associated with each letter (int)
        slices - List containing the data for each slice of pie     (list)
        grade - Contains the title for each slice of pie            (list)
        colors - contains the color code for each slice of pie      (list)
        bins - sorting method for the data input into the histogram (list)
    '''
    for x in student_grades:
        if type(x) != float and type(x) != int:
            print('plot_chem_eng_101_grades: error - items in parameter must be \
            defined as a number')
            return False
        elif x > 100 or x < 0:
            print('plot_chem_eng_101_grades: error - items in parameter must fit \
            within the range [0, 100]')
            return False

    A = 0
    B = 0
    C = 0
    D = 0
    F = 0

    for x in student_grades:
        if x < 60:
            F += 1
        elif x < 70 and x >= 60:
            D += 1
        elif x < 80 and x >= 70:
            C += 1
        elif x < 90 and x >= 80:
            B += 1
        else:
            A += 1

    slices = [A,B,C,D,F]        #pie chart info
    grade = ['A\'s','B\'s', 'C\'s', 'D\'s', 'F\'s']
    colors = ['c', 'm', 'r', 'g', 'w']
    plt.title('Ratio of Letter Grades\nfor Exam')
    plt.pie(slices, labels=grade, colors=colors,
            autopct='%1.1f%%', startangle= 90)
    plt.show()

                    # histogram info
    bins = [0, 60, 70, 80, 90, 100]
    plt.xlabel('Letter Grades\n(F, D, C, B, A)')
    plt.ylabel('Number of Students')
    plt.title('Ratio of Letter Grades\nfor Exam')
    plt.hist(student_grades, bins, histtype='bar', rwidth=0.9)
    plt.show()

    return True


assertEqual(plot_chem_eng_101_grades([0,20,40,60, 70,80,90,100]),True)
assertEqual(plot_chem_eng_101_grades([0,20,40,60,80,90,110]),False)
assertEqual(plot_chem_eng_101_grades([0,-20, 25,40,60,80,90,100]),False)
assertEqual(plot_chem_eng_101_grades([0,20,'40',60,80,90,100]),False)







print()
print('Problem 7')
def weighted_filter(raw_data_filename, filtered_data_filename):
    '''
    Create new data that, when plotted, will be smoother than the original data
    Parameters:
        raw_data_filename - filename of the file contining the original data (string)
        filtered_data_filename - the filename of the file where the new data will be
            stored  (string)
    Variables:
        my_file - used to open the filtered_data_filename document
        line_count - total number of lines in the original document
        current_count - current line of the while loop while running through the
            original data
        data - a list that has all of the original data stored in it
        a - the first of the three numbers to be averaged for the new data
        b - the second of the three numbers to be averaged for the new data
        c - the third of the three numbers to be averaged for the new data
        solution - stores the new value to be input into the new document
    '''
    my_file = open(filtered_data_filename, 'w')
    line_count = 0
    current_line = 0
    with open(raw_data_filename, 'r') as f:
        data = f.readlines()        #store the data in a list

    with open(raw_data_filename, 'r') as f:
        for line in f:              # count the number of lines in the file
            line_count += 1

    while current_line < line_count - 2:
        current_line += 1
        a = float(data[current_line - 1].rstrip('\n'))
        b = float(data[current_line].rstrip('\n'))
        c = float(data[current_line + 1].rstrip('\n'))

        solution = str(format((a + 2*b + c) / 4, '.2f'))
        my_file.write(solution + '\n')

    my_file.close()

weighted_filter('lab4_raw_data.txt','lab4_filtered_data.txt')





print()
print('Problem 8')
def input_roster():
    '''
    Takes a file containing a list of names in lastname,firstname format and create a
        new file that contains the same list organized in firstname lastname format
    Variables:
        new_file - The new file to be created (TextIOWrapper)
        my_file - Specifies the file being read, holds the last_name,first_name
            format      (string)
        list1 - contains the separated last_name and first_name from my_file    (list)
        first_name - The first name of each object in list1 (string)
        last_name -  The last name of each object in list1  (string)
    '''
    new_file = open('roster_first_last.txt', 'w')
    my_file = str(input('Specify the file you want to open: '))

    with open(my_file) as f:
        for line in f:
            list1 = line.split(',')
            first_name = list1[1].rstrip('\n')
            last_name = list1[0]

            new_file.write(first_name + ' ' + last_name + '\n')

    new_file.close()

input_roster()
