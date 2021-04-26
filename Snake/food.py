import pygame
import sys
import random
from settings import *

##  Food Class
class Food():
    def __init__(self):
        self.pos = (0,0)
        self.foodColor = (223, 163, 49)
        self.randomPos()
    ##  randomPos
    #   @param self The object pointer
    #   finds a random pos on the grid to place a food square
    def randomPos(self):
        self.pos = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    ##  draw
    #   @param self The object pointer
    #   @param surface Serves as variable that holds the canvas python uses to draw on the screen
    #   draws the food sprite
    def draw(self, surface):
        r = pygame.Rect((self.pos[0], self.pos[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.foodColor, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
