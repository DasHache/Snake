from Tkinter import *
import random
import time, threading

class Ground(Canvas):
    def __init__(self, space, w, h):
        Canvas.__init__(self, space, bg='black', height=h, width=w)
        self.place(x=0, y=0)


class Cell:

    def __init__(self, x, y, size):
        self.id = 0
        self.x = x
        self.y = y
        self.s = size
        self.hab = 0

    def move(self, qq):
        print "elle bouge"
        pass

    def draw(self, g):
        print 'On dessine la cellule: [' + str(self.x) +','+ str(self.y)+']'
        if self.hab != 0:
            print '! On dessin un habitant dans cette cellule: ' + str(self.hab.name)
            
        x1 = self.x * self.s
        y1 = self.y * self.s
        x2 = x1 + self.s
        y2 = y1 + self.s
        print('Cell.draw: ', x1, y1, x2, y2)
        g.create_oval(x1, y1, x2, y2, fill="red")

    def draw2(self, g, color):
        #print 'On dessine la cellule: [' + str(self.x) +','+ str(self.y)+']'
        if self.hab != 0:
            print '! On dessin un habitant dans cette cellule: ' + str(self.hab.name)
            x1 = self.x * self.s
            y1 = self.y * self.s
            x2 = x1 + self.s
            y2 = y1 + self.s
            g.create_oval(x1, y1, x2, y2, fill="blue")


        #time.sleep(0.1)
        x1 = self.x * self.s
        y1 = self.y * self.s
        x2 = x1 + self.s
        y2 = y1 + self.s
        #print('Cell.draw: ', x1, y1, x2, y2)
       # g.create_rectangle(x1, y1, x2, y2, fill=color)

        
class World:

    speed = 1 #update every 1s
    step = 50
    h = step*10
    w = step*10
    xs = range(w/step)
    ys = range(h/step)
    
    def __init__(self):
        # window
        self.space = Tk()
        self.space.geometry(str(self.h)+"x"+str(self.w))
        # canvas
        self.ground = Ground(self.space, self.w, self.h)
        self.coords = [ [x,y] for x in self.xs for y in self.ys]
        self.cells = [ [Cell(x, y, self.step)  for y in self.ys] for x in self.xs]

        self.draw()

    def move(self):
        [[c.move(self.ground ) for c in r] for r in self.cells]


    def draw(self):
        for y in self.ys:
            self.draw_parallel(y)
        for x in self.xs:
            self.draw_meridian(x)

        #[[c.hab.draw() for c in r if c.id != 0] for r in self.cells]
        colors = ["blue", "red", "green", "yellow", "magenta"]
        color = colors[random.randint(0,4)]
        [[c.draw2(self.ground, color) for c in r] for r in self.cells]

    def draw_parallel(self, i):
        y = 0 + i * self.step
        self.ground.create_line(0, y, self.w, y, fill="dark grey")
        
    def draw_meridian(self, i):
        x = 0 + i * self.step
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
        self.run_update()
        self.space.mainloop()

    def update(self):
        print 'update'

        # change the world

        self.move()
        self.draw()

        
    def run_update(self):
        print 'run_update'
        self.update()
        threading.Timer(self.speed, self.run_update).start()
        

        
    def add(self, object, x, y):
        c = self.cells[x][y]
        c.id = 1
        c.hab = object


    def pr(self):
        [[ self.cells[x][y].id  for y in self.ys] for x in self.xs]
        
