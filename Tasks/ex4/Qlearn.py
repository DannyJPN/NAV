import numpy
import pygame
import random
import time
import copy
TRAP=2
KRYSA=1
SEJR=3
FREE=0
KRYSASTART=4
STEPPED=-1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0) 
PURPLE=(255,0,255)
WIDTH=20
HEIGHT=20
GRIDWIDTH=10
GRIDHEIGHT=10
learnrate = 0.1
itercount=5000
probab_update_constant=1.5
sejrnalezen=0
krysachcipla=0

MARGIN=5
buttonheight=20
TOTALGRIDWIDTH = MARGIN+(WIDTH+MARGIN)*GRIDWIDTH
TOTALGRIDHEIGHT=MARGIN+(HEIGHT+MARGIN)*GRIDHEIGHT


qlearnsize=GRIDWIDTH*GRIDHEIGHT
GREENSTEP=255//itercount
GREENSTEP+=1
print("Green step = {0}".format(GREENSTEP))
EnviMap=[]
AgentMem=[]
grid=[]
probabmatrix=[]
def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    

def TrueInd(i,j):
    return i*GRIDWIDTH+j

def Coors(fullindex):
    return [fullindex//GRIDWIDTH,fullindex%GRIDWIDTH]

numtraps=numpy.random.randint(0,int((GRIDHEIGHT+GRIDWIDTH)/2))**2
#numtraps=3
traplocs=[list(x) for x in numpy.random.randint([0,0],[GRIDHEIGHT,GRIDWIDTH],size=[numtraps,2])]
#traplocs=[[1,1],[2,2],[3,3]]

print("Traplocs = {0}".format(traplocs))
cheeseloc=[numpy.random.randint(0,GRIDHEIGHT),numpy.random.randint(0,GRIDWIDTH)]
print("Cheeseloc = {0}".format(cheeseloc))

while cheeseloc in traplocs:
    cheeseloc=[numpy.random.randint(0,GRIDHEIGHT),numpy.random.randint(0,GRIDWIDTH)]
    print("Cheeseloc = {0}".format(cheeseloc))

#cheeseloc=[3,1]
mouseloc=[numpy.random.randint(0,GRIDHEIGHT),numpy.random.randint(0,GRIDWIDTH)]
#mouseloc=[0,0]

print("Mouseloc = {0}".format(mouseloc))
while mouseloc in traplocs or mouseloc == cheeseloc:
    mouseloc=[numpy.random.randint(0,GRIDHEIGHT),numpy.random.randint(0,GRIDWIDTH)]
    print("Mouseloc = {0}".format(mouseloc))
origmouseloc=copy.deepcopy(mouseloc)
stepcounter=0

def NajdiSejra():
    global mouseloc
    ResetMouse()
    pathway=[]
    i=0
    while True:
    
        mouseindex = TrueInd(mouseloc[0], mouseloc[1])
        print("Epoch {2} Mouse is at {0} ({1})".format(mouseloc, mouseindex,i))
        indices = [a for a, x in enumerate(EnviMap[mouseindex]) if x != -1]
        print("Possible indices {0} ".format(indices))
        nextitem = numpy.max([AgentMem[mouseindex][ind] for ind in indices])
        nextindex=AgentMem[mouseindex].index(nextitem)
        print("Chosen index = {0}".format(nextindex))
       
        
        stepcounter=i+1
        grid[mouseloc[0]][mouseloc[1]]=STEPPED*stepcounter
        #print("Gridmap {0}".format(grid))
        mouseloc=Coors(nextindex)
        grid[mouseloc[0]][mouseloc[1]]=KRYSA
        pathway.append(mouseloc)
        print("----")
        if (mouseloc == cheeseloc):
            print("SEJR nalezen {0} Pathway {1}".format(mouseloc,pathway))
            break
        if (mouseloc in traplocs):
            print("Krysa chcipla {0} Pathway {1}".format(mouseloc,pathway))
            break
        if i > itercount:
            print("Krysa {0} nevi kde je syr :( {1}".format(mouseloc,pathway))
            break
        i+=1
    grid[origmouseloc[0]][origmouseloc[1]]=KRYSASTART

def ResetMouse():
    global mouseloc
    mouseloc=copy.deepcopy(origmouseloc)

    for i in range(GRIDHEIGHT):
        for j in range(GRIDWIDTH):
            if [i,j] == cheeseloc:
                grid[i][j]=SEJR
            elif [i,j] in traplocs:
                grid[i][j]=TRAP
            elif [i, j] == mouseloc:
                grid[i][j]=KRYSA
            else:
                grid[i][j]=FREE

def Learn():
    
    global mouseloc
    global stepcounter
    global krysachcipla
    global sejrnalezen
#    for i in range(itercount):
    ResetMouse()
    pathway = []
    i=0
    #for i in range((qlearnsize*(qlearnsize-1))):
    while True:
        print("Epoch {1} ITER: {0}".format(i,k))
        mouseindex = TrueInd(mouseloc[0],mouseloc[1])
        print("Mouse is at {0} ({1})".format(mouseloc,mouseindex))
        indices = [a for a, x in enumerate(EnviMap[mouseindex]) if x !=-1]
        #print("Possible indices {0} from {1}".format(indices,EnviMap[mouseindex]))
        #print("Possible indices {0} probabs {2} from {1}".format(indices,EnviMap[mouseindex],probabmatrix[mouseindex]))
        #nextindex = numpy.random.choice(indices,p=probabmatrix[mouseindex])
        
        borderline=k/itercount
        probab=numpy.random.uniform()
        if probab < borderline:
            nextitem = numpy.max([AgentMem[mouseindex][ind] for ind in indices])
            nextindex=AgentMem[mouseindex].index(nextitem)
            print("Chosen index {0} (prob {1})".format(nextindex,borderline))
            #print("Chosen index (prob {4}) = {0}({3}) from indices {1} ({2})".format(nextindex, indices,AgentMem[mouseindex] ,
            #                                                                AgentMem[mouseindex][nextindex],borderline))
        else:
            nextindex = numpy.random.choice(indices)
            #print("Chosen index = {0}({2}) from indices {1} ".format(nextindex,indices,EnviMap[mouseindex][nextindex]))
        #print("Chosen index = {0}({3}) from indices {1} probabs {2}".format(nextindex,indices,probabmatrix[mouseindex],EnviMap[mouseindex][nextindex]))
        #newprobabs=copy.deepcopy(probabmatrix[mouseindex])
        #if EnviMap[mouseindex][nextindex] <0:
        #    newprobabs[indices.index(nextindex)] /=probab_update_constant
        #elif EnviMap[mouseindex][nextindex] >0:
        #    newprobabs[indices.index(nextindex)] *=probab_update_constant
        #
        #norm_newprobabs=list(numpy.divide(newprobabs,numpy.sum(newprobabs)))
        #print("Probabs {0} -> {1} -> {2}".format(probabmatrix[mouseindex],newprobabs,norm_newprobabs))
        #probabmatrix[mouseindex]=copy.deepcopy(norm_newprobabs)
        
            
        nextindices = [b for b, x in enumerate(AgentMem[nextindex]) if EnviMap[nextindex][b] != -1]
        items=[AgentMem[nextindex][index] for index in nextindices]
        #print("Nextactions = {0} from {1} / {2}".format(nextindices,EnviMap[nextindex],AgentMem[nextindex]))
        #Qval = max([x for i, x in enumerate(EnviMap[nextindex])])
        Qval = max(items)
        print("Qval = {0} from {1}".format(Qval,items))
        stepcounter=i+1
        #print("AgentMem[{0},{1}] ({2}) = EnviMap[{0},{1}] ({3}) + {4} * {5}".format(mouseindex,nextindex,AgentMem[mouseindex][nextindex],EnviMap[mouseindex][nextindex],learnrate,Qval))
        AgentMem[mouseindex][nextindex]=EnviMap[mouseindex][nextindex] + learnrate*Qval
        #print("AgentMem[{0},{1}] ({2})".format(mouseindex,nextindex,AgentMem[mouseindex][nextindex]))
        grid[mouseloc[0]][mouseloc[1]]=STEPPED*stepcounter
        #print("Gridmap {0}".format(grid))
        mouseloc=Coors(nextindex)
        grid[mouseloc[0]][mouseloc[1]]=KRYSA
        pathway.append(mouseloc)
        #print("AgentMem:\n {0}".format('\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in AgentMem])))
        #print("EnviMap:\n {0}".format('\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in EnviMap])))
        #print("Probabs:\n {0}".format('\n'.join([''.join(['{:20}'.format(item) for item in row]) for row in probabmatrix])))
        
        if(mouseloc==cheeseloc):
            print("SEJR nalezen {0} Pathway {1}".format(mouseloc,pathway))
            sejrnalezen+=1
            break
        if(mouseloc in traplocs):
            print("Krysa chcipla {0} Pathway {1}".format(mouseloc,pathway))
            krysachcipla+=1
            break
        i+=1
        print("-------------")
    grid[origmouseloc[0]][origmouseloc[1]]=KRYSASTART    
    
  


for i in range(qlearnsize):
    EnviMap.append([])
    AgentMem.append([])
    for j in range(qlearnsize):
        EnviMap[i].append(-1)
        AgentMem[i].append(0)

for i in range(GRIDHEIGHT):
    grid.append([])
    for j in range(GRIDWIDTH):
        if [i,j] == cheeseloc:
            grid[i].append(SEJR)
        elif [i,j] in traplocs:
            grid[i].append(TRAP)
        elif [i, j] == mouseloc:
            grid[i].append(KRYSA)
        else:
            grid[i].append(FREE)
        print("Point {0} is {1}".format((i,j),grid[i][j]))

for i in range(GRIDHEIGHT):
    for j in range(GRIDWIDTH):
        neighbors = []
        if (i+1)<GRIDHEIGHT:
            neighbors.append([i + 1, j])
        if(i-1)>=0:
            neighbors.append([i - 1, j])
        if(j+1)<GRIDWIDTH:
            neighbors.append([i , j+1])
        if(j-1)>=0:
            neighbors.append([i , j-1])
        mainpoint = [i,j]
        maintotalindex=TrueInd(i,j)
        for nei in neighbors:
            totalindex =TrueInd(nei[0],nei[1])
            print("Point {0} ({1}) has neighbor {2} ({3})".format(mainpoint,maintotalindex,nei,totalindex))
            edgeval = 0
            if (grid[nei[0]][nei[1]] == SEJR):
                edgeval=5000
                print("Point ({0},{1}) Neighbor ({2},{3}) SEJR".format(i,j,nei[0],nei[1]))
            elif (grid[nei[0]][nei[1]] == TRAP):
                edgeval=-5000
                print("Point ({0},{1}) Neighbor ({2},{3}) TRAP".format(i,j,nei[0],nei[1]))
            
            
            EnviMap[maintotalindex][totalindex]=edgeval
        print("---")



print(EnviMap)
for i in range(qlearnsize):
    routecount=len([x for  x in EnviMap[i] if x !=-1])
    probabs = [1]*routecount
    norm_probabs = list(numpy.divide(probabs,numpy.sum(probabs)))
    probabmatrix.append(norm_probabs)
    print("{0} routes of probability {2} in {1}".format(routecount,EnviMap[i],norm_probabs))
    

pygame.init()
winwidth=TOTALGRIDWIDTH
winheight=(TOTALGRIDHEIGHT)+(MARGIN+buttonheight)*3+MARGIN
WINDOW_SIZE = [winwidth, winheight]
screen = pygame.display.set_mode(WINDOW_SIZE)
font = pygame.font.Font('freesansbold.ttf',20)
learn_button=(MARGIN,TOTALGRIDHEIGHT,TOTALGRIDWIDTH-MARGIN*2,buttonheight)
learnname, learnname_Rect = text_objects("Learn",BLACK)
learnname_Rect.center = winwidth/2 , ((learn_button[1]+learn_button[3])+learn_button[1])/2
test_button=(MARGIN,TOTALGRIDHEIGHT+MARGIN+buttonheight,TOTALGRIDWIDTH-MARGIN*2,buttonheight)
testname, testname_Rect = text_objects("Najit Sejra",BLACK)
testname_Rect.center = winwidth/2 , ((test_button[1]+test_button[3])+test_button[1])/2
reset_button=(MARGIN,TOTALGRIDHEIGHT+(MARGIN+buttonheight)*2,TOTALGRIDWIDTH-MARGIN*2,buttonheight)
resetname, resetname_Rect = text_objects("Reset mouse",BLACK)
resetname_Rect.center = winwidth/2 , ((reset_button[1]+reset_button[3])+reset_button[1])/2



pygame.display.set_caption("Kde je sejr")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
k=-1
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            
            if(column < GRIDWIDTH and row < GRIDHEIGHT):
                # Set that location to one
                if grid[row][column] == FREE:
                    print("Tu nic neni ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
                elif grid[row][column] == KRYSA:
                    print("Krysa ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
                elif grid[row][column]==TRAP:
                    print("Cvak ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
                elif grid[row][column]==SEJR:
                    print("SEJR ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
                elif grid[row][column]==KRYSASTART:
                    print("Odsud lezla krysa ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
                elif grid[row][column]<=STEPPED:
                    print("Tu byla krysa v kole {0}".format(-grid[row][column]), pos, "Grid coordinates: ", row, column)
                
                else:
                    print("Clicked non-white cell ({0})".format(grid[row][column]), pos, "Grid coordinates: ", row, column)
            else:
                if(pos[1] > learn_button[1] and pos[1] <= learn_button[1]+learn_button[3]):
                    print("Clicked learn button")
                    k=0
                    krysachcipla=0
                    sejrnalezen=0
                elif (pos[1] > test_button[1] and pos[1] <= test_button[1] + test_button[3]):
                    print("Clicked test button")
                    NajdiSejra()
                elif (pos[1] > reset_button[1] and pos[1] <= reset_button[1] + reset_button[3]):
                    print("Clicked reset button")
                    ResetMouse()
                else:
                    print("Clicked elsewhere")
                
                    
    if k >= 0:
        Learn()
        print("Epoch {0} ----".format(k))
        

 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(GRIDHEIGHT):
        for column in range(GRIDWIDTH):
            color = WHITE
            if grid[row][column] == FREE:
                color = WHITE
            elif grid[row][column] == KRYSA:
                color = BLUE
            elif grid[row][column]==TRAP:
                color=RED
            elif grid[row][column]==KRYSASTART:
                color=PURPLE                
            elif grid[row][column]==SEJR:
                color=YELLOW          
            elif grid[row][column]<=STEPPED:
                PATHCOLOR=GREENSTEP*(1+(-grid[row][column]))
                if PATHCOLOR > 255:
                    PATHCOLOR = 255
                color=(255-PATHCOLOR,255,255-PATHCOLOR)
                #print("Assigning color {0} to cell {1} ({2})".format(color,(row,column),grid[row][column]))
                color=GREEN
                
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.draw.rect(screen,GREEN,learn_button)
    pygame.draw.rect(screen, GREEN, test_button)
    pygame.draw.rect(screen, GREEN, reset_button)
    
    screen.blit(learnname,learnname_Rect)
    screen.blit(testname, testname_Rect)
    screen.blit(resetname, resetname_Rect)
    
    
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    if k >= 0:
        k+=1
        if k >= itercount:
            print("AgentMem:\n {0}".format('\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in AgentMem])))
            print("EnviMap:\n {0}".format('\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in EnviMap])))
            print("Krysa chcipla {0}x, sejr nalezen {1}x".format(krysachcipla,sejrnalezen))
            k=-1
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
