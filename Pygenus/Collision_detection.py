from .Vectors2D import Vect2D as vec

def resolve_collisions(Objects:list):
    for i in range(0,len(Objects)-1):
        for j in range(i+1,len(Objects)):
            Test1=Objects[i][0]
            Test2=Objects[j][0]
            Vector=(Test1.position).get_linking_vector(Test2.position)
            if Vector.magnitude<=10:
                n = vec.normalise(Vector)
                impulse=n.dot((-1-Test1.restitution*Test2.restitution)*(Test1.linear_velocity-Test2.linear_velocity))/n.dot(n*(1/Test1.mass+1/Test2.mass))
                Test1.linear_velocity= Test1.linear_velocity+(impulse/Test1.mass)*n
                Test2.linear_velocity= Test2.linear_velocity-(impulse/Test2.mass)*n
                displacement=10-Vector.magnitude
                Test1.position-=(displacement*(Test2.mass/(Test1.mass+Test2.mass)))*n
                Test2.position+=(displacement*(Test1.mass/(Test1.mass+Test2.mass)))*n
    return