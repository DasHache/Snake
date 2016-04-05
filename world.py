from Tkinter import *
import random

class Ground(Canvas):
    def __init__(self, space, w, h):
        Canvas.__init__(self, space, bg='black', height=h, width=w)
        self.place(x=0, y=0)


class World:

    step = 50
    h = 500
    w = 500
    xs = range(w/step)
    ys = range(h/step)
    
    def __init__(self):
        # window
        self.space = Tk()
        self.space.geometry(str(self.h)+"x"+str(self.w))
        # canvas
        self.ground = Ground(self.space, self.w, self.h)
        self.cells = [ x+y*10  for x in self.xs for y in self.ys]
        self.coords = [ [x,y] for x in self.xs for y in self.ys]

        self.draw()

    def draw(self):
        for y in self.ys:
            self.draw_parallel(y)
        for x in self.xs:
            self.draw_meridian(x)
            
    def draw_parallel(self, i):
        y = 0 + i * self.step
        print('y = ', y)
        self.ground.create_line(0, y, self.w, y, fill="dark grey")
        
    def draw_meridian(self, i):
        x = 0 + i * self.step
        print('x = ', x)
        self.ground.create_line(x, 0, x, self.h, fill="dark grey")
        
    def rand(self):
        rand_y = random.randint(self.border, self.ground.h)
        rand_x = random.randint(self.border, self.ground.w)
        return [rand_x, rand_y]

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
        
    def start(self):
        self.space.bind('<KeyPress>', self.change_direction)
        self.space.mainloop()
