# Sada Mehari, Dylan Leh

from math import pi
from cisc106_34 import *

def calculate_grade(lab_score,test_score):
    '''
    Calculate a student's grade.
    Parameters:
      lab_score (number)
      test_score (number)
    Returns:
      grade (number)
    '''
    # calculate and return the grade
    grade = (lab_score + test_score) / 200
    return grade

assertEqual(calculate_grade(47.3, 122.5), 0.849)
assertEqual(calculate_grade(42.5, 142.7), 0.926)
assertEqual(round(calculate_grade(46.6, 131.5), 2), 0.89)

print()
print('Problem 1')
assertEqual(calculate_grade(48.6, 138.2), .934)
assertEqual(calculate_grade(44.2, 133.2), .887)
assertEqual(calculate_grade(49.2, 150), .996)

print ()
print('Problem 2')
# Calculate the area of a trapezoid
def calculate_trapezoid_area(base_1, base_2, height):
    '''
    Calculate the area of a trapezoid.
    Parameters:
        base_1(number)
        base_2 (number)
        height (number)
    Returns:
        area (number)
    '''
    area = (base_1 + base_2) * height / 2
    return area

assertEqual(calculate_trapezoid_area(1, 3, 2), 4)
assertEqual(calculate_trapezoid_area(32.0, 0.0, 4.0), 64.0)
assertEqual(round(calculate_trapezoid_area(0.14, 15.07,21.20), 2), 161.23)
assertEqual(calculate_trapezoid_area(6, 10, 19), 152)
assertEqual(calculate_trapezoid_area(22.0, 38.0, 4.0), 120.0)
assertEqual(round(calculate_trapezoid_area(0.18, 14.07,20.20), 2), 143.92)

print()
print('Problem 3')

def calculate_cylinder_volume(radius, height):
    '''
    Calculate the volume of a cylinder.
    Parameters:
      radius (number)
      height (number)
    Returns:
      volume (number)
    '''
    volume = pi * radius ** 2 * height
    return volume

assertEqual(round(calculate_cylinder_volume(5, 5), 3), 392.699)
assertEqual(round(calculate_cylinder_volume(13, 22), 2), 11680.44)
assertEqual(round(calculate_cylinder_volume(4.5, 9.2), 2), 585.28)

print()
print('Problem 4')

def make_string_strata(string1, string2):
    '''
    Creates a new string out of two given strings.
    Parameters:
      string1 (string)
      string2 (string)
    Returns:
      new_string (string)
    '''
    new_string = '{}|{}|{}'.format(string1,string2,string1)
    return new_string

assertEqual(make_string_strata("bbb","a"), "bbb|a|bbb")


print()
print('Problem 5')

def bill_amount(MB, base):
    '''
    Calculate a monthly data bill.
    Parameters:
      base (number)
      MB (number)
    Returns:
      bill (number)
    '''
    if MB <= 500 :
        bill = base
    elif MB > 500 and MB <= 2500 :
        bill = base * 1.25 + (MB-500) * .01
    elif MB > 2500 and MB <= 12500 :
        bill = (base * 3.75) + ((MB-2500) * .025)
    elif MB > 12500 :
        bill = 30 * base
    return bill

assertEqual(bill_amount(145, 10), 10)
assertEqual(round(bill_amount(920.8, 10.0), 2), 16.71)
assertEqual(round(bill_amount(8607, 10.0), 2), 190.18)
assertEqual(bill_amount(15025, 10), 300)
        
print()
print('Problem 6')

'''
    Convert seconds to days.
    Parameters:
        seconds (number)
'''

def time_calculator(seconds):
#86400 is the number of seconds in a day. if days (see below) comes out to 2.465
#then there are a total of 2 days with a remainder of 0.465. We will use the 465
#in calculating the number of hours, and the remainder in that to minutes,
#and so on.

    days = int(seconds / 86400)
    time_remaining_after_days = seconds % 86400
    
    hours = int(time_remaining_after_days / 3600) #3600 seconds in an hour
    time_remaining_after_hours = time_remaining_after_days % 3600
    
    minutes = int(time_remaining_after_hours/60) #60 seconds in a minute
    time_remaining_after_minutes = time_remaining_after_hours % 60
    
    print('{} seconds equals {} day(s), {} hour(s), {} minute(s), and {} \
second(s).'.format(seconds, days, hours, minutes, time_remaining_after_minutes))

