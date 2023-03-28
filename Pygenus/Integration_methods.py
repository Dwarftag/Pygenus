
IM_Dictionnary={}

def null():
    return

#Explicit Euler method
def EEM(object,dt):
    object.position += object.linear_velocity*dt
    object.velocity += object.acceleration*dt
    return

#Improved Euler method
def IEM(object,dt):
    return

#Semi-implicit Euler
def SIE(object,dt):
    object.linear_velocity += object.acceleration*dt
    object.position += object.linear_velocity*dt
    return

#Implicit Euler
def IE(object,dt):
    return

#Verlet integration
def Verlet(object,dt):
    object.linear_velocity=object.position-object.old_position
    object.old_position=object.position
    object.position += object.linear_velocity+object.acceleration*(dt**2)
    return

#Runge-Kutta 4 Method
def RK4M(object,dt):
    return

#Midpoint Method
def Midpoint(object,dt):
    return

def solve_motion(IM:str,body,dt:float):
    a = IM_Dictionnary.get(IM)
    if type(a)!=type(null):
        raise Exception("Could not find a valid integration method")
    else:
        a(body,dt)

def add_method(key:str,method):
    IM_Dictionnary[key]=method
    return 0

def remove_method(key:str):
    IM_Dictionnary.pop(key) 