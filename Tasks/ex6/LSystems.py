import copy
import math
import turtle
import time
import numpy

class LSystem:
    def __init__(self, angle,axiom,rules):
        self.angle = angle
        self.axiom = axiom
        self.rules = rules
    
    def Expand(self,iterations):
        result=copy.deepcopy(self.axiom)
        print("Initial: {}".format(result))
        for i in range(iterations):
            for k in self.rules.keys():
                result=result.replace(k,self.rules[k])
                print("Iter {} len {}".format(i,len(result)))
        return result




def RadianToDegree(radian):
    return 180*radian/math.pi

stack=[]
hrange=[0,0]
vrange=[0,0]
def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "[":
            stack.append((aTurtle.position(),aTurtle.heading()))
            #print("Saving position {}".format(aTurtle.position()))
            #print("Saving angle {}".format(aTurtle.heading()))
            
        elif cmd=="]":
            item=stack.pop()
            aTurtle.setposition(item[0])
            aTurtle.setheading(item[1])
        pos = aTurtle.position()
        if pos[0] < hrange[0]:
            hrange[0]=pos[0]
        if pos[0] > hrange[1]:
            hrange[1]=pos[1]
        if pos[1] < vrange[0]:
            vrange[0]=pos[1]
        if pos[1] > vrange[1]:
            vrange[1]=pos[1]
        scrsize=turtle.screensize()
        print("New borders X{} Y{} size {}".format(hrange,vrange,scrsize))
        if numpy.sum(numpy.abs(hrange)) > scrsize[0]:
            turtle.screensize( numpy.max(numpy.abs(hrange))*2,scrsize[1])
            print("Width updated from {} to {}",scrsize,turtle.screensize())
        if numpy.sum(numpy.abs(vrange)) > scrsize[1]:
            turtle.screensize(scrsize[0], numpy.max(numpy.abs(vrange))*2)
            print("Height updated from {} to {}",scrsize,turtle.screensize())
        
            
systemA = LSystem(90,"F+F+F+F",{"F":"F+F-F-FF+F+F-F"})
systemB = LSystem(60,"F++F++F",{"F":"F+F--F+F"})
systemC = LSystem(RadianToDegree(math.pi/7),"F",{"F":"F[+F]F[-F]F"})
systemD = LSystem(RadianToDegree(math.pi/8),"F",{"F":"FF+[+F-F-F]-[-F+F+F]"})
systemE = LSystem(111,"F",{"F":"F--FB[F+F+F+F+F]+[+F-F-F]-FB+-[F+F-B]FF[-F+F+F]"})


    


def main():
    instruct = systemC.Expand(10)   # create the string

    dist=4
    tortspeed=00
    print(len(instruct))
    time.sleep(3)
    #print(instruct)
    tortoise = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    turtle.screensize(1000,500)
    tortoise.up()
    tortoise.setheading(0)
    leftside = turtle.screensize()[0]/2
    tortoise.setposition(-leftside,00)
    tortoise.down()
    tortoise.speed(tortspeed)
    print("Init point {}".format(tortoise.position()))
    print(turtle.screensize())
    drawLsystem(tortoise,instruct,systemB.angle,dist)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()



