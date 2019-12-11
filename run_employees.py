from db_employees_oop import *
products_table = NWEmployees()

while True:
    print('Choose option 1 for information on all employees')
    print('Choose option 2 for information on a employee using employee ID')
    print('Choose option 3 for information on top 10 products by price')
    user_choice = input('Choose an option: ').strip()

    if user_choice == '1':
        products_table.all_employees()

    elif user_choice == '2':
        print(products_table.one_employee().fetchone())

    elif user_choice == '3':
        print(products_table.top_10_price())

    elif 'exit' in user_choice:
        print('exited')
        break

    else:
        print('Option chosen is not valid')