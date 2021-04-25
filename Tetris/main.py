import pygame
from pygame.locals import*
from Blocks import*
from Game import*

pygame.init()
##Screen variable, sets the pygame window dimensions
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Tetris")

##clock variable sets the refresh rate of pygame window
clock = pygame.time.Clock()

##run bool
run = True
##accelerate variable
accelerate = 25
##speed variable
speed = 0

##newGame variable set equal to the tetris game
newGame = Game(20, 13)

##faster variable
faster = False

##variables for testing
m_left = False
m_right = False
m_rotate = False
m_down=False

##lightsteelblue color
lightsteelblue = (188, 210, 238, 255)
##floralwhite color
floralwhite= (255, 250, 240, 255)
##coral color
coral = (255, 127, 80, 255)
##font1
font1 = pygame.font.SysFont(None, 70)
##font2
font2 = pygame.font.SysFont(None, 30)
##font3
font3 = pygame.font.SysFont(None, 100)

##print_text
#prints text to the screen
def print_text(screen, font, x, y, text, color):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


while run:
    screen.fill((0,0,0))
    Score = str(newGame.score) 
    pygame.draw.line(screen,coral,(450,50),(450,650),3)
    print_text(screen, font1,490,85, "Score:"+Score,lightsteelblue)
    print_text(screen, font1,490,350, "Menu: ", lightsteelblue)
    print_text(screen, font2,490,410, "Press Up: Rotate", floralwhite)
    print_text(screen, font2,490,450, "Press Left: Move Left", floralwhite)
    print_text(screen, font2,490,490, "Press Right: Move Right", floralwhite)

    speed = speed + 1
    # the number that speed % smaller, the downwords spees faster
    if speed % 5 == 0 or faster:
            newGame.DownWords()

    for i in range(0,newGame.height):
        for j in range(0,newGame.width):
            if newGame.field[i][j] > 0:
                pygame.draw.rect(screen, colors[newGame.field[i][j]],[newGame.horizontal + newGame.size * j + 1, newGame.vertical + newGame.size * i + 1, newGame.size - 2, newGame.size - 1])
            pygame.draw.rect(screen, (66, 66, 66, 255), [newGame.horizontal + newGame.size * j, newGame.vertical + newGame.size * i, newGame.size, newGame.size], 1)

    if newGame.figure is None:
        newGame.Start()
    else:
        for i in range(0,newGame.height):
            for j in range(0,4):
                placement = i * 4 + j
                if placement in newGame.figure.shape():
                    pygame.draw.rect(screen, colors[newGame.figure.color],[newGame.horizontal + newGame.size * (j + newGame.figure.horizontal) + 1,newGame.vertical + newGame.size * (i + newGame.figure.vertical) + 1,newGame.size - 2, newGame.size - 2])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                newGame.rotate()
                m_rotate=True
            if event.key == pygame.K_DOWN:
                faster = True
                m_down=True
            if event.key == pygame.K_LEFT:
                newGame.moveLeft()
                m_left=True
            if event.key == pygame.K_RIGHT:
                newGame.moveRight()
                m_right=True

        if event.type == pygame.KEYUP:
            faster = False

        if event.type == pygame.QUIT:
            run  = False
            
    ## Game over when blocks reach the top 
    if newGame.state == "off":
        print_text(screen, font3,100,250, "Game Over", floralwhite)

    pygame.display.update()
    clock.tick(accelerate)

pygame.quit()
