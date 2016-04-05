from time import sleep
from Tkinter import *
import time, threading
import random
from snake import Snake
from ptitpois import Ptitpois
from world import World

w = World()


w.start()

# step = 45

# fen = Tk()
# fen.geometry("600x600")
# canv=Canvas(fen, bg='black', height=500,width=500)
# canv.place(x=0, y=0)

# vasya = Snake(canv, step, step)
# vasya.name = 'shinigami'

# Ptitpois(canv, random.randint(0,500) / step * step , random.randint(0,500) / step * step)
# Ptitpois(canv, random.randint(0,500) / step * step , random.randint(0,500) / step * step )






