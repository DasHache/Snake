from random import randint 

class Mortal:

    width = 10
    height = 10
    
    def __init__(self, world, coords):
        self.w = world
        self.name = 'mortal'
        self.coord_x = coords[0]
        self.coord_y = coords[1]
        self.draw()
        self.live()

    def draw(self):
        x = self.coord_x
        y = self.coord_y
        x1 = x - self.width
        y1 = y - self.height
        x2 = x + self.width
        y2 = y + self.height

        self.body = self.w.create_oval(x1,y1,x2,y2,fill="white")
    
    def live(self):
        import time, threading
        print("living: ", self.name)
        threading.Timer(1, self.live).start()
        print("living, done")

    def move(self):
        x = self.coord_x
        y = self.coord_y
        x1 = x - self.width
        y1 = y - self.height
        x2 = x + self.width
        y2 = y + self.height

        print x1, x2, y1, y2
        self.ground.coords(self.body , x1, y1, x2, y2)
        self.ground.update()


    def move_right(self):
        self.coord_x = self.coord_x + 20
        self.move()

    def move_left(self):
        self.coord_x = self.coord_x - 20
        self.move()

    def move_up(self):
        self.coord_y = self.coord_y - 20
        self.move()

    def move_down(self):
        self.coord_y = self.coord_y + 20
        self.move()



class Krokodile(Mortal):

    pass

        
        
