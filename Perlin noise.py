import math,random
from operator import mul
angularGain=1
angularDecay=1+1/16
cameraOrientation=[[1,0,0,0],[0,0,0]] #position and velocity (by the sine of which position is multiplied each frame)
dims=3
size=math.floor(64**(1/dims))
normalisation=0
smoothness=1
perlin=[0]*size**dims
vectorField=[]
print("testing")
pi=3.1415926535897932384626433832795028841971693993751058209749445923 #should work (is only working in floating points)

def randomUnitVector():
    direction=random.random()*2*pi
    z=random.random()*2-1
    magnitude=1-z**2
    return [magnitude*math.cos(direction-pi/2*i) for i in range(2)]+[z] #(the sign is a subtle reference to Euler's constant)

def dotProduct(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])

def weight(position,vector,fieldSize): #it has direction and magnitude (oh yeah)
    i=0
    for di in range(dims):
        i*=fieldSize
        i+=vector[di]%fieldSize
    return dotProduct([vector[di]-position[di] for di in range(dims)],vectorField[i])

def interpolate(a,b,width):
    if smoothness==0:
        interpolation=width
    elif smoothness==1:
        interpolation=(3-2*width)*width**2
    elif smoothness==2:
        interpolation=(width*(width*6-15)+10)*width**3
    return (b-a)*interpolation+a

def doInterpolation(position,vector,fieldSize):
    binaryCounter=[0]*dims
    interpolations=[0]*dims
    for u in range(2**dims):
        interpolated=weight(position,[math.floor(position[di]+binaryCounter[di]) for di in range(dims)],fieldSize)
        i=0
        while i<len(binaryCounter) and binaryCounter[i]==1:
            binaryCounter[i]=0
            interpolated=interpolate(interpolations[i],interpolated,position[i]%1)
            i+=1
        if i<len(binaryCounter):
            binaryCounter[i]=1
            interpolations[i]=interpolated
    return interpolated

def overlayPerlin(fieldSize,magnitude):
    global vectorField
    vectorField=[]
    for u in range(fieldSize**dims):
            vectorField.append(randomUnitVector())
    samplingGranularity=size/fieldSize
    dis=[-0.5]*dims
    di=0
    i=0
    while True:
        perlin[i]+=doInterpolation(dis,vectorField,fieldSize)
        i+=1
        dis[di]+=1/samplingGranularity
        if dis[di]>size:
            di+=1
            if di==dims:
                exit()
        else:
            di=0
overlayPerlin(4, 1)
print(perlin)