from Vectors2D import Vect2D as vec

class Mesh:
    def __init__(self,object):
        self.center = object.position
        self.object=object
    
    def actualise_pos(self):
        self.center=self.object.position

class Circle(Mesh):
    def __init__(self,object,r):
        super().__init__(object)
        self.radius=r
        return

class Rectangle(Mesh):
    def __init__(self,object,width,height):
        super().__init__(object)
        self.width=width
        self.height=height
        return
    