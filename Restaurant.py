# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune

import project

# Create Menu
menu = project.Menu()
tables = project.read_tables()

# Command options
options = {'A': 'lists all appetizers',
           'B': 'lists all beverages',
           'E': 'lists all entrees',
           'D': 'lists all desserts',
           'C': 'close the program',
           'O': 'place an order',
           '#': 'table num required for all options'
           }

# Take commands from the user
while True:
    ui = input('input: ').lower().lstrip()

    # Check user for valid input
    if ui[0].upper() not in options:
        print('Valid commands:')
        for k, v in options.items():
            print('\t', k, '-', v)
        continue

    # Check if user quits
    if ui == 'c':
        print('closing.')
        break

    # List menu items
    if ui == 'a':
        print('\nAppetizers:')
        for k, v in menu['appetizers'].items():
            print('    ' + k + ': %-20s $%.2f' % (v['desc'], v['price']))
        continue
    elif ui == 'b':
        print('\nBeverages:')
        for k, v in menu['beverages'].items():
            print('    ' + k + ': %-20s $%.2f' % (v['desc'], v['price']))
        continue
    elif ui == 'e':
        print('\nEntrees:')
        for k, v in menu['entrees'].items():
            print('    ' + k + ': %-20s $%.2f' % (v['desc'], v['price']))
        continue
    elif ui == 'd':
        print('\nDesserts:')
        for k, v in menu['desserts'].items():
            print('    ' + k + ': %-20s $%.2f' % (v['desc'], v['price']))
        continue

    # Check for a valid order
    order = ui.split(' ')
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


