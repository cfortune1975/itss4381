# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune


class Order:
    def __init__(self, arg_order):
        self.__order = arg_order
        self.check_order(self.__order)

    def __str__(self):
        return str(self.__order)

    def get_order(self):
        return self.__order

    # TODO: Charles finish the orders
    @staticmethod
    def check_order(order):
        menu = Menu()
        for item in menu:
            print(menu[item])
        if order in menu.get_menu():
            print('test true')
            return True
        else:
            print('No items with code', 'X')
            return False


    # TODO: Charles finish the orders
    #def place_orders(self, table, order):
    #    """ Place order for a specific table """
    #     validCommands = ['a', 'b', 'c', 'd', 'e', 's']
    #     command = input("Enter commands separated by spaces, or c to close: ")
    #     command = command.split(' ')
    #     for cm in range(0, len(command), 1):
    #         if command[cm] in validCommands and command[cm].lower() != 'c':
    #             if command[cm].lower() == 'a':
    #                 print(order['a1'], order['a2'])
    #             elif command[cm].lower() == 'b':
    #                 print(order['b1'], order['b2'])
    #             elif command[cm].lower() == 'd':
    #                 print(order['d1'], order['d2'])
    #             elif command[cm].lower() == 'e':
    #                 print(order['e1'], order['e2'])
    #         elif command[cm].lower() in order:
    #             print(order[command[cm]])
    #         elif command[cm].lower() == 'o':
    #             print("")
    #         elif command[cm].lower() == 'c':
    #             exit(1)
    #         else:
    #             print("Error: " + command[cm] + " is not a valid command!")

    @staticmethod
    def print_receipt(order, menu):
        # Calculate order
        receipt_item = [] * len(order)
        receipt_price = [] * len(order)
        total = 0.0
        for o in range(len(order)):
            for k in range(len(menu)):
                if order[o] in menu[k]:
                    receipt_item.append(order[1])
                    receipt_price.append(order[2])
                    total += order[2]

        print('\n%15s' % 'Receipt')
        print('%-20s %5s' % ('item(s)', 'price'))
        print('%-19s %5s' % ('----------', '-------'))
        for i in range(len(receipt_item)):
            print('%-20s %5.2f' % (receipt_item[i], receipt_price[i]))
        print('%27s' % '-------')
        print('%26.2f' % total)


class Table:
    __available = True

    def __init__(self, arg_table, arg_max, arg_guests=0, arg_order=False):
        self.__table = arg_table
        self.__maxSeats = arg_max
        self.__guests = arg_guests
        self.__order = arg_order

    def __str__(self):
        if self.__order:
            ordered = "has"
        else:
            ordered = "hasn't"

        return 'Table: ' + str(self.__table) + ' has ' + str(self.__maxSeats) + ' seats, with ' + \
               str(self.__guests) + ' guests and ' + ordered + ' ordered.'

    def get_guests(self):
        return self.__guests

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def table(self):
        return self.__table - 1

    @property
    def available(self):
        return self.__available

    def seat_guest(self, count):
        if not self.available:
            print('Table', self.table, 'already occupied!')
            return
        if count <= self.__maxSeats:
            self.__guests = count
            self.__available = False
            print('Party of', count, 'assigned to table', self.table)
        else:
            print("Sorry, max " + str(self.__maxSeats) +
                  " seats in Table " + str(self.__table) + "!")

    def unseat_guest(self):
        self.__available = True
        self.__guests = 0


class MenuItem:
    def __init__(self, arg_item_code, arg_name, arg_price):  # instantiates object
        self.__code = arg_item_code
        self.__name = arg_name
        self.__price = arg_price

    def __str__(self):
        return self.__code + ' ' + self.__name + ' ' + str(self.__price)


class Menu:
    def __init__(self, arg_menu=[]):
        self.__menu = arg_menu
        self.read_menu()

    # not how the built in __str__ function works
    # def __str__(self):
    #     for m in self.__menu:
    #         print(m)

    def get_menu(self):
        return self.__menu

    def read_menu(self):
        # open table menu.txt file to import.
        try:
            file = open("Menu.txt", 'r')
        except IOError:
            print("missing menu.txt file.")
            return []

        # Read in menu information.
        raw_data = file.readlines()
        file.close()

        # this loop cleans up the text in menu.txt.
        for i in range(len(raw_data) - 1):
            raw_data[i] = raw_data[i].strip('\n')
            raw_data[i] = raw_data[i].rstrip(' ')

        # this loop turns raw_data into MenuItems.
        for k in raw_data:
            temp = k.split(' ')
            arg_code = temp[0]
            arg_name = temp[1].replace('_', ' ')
            arg_price = float(temp[2])
            self.__menu.append(MenuItem(arg_code, arg_name, arg_price))

        return self.__menu

    def print_menu(self):
        for item in self.__menu:
            print(item)


def read_tables():
    # open table config file
    try:
        config = open('config.txt', 'r')
    except IOError:
        print("Missing table config.txt file.")
        return []

    # Read in table information
    raw_data = config.readlines()
    config.close()

    # Clean up raw data
    for i in range(len(raw_data) - 1):
        raw_data[i] = raw_data[i].strip('\n')
        raw_data[i] = raw_data[i].rstrip(' ')

    # convert raw_data into Table Object
    table = []
    for item in raw_data:
        temp = item.split(' ')
        table.append(Table(int(temp[0]), int(temp[1])))

    return table
