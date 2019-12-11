import pyodbc

# these are our variables to connect
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# making the connection
docker_Northwind = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# making a cursor
cursor = docker_Northwind.cursor()

# execute some sql commands
cursor.execute("Select * from Customers where city like 'London'")

# fetching data executed from sql command and print
# cursor will maintain state
# row = cursor.fetchone()
# print(row)

# cursors maintaining state
# print(cursor.fetchone())
# print(cursor.fetchone())

# accessing specific data or column
    # use the column name as a attribute of the entry
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName, row.ContactName)

# fetchall method - bad practice
# all_rows = cursor.fetchall()
# print(all_rows)
# print(len(all_rows))
#
# for row in all_rows:
#     print(row.CompanyName)

# to get lots of data - use a while loop and fetchone at a time
rows = cursor.execute("select * from Products")

while True:
    record = cursor.fetchone()
    if record is None:
        break
    print(record.UnitPrice)