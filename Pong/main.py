import pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((750,500))
pygame.display.set_caption('Pong')

# run = True

class Paddle: 
    def __init__(self):
        self.x = 10
        self.y = 10

    def drawPaddle(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x, self.y, 10, 80))
        pygame.display.update()
    
    def move(self, newY):
        self.y +=  newY


paddle1 = Paddle()
clock = pygame.time.Clock()

def main():
    run = True
    # pygame.time.delay(100)
    clock.tick(5)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            paddle1.move(1)
        if key[pygame.K_w]:
            paddle1.move(-1)

        screen.fill((0,0,0))
        paddle1.drawPaddle() 
    
main()
pygame.quit()