#Sada Mehari Dylan Leh
from random import randint
Addition = 'a'
Subtraction = 's'
Multiplication = 'm'
Division = 'd'
Exponentiation = 'e'
Random = 'r'
Quit = 'q'

x1 = 0   #global variables that keep track of when the correct answer is given
x2 = 0
x3 = 0
x4 = 0
y = 0

def main():
    choice = 0

    while choice != Quit:
        display_menu()
        choice = str(input('Enter Your Choice:'))

        if choice == Subtraction:
            print('Subtraction')
            print()
            subtraction()
        elif choice == Addition:
            print('Addition')
            print()
            addition()
        elif choice == Multiplication:
            print('Multiplication')
            print()
            multiplication()
        elif choice == Division:
            print('Division')
            print()
            division()
        elif choice == Exponentiation:
            print('Exponentiation')
            print()
            exponentiation()
        elif choice == Random:
            print('Random')
            print()
            randomFunction()
        elif choice == Quit:
            print('Thank you for using the CISC106 Basic Math Instructor \
program. Goodbye.')
            
        else:
            print('Error: Invalid selection, please enter a valid choice.’')

def addition():
    '''
    Add two random numbers together
    Variables:
        runs: Counts te number of problems that the program has sent the student
        complete: Boolean that determines when to move to the next question
        tries: Counts number of attemps on a problem
        x: First random number
        y: Second random number
    '''
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        x = randint(0,20)
        y = randint(0,20)
        while not(complete):
            answer = x + y
            response = int(input('What is {} + {}?: '.format(x, y)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
                tallyUp(tries)
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    tallyUp(tries)
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
        print()
                    
                
def subtraction():
    '''
    Subtracts a random number from another number, always keeping
        the value positive (+)
    Variables:
        runs: Counts te number of problems that the program has sent the student
        complete: Boolean that determines when to move to the next question
        tries: Counts number of attemps on a problem
        x: First random number
        y: Second random number
    '''
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        x = randint(0,20)
        y = randint(0,20)
        if y > x: # Code that guaruntees the first number will be greater than
            temp = x # The second number
            x = y
            y = temp
        while not(complete):
            answer = x - y
            response = int(input('What is {} - {}?: '.format(x, y)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
                tallyUp(tries)
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    tallyUp(tries)
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
        print()


def multiplication():
    '''
    Multiplies two random numbers together
    Variables:
        runs: Counts te number of problems that the program has sent the student
        complete: Boolean that determines when to move to the next question
        tries: Counts number of attemps on a problem
        x: First random number
        y: Second random number
    '''
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        x = randint(0,15)
        y = randint(0,15)
        while not(complete):
            answer = x * y
            response = int(input('What is {} * {}?: '.format(x, y)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
                tallyUp(tries)
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    tallyUp(tries)
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
        print()

def division():
    '''
 Divides to numbers from each other, guaruntees a whole number answer
    Variables:
        runs: Counts te number of problems that the program has sent the student
        complete: Boolean that determines when to move to the next question
        tries: Counts number of attemps on a problem
        quotient: First random number
        divisor: Second random number
    '''
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        quotient = randint(0,15)
        divisor = randint(1,15)
        while quotient % divisor != 0:  # Keeps finding a new divisor until the
            divisor = randint(1,15) # answer output is a whole number
        while not(complete):
            answer = quotient / divisor
            response = int(input('What is {} / {}?: '.format(quotient, divisor)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
                tallyUp(tries)
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    tallyUp(tries)
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
        print()

def exponentiation():
    '''
Exponentiates two numbers together, garunteeing an answer less than 2500
    Variables:
        runs: Counts te number of problems that the program has sent the student
        complete: Boolean that determines when to move to the next question
        tries: Counts number of attemps on a problem
        exponent: First random number
        base: Second random number
    '''
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        exponent = randint(0,12)
        base = randint(0,12)
        while base ** exponent > 2500: # Finds a new base until the base raised
            base = randint(0,12) # to the exponent is an answer less than 2500
        while not(complete):
            answer = base ** exponent
            response = int(input('What is {} ** {}?: '.format(base, exponent)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
                tallyUp(tries)
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    tallyUp(tries)
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
        print()

def randomFunction():
    '''
    Calls a random math function for the user
    Variables:
        call: Determines the function to be called
    '''
    call = randint(1,5)
    if call == 1:
        addition()
    elif call == 2:
        subtraction()
    elif call == 3:
        multiplication()
    elif call == 4:
        division()
    elif call == 5:
        exponentiation()

def display_menu():
    '''
 Displays the menu for the user
    '''
    print('MENU')
    print('(a) Addition')
    print('(s) Subtraction')
    print('(m) Multiplication')
    print('(d) Division')
    print('(e) Exponentiation')
    print('(r) Random Type')
    print('(q) Quit')

def tallyUp(tries):
    '''
Determines number of questions answered, and on what tier they we answered
    correct, or if they were not answered correctly at all
    Parameters:
        tries: number of attempts on a problem
    '''
    if tries == 0:
        global x1
        x1 += 1
    elif tries == 1:
        global x2
        x2 +=1
    elif tries == 2:
        global x3
        x3 += 1
    elif tries == 3:
        global x4
        x4 += 1
        
    global y
    y += 1


main()

print('RESULTS: Of the {} questions given to you, you correctly answered \
{} on the first try, {} on the second try, and {} on the third try. \
You answered {} of the {} questions incorrectly.'.format(y,x1,x2,x3,x4,y))

