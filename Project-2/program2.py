# Dylan Leh (Working alone, don't dock points for missing partner's name)

Delete = 'd'        # lines 3-9: allows user input to access various functions
Find = 'f'
Insert = 'i'
Print = 'p'
Read = 'r'
Query = 'q'
Exit = 'e'
finalData = []      # list that holds the merged database after running 'r' function
FIRST = 0           # index nmber of each record that holds record's first name
LAST = 1            # index nmber of each record that holds record's last name
SECTION = 2         # index nmber of each record that holds record's section
GRADE = 3           # index nmber of each record that holds record's grade
rRun = False        # True if read function has been run, False otherwise

print('-----------------------------------------------------------------')
print('Welcome to the CISC106 Database Processing Program. This program ')
print('allows you to interact with simple database about students.')
print('-----------------------------------------------------------------')
def main():
    '''
    Drives the program to allow users to edit, search through, or view the
    different records in a database. The user picks which of the three functions
    they would like to run via a list of options.
    Variables:
        rRun - determines if the read and merge function has ran yet
        choice - user input that determines which function will run (string)
    '''
    choice = 0
    global rRun

    print()

    while choice != Exit:
        menu()
        choice = str(input('Enter Your Choice: '))

        if not(rRun):
            if choice == Read:
                readMerge()
                rRun = True
            elif choice == Exit:
                print('Thank you for using the CISC106 Database Processing \
program. Goodbye.')
            elif (choice == Delete or choice == Find or choice == Insert or
                  choice == Print or choice == Query):
                print('Error: \'{}\' cannot be performed before the read \
and merge operation has been performed'.format(choice))
            else:
                print('\'{}\' is not a valid menu option, \
please enter a valid choice.'.format(choice))

        else:

            if choice == Delete:
                deleteFunction()

            elif choice == Find:
                findFunction()

            elif choice == Insert:
                insertFunction()

            elif choice == Print:
                printFunction()

            elif choice == Read:
                print("Error: 'r' has already been performed and cannot perform again.")

            elif choice == Query:
                queryGrades()

            elif choice == Exit:
                print()
                print('Thank you for using the CISC106 Database Processing \
program. Goodbye.')

            else:
                print('\'{}\' is not a valid menu option, \
please enter a valid choice.'.format(choice))

        print()




def deleteFunction():
    '''
    Allows the user to delete a record from the database
    Variables:
        finalData - global, the database that holds the records (list)
        LAST - global, placeholder variable that leads to the last name stored in
            each record of the database (int)
        found - Keeps track if a file was found in the database (boolean)
        counter - counter for how many times the loop has run (int)
    '''
    name = str(input('Enter the last name attached to the file you want to remove: '))

    global LAST
    found = False
    counter = -1

    for x in finalData:
        counter += 1
        if name == finalData[counter][LAST]:
            found = True
            print('The following record was removed from the database')
            print(' ', finalData[counter])
            finalData.pop(counter)

    if found == False:
        print('deleteFunction: error - Last name not found in database.')




def findFunction():
    '''
    Allows the user to scan the database records for a last name, then displays the
        record when it is found
    Variables:
        name - variable that holds the last name that is to be searched for in the
            database (string)
        finalData - global, the database that holds the records (list)
        LAST - global, placeholder variable that leads to the last name stored in
            each record of the database (int)
        found - Keeps track if a file was found in the database (boolean)
        counter - counter for how many times the loop has run (int)
    '''
    global LAST
    counter = -1
    found = False

    name = str(input('Enter the last of name the record you are trying to find: '))
    for x in finalData:
        counter += 1
        if name == finalData[counter][LAST]:
            print('The following record was found in the database')
            print(' ', x)
            found = True

    if not(found):
        print('findFunction: error - record not found')





def insertFunction():
    '''
    Allows the user to insert a new record into the database. Does not proceed if given
        data is invalid. Inserts record so that the database remains sorted by last name
    Variables:
        finalData - global, the database that holds the records (list)
        LAST - global, placeholder variable that leads to the last name stored in
            each record of the database (int)
        found - Keeps track if a file was found in the database (boolean)
        counter - counter for how many times the loop has run (int)
        record - list that holds the contents of the record to be inserted (list)
        first - user input that holds the new record's first name (string)
        last - user input that holds the new record's last name (string)
        section - user input that holds the new record's section (int)
        grade - user input that holds the new record's grade (float)
    '''
    found = False
    record = []
    counter = -1
    global LAST

    print('Enter information for the new database record:')
    first = str(input('First name: '))

    while not(found):
        last = str(input('Last name: '))

        for x in finalData:
            counter += 1
            if last == finalData[counter][LAST]:
                print('insertFunction: error - Last name \'{}\' already \
exists.'.format(last))
                return None
            elif counter == len(finalData) - 1:
                if last != finalData[counter][LAST]:
                    found = True

    found = False
    counter = -1

    while not(found):
        section = int(input('Enter section: '))

        for x in finalData:
            counter += 1
            if section < 20 or section > 23:
                print('insertFunction: error - Invalid section; must be between 20 & 23')
                return None
            elif counter == len(finalData) - 1:
                if section >= 20 and section <= 23:
                    found = True

    found = False
    counter = -1
    while not(found):
        grade = float(input('Enter grade: '))

        for x in finalData:
            counter += 1
            if grade < 0 or grade > 100:
                print('insertFunction: error - Invalid grade; must be between 0 & 100')
                return None
            elif counter == len(finalData) - 1:
                if grade >= 0 and grade <= 100:
                    found = True

    record.append(first)
    record.append(last)
    record.append(section)
    record.append(grade)

    counter = -1
    for x in finalData:
        counter+=1
        if finalData[counter][LAST] < last and finalData[counter + 1][LAST] > last:
            finalData.insert(counter + 1, record)
            break
    print()
    print('The following record has been added to the database:')
    print(' ', finalData[counter + 1])



