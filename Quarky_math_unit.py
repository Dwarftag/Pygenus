import math

def Clamp(n,min,max):
    if n<min:
        n=min
    if n>max:
        n=max
    return n

def area_of_circle(r):
    return math.pi**2*r

def area_of_rectangle(length,width):
    return length*width