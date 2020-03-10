#!env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class MazeRobot(metaclass=ABCMeta):
    @abstractmethod
    def init_robot(self): pass

    @abstractmethod
    def choose_dir(self): pass

class MazeRobotTest(MazeRobot):
    def init_robot(self):
        print("Init robot")

    def choose_dir(self):
        print("run")

robot = MazeRobotTest()
robot.init_robot()
