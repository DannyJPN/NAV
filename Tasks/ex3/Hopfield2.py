#initilising
import pygame
import random
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
 
width = 20
height = 20
margin = 5#gap between 

current = 0
bank = 0
turnnumber = 0

grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) 
 
pygame.init()
GameR = [600,600]
gameD = pygame.display.set_mode(GameR)
pygame.display.set_caption("Pirate Game")
 
done = False
clock = pygame.time.Clock()
#-------------------------------------------------------------------------------------------------------
#FUNCTIONS

#---------------------------------------------------------------------------
#MAIN LOOP:

done = False

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change the x/y screen coordinates to grid coordinates
            column = event.pos[0] // (width + margin)
            row = event.pos[1] // (height + margin)
            if grid[row][column] == 1:
                grid[row][column] = 0
                print("Click ", event.pos, "Grid coordinates: ", row, column," Whited")
            if grid[row][column] == 0:
                grid[row][column] = 1
                print("Click ", event.pos, "Grid coordinates: ", row, column," Blacked")
           
    gameD.fill(black)
 
    #Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 0:
                color = white
            elif grid[row][column] == 1:
                color = black
            cell_rect = ((margin + width) * column + margin, (margin + height) * row + margin, width, height)
            pygame.draw.rect(gameD, color, cell_rect)
    print(grid)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()