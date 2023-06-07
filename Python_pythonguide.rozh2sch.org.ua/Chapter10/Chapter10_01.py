class SportResults():
    def __init__(self, name='Jack', points = 25):
        self.name = name
        self.points = points

    def pr(self):
        print('From class', self.name, 'with', str(self.points))

diving = SportResults('Suzy')
diving.name = 'Bob'
diving.points = 150
diving.pr()