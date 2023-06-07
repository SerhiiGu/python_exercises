class Car(): 
    """Проста модель автомобіля."""
    def __init__(self, make, model, year):
        """Ініціалізація атрибутів опису автомобіля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Повертає опис у відформатованому вигляді."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Виводить пробіг автомобіля у км."""
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    def update_odometer(self, km):
        """Встановлення заданого значення на одометрі.
        При спробі зворотного прокручування зміна відхиляється."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kkm):
        """Збільшує показники одометра із заданим збільшенням."""
        self.odometer_reading += kkm

    def fill_petrol_tank(self):
        """Виводить інформацію про наяність бака для бензину."""
        print("This car is equipped with a petrol tank.")


class Battery(): 
    """Проста модель акумулятора електромобіля."""
    def __init__(self, battery_size=70): 
        """Ініціалізує атрибути акумулятора."""
        self.battery_size = battery_size

    def describe_battery(self): 
        """Виводить інформацію про потужність акумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self): 
        """Виводить приблизний запас ходу для акумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 300
        message = "This car can go approximately " + str(range)
        message += " kilometers on a full charge."
        print(message)


class ElectricCar(Car): 
    """Представляє аспекти автомобіля, специфічні для електромобілів."""
    def __init__(self, make, model, year): 
        """Ініціалізує атрибути класу-батька."""
        super().__init__(make, model, year) 
        self.battery = Battery()

    def fill_petrol_tank(self):
        """У електромобілів немає бензобаку."""
        print("This car doesn't need a petrol tank!")


#my_new_car = Car('citroen', 'c3', 2018)
#print(my_new_car.get_descriptive_name())
#my_new_car.fill_petrol_tank()

my_tesla = ElectricCar('tesla', 'model s', 2018) 
print(my_tesla.get_descriptive_name())
#my_tesla.update_odometer(500)
#my_tesla.read_odometer()
my_tesla.battery.battery_size = 90
my_tesla.battery.describe_battery()
my_tesla.fill_petrol_tank()
my_tesla.battery.get_range()