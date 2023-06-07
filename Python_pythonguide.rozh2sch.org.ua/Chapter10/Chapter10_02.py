class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def get_desc(self):
        desc = 'Element ' + self.name + ' have symbol ' + self.symbol + ' and number ' + str(self.number)
        return desc

elem = Element('Silicium', 'Si', 14)
print(elem.get_desc())

dict = { 'name': 'Argentum', 'symbol': 'Ag', 'number': 47 }

elem2 = Element(dict['name'], dict['symbol'], dict['number'])
print(elem2.get_desc())