from PIL import Image
from numpy import complex, array
import colorsys
  
# setting the width of the output image as 1024
WIDTH = 1024
itercount = 100

winwidth=700
winheight=int((winwidth/3.5) *2)
# a function to return a tuple of colors
# as integer value of rgb
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


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
    
    
# function defining a mandelbrot
def mandelbrot(x, y,iters):
    c = complex(x, y)
    z = 0
    for i in range(1, iters):
        if abs(z) > 2:
            return rgb_conv(i)
        z = z**2 + c
    return (0, 0, 0) #black
  
# creating the new image in RGB mode
#img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
img = Image.new('RGB', (winwidth, winheight))

pixels = img.load()
  
for x in range(img.size[0]):
  
    # displaying the progress as percentage
    #print("%.2f %%" % (x / WIDTH * 100.0)) 
    print("%.2f %%" % (x / winwidth * 100.0)) 
    
    for y in range(img.size[1]):
        #pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4),    (y - (WIDTH / 4)) / (WIDTH / 4),itercount)
        point = Rescale((x,y),(-2.5,1),(-1,1))
        pixels[x, y] = mandelbrot(point[0],point[1],itercount)
# to display the created fractal after 
# completing the given number of iterations
img.show()