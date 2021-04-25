from main import *


def testPaddleMove():
    paddle = Paddle(100)
    paddle.move(-1)
    if paddle.y != 200:
        print("TEST CASE 1: Paddle moves up and down the correct amount of units: Failed")
        return
    paddle.move(1)
    if paddle.y != 210:
        print("TEST CASE 1: Paddle moves up and down the correct amount of units: Failed")
        return

    print("TEST CASE 1: Paddle moves up and down the correct amount of units: Passed")

def testPaddleXcoordinate():
    paddle = Paddle(100)
    if paddle.x == 100:
        print("TEST CASE 2: Paddle starts at given X coordinate: Passed")
    else:
        print("TEST CASE 2: Paddle starts at given X coordinate: Failed")

def testPaddleCheckForWall():
    paddle = Paddle(100)
    paddle.y = 420
    paddle.checkForWall()
    if paddle.y != 420:
        print("TEST CASE 3: Paddle can't go through upper and lower walls: Failed")
        return
    paddle.y = -10
    paddle.checkForWall()
    if paddle.y != 0:
        print("TEST CASE 3: Paddle can't go through upper and lower walls: Failed")
        return
         
    print("TEST CASE 3: Paddle can't go through upper and lower walls: Passed")

def testBallStartCoordinates():
    ball = Ball()
    if ball.x == 375 and ball.y == 250:
        print("TEST CASE 4: Ball starts in the middle of screen: Passed")
        return
    print("TEST CASE 4: Ball starts in the middle of screen: Passed")

def testBallWallBounce():
    ball = Ball()
    ball.y = 510
    ball.checkForWall()
    if ball.yDirection != -1:
        print("TEST CASE 5: Ball's direction correct according to wall bounce: Failed")
        return
    ball.y = -10
    ball.checkForWall()
    if ball.yDirection != 1:
        print("TEST CASE 5: Ball's direction correct according to wall bounce: Failed")
        return
         
    print("TEST CASE 5: Ball's direction correct according to wall bounce: Passed")

def testBallMove():
    ball = Ball()
    ball.move()
    if ball.x != 385 and ball.y != 260:
        print("TEST CASE 6: Ball moves correctly according to direction and speed: Failed")
    ball.xDirection = -1
    ball.yDirection = -1
    ball.move()
    if ball.x != 375 and ball.y != 250:
        print("TEST CASE 6: Ball moves correctly according to direction and speed: Failed")

    print("TEST CASE 6: Ball moves correctly according to direction and speed: Passed")

def pongTests():
    testPaddleMove()
    testPaddleXcoordinate()
    testPaddleCheckForWall()
    testBallStartCoordinates()
    testBallWallBounce()
    testBallMove()

pongTests()