# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune

import project

# Create Menu and Table objects.
# menu = project.Menu([])  # creates an empty array
tables = project.read_tables()

##############################
# Testing only remove in final
# for item in menu.getMenu():
#     print(item)
# menu.print_menu()
# for item in range(len(tables)):
#     print(tables[item])
# tables[0].order = ['a1', 'a2']
# print(menu.get_key())
# exit()
##############################

# Command options.
commands = {'P': 'Seat a party with # of guests.',
            'L': 'List the menu options.',
            'O': 'Place an order.',
            'S': 'Serve guests their order.',
            'C': 'Close the order and show receipt.'
            }

# Take commands from the user
print('Enter table number followed with command (1 P2)')
while True:
    # Get user input and clean.
    cm = input('input: ').upper()
    cm = cm.lstrip().rstrip().split(' ')

    # Check first command for table numbers
    if not cm[0].isdigit():
        print('The first part of the command needs to be a table number.')
        continue

    # check if table exists
    table_num = int(cm[0])
    exists = False
    for num in range(len(tables)):
        if table_num == tables[num].table:
            exists = True

    if not exists:
        print('Table:', table_num, 'does not exist')
        continue

    # Seat a party at a table
    elif cm[1][0] == 'P':
        count = int(cm[1][1:])
        tables[table_num].seat_guest(count)

    # List menu items
    elif cm[1][0] == 'L':
        menu.print_menu()
        continue

    # place the guests order
    elif cm[1][0] == 'O':
        has_ordered = cm[2:]

        if len(has_ordered) < 1:
            print('\nUsage:')
            print('  O followed by menu codes separated by a space.')
            print('  (Sample: O A1 E2 C1 D2)')
            continue

        tables[table_num].take_orders(has_ordered)

        if not tables[table_num].order:
            print('Nothing ordered table', table_num)

    # Serve the customer's order

    elif cm[1][0] == 'S':
        if tables[table_num].order:
            if tables[table_num].available=='Ordered':
                tables[table_num].served.extend(tables[table_num].order)
                tables[table_num].order=0
                tables[table_num].available = 'Served'
                print('Food served in table', table_num)
            else:
                print('Order not placed at Table', table_num, 'yet!')

    # TODO: Close and calculate guest's order
    elif cm[1][0] == 'C':
        print('Closing table. Here is the bill.')
        # dummy = project.Order(orders)
        # dummy.print_receipt(orders, menu)
        tables[table_num].print_recepit(tables[table_num].served, tables[table_num].menu)

    # Show valid commands if user entered wrong
    else:
        print('\nValid commands:')
        for k, v in commands.items():
            print('\t', k, '-', v)
