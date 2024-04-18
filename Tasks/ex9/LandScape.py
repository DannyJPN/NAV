import numpy
import matplotlib.pyplot as plt
import time

BLACKEST = (30, 30, 30)
WHITEST = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)



iterations=25
lines= 3
linelen=100

scale=1
roughness=0.6

def GetBaseLine(linelen,height):
    return [[-linelen/2,height],[linelen/2+1,height]]
    
def ColorToHex(colortuple):
    return '#%02x%02x%02x' % colortuple

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
    

def LandScape(line,iters,maxshift,roughness,scale):
    start = time.time()

    minishift = -maxshift
    maxishift=maxshift+1
    newpoints = {}
    print(line)
    print("Scale begin {}".format(scale))
    for it in range(iters):
        
        
        for i in range(len(line)-1):
            shift = (numpy.random.random()*2-1)*scale
            new = [(line[i][0]+line[i+1][0])/2,(line[i][1]+line[i+1][1])/2+shift]
            #print("New point {}".format(new))
            newpoints[i+1]=new
            scale*=roughness
            #print("New scale {}".format(scale))
        print("Generating done")
        for i,p in reversed(newpoints.items()):
            #print("Insert point {} on position {}".format(p,i))
            line.insert(i,p)
        #print("Iter {}  =  {}".format(it,line))
        end = time.time()
        print("Iter {} ({})".format(it,end-start))
        #print("----")
    return line
    
xs=[]
ys=[]
colorstep=   (ColorToSingle(WHITEST)-ColorToSingle(BLACKEST))//lines
print("COLORSTEP {}".format(colorstep))
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot()
linecolor = ColorToSingle(WHITEST)
for i in reversed(range(lines)):
    points=GetBaseLine(linelen,i*4)
    finalline=LandScape(points,iterations-i,i,roughness**(lines-i),scale*i*2)
    x=list(numpy.array(points)[:,0])
    y=list(numpy.array(points)[:,1])
    ax.plot(x, y,color=ColorToHex(BLACKEST),marker=".")
    ax.fill_between(x,y,color=numpy.divide(ColorToRGB(linecolor),256))
    
    
    
    linecolor -= colorstep
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')


plt.show()