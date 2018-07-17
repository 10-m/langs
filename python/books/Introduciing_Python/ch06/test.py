#!env python3
# -*- coding: utf-8 -*-

class Thing():
    pass

print(Thing)

example = Thing()
print(example)

class Thing2():
    letters = 'abc'

print(Thing2.letters)

class Thing3():
    def __init__(self):
        self.letters = 'xyz'

print(Thing3().letters)

class Element():
    def __init__(self, element):
        self.element = element
    def dump(self):
        print(self.element)
    def __str__(self):
        return(self.element['name']
               + ', '
               + self.element['symbol']
               + ', '
               + str(self.element['number']))

hydrogen = Element({'name': 'Hydrogen', 'symbol': 'H', 'number': 1})
hydrogen.dump()
print(hydrogen)

class Element2(Element):
    def __init__(self, element):
        self.__element = element
    @property
    def element(self):
        return(self.__element)
    @element.setter
    def element(self):
        self.__name = element

hydrogen2 = Element2({'name': 'Hydrogen', 'symbol': 'H', 'number': 1})
print(hydrogen2.element)

class Bear():
    def eats(self):
        return('berries')

class Rabbit():
    def eats(self):
        return('clover')

class Octothorpe():
    def eats(self):
        return('campers')

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())

class Laser():
    def does(self):
        return('disintegrate')

class Claw():
    def does(self):
        return('crush')

class SmartPhone():
    def does(self):
        return('ring')

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smart_phone = SmartPhone()
    def does(self):
        print('Laser : ' + self.laser.does())
        print('Claw : ' + self.claw.does())
        print('SmartPhone : ' + self.smart_phone.does())

robot = Robot()
robot.does()
