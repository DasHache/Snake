from Tkinter import *
import random

class Ground(Canvas):
    
    def __init__(self, space, h, w, b):
        self.h = h - 2*b
        self.w = w - 2*b
        Canvas.__init__(self, space, bg='black', height=self.h, width=self.w)
        self.place(x=b, y=b)
    
class World:

    border = 10
    def __init__(self, size=[600,600]):
        self.h = size[0]
        self.w = size[1]
        # window
        self.space = Tk()
        self.space.geometry(str(self.h)+"x"+str(self.w))
        # canvas
        self.ground = Ground(self.space, self.h, self.w, self.border)

    def rand(self):
        rand_y = random.randint(self.border, self.ground.h)
        rand_x = random.randint(self.border, self.ground.w)
        return [rand_x, rand_y]
