"""1. Онлайн-магазин.
a. Створіть клас з ім’ям Shop(). Метод __init__() класу Shop() повинен містити два атрибути: shop_name і store_type. \
    Створіть метод describe_shop(), який виводить два атрибути, і метод open_shop(), який виводить \
    повідомлення про те, що онлайн-магазин відкритий. Створіть на основі класу екземпляр з ім’ям store. \
    Виведіть два атрибути окремо, потім викличте обидва методи.
b. Створіть три різних екземпляри класу, викличте для кожного екземпляру метод describe_shop().
c. Додайте атрибут number_of_units зі значенням за замовчуванням 0; він представляє кількість видів \
    товару у магазині. Створіть екземпляр з ім’ям store. Виведіть значення number_of_units, \
    а потім змініть number_of_units і виведіть знову.
d. Додайте метод з ім’ям set_number_of_units(), що дозволяє задати кількість видів товару. \
    Викличте метод з новим числом, знову виведіть значення. Додайте метод з ім’ям increment_number_of_units(), \
    який збільшує кількість видів товару на задану величину. Викличте цей метод.
e. Напишіть клас Discount(), що успадковує від класу Shop(). Додайте атрибут з ім’ям discount_products \
    для зберігання списку товарів, на які встановлена знижка. Напишіть метод get_discounts_ptoducts, \
    який виводить цей список. Створіть екземпляр store_discount і викличте цей метод.
f. Збережіть код класу Shop() у модулі. Створіть окремий файл, що імпортує клас Shop(). \
    Створіть екземпляр all_store і викличте один з методів Shop(), щоб перевірити, \
    що команда import працює правильно."""

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


class Discount(Shop):
    def __init__(self, shop_name, shop_type, number_of_units, discount_products):
        super().__init__(shop_name, shop_type, number_of_units)
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        [print(i, end=' ') for i in self.discount_products]
        print()

#shop1 = Shop('Waikiki', 'clothes')
#shop1.describe_shop()
#shop1.open_shop()
#shop1.set_number_of_units(35)
#shop1.get_number_of_units()
#shop1.increment_number_of_units(8)
#shop1.get_number_of_units()

store_discount = Discount('Name2', 'Type2', 81, ['Item1', 'Item2', 'Item3'])
store_discount.get_discounts_ptoducts()
store_discount.describe_shop()
store_discount.get_number_of_units()