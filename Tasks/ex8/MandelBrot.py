import pygame
import cmath

diam=2
iters=10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

# Set the HEIGHT and WIDTH of the screen
winwidth=700
winheight=int((winwidth/3.5) *2)
WINDOW_SIZE = [winwidth, winheight]
def NewPoint(point,constant):
    complexpoint = complex(point[0],point[1])
    complexconstant = complex(constant[0],constant[1])
    newpoint= complexpoint**2 + complexconstant
    return (newpoint.real,newpoint.imag)
    



def ColorToSingle(RGB):
    color=0
    for i in range(len(RGB)):
        color+=RGB[i]*(256**(len(RGB)-i-1))
    return color


def ColorToRGB(colornum):
    color=[]
    while colornum > 0:
        col=colornum%256
        colornum//=256
        color.append(col)
    return tuple(reversed(color))

STEP=   ColorToSingle(WHITE)//iters
print("STEP = {}".format(STEP))

def AssignColor(iteration,escaped):
    color=BLACK
    if not escaped:
        color=BLACK
    else:
        colorcode = ColorToSingle(WHITE)-STEP*iteration
        
        color = ColorToRGB(colorcode)
        #print("Color code {} {}".format(hex(colorcode),color))
    return color

def Rescale(point,widthscales,heightscales):
    widthscales=list(widthscales)
    heightscales=list(heightscales)
    widthscales.sort()
    heightscales.sort()
    
    widthrange = (widthscales[1]-widthscales[0])
    widthratio = widthrange/winwidth
    heightrange = (heightscales[1]-heightscales[0])
    heightratio = heightrange/winheight
    scalepoint=(point[0]*widthratio+widthscales[0],point[1]*heightratio+heightscales[0])
    return scalepoint
        

def Mandelbrot(winwidth,winheight,iters):
    pixelmap = [[0]*winwidth]*winheight

    for pixy in range(winheight):
        for pixx in range(winwidth):

            cpoint = Rescale((pixx,pixy),(-2.5,1),(-1,1))
            zpoint=(0,0)
            escpoint=False
            escape = diam**2
            for it in range(iters):
                if (zpoint[0]**2+zpoint[1]**2) > escape:
                    escpoint=True
                    print("Point {} escaped in {} iters".format((pixx,pixy),it+1))
                    break
                    
                zpoint=NewPoint(zpoint,cpoint)
            if not escpoint:
                print("Point {} remained for {} iters".format((pixx,pixy),it+1))
            pixelmap[pixy][pixx]=ColorToSingle(AssignColor(it,escpoint))
            #print("Point {} got color {}".format((pixx,pixy),hex(pixelmap[pixy][pixx])))
    return pixelmap
pixelmap = Mandelbrot(winwidth,winheight,iters)    
pygame.init()



screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Mandelbrot")
surf = pygame.Surface((winwidth,winheight))



 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
done = False
# -------- Main Program Loop -----------
while not done:
    pxarray = pygame.PixelArray(surf)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEWHEEL:
            # User clicks the mouse. Get the position
            if event.y > 0:
                print("Scroll up")
            elif event.y < 0:
                print("Scroll down")
            else:
                print("Wheel click")
        
 
    # Set the screen background
    screen.fill(BLACK)
    for pixy in range(winheight):
        for pixx in range(winwidth):
            pxarray[pixx,pixy]=pixelmap[pixy][pixx]
    img = pxarray.make_surface()
    screen.blit(img,(0,0))
    pxarray.close()
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
