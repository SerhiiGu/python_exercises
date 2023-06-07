class Shop():
    def __init__(self, shop_name, shop_type, number_of_units = 0):
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print('Shop name:', self.shop_name, 'Shop type:', self.shop_type)

    def open_shop(self):
        print('Online shop', self.shop_name, 'is opened!')

    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units
        return self.number_of_units

    def increment_number_of_units(self, inc):
        self.number_of_units += inc
        return self.number_of_units
    
    def get_number_of_units(self):
        print(self.number_of_units)