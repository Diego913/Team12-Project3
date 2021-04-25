import pygame
import sys
import random
from settings import *

## Snake Class
class Snake():
    def __init__(self):
        self.pos = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.snakeColor = (17, 24, 47)
        self.gameScore = 0
        self.lengthBody = 1
        self.death = False

    ##  Draws snake onto screen
    #   @param self The object pointer
    #   @param surface Serves as variable that holds the canvas python uses to draw on the screen
    #   draws the snake sprite
    def draw(self,surface):
        for p in self.pos:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.snakeColor, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    ##  Moves the snake according to key buttons
    #   @param self The object pointer
    #   handles movement of snake through listening for key presses
    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

    ##  Returns position of snakes's head
    #   @param self The object pointer
    #getter function that returns the location of the head of the snake
    def headPos(self):
        return self.pos[0]

    ##  Tunrs the snake 
    #   @param self The object pointer
    #   @param point holds the direction from user input
    #   paths how the snake turns on the grid
    def turn(self, point):
        if self.lengthBody > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    ##  Moves the snake, performs growth and death scenario
    #   @param self The object pointer
    #   handles the movement of the snake and its body parts as it gets bigger
    def move(self):
        currentPos = self.headPos()
        x,y = self.direction
        new = (((currentPos[0]+(x*gridsize))%screen_width), (currentPos[1]+(y*gridsize))%screen_height)
        #triggers when the snake touches itself, serves as one of the ways the snake dies
        if len(self.pos) > 2 and new in self.pos[2:]:
            self.death = True
        else:
            self.pos.insert(0,new)
            if len(self.pos) > self.lengthBody:
                self.pos.pop()

            #This resets snake when it touches the edge of the screen
            if currentPos[0] == screen_width:
                self.death = True
            if currentPos[0] == 0:
                self.death = True
            if currentPos[1] == screen_height:
                self.death = True
            if currentPos[1] == 0:
                self.death = True

    ##  Restarts the snake game due to death
    #   @param self The object pointer
    #   resets the game game by making the snake the oringal length, placing them in the middle of the screen, resetting the score, and sending them in a random direction
    def reset(self):
        death = False
        self.gameScore = 0
        self.lengthBody = 1
        self.pos = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
