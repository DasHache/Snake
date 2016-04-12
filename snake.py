__author__ = 'DasHache'
import time, threading
################################ Snake Class

# class WorldObjectPart:

#     def __init__(self):
        
# class WorldObject:

#     def __init__(self):
#         self.size = [nX, nY] # number of cell by x, by y
#         self.shape = [[WorldObjectPart(x, y) for x in nX] for y in nY]

class Snake:
    speed=0.1
    snakestep=9
    def __init__(self):
        self.width = 10
        self.height = 10
        self.name = 'snake'
        self.dir = "stop"

    def draw(self):
        
        pass
        # x = self.coord_x
        # y = self.coord_y
        # x1 = x - self.width
        # y1 = y - self.height
        # x2 = x + self.width
        # y2 = y + self.height

        # self.body = self.ground.create_oval(x1,y1,x2,y2,fill="blue")

    def draw_move(self):
        x = self.coord_x
        y = self.coord_y
        x1 = x - self.width
        y1 = y - self.height
        x2 = x + self.width
        y2 = y + self.height

        print x1, x2, y1, y2
        self.ground.coords(self.body , x1, y1, x2, y2)
        self.ground.update()

    def move(self):
        print self.dir
        x = self.coord_x
        y = self.coord_y
        if self.dir == "stop":
            x = x+0
            y = y+0
        if self.dir == "up":
            y = y-self.snakestep
        if self.dir == "down":
            y = y+self.snakestep
        if self.dir == "left":
            x = x-self.snakestep
        if self.dir == "right":
            x = x+self.snakestep

        self.coord_x=x
        self.coord_y=y


        self.draw_move()
        threading.Timer(self.speed, self.move).start()



    def move_right(self):
        self.coord_x = self.coord_x + self.snakestep
        self.move()

    def move_left(self):
        self.coord_x = self.coord_x - self.snakestep
        self.move()

    def move_up(self):
        self.coord_y = self.coord_y - self.snakestep
        self.move()

    def move_down(self):
        self.coord_y = self.coord_y + self.snakestep
        self.move()


################################ End of Snake Class
