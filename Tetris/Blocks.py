import random


##Define some basic color and shapes(including their rotation)
colors = [
    (1,1,1),
    (255, 182, 193, 255),
    (141, 182, 205, 255),
    (255, 160, 122, 255),
    (240, 128, 128, 255),
    (221, 160, 221, 255),
    (32, 178, 170, 255)
    ]
##Defines shape of the block(e.g. L shape or square shape)
blockShape = [
        [[2,6,10,14], [0,1,2,3]],# —— and |
        [[1,5,6,10], [2,3,5,6], [2,5,6,9], [1,2,6,7]],# Z type
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],# Left L type
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],# Right L type
        [[2,5,6,7], [2,5,6,10], [5,6,7,10], [2,6,7,10]],# 凸 type
        [[1, 2, 5, 6]],# suqare type
    ]

##Figure Class
#configures the horizontal and vertical shapes then randomizes the color and orientation of the shape
#
#
class Figure:
    horizontal = 0
    vertical = 0

    ## The constructor
    #initializes horizontal, vertical, and rotation
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
        self.rotation=0 #record the rotation times

        self.type = random.randint(0, len(blockShape) - 1)
        # the random color start from (255, 182, 193, 255),
        # since the first color will disapper on the screen
        self.color = random.randint(1, len(colors) - 1)


    #call whenever player rotate the shape
    ##rotate function
    #calls whenver player rotates the shape
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(blockShape[self.type])
    ##shape function
    #returns the shape of the block, including the type of shape and orientation of it
    def shape(self):
        return blockShape[self.type][self.rotation]
