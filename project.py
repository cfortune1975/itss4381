# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune


class Order:
    def __init__(self):
        self.__order = []

    def __str__(self):
        return str(self.__order)

    def get_order(self):
        return self.__order

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
    def __init__(self, arg_table, arg_max):
        self.__table = arg_table
        self.__maxSeats = arg_max
        self.__available = 'Open'
        self.__guests = 0
        self.__order = Order()
        self.__served = []
        self.__menu = Menu()

    def __str__(self):
        if not self.__order:
            order = "empty"
        else:
            order = self.__order

        return 'Table: ' + str(self.__table) + ' has ' + str(self.__maxSeats) + ' seats, with ' + \
               str(self.__guests) + ' guests and ordered: ' + order

    def get_guests(self):
        return self.__guests

    @property
    def menu(self):
        return self.__menu

    @property
    def served(self):
        return self.__served

    def take_orders(self, order):
        if self.__available == 'Open':
            print('No one is seated at Table', self.__table)
            return
        else:
            order_list = []
            for item in order:
                if item in self.__menu.menu:
                    order_list.append(self.__menu.menu[item])
                else:
                    print('No item with code ' + item)
            if self.__order.get_order():
                print(len(order_list), 'additional items ordered for Table ', self.__table)
            else:
                print(len(order_list), 'items ordered for Table', self.__table)
            self.__order.get_order().extend(order_list)
            self.__available = 'Ordered'

        return len(order_list)

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
        if not self.available == 'Open':
            print('Table', self.table, 'already occupied!')
            return
        if count <= self.__maxSeats:
            self.__guests = count
            self.__available = 'Seated'
            print('Party of', count, 'assigned to table', self.table)
        else:
            print("Sorry, max " + str(self.__maxSeats) +
                  " seats in Table " + str(self.table) + "!")

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
    def __init__(self):
        self.menu = {}
        self.read_menu()

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
            self.menu[arg_code] = (MenuItem(arg_code, arg_name, arg_price))

        return self.menu

    def print_menu(self):
        for item in self.menu:
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
