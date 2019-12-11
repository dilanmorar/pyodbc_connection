import pyodbc
from db_connect_oop import *

class NWProducts(MSDBConnection):

    def read_all(self):
        # build SQL query
        query = 'select * from products'
        # execute query
        data = self._MSDBConnection__sql_query(query)
        # return an iteratable object
        return data

    def set_id(self):
        id = int(input('Insert product id: '))
        return id

    def read_one(self):
        id = self.set_id()
        query = f"select * from products where ProductID = {id}"
        id_info = self._MSDBConnection__sql_query(query)
        return id_info

    def print_all(self):
        query = 'select * from products'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def top_10_price(self):
        query = "select top 10 * from Products order by UnitPrice desc"
        top_10_data = self._MSDBConnection__sql_query(query)
        while True:
            record = top_10_data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def bottom_10_price(self):
        query = "select top 10 * from Products order by UnitPrice asc"
        bottom_10_data = self._MSDBConnection__sql_query(query)
        while True:
            record = bottom_10_data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def set_product_name(self):
        product_name = input('Insert product name: ')
        return product_name

    def search_product(self):
        product_name = self.set_product_name()
        query = f"select * from products where ProductName = '{product_name}'"
        product_name_info = self._MSDBConnection__sql_query(query)
        return product_name_info

    def avg_price(self):
        query = "select top 10 * from Products order by UnitPrice asc"
        bottom_10_data = self.__sql_query(query)
        while True:
            record = bottom_10_data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def max_price(self):
        query = "select top 1 * from Products order by UnitPrice desc"
        top_1_data = self._MSDBConnection__sql_query(query)
        while True:
            record = top_1_data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def min_price(self):
        query = "select top 1 * from Products order by UnitPrice asc"
        bottom_1_data = self._MSDBConnection__sql_query(query)
        while True:
            record = bottom_1_data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def price_range(self):
        pass

    def add_product(self):
        pass


# gets top 10 products by price - formatted
# gets bottom products by price - formatted
# search product by name
# average price
# max price
# min Price
# products in price range
# create one product

# read / list all
# print(NWProducts().read_all().fetchone())

# read one id
# print(NWProducts().read_one().fetchone())

# print all products using the while loop fetchone
# print(NWProducts().print_all())

# ask for input --> front end -- input()
# create one --> makes things persistent in db

# update one

# delete one
