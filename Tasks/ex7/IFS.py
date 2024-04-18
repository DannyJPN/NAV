import numpy
import matplotlib.pyplot as plt


AffineMatrixA=[

 
[0.00,0.00,0.01,0.00,0.26,0.00,0.00,0.00,0.05,0.00,0.00,0.00],
[0.20,-0.26,-0.01,0.23,0.22,-0.07,0.07,0.00,0.24,0.00,0.80,0.00],
[-0.25,0.28,0.01,0.26,0.24,-0.07,0.07,0.00,0.24,0.00,0.22,0.00],
[0.85,0.04,-0.01,-0.04,0.85,0.09,0.00,0.08,0.84,0.00,0.80,0.00]
 
]
AffineMatrixB=[
[0.05,0.00,0.00,0.00,0.60,0.00,0.00,0.00,0.05,0.00,0.00,0.00],
[0.45,-0.22,0.22,0.22,0.45,0.22,-0.22,0.22,-0.45,0.00,1.00,0.00],
[-0.45,0.22,-0.22,0.22,0.45,0.22,0.22,-0.22,0.45,0.00,1.25,0.00],
[0.49,-0.08,0.08,0.08,0.49,0.08,0.08,-0.08,0.49,0.00,2.00,0.00]
]


def GeneratePoints(dimension,pointcount,mini,maxi):
    pointlist = list(list(x) for x in numpy.round(numpy.random.rand(pointcount,dimension),2)*(maxi-mini)+mini)
    return pointlist

def ApplyMatrix(matrix,vect):
    row = numpy.random.randint(len(matrix))
    #print("{0}. row = {1}".format(row,matrix[row]))
    
    affinetrans=numpy.reshape(matrix[row][0:(len(vect)**2)],(len(vect),len(vect)))
    #print(affinetrans)
    midtrans=numpy.matmul(affinetrans,numpy.reshape(vect,(-1,1)))
    #print(midtrans)
    lasttrans=numpy.reshape(matrix[row][-len(vect):],(-1,1))
    #print(lasttrans)
    finalpoint=numpy.add(midtrans,lasttrans)
    #print(finalpoint)
    return finalpoint

w = GeneratePoints(3,1,-10,10)[0]
w=[0,0,0]
print("Init point {0} len {1}".format(w,len(w)))


iterations=50000
points=[]
points.append(w)
for i in range(iterations):
    nextw=ApplyMatrix(AffineMatrixA,w)
    points.append(numpy.reshape(nextw,(1,-1))[0])
    w=nextw

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
xs=[]
ys=[]
zs=[]
pidx=0
for p in points:
    print("Point {} = {} ".format(pidx,p))
    
    x=p[0]
    y=p[1]
    z=p[2]
    
    xs.append(x)
    ys.append(y)
    zs.append(z)
    pidx+=1
    
    
ax.scatter(xs, ys, zs, marker="o",color="blue")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()