from time import sleep
from Tkinter import *
import time, threading
import random
from snake import Snake
from ptitpois import Ptitpois

step = 45

fen = Tk()
fen.geometry("600x600")
canv=Canvas(fen, bg='black', height=500,width=500)
canv.place(x=0, y=0)

vasya = Snake(canv, step, step)
vasya.name = 'shinigami'

Ptitpois(canv, random.randint(0,500) / step * step , random.randint(0,500) / step * step)
Ptitpois(canv, random.randint(0,500) / step * step , random.randint(0,500) / step * step )



print 'Vasya\'s name: ', vasya.name

def change_direction(event):
    print 'tu a appuye le bouton:' + event.char
    print 'snake dir changed'
    key = event.char
    if key == "d":
        vasya.dir="right"
    if key == "a":
        vasya.dir="left"
    if key == "w":
       vasya.dir="up"
    if key == "s":
        vasya.dir="down"


def move_snake(event):
    print 'tu a appuye le bouton:' + event.char
    print 'snake moved to... '
    key = event.char
    if key == "d":
        vasya.move_right()
    if key == "a":
        vasya.move_left()
    if key == "w":
       vasya.move_up()
    if key == "s":
        vasya.move_down()


fen.bind('<KeyPress>', change_direction)
fen.mainloop()

