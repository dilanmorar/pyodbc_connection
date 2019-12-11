import pyodbc
from db_connect_oop import *

class NWEmployees(MSDBConnection):

    def all_employees(self):
        query = 'select * from employees'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)

    def one_employee(self):
        employee_id = input('Input employee id: ')
        query = f"select * from employees where EmployeeID = '{employee_id}'"
        employee_id_info = self._MSDBConnection__sql_query(query)
        return employee_id_info

    def employee_search(self):
        employee_name = input('Insert employee name: ')
        query = f"select * from employees where FirstName = '%{employee_name}%' or LastName = '%{employee_name}%'"
        employee_name_info = self._MSDBConnection__sql_query(query)
        return employee_name_info
# search for one employee by first name or last name
