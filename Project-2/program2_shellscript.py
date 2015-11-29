Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
-----------------------------------------------------------------
Welcome to the CISC106 Database Processing Program. This program 
allows you to interact with simple database about students.
-----------------------------------------------------------------

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: z
'z' is not a valid menu option, please enter a valid choice.

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: d
Error: 'd' cannot be performed before the read and merge operation has been performed

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: i
Error: 'i' cannot be performed before the read and merge operation has been performed

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: r
Enter the name of the first file you want to merge: sample-r1.txt
Enter the name of the second file you want to merge: sample-r2.txt
Files sample-r1.txt and sample-r2.txt have been read and merged.

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: r
Error: 'r' has already been performed and cannot perform again.

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: p
['Bud', 'Abbott', 21, 92.3]
['Don', 'Adams', 21, 90.4]
['Mary', 'Boyd', 22, 91.4]
['Jill', 'Carney', 23, 76.3]
['Hillary', 'Clinton', 20, 82.1]
['Diane', 'Keaton', 20, 61.1]
['Randy', 'Newman', 20, 41.2]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: i
Enter information for the new database record:
First name: Amy
Last name: Adams
insertFunction: error - Last name 'Adams' already exists.

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: i
Enter information for the new database record:
First name: Amy
Last name: Adam
Enter section: 12
insertFunction: error - Invalid section; must be between 20 & 23

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: i
Enter information for the new database record:
First name: Amy
Last name: Adam
Enter section: 22
Enter grade: 12345
insertFunction: error - Invalid grade; must be between 0 & 100

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: f
Enter the last of name the record you are trying to find: Adams
The following record was found in the database
  ['Don', 'Adams', 21, 90.4]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: d
Enter the last name attached to the file you want to remove: Adams
The following record was removed from the database
  ['Don', 'Adams', 21, 90.4]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: i
Enter information for the new database record:
First name: Amy
Last name: Adams
Enter section: 22
Enter grade: 82.7

The following record has been added to the database:
  ['Amy', 'Adams', 22, 82.7]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: q
Enter 'g' for grade query, 's' for section query: g
Enter grade threshold: 104.5
queryGrades: error - input out of range 0 - 100

There were no records with a great greater than or equal to 104.5.
Enter grade threshold: 84.4
The records with a grade greater than or equal to 84.4 are:
['Bud', 'Abbott', 21, 92.3]
['Mary', 'Boyd', 22, 91.4]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: q
Enter 'g' for grade query, 's' for section query: s
Enter the section number you want to query (20 - 23): 19
queryGrades: error - input out of range 20 - 23

There were no records with a section number of 19.
Enter the section number you want to query (20 - 23): 21
The records with a section number of 21 are:
['Bud', 'Abbott', 21, 92.3]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: p
['Bud', 'Abbott', 21, 92.3]
['Amy', 'Adams', 22, 82.7]
['Mary', 'Boyd', 22, 91.4]
['Jill', 'Carney', 23, 76.3]
['Hillary', 'Clinton', 20, 82.1]
['Diane', 'Keaton', 20, 61.1]
['Randy', 'Newman', 20, 41.2]

---------------MENU----------------
Database operations:
  (d) delete a record
  (e) exit the program
  (f) find a record
  (i) insert a record
  (p) print the database
  (q) query grades and section
  (r) read and merge
-----------------------------------
Enter Your Choice: e

Thank you for using the CISC106 Database Processing program. Goodbye.

>>> 
