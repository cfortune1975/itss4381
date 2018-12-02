# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune

import project

# Create Menu
menu = project.Menu()
tables = project.read_tables()

##############################
# Testing only remove in final
# for item in menu.getMenu():
#     print(item)
# menu.print_menu()
# for item in tables:
#     print(item)
##############################

# Command options
commands = {'P': 'Seat a party with # of guests.',
            'L': 'List the menu options.',
            'O': 'Place an order.',
            'S': 'Serve guests their order.',
            'C': 'Close the order and show receipt.'
            }

# Take commands from the user
print('Enter table number followed with command (1 P2)')
while True:
    cm = input('input table# with command: ').upper().lstrip().rstrip().split(' ')

    # user command error checking
    if not cm[0].isdigit():
        print('The first part of the command needs to be a table number')
        continue

    # show valid commands if user entered wrong
    if cm[1][0] not in commands.keys():
        print('\nValid commands:')
        for k, v in commands.items():
            print('\t', k, '-', v)
        continue

    # List menu items
    if cm[1][0] == 'L':
        menu.print_menu()
        continue

    # Check if user quits
    if cm[1][0] == 'C':
        print('closing.')
        break

    # Check for a valid order
    order = cm.split(' ')
    if len(order) < 2:
        print('\nUsage:')
        print('    O followed by a few codes separated by a space.')
        print('    (Sample: O a1 e2 b3 d2)')
        continue

    # Calculate order
    receiptItem = [] * len(order)
    receiptPrice = [] * len(order)
    total = 0
    for o in range(1, len(order)):
        # print(order[o])
        for k in menu.keys():
            if order[o] in menu[k]:
                receiptItem.append(menu[k][order[o]]['desc'])
                receiptPrice.append(menu[k][order[o]]['price'])
                total += menu[k][order[o]]['price']
                continue
            # else:
            #   print(order[o], 'does not exist in menu.')
            #   break;


