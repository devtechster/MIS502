# Variables can be: ints – integers or whole numbers,   #
#                   floats - real numbers with decimals #
#                   booleans - logical true/false, or
#                   strings 'Managing Data for Analytics' #
# Python will interpret a variable type when it is declared #
#    name = value    |   we will use print() and type() functions #
# Variable names do not contain spaces,
#   so use the underscore _ instead of spaces or no spaces (i.e., camelCase)#
#                                                  #
# ints, floats, booleans, strings #
# operations we can perform #

# ints - Integers #
number_of_friends = 10
print(number_of_friends)
print(type(number_of_friends))

number_of_friends = number_of_friends + 5
print(number_of_friends)
print(type(number_of_friends))

# floats - real numbers with decimals #

number_of_friends = 10
number_of_friends = number_of_friends + 5

paycheck = 845.23
print(type(paycheck))
print(paycheck)

paycheck = (paycheck / number_of_friends)
print(type(paycheck))
print(paycheck)

paycheck = (paycheck / number_of_friends)
print(type(paycheck))
print(paycheck)

paycheck = 845
print(type(paycheck))
print(paycheck)
# what happened to the paycheck variable?                   #
# paycheck was reassigned a whole number and became an ints #

# booleans - logical True or False #

number_of_friends = 10
number_of_friends = number_of_friends + 5
paycheck = 845.23
paycheck = 845

# boolen variables can be directly assigned True or False #
isWindowOpen = False
# boolean variables can be assigned a comparison True of False #
isDoorClosed = 7 > 4

print(type(isWindowOpen))
print(isWindowOpen)
print(type(isDoorClosed))
print(isDoorClosed)

# strings or text -- characters all strung together in a variable #
# strings should be encased in '' or "", just end with what you start #
number_of_friends = 10
number_of_friends = number_of_friends + 5
paycheck = 845.23
paycheck = 845
isWindowOpen = False
isDoorClosed = 7 > 4

last_name = 'Ryan'           # all text like a last name, with the first character capitalized  #
passcode = "RyAN0884##"      # upper case, lower case characters, numbers, and extended characters #
curr_grade = ''              # empty string with no characters #
blanks = "     "             # string of five blanks spaces #
number = '15'                # string of numbers 15 | note:  number = '15' does not equal a value of 15  #

print(type(last_name))
print(last_name)
print(type(passcode))
print(passcode)
print(type(curr_grade))
print(curr_grade)
print(type(blanks))
print(blanks)
equality = (number == number_of_friends)
print(type(equality))
print(equality)

# Collections in Python:  tuples, lists, dictionaries        #

full_name = ('John', 'Doe')
inventory_item = ('pencil', 45)
roster_names = ['Hugang', 'George', 'Lucky', 'Jose', 'Renee']
roster_of_names = list(roster_names)

print(type(roster_names))
print(roster_names)

print(type(roster_of_names))
print(roster_of_names)

print(type(roster_of_names[2]))
print(roster_of_names[2])

# Collections in Python:  tuples, lists, dictionaries        #

full_name = ('John', 'Doe')
inventory_item = ('pencil', 45)
roster_names = ['Hugang', 'George', 'Lucky', 'Jose', 'Renee']
roster_of_names = list(roster_names)

cabinet_inventory = {'pencil':45, 'pencil colored':14, 'pen black': 10, 'pen blue': 15, 'pen red': 5}

print(type(cabinet_inventory))
print(cabinet_inventory)

print(type(cabinet_inventory['pencil']))
print(cabinet_inventory['pencil'])

print("# of blue pens ",cabinet_inventory['pen blue'])
print("# of pens ", cabinet_inventory['pen red'] + cabinet_inventory['pen black'] + cabinet_inventory['pen blue'])

# Collections in Python:  tuples, lists, dictionaries        #
full_name = ('John', 'Doe')
roster_names = ['Hugang', 'George', 'Lucky', 'Jose', 'Renee']
customer1 = full_name
full_name = ('Alice','Smith')
customer2 = full_name
customers = customer1 + customer2
removed_value1 = roster_names[3]
removed_value2 = roster_names[4]
roster_names.append(customer1[0])
roster_names.append(customer2[0])
del roster_names[3]
roster_names.append('Doug')
roster_names.pop(3)
roster_names.append('Peiwei')
roster_of_names = list(roster_names)
roster_names.append(customer1[0])
roster_names.append(customer2[0])
print('length = ', len(roster_names), '; min = ', min(roster_names), '; max = ', max(roster_names))
print(roster_names)
print('removed values ', removed_value1, ', ', removed_value2)

# Collections in Python:  tuples, lists, dictionaries        #
cabinet_inventory = {'pencil':45, 'pencil colored':14, 'pen black': 10, 'pen blue': 15, 'pen red': 5}
print(cabinet_inventory.keys())
print(cabinet_inventory.values())
print(cabinet_inventory.items())
cabinet_inventory['pencil colored'] = 25
print("# black pens ",cabinet_inventory['pen black'], '; # blue pens = ', cabinet_inventory['pen blue'])
print("# of pens ", cabinet_inventory['pen red'] + cabinet_inventory['pen black'] + cabinet_inventory['pen blue'])
print('min inventory quantity = ', min(cabinet_inventory.values()))
print('# of inventory quantities = ', len(cabinet_inventory.values()), '; max inventory quantity = ', max(cabinet_inventory.values()))
print(cabinet_inventory.items())
green_pens = {'pen green': 5}
cabinet_inventory.update(green_pens)
del cabinet_inventory['pencil colored']
print(cabinet_inventory.items())
cabinet_inventory.clear()
print(cabinet_inventory.items())

# Control flow:       if condition to test:                                         #
# if statements             code to execute if test is true                         #
#                     elif  condition to test:                                      #
#                           code to execute if elif test is true                    #
#                     else:                                                         #
#                           code to execute if elif is false                        #
expense_budget = 1000.00
expense_item_cost = 200.00
isExpenseSpendingAllowed = True

if expense_item_cost <= expense_budget and isExpenseSpendingAllowed == True:
       expense_budget -= expense_item_cost
       print(expense_item_cost, ' charged against your expense budget.')
       print('Remaining expense budget = ', expense_budget)
elif   isExpenseSpendingAllowed == False:
       print('Currently, expense spending is not approved')
else:
       print('Your expense budget balance ', expense_budget, ' is less than the expense item cost ', expense_item_cost)



# Control flow:       while condition:                                         #
# while loops               execute code while condition is true               #
expense_budget = 1000.00
expense_item_cost = 200.00
isExpenseSpendingAllowed = True
total = 0
index = 1
while index < 10:
    total += 1
    index += 1
    print('total = ', total)
    print('index = ', index)
    if expense_budget > 0 and expense_budget >= expense_item_cost and isExpenseSpendingAllowed == True:
       expense_budget -= expense_item_cost
       print(expense_item_cost, ' charged against your expense budget.')
       print('Remaining expense budget = ', expense_budget)
    elif   isExpenseSpendingAllowed == False:
       print('Currently, expense spending is not approved')
       break
    else:
       print('Your expense budget balance ', expense_budget, ' is less than the expense item cost ', expense_item_cost)
       break


