__author__ = 'DasHache'
class Ptitpois:

    def __init__(self, canvas,x,y):
        self.ground = canvas
        self.width = 5
        self.height = 5
        self.name = 'ptitpois'
        self.coord_x = x
        self.coord_y = y
        self.draw()

    def draw(self):
        x = self.coord_x
        y = self.coord_y
        x1 = x - self.width
        y1 = y - self.height
        x2 = x + self.width
        y2 = y + self.height

        self.body = self.ground.create_oval(x1,y1,x2,y2,fill="white")
