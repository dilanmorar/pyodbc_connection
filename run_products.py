from db_products_oop import *
products_table = NWProducts()

while True:
    print('Choose option 1 for information on all products')
    print('Choose option 2 for information on a specific product using product ID')
    print('Choose option 3 for information on top 10 products by price')
    print('Choose option 4 for information on bottom 10 products by price')
    print('Choose option 5 for information on a specific product using product name')
    print('Choose option 6 for the average price')
    print('Choose option 7 for the maximum price')
    print('Choose option 8 for the minimum price')
    print('To end enter "exit": ')
    user_choice = input('Choose an option: ').strip()

    if user_choice == '1':
        products_table.print_all()

    elif user_choice == '2':
        print(products_table.read_one().fetchone())

    elif user_choice == '3':
        print(products_table.top_10_price())

    elif user_choice == '4':
        print(products_table.bottom_10_price())

    elif user_choice == '5':
        print(products_table.search_product().fetchone())

    elif user_choice == '6':
        pass

    elif user_choice == '7':
        print(products_table.max_price())

    elif user_choice == '8':
        print(products_table.min_price())

    elif 'exit' in user_choice:
        print('exited')
        break

    else:
        print('Option chosen is not valid')