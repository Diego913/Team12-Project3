from snake import *
from food import *
from settings import *


def testSnakeSpawn():
    snake = Snake()
    if snake.pos[0] == (480/2,480/2):
        print("TEST 1 CASE: Snake spawns in the middle of the screen correctly: PASSED")
        return
    print("TEST 1 CASE: Snake does not spawn in the middle of the screen correctly: FAILED")


def testFoodSpawn():
    food = Food()
    food.randomPos()
    if food.pos != (0,0):
        print("TEST 2 CASE: Food correctly spawns in a random location: PASSED")
        return
    print("TEST 2 CASE: Food does not correctly spawn in a random location: FAILED")


def testSnakeMove():
    snake2 = Snake()
    snake2.move()
    if snake2.pos[0] != (480/2,480/2):
        print("TEST 3 CASE: Snake correctly moves when function is called: PASSED")
        return
    print("TEST 3 CASE: Snake does not does not move when function is called: FAILED")



def testSnakeDeath():
    snake3 = Snake()
    snake3.pos[0] = (0,0)
    snake3.move()
    if snake3.death == True:
        print("TEST 4 CASE: Snake dies when it moves beyond the screen dimensions: PASSED")
        return
    print("TEST 4 CASE: Snake does not die when it goes beyond screen dimensions: FAILED")





def testSnakeEat():
    snake4 = Snake()
    food2 = Food()
    food2.randomPos()
    loc = food2.pos
    snake4.pos[0] = loc
    if snake4.headPos() == food2.pos:
        food2.randomPos()
    if loc != food2.pos:
        print("TEST 5 CASE: Food changes location when snake eats it: PASSED")
        return
    print("TEST 5 CASE: Food does not change location when snake eats it: FAILED")




def testSnakeSize():
    snake5 = Snake()
    snake5.lengthBody += 1
    if snake5.lengthBody > 1:
        print("TEST 6 CASE: Snakes body correctly increases in size: PASSED")
        return
    print("TEST 6 CASE: Snakes body does not increase in size when called: FAILED")





def snakeTests():
    testSnakeSpawn()
    testFoodSpawn()
    testSnakeMove()
    testSnakeDeath()
    testSnakeEat()





snakeTests()
