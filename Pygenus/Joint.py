from .Vectors2D import Vect2D as vec

class Spring():

    def __init__(self,anchor1,anchor2,length,stifness,damping):
        self.anchor_1=anchor1
        self.anchor_2=anchor2
        self.length=length
        self.stifness=stifness
        self.dampening=damping
    
    def solve_joint(self):
        link=(self.anchor_1.position).get_linking_vector(self.anchor_2.position)
        n=link.normalise()
        self.anchor_1.force -= ((self.length-link.magnitude)*self.stifness-((self.anchor_1.linear_velocity).get_linking_vector(self.anchor_2.linear_velocity)).dot(n)*self.dampening)*n
        self.anchor_2.force += ((self.length-link.magnitude)*self.stifness-((self.anchor_1.linear_velocity).get_linking_vector(self.anchor_2.linear_velocity)).dot(n)*self.dampening)*n