
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
    object.velocity += object.acceleration*dt
    object.position += object.linear_velocity*dt
    return

#Implicit Euler
def IE(object,dt):
    return

#Verlet integration
def Verlet(object,dt):
    object.velocity=object.position-object.old_position
    object.old_position=object.position
    object.position=object.position+object.velocity*dt+object.acceleration*dt**2
    return

#Runge-Kutta 4 Method
def RK4M(object,dt):
    return

#Midpoint Method
def Midpoint(object):
    return