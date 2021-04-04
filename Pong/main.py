import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((750,500))
pygame.display.set_caption('Pong')
font = pygame.font.SysFont("arial", 20)
## Ball Class
class Ball:
    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        self.x = 375
        self.y = 250
        self.yDirection = 1
        self.xDirection = 1
        self.speed = 10

    ## drawBall
    #  @param The object pointer
    def drawBall(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x, self.y, 10, 10))

    ## move
    #  @param The object pointer
    def move(self):
        self.x += self.speed * self.xDirection
        self.y += self.speed * self.yDirection

    ##checkForWall
    #  @param The object pointer
    def checkForWall(self):
        if self.y > 500:
            self.yDirection = -1
        if self.y < 0:
            self.yDirection = 1

##Paddle Class
#
class Paddle:

    ## The constructor
    #  @param self The object pointer
    def __init__(self, xCoor):
        self.x = xCoor
        self.y = 210
        self.score = 0

    ## drawPaddle
    #  @param self The object pointer
    def drawPaddle(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x, self.y, 20, 80))

    ## move
    #  @param self The object pointer
    #  @parm direction determines the direction of the paddle
    def move(self, direction):
        self.y += 10 * direction

    ## checkForWall
    #  @param self The object pointer
    def checkForWall(self):
        if self.y < 0:
            self.y = 0
        if self.y > 420:
            self.y = 420

ball = Ball()
paddle1 = Paddle(30)
paddle2 = Paddle(700)
clock = pygame.time.Clock()

## draw
#  draws the paddle and ball
def draw():
    if gameOver() == False:
        screen.fill((0,0,0))
        ball.drawBall()
        paddle1.drawPaddle()
        paddle2.drawPaddle()
        scoreboard()
        pygame.display.update()
        clock.tick(25)
    else:
        gameOverScreen()
        pygame.display.update()

## scoreboard
#  renders the wording for the scoreboard
def scoreboard():
    player1Score = font.render("Player 1 Score: {0}".format(paddle1.score), 1, (255,255,255))
    player2Score = font.render("Player 1 Score: {0}".format(paddle2.score), 1, (255,255,255))
    screen.blit(player1Score, (170, 0))
    screen.blit(player2Score, (420, 0))


def checkPaddleBounce():
    if ball.x <= 50 and (ball.y >= paddle1.y and ball.y <= paddle1.y + 80):
            ball.xDirection = 1
    if ball.x >= 690 and (ball.y >= paddle2.y and ball.y <= paddle2.y + 80):
            ball.xDirection = -1

def score():
    if ball.x > 750:
            paddle1.score += 1
            resetBall("p1")
    if ball.x < 0:
            paddle2.score += 1
            resetBall("p2")

def resetBall(paddle):
    ball.x = 375
    ball.y = 250
    if paddle == "p1":
        ball.xDirection = -1
    elif paddle == "p2":
        ball.xDirection = 1

def gameOver():
    if paddle1.score == 2:
        return True
    if paddle2.score == 2:
        return True
    return False

def gameOverScreen():
    if paddle1.score == 5:
        screen.fill((0,0,0))
        go = font.render("Player 1 Wins", 1, (255,255,255))
        screen.blit(go, (375,250))
    elif paddle2.score == 5:
        screen.fill((0,0,0))
        go = font.render("Player 2 Wins", 1, (255,255,255))
        screen.blit(go, (375,250))

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            paddle1.move(1)
        if key[pygame.K_w]:
            paddle1.move(-1)
        if key[pygame.K_k]:
            paddle2.move(1)
        if key[pygame.K_i]:
            paddle2.move(-1)

        if gameOver() == False:
            score()
            checkPaddleBounce()
            ball.checkForWall()
            ball.move()
            paddle1.checkForWall()
            paddle2.checkForWall()

        draw()

main()
pygame.quit()
