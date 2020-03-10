#!env python3
# -*- coding: utf-8 -*-

class Car:
    def __init__(self, owner):
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner

    def turn_left(self):
        ''' turn left handle '''
        self.handle -= 90

    def turn_right(self):
        ''' turn right handle '''
        self.handle += 90

    def show_status(self):
        print("---")
        print("owner:", self.owner)
        print("car_type:", self.car_type)
        print("handle:", self.handle)

class Van(Car):
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "van"

    def open_door(self):
        print("open door")

    def close_door(self):
        print("close door")

help(Car)


car1 = Van("Taro")
car1.turn_left()
car1.show_status()
