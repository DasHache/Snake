from time import sleep
from Tkinter import *
import time, threading
import random
from snake import Snake
from ptitpois import Ptitpois
from world import World

w = World()
vasya = Snake()

w.add(vasya,5, 5)
w.draw()
w.start()





