from pygame.constants import K_PAUSE
from Blocks import*

class Game:
    state = "on"
    field = []
    height = 0
    width = 0
    horizontal = 20
    vertical = 50
    size = 30
    figure = None

    def Start(self):
        self.figure = Figure(5, 0)

    def __init__(self, m_height, m_width):
        self.height = m_height
        self.width = m_width
        for i in range(0,m_height):
            space = []
            for j in range(0,m_width):
                space.append(0)
            self.field.append(space)
    
    def intersects(self):
        intersection = False
        # Because every shape contains 4 blocks 
        # travelsal
        for i in range(0,4):
            for j in range(0,4):
                if i * 4 + j in self.figure.shape():
                    if (j + self.figure.horizontal > self.width - 1) or (i + self.figure.vertical > self.height - 1) or (self.field[i + self.figure.vertical][j + self.figure.horizontal] > 0) or (j + self.figure.horizontal < 0) or ( j + self.figure.horizontal < 0):
                        intersection = True
        return intersection

    def eliminate(self):
        line = 0
        for i in range(1, self.height):
            current = 0
            for j in range(0,self.width):
                if self.field[i][j] == 0:
                    current = current + 1
            if current == 0:
                line = line + 1
                for k in range(i, 1, -1):
                    for z in range(0,self.width):
                        self.field[k][z] = self.field[k - 1][z]
    
    def CantPlace(self):
        for i in range(0,self.height):
            for j in range(0,4):
                if i * 4 + j in self.figure.shape():
                    self.field[i + self.figure.vertical][j + self.figure.horizontal] = self.figure.color
        self.eliminate()
        self.Start() 
        if self.intersects():
            newGame.state = "off"

    def moveLeft(self):
        before = self.figure.horizontal
        self.figure.horizontal = self.figure.horizontal - 1
        if self.intersects():
            self.figure.horizontal = before

    def moveRight(self):
        before = self.figure.horizontal
        self.figure.horizontal = self.figure.horizontal + 1
        if self.intersects():
            self.figure.horizontal = before

    def rotate(self):
        before = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = before

    def DownWords(self):
        self.figure.vertical = self.figure.vertical + 1
        if self.intersects():
            self.figure.vertical = self.figure.vertical - 1
            self.CantPlace()

 

