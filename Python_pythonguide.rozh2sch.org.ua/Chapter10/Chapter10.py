"""
class Dog():
    "Проста модель собаки."
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def sit(self): 
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('jessie', 5) 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.roll_over()
"""

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def display(self):
        return 'Name: ' + self.name


man = Person('Dennis') 
print(man.display()) 
man.__name = 'Jack' 
print(man.display()) 
man.name = 'Jack' 
print(man.display()) 
print(man.name)
