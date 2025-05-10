# Functions, parameters, return values                                            #
# Syntax for Functions                                                            #
#                          def function_name(parameters):                         #
#                              function body, Python code to execute              #
#                              return statements                                  #
#                                                                                 #
# Functions only execute when called from within Python code                      #

# Example:  Creating a Function to move a player's position in a game             #

current_position = 5

def move_player():                           # Defines the function move_player                   #
    by_amount = 2                            # Establishes by_amount variable                     #
    global current_position                  # Makes current_position a global variable           #
    current_position += by_amount            # Increments player's current_position by by_amount  #

print('old position = ', current_position)   # print players' position                            #
move_player()                                # calls the function move_player()                   #
print('new position = ', current_position)   # print out player's new position                    #


# Example:  Adding a parameter to the move_player() function to move a player's position in a game by_amount #

current_position = 5
def move_player(by_amount):                  # Defines the function move_player with by_amount parameter        #
    'by_amount parameter moves player left to right'   # Function document string, docstring                    #
    global current_position                  # Makes current_position a global variable                         #
    current_position += by_amount            # Increments player's current_position by by_amount                #

print('old position = ', current_position)   # print players' position                                         #
move_player(2)                               # calls the function move_player() with parameter by_amount = 2   #
print('new position = ', current_position)   # print out player's new position                                 #
move_player(-5)                              # calls the function move_player() with parameter by_amount = -5  #
print('new position = ', current_position)   # print out player's new position                                 #

# Example:  Parameters in the move_player() function move a player's position by by_amount and return new_position #
current_position = 5

def move_player(current_position,by_amount):      # Defines function with current_position and by_amount parameters   #
    'by_amount moves player current_position left to right'   # Function document string, docstring                   #
    return current_position + by_amount           # Returns player's current_position incremented by by_amount        #

print('beginning position = ', current_position)  # print players' position                                           #
new_position = move_player(current_position, 2)   # returns new_position = current_position incremented by by_amount  #
print('new position = ', new_position)            # print out player's new position                                   #
new_position = move_player(new_position, -5)      # returns new_position = new_position incremented by by_amount = -5 #
print('new position = ', new_position)            # print out player's new position                                   #
print('distance player moved = ', new_position - current_position)   # print out distance player moved                #

# Functions, parameters, return values                                                                             #
# Functions only execute when called from within Python code                                                       #
# Syntax for Functions                                                                                             #
#                          def function_name(parameters):                                                          #
#                              function body, Python code to execute                                               #
#                              return statements                                                                   #
#                                                                                                                  #
# Example:  Parameters in the move_player() function move a player's position by by_amount and return new_position #
def print_player_position(current_position, by_amount):  # Defines function to print player's position #
    """print_play_position() prints the new position and player movement"""   # Function document string, docstring #
    global new_position, total_movement, movement
    total_movement = total_movement + abs(by_amount)  # calculates total movement in spaces left or right #
    print("player's position = ", current_position)
    print("player's new position = ", current_position + by_amount)
    print('distance player moved = ', by_amount)
    print('total distance player has moved = ', total_movement)
def move_player(current_position, by_amount):  # Defines function with current_position and by_amount parameters   #
    """by_amount moves player current_position left to right"""  # Function document string, docstring             #
    print_player_position(current_position, by_amount)
    return current_position + by_amount  # Returns player's current_position incremented by by_amount        #
current_position = 5
total_movement = 0
by_amount = 2
position = move_player(current_position, by_amount)  # returns current_position incremented by by_amount = 2 #
by_amount = -5
current_position = position
position = move_player(current_position, by_amount)  # returns current_position incremented by by_amount = -5 #
by_amount = 6
current_position = position
position = move_player(current_position, by_amount)  # returns current_position incremented by by_amount = 6   #
by_amount = -3
current_position = position
position = move_player(current_position, by_amount)  # returns current_position incremented by by_amount = -3  #


# Classes and Objects

class OurCustomer:
    # attributes - representations of the class stored in variables (e.g., strings, dictionaries, arrays, or objects) #
    name = ''
    email = ''
    sales = 0
    returns = 0
    # initializer - ways to create new instances of an object
    def __int__(self, name):
        self.name = name
        self.email = email
        self.sales = sales
        self.returns = returns
    # behaviour - methods as functions
    def add_email(self, new_email):
        self.email = new_email
    def bought_item(self, amount):
        self.sales += amount
    def return_item(self, ret_amount):
        self.returns += ret_amount
new_customer = OurCustomer()
new_customer.name = 'John Doe'
new_customer.add_email('jdoe@gmail.com')
new_customer.bought_item(145)
new_customer.return_item(0)
print(new_customer)
print('Our new customer is ', new_customer.name)
print("This customer's email is ", new_customer.email)
print('This customer has purchased items totaling $', new_customer.sales)
print('This customer has returned items totaling $', new_customer.returns)

