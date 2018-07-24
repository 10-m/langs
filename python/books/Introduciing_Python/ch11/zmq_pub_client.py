#!env python3
# -*- coding: utf-8 -*-
import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
topicfilter = "".encode('utf-8')
subscriber.setsockopt(zmq.SUBSCRIBE, topicfilter)

while True:
  message = subscriber.recv()
  print(message)
