from db_products_oop import *
products_table = NWProducts()

while True:
    print('Choose option 1 for information on all products')
    print('Choose option 2 for information on a specific product')
    user_choice = input('Choose an option: ').strip()

    if user_choice == '1':
        products_table.print_all()

    elif user_choice == '2':
        print(NWProducts().read_one().fetchone())

    elif 'exit' in user_choice:
        print('exited')
        break

    else:
        print('Option chosen is not valid')