def printFunction():
    '''
    Prints the entire database on separate lines for the user
    '''
    for x in finalData:
        print(x, sep = '\n')


def readMerge():
    '''
    Reads in two separate sorted databases and combines them into one sorted database
    Variables:
        finalData - the final list of data to be used throughout the program,
            manipulated by the programs other functions
        file1 - first file to be read into the prgram, merged with file2    (string)
        file2 - second file to be read into the program, merged with file1  (string)
        data1 - database made up of the data from file1, all string elements (list)
        data2 - database made up of the data from file2, all string elements (list)
        newdata1 - copy of data1, except string elements are converted to float and int
            where necessary (list)
        newdata2 - copy of data2, except string elements are converted to float and int
            where necessary (list)
        n1 - counter to determine current position of newdata1 when merging the lists
            (int)
        n2 - counter to determine current position of newdata2 when merging the lists
            (int)
    '''
    file1 = str(input('Enter the name of the first file you want to merge: '))
    file2 = str(input('Enter the name of the second file you want to merge: '))

    with open(file1, 'r') as f:
        data1 = f.readlines()

    with open(file2, 'r') as f:
        data2 = f.readlines()

    newdata1 = []
    newdata2 = []

    for x in data1:
        list1 = x.split(' ')
        list1[0] = str(list1[0])
        list1[1] = str(list1[1])
        list1[2] = int(list1[2])
        list1[3] = float(list1[3])
        newdata1.append(list1)

    for x in data2:
        list1 = x.split(' ')
        list1[0] = str(list1[0])
        list1[1] = str(list1[1])
        list1[2] = int(list1[2])
        list1[3] = float(list1[3])
        newdata2.append(list1)

    n1 = 0
    n2 = 0

    while n1 < len(newdata1) and n2 < len(newdata2):
        if newdata1[n1][1] >= newdata2[n2][1]:
            finalData.append(newdata2[n2])
            n2 += 1
        else:
            finalData.append(newdata1[n1])
            n1 += 1

    while n1 < len(newdata1):
        finalData.append(newdata1[n1])
        n1 += 1
    while n2 < len(newdata2):
        finalData.append(newdata2[n2])
        n2 += 1

    print('Files {} and {} have been read and merged.'.format(file1, file2))

def queryGrades():
    '''
    Allows the user to search a list and return all records with a specific value
        determined by the user
    Variables:
        firstLevel - Determines if the user enters correct input when asked for a choice
            of either 'g' or 's'    (bool)
        secondLevel - Determines if the user enters valid input when asked for either a
            integer value or a float value  (bool)
        SECTION - global, placeholder variable that leads to the section # stored in
            each record of the database (int)
        GRADE - global, placeholder variable that leads to the grade stored in
            each record of the database (int)
        counter - counter for how many times the loop has run (int)
        records - list that contains all records that fit the query criteria (list)
        found - Rings true if at least one record was found in the query, false
            otherwise (bool)
        query - user input to determine which type of query will be run (string)
        section - user input to determine what section to query by (int)
        grade - user input to determine which grade to query by (float)
    '''
    firstLevel = False
    secondLevel = False
    global SECTION
    global GRADE
    counter = -1
    records = []
    found = False

    while not(firstLevel):
        query = str(input('Enter \'g\' for grade query, \'s\' for section query: '))
        if query != 'g' and query != 's':
            print('queryGrades: error - invalid input (enter \'g\' or \'s\')')
            print()
        else:
            firstLevel = True



    if query == 's':
        while not(secondLevel):
            counter = -1

            section = int(input('Enter the section number you want to query \
(20 - 23): '))
            if section < 20 or section > 23:
                print('queryGrades: error - input out of range 20 - 23')
                print()
            else:
                secondLevel = True

            for x in finalData:
                counter += 1
                if finalData[counter][SECTION] == section:
                    found = True
                    records.append(counter)

            if found:
                print('The records with a section number of {} are:'.format(section))
            else:
                print('There were no records with a section number \
of {}.'.format(section))

    if query == 'g':
         while not(secondLevel):
            counter = -1

            grade = float(input('Enter grade threshold: '))
            if grade < 0 or grade > 100:
                print('queryGrades: error - input out of range 0 - 100')
                print()
            else:
                secondLevel = True

            for x in finalData:
                counter += 1
                if grade <= finalData[counter][GRADE]:
                    found = True
                    records.append(counter)

            if found:
                print('The records with a grade greater than or equal to {} \
are:'.format(grade))
            else:
                print('There were no records with a great greater than or \
equal to {}.'.format(grade))

    for x in records:
        print(finalData[x], sep='\n')



def menu():
        '''
     Displays the menu for the user
        '''
        print('---------------MENU----------------')
        print('Database operations:')
        print('  (d) delete a record')
        print('  (e) exit the program')
        print('  (f) find a record')
        print('  (i) insert a record')
        print('  (p) print the database')
        print('  (q) query grades and section')
        print('  (r) read and merge')
        print('-----------------------------------')


main()
