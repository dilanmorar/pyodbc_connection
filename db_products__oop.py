import pyodbc
from db_connect_oop import *

class NWProducts(MSDBConnection):
    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def read_all(self):
        # build SQL query
        query = 'select * from products'
        # execute query
        data = self.__sql_query(query)
        # return an iteratable object
        return data

    def set_id(self):
        id = int(input('Insert product id: '))
        return id

    def read_one(self):
        id = self.set_id()
        query = f"select * from products where ProductID = {id}"
        id_info = self.__sql_query(query)
        return id_info

    def print_all(self):
        query = 'select * from products'
        data = self.__sql_query(query)
        while True:
            return print(NWProducts().read_all().fetchone())

# read / list all
products = NWProducts().read_all()
print(products.fetchone())

# read one id
product = NWProducts().read_one()
print(product.fetchone())


# print all products using the while loop fetchone
product

    # ask for input --> front end -- input()
    # create one --> makes things persistent in db

    # update one

    # delete one
