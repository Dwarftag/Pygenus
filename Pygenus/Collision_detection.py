from .Vectors2D import Vect2D as vec


def resolve_collisions(Objects:list):
    for i in range(0,len(Objects)-1):
        for j in range(i+1,len(Objects)):
            
            B1= Objects[i][0]
            B2= Objects[j][0]
            M1= Objects[i][1]
            M2= Objects[j][1]

            Vector=(M1.center).get_linking_vector(M2.center)
            S= M1.radius+M2.radius

            if Vector.magnitude<= S :
                n = vec.normalise(Vector)
                impulse=n.dot((-1-B1.restitution*B2.restitution)*(B1.linear_velocity-B2.linear_velocity))/n.dot(n*(1/B1.mass+1/B2.mass))
                B1.linear_velocity= B1.linear_velocity+(impulse/B1.mass)*n
                B2.linear_velocity= B2.linear_velocity-(impulse/B2.mass)*n
                displacement= S -Vector.magnitude
                B1.position-=(displacement*(B2.mass/(B1.mass+B2.mass)))*n
                B2.position+=(displacement*(B1.mass/(B1.mass+B2.mass)))*n
                M1.actualise_pos()
                M2.actualise_pos()
    return