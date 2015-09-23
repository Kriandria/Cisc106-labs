# Dylan Leh

print('Problem 1')
# This code is here to display my name and college major
print('Dylan Leh')
print('Computer Engineering')



print()
print('Problem 2')
# The program requests a projected amount of sales, and displays annual
# profit at a rate of 23% the gross profit
projected_profit = float(input('Projected amount of total sales for the company ($): '))
annual_profit = projected_profit * 0.23
print("The projected annual profit is ${}".format(format(annual_profit, '.2f')))
#Also, sorry about the format, i know we havn't technically learned it in class yet
#But my first instinct was to use .format to make the dollar sign appear clearly



print()
print('Problem 3')
#Program that converts sqft to acres
sqft = float(input('Total sqaure feet of land (ft^2): '))
acres = format(sqft / 43560, '.6f')
print(sqft, "square feet is equivalent to", acres, "acres.")







print()
print('Problem 4')
#Asks for the prices of 5 items, adds them, calculates sales tax, sums
#the total of pre tax and tax, and displays all of calculated information
item1 = float(input('Price of the first item ($): '))
item2 = float(input('Price of the second item ($): '))
item3 = float(input('Price of the third item ($): '))
item4 = float(input('Price of the fourth item ($): '))
item5 = float(input('Price of the fifth item ($): '))

subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * 0.07
total = subtotal + sales_tax

subtotal = format(subtotal, '.2f')
print('The subtotal is $'+ subtotal)
sales_tax = format(sales_tax, '.2f')
print('The sales sax is $' + sales_tax)
total = format(total, '.2f')
print('The total is $'+ total)









print()
print('Problem 6')
# Program will determine subtotal, state sales tax, county sales tax, total sales tax,
# and the total of the sale
subtotal = float(input('Cost of current purchase ($): '))
sSalesTax = format(subtotal * 0.05, '.2f')
cSalesTax = format(subtotal * 0.025, '.2f')
tTotal = format(float(sSalesTax) + float(cSalesTax), '.2f')
total = format(float(subtotal) + float(tTotal), '.2f')

subtotal = format(subtotal, '.2f')

print('The subtotal of the purchase is ${}'.format(subtotal))
print('The state sales tax is ${}'.format(sSalesTax))
print('The county sales tax is ${}'.format(cSalesTax))
print('The total tax is ${}'.format(tTotal))
print('The total cost of the purchase is $' + total)










print()
print('Problem 8')
# Takes a given bill for a restaurant, and calculates sales tax and a recommended tip
# for said bill
subtotal = float(input('Cost of current meal ($): '))
tip = format(subtotal * 0.18, '.2f')
tax = format(subtotal * 0.07, '.2f')
total = format(float(subtotal) + float(tip) + float(tax), '.2f')

subtotal = str(format(subtotal, '.2f'))

print('The subtotal of the bill is ${}'.format(subtotal))
print('The recommended tip for this purchase is ${}'.format(tip))
print('The total tax for the bill is ${}'.format(tax))
print('The total cost of the bill is ${}'.format(total))









print()
print('Problem 10')
# Calculate total ingredients needed for speciied amount of cookies
sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48
cookies = int(input('How many cookies would you like to bake? :'))

sCalledFor = format(sugar * cookies, '.2f')
bCalledFor = format(butter * cookies, '.2f')
fCalledFor = format(flour * cookies, '.2f')

print('You will need {} cups of sugar, \
{} cups of butter, \
and {} cups of flour.'.format(sCalledFor,bCalledFor,fCalledFor))







print()
print('Problem 11')
# Calculates the male and female percentage makeup of a class of students
males = int(input('How many males are in the class? (Students): '))
females = int(input('How many females are in the class? (Students): '))
students = males + females

malesPer = format(males / students * 100, '.2f')
femalesPer = format(100.00 - float(malesPer), '.2f')

print('The percentage of males in the class is {}%.'.format(malesPer)) 
print('The percentage of females in the class is {}%.'.format(femalesPer)) 
