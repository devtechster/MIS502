# Mining & Storing Data - reading and storing data - using sqlite3 package to access a SQL database#
import pandas as pd
import sqlite3
desired_width = 400                                        # variable for desired_width = 400
pd.set_option('display.width', desired_width)              # sets run screen width to 400
pd.set_option('display.max_columns', 20)                   # sets run screen column display to 20
pd.set_option('display.max_rows', 100)                     # sets run screen rows display to 100
#--------------------------------------------------------- # using sqlite3 package library to read a SQLite database
con = sqlite3.connect('test.db')                                   # establish connection to SQLite test.db
cur = con.cursor()                                                 # assign variable to con.cursor() function
for row in cur.execute('SELECT * FROM physician LIMIT 10;'):        # result of SQL script #1 execution iterated by row
    print(row)                                                     # print SQL projection row by row with the 'for loop'
print('                                      ')                    # line separator
for row in cur.execute('SELECT * FROM procedure LIMIT 10;'):        # result of SQL script #2 execution iterated by row
    print(row)                                                     # print SQL projection row by row with the 'for loop'
con.close()                                                        # close the database connection
#--------------------------------------------------------- # using a user defined function to execute a SQL script
def exec_sql():                                            # user defined function to execute a SQL script
    print('                             ')                 # separator line
    print(SQL_script)                                      # print the SQL script to execute
    cur = con.cursor()                                     # assign cur to the connection.cursor() function
    for row in cur.execute(SQL_script):                    # 'for loop' to  receive SQL projection by row
        print(row)                                         # print row by row of projection
con = sqlite3.connect('test.db')                           # establishes connection to SQLite database (open db)
SQL_script = 'SELECT * FROM physician lIMIT 10;'            # assign SQL_script variable to SQL script #1
exec_sql()                                                 # execute user defined function exec_sql() for SQL script #1
SQL_script = 'SELECT * FROM procedure LIMIT 10;'            # assign SQL_script variable to SQL script #2
exec_sql()                                                 # execute user defined function exec_sql() for SQL script #1
con.close()                                                # closes SQLite database connection

'''
# ------------------------------ # reading a SQL script projection to a Pandas df and then writing the df to a CSV file
con = sqlite3.connect('test.db')                           # establish connection to SQLite database test.db
df = pd.read_sql_query("SELECT * FROM physician", con)     # execute SQL script and load project into Pandas df
print(df.head(4))                                          # print top four rows of df
print(df.shape)                                            # print df rows & columns
con.close()                                                # closes SQLite database connection
df.to_csv('physicians.csv', index=False)                   # writes df to a CSV file named physicians.csv
# ---------------------------------------------------------# end of sqlite3 examples

# Mining & Storing Data - reading and storing data - reading a NumPy array from a CSV and saving the array to a CSV #
import pandas as pd
import numpy as np
desired_width = 400                                        # variable for desired_width = 400
pd.set_option('display.width', desired_width)              # sets run screen width to 400
pd.set_option('display.max_columns', 20)                   # sets run screen column display to 20
pd.set_option('display.max_rows', 100)                     # sets run screen rows display to 100
#------------------------------------------------------- # read a 6x6 array, square elements, write a 6x6 matrix to CSV
my_array = np.loadtxt('numpy_6x6_array.csv',delimiter=",",skiprows=1)  # read CSV file into a NumPy array
print(my_array, type(my_array))                            # print my_array & the variable type of my_array
print('                              ')                    # separator line
my_matrix = np.matrix(my_array**2)                         # square each my_array element and convert to NumPy matrix
print(my_matrix, type(my_matrix))                          # print my_matrix & the variable type of my_matrix
np.savetxt("my_matrix_6x6.csv", my_matrix, delimiter=",")  # write my_matrix as a CSV in the Python code subdirectory
# ------------------------------------------------------- # end of reading CSV into NumPy array | writing to a CSV file


# Mining & Storing Data - reading and storing data - reading chunks of a df from CSV; writing/appending to a CSV file #
import pandas as pd
import numpy as np
desired_width = 400                                        # variable for desired_width = 400
pd.set_option('display.width', desired_width)              # sets run screen width to 400
pd.set_option('display.max_columns', 20)                   # sets run screen column display to 20
pd.set_option('display.max_rows', 100)                     # sets run screen rows display to 100
# ------------------------------------------------ # read a 6x8594 array in chunks; write/ append to a CSV file
chunks = 2000                                             # declare chunks variable and assign value of 1000
eof = 8594                                                # end of CSV file is 8594
i = 0
if i <= eof:
    for chunk in pd.read_csv('numpy_6x8594_array.csv',skiprows=i,header=0,chunksize=chunks):  # read CSV file into chunk
        my_array = chunk.to_numpy(dtype=int)                      # convert chunk df to numpy array (integers)
        my_matrix = np.matrix(my_array**2)                        # square elements of my_array as a matrix
        print(my_array[0:5,:], type(my_array))                    # print my_array (5 rows) & the variable type
        print('                              ')                   # separator line
        print(my_matrix[0:5,:], type(my_matrix))                  # print my_matrix (5 rows) & the variable type
        if i < 1:                                                 # if statement to CSV write i = 0, else append i > 0
           np.savetxt('my_matrix_6x8594.csv', my_matrix, delimiter=',')  # write my_matrix_6x8954.csv as a CSV file
        else:
           csv_file = open('my_matrix_6x8594.csv', 'a')                  # create a open file variable for appending
           np.savetxt(csv_file, my_matrix)                               # append to my_matrix_6x8594 as a CSV file
           csv_file.close()
        i = i + chunks                                                     # increment counter
# ---------------------------------------------------------------- # end of reading/writing/appending CSV file

'''