# sqlite import
import sqlite3
# establish connection to SQLite test.db
con = sqlite3.connect("HMIS.db")
# assign variable to con.cursor() function
cur = con.cursor()
# result of SQL script #1 execution iterated by row
for row in cur.execute(
    """
    SELECT Application || " --- " || Status AS App_Stat_Rural_MA, COUNT(*)
    FROM (
        SELECT Name, Application, Status, City, State, LENGTH(Name) AS name_length, UPPER(State) AS state_upper
        FROM (
            SELECT Name, Application, Status, City, State
            FROM LEADS
            WHERE State = "MA"
        )
        WHERE City NOT IN ("Boston", "Cambridge", "Lowell", "Springfield", "Worcester", "Newton")
        ORDER BY City, Name
    )
    GROUP BY App_Stat_Rural_MA, name_length, state_upper
    ORDER BY COUNT(*) DESC
    LIMIT 10;
"""
):
    # print SQL projection row by row with the 'for loop'
    print(row)
# close the database connection
con.close()
# using a user defined function to execute a SQL script
def exec_sql():
    # print the SQL script to execute
    print(SQL_script)
    # assign cur to the connection.cursor() function
    cur = con.cursor()
    # 'for loop' to  receive SQL projection by row
    for row in cur.execute(SQL_script):
        # print row by row of projection
        print(row)


# establishes connection to SQLite database (open db)
con = sqlite3.connect("HMIS.db")
SQL_script = print(
    """
SELECT Application || " --- " || Status AS App_Stat_Rural_MA, COUNT(*)
FROM ( SELECT Name, Application, Status, City, State, LENGTH(Name) AS name_length, UPPER(State) AS state_upper
        FROM ( SELECT Name, Application, Status, City, State FROM LEADS WHERE State = "MA" )
        WHERE City NOT IN ("Boston", "Cambridge", "Lowell", "Springfield", "Worcester", "Newton")
        ORDER BY City, Name )
GROUP BY App_Stat_Rural_MA, name_length, state_upper
ORDER BY COUNT(*) DESC
LIMIT 10;
""" )
# execute user defined function exec_sql() for SQL script
exec_sql()
con.close()
