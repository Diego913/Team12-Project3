from pygame.constants import K_PAUSE
from Blocks import*

##Game
#Class that controls the functions and runs the entire tetris game
#
class Game:
    state = "on"
    field = []
    height = 0
    width = 0
    horizontal = 20
    vertical = 50
    size = 30
    figure = None
    score=0
    cancle = False
    ## Start
    # @param self The object pointer
    #  gives sets self.figure the object Figure(5,0)
    def Start(self):
        self.figure = Figure(5, 0)

    ## Constructor of Game
    #  @param self The object pointer
    #  @param m_height used to initialize the height
    #  @param m_width used to initialize the widths
    #  initializes height, width, and space list
    def __init__(self, m_height, m_width):
        self.height = m_height
        self.width = m_width
        self.score = 0
        for i in range(0,m_height):
            space = []
            for j in range(0,m_width):
                space.append(0)
            self.field.append(space)

    ## intersects
    #  @param The object pointer
    #  check function that ensures shapes do not intersect
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

    ## eliminate
    #  @param The object pointer
    #  removes the bottom when all of the shapes cover it.
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
        self.score += line ** 2
        self.cancle=True

    ## CantPlace
    #  @param The object pointer
    #  checker function that prevents the player from placing a shape at an invalid position
    def CantPlace(self):
        for i in range(0,self.height):
            for j in range(0,4):
                if i * 4 + j in self.figure.shape():
                    self.field[i + self.figure.vertical][j + self.figure.horizontal] = self.figure.color
        self.eliminate()
        self.Start()
        if self.intersects():
            self.state = "off"

    ## moveLeft
    #  @param The object pointer
    #  moves the shape left one space
    def moveLeft(self):
        before = self.figure.horizontal
        self.figure.horizontal = self.figure.horizontal - 1
        if self.intersects():
            self.figure.horizontal = before

    ## moveRight
    #  @param The object pointer
    #  moves the shape right one space
    def moveRight(self):
        before = self.figure.horizontal
        self.figure.horizontal = self.figure.horizontal + 1
        if self.intersects():
            self.figure.horizontal = before

    ## rotate
    #  @param The object pointer
    #  rotates the shape
    def rotate(self):
        before = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = before

    ## DownWords
    #  @param The object pointer
    #  moves the shape down the screen
    def DownWords(self):
        self.figure.vertical = self.figure.vertical + 1
        if self.intersects():
            self.figure.vertical = self.figure.vertical - 1
            self.CantPlace()
