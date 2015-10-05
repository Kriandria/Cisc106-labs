#Sada Mehari Dylan Leh
from random import randint
Addition = 'a'
Subtraction = 's'
Multiplication = 'm'
Division = 'd'
Exponentiation = 'e'
Quit = 'q'

def main():
    choice = 0

    while choice != Quit:
        display_menu()
        choice = str(input('Enter Your Choice:'))

        if choice == Subtraction:
            print('Subtraction')
            subtraction()
        elif choice == Addition:
            print('Addition')
            addition()
        elif choice == Multiplication:
            print('Multiplication')
        elif choice == Division:
            print('Division')
        elif choice == Exponentiation:
            print('Exponentiation')
        elif choice == Quit:
            print('Quit')
        else:
            print('Error: Invalid selection, please enter a valid choice.’')

def addition():
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
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')
                
def subtraction():
    runs = 0
    while runs < 4:
        complete = False
        tries = 0
        x = randint(0,20)
        y = randint(0,20)
        if y > x:
            temp = x
            x = y
            y = temp
        while not(complete):
            answer = x - y
            response = int(input('What is {} - {}?: '.format(x, y)))
    
            if response == answer:
                print('That is correct!')
                runs += 1
                complete = True
            else:
                tries += 1
                if tries == 3:
                    runs += 1
                    complete = True
                    print('That is incorrect, the correct answer was',answer)
                else:
                    print('That is the incorrect answer. Please Try again.')


def display_menu():
    print('MENU')
    print('(a) Addition')
    print('(s) Subtraction')
    print('(m) Multiplication')
    print('(d) Division')
    print('(e) Exponentiation')
    print('(q) Quit')

main()



