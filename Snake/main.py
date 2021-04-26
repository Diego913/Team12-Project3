import pygame
import sys
import random
import snake
from settings import *
from snake import Snake
from food import Food

##  Draws the grid
#   @param surface Serves as variable that holds the canvas python uses to draw on the screen
#   draws the checkerboard pattern onto the screen, creating the board the snake moves on
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(16, 224, 235), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (9, 78, 217), rr)


##  Main function that has the main game loop
#   main function that serves that collects all of the functions from each class and uses them to run the game
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("impact",16)
    run= True
    #main game loop that runs until the snake dies
    while (run):
        clock.tick(10)
        snake.movement()
        drawGrid(surface)
        snake.move()
        if snake.headPos() == food.pos:
            snake.lengthBody += 1
            snake.gameScore += 1
            food.randomPos()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        textScore = myfont.render("Score {0}".format(snake.gameScore), 1, (0,0,0))
        screen.blit(textScore, (5,10))
        if snake.death == True:
            myfont = pygame.font.SysFont("impact",28)
            run = False
            screen.fill((0,0,0))
            textDead = myfont.render("Your Final Score is {0}".format(snake.gameScore), 1, (255, 255, 255))
            screen.blit(textDead, ((screen_width//2)-200, (screen_height//2)-50))
            textRestart = myfont.render("Press Spacebar to Restart!",1, (255, 255, 255))
            screen.blit(textRestart, ((screen_width//2)-210, (screen_height//2)-25))
        pygame.display.update()
    while run == False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        run = True
                        main()
    pygame.display.update()


main()
