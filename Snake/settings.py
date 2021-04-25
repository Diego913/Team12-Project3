##  Settings
#   stores all global variables so that all files can access them easily


#determines the dimensions of the pygame window
screen_width = 480
screen_height = 480

#determines the dimensions of the grid squares
gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

#determines the speed the snake will go in each direction
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)
