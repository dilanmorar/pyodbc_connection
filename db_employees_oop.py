import pyodbc
from db_connect_oop import *

class NWEmployees(MSDBConnection):
    def all_employees(self):
        query = 'select * from employees'
        data = self.MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)

# get all employees data

# get one employee by id

# search for one employee by first name or last name
