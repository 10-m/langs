#!env python3
# -*- coding: utf-8 -*-

class Game:
    def __goal(self):
        print("private")

    def play(self):
        print("public")

game = Game()
game.play()
game.__goal()
