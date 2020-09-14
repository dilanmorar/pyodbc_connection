# pyodbc_connection

Using the package pyodbc in python to connect to a database (SQL) by importing it. Also go through using libraries, modules and packages. In this repository the database we will be using is Northwind which can be obtained by pulling the image from dockerhub (`docker pull kcornwall/sqlnorthwind`). It contains information about products and employees.

## Modules, Libraries and Packages

### Libraries

Refer to python standard libraries.
They come standard with python but need to be imported

### Modules

These are python files that we import into our programs.
We create and import our own modules internally.

### Packages

These are external modules, that we need to install (externally) and then import them.
These are modules usually written in OOP style, that abstract something.

These things that abstracted include:
- connection to a service (google maps or google image recognition, api, price of stocks, price of bitcoin)
- tools or calculator (prime number calculator, other complex calculators)
- front-end tools - like JS compiler or other things like scss
- full fledged frameworks
- connection to Databases or using HTTP protocols

#### Searching
- google
- look at repos
- previous experience
- https://pypi.org/
- analyse if its maintained and how/why you will use it

#### Installing
- pip - pythons package manager(deals with dependencies and installs in virtual environment, will also probably have to install pip)
- pycharm - you can just add to interpreter

#### Using
- import and call your functions
- follow the documentation

## pyodbc

This package allows us to connect to a database such as SQL which is what
we have done in this repository.

### Connecting

We have connected to the database from python in the db_connect.py file and need to define the following parameters as variables: server, database, username and password. Also make the connection and create a cursor.

Then create a class (MSDBConnection) and include the parameter attributes in the class, the connection and the cursor. This can be seen in the db_connect_oop.py file.

### Running the queries in python

To run queries you can setup a method (such as in db_employees_oop.py and db_products_oop.py) which contains the query you want to process, and create a loop to output all outcomes.

Then create a run file (run_employees.py and run_products.py) which can be used by a user that they can input information and that will return the desired information.
