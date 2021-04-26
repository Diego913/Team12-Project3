from main import*
from Blocks import*
from Game import*

reached = False
def ReachTop():
    if run == False:
        if newGame.state =="on":
            print("TEST CASE 1: Game reach the screen top: Failed")
            return
    print("TEST CASE 1: Game reach the screen top: Passed")
    reached ==True
    return

def testFigure():
    if newGame.figure == None:
        print("TEST CASE 2: Create a new figure of blocks: Failed")
        return
    print("TEST CASE 2: Create a new figure of blocks: Passed")
    return

def testMove():
    if m_left == True:
        print("TEST CASE 3a: Blocks move Left work: Passed")
    if m_right == True:
        print("TEST CASE 3b: Blocks move right work: Passed")
    if m_down == True:
        print("TEST CASE 3c: Press down to accelerate work: Passed")
    if m_rotate == True:
        print("TEST CASE 3d: Press up to blocks work: Passed")
        return
    print("TEST CASE 3: Player pressed keyboard: Failed")
    return   
    
def scoreChange():
    if newGame.cancle:
        if newGame.score > 0: 
            print("TEST CASE 4: The Score changes after eliminate a line: Passed")
            return

ReachTop()
testFigure()
testMove()
scoreChange()