number_of_seconds = int(input('How many seconds would you like to convert: '))
time_calculator(number_of_seconds)

print()
print('Problem 7')

'''
    Swaps the values of the 10th and hundredth placeholders of a number.
    Parameters:
        number (number)
'''

def swap_2_of_3(number):
    number_string = str(number) # converts the given number to string
    length = len(number_string) # determines the length of the string
    
    if length >= 3: # if there is a hundredth num., find it. else, make it
        hundred = number_string[-3]# [-3] finds the 3rd item from the end in a
    else:                           # list, or in this case, string/number
        hundred = '0'
        
    if length >= 2: # if there is a 10th num., find it. else, make it
        tens = number_string[-2]
    else:
        tens = '0'

    if length > 2:  #Saves all parts of number before the hundredth place value
        pre_swap = number_string[:(length - 3)]
    else:
        pre_swap = ''
                                            
    return int((pre_swap + tens + hundred + number_string[-1:]))
                                            # ^ the ones digit of the number
assertEqual(swap_2_of_3(326), 236)
assertEqual(swap_2_of_3(930), 390)
assertEqual(swap_2_of_3(20), 200)
assertEqual(swap_2_of_3(7), 7)
assertEqual(swap_2_of_3(500), 50)
assertEqual(swap_2_of_3(439), 349)
assertEqual(swap_2_of_3(218), 128)
assertEqual(swap_2_of_3(-326), -236)
assertEqual(swap_2_of_3(-543), -453)
print ()
print('Problem 8')


'''
    Determines if a loan should be approved for a person.
    Parameters:
      loan_amount (number)
      current_salary (number)
      current_cash (number)
      non_cash_assets (number)
      credit_score (number)
      last_name (string)
    Returns:
      mortgage_decision (string)
'''

    
def mortgage_approval(loan_amount, current_salary, current_cash, \
non_cash_assets, credit_score, last_name):
    mortgage_decision = ''
    
    if current_cash < loan_amount *.15:
        mortgage_decision = 'No'
    elif credit_score < 590:
        mortgage_decision = 'No'
    elif credit_score >= 590 and credit_score < 700:
            if current_cash <= loan_amount * .25:
                mortgage_decision = 'No'
            else:
                mortgage_decision = 'Maybe'
    elif current_salary < .333 * (loan_amount - current_cash):
         mortgage_decison = 'No'
    elif last_name == 'Doe' and non_cash_asset < 750000:
        mortgage_decision = 'No'
    elif current_cash < loan_amount:
        mortgage_decision = 'Maybe'
    else:
        mortgage_decision = 'Yes'

    return mortgage_decision

assertEqual(mortgage_approval(100, 200, 10, 500000, 500, 'Pie'), 'No')
assertEqual(mortgage_approval(2000, 1400, 2500, 900000, 580, 'Des'), 'No')
assertEqual(mortgage_approval(7000, 900, 5500, 450000, 650, 'Eye'), 'Maybe')
assertEqual(mortgage_approval(2000, 130, 1500, 30000, 600, 'Est'), 'Maybe')
assertEqual(mortgage_approval(9000, 8880, 1900, 740000, 630, 'Doe'), 'No')
assertEqual(mortgage_approval(1800, 3000, 1500, 500000, 720, 'Kan'), 'Maybe')
assertEqual(mortgage_approval(1100, 4400, 1900, 500000, 760, 'Elv'), 'Yes')
assertEqual(mortgage_approval(1000, 270, 250, 500000, 600, 'Lin'), 'No')
assertEqual(mortgage_approval(5000, 7000, 12000, 800000, 670, 'Ash'), 'Maybe')
