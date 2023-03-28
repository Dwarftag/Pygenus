import math

class Vect2D():

    x=float
    y=float

    def __init__(self,coordx,coordy):
        self.x=coordx
        self.y=coordy
        return
        
    def __eq__(self,other:"Vect2D")->bool:
        if type(other)==Vect2D:   
            if other.x==self.x and other.y==self.y:
                return True
            else:
                return False
        else:
            raise TypeError("unsupported operand type(s) for =: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'Vect2D'")
    
    def __neq__(self,other:"Vect2D")->bool:
        if type(other)==Vect2D:   
            if other.x!=self.x or other.y!=self.y:
                return True
            else:
                return False
        else:
            raise TypeError("unsupported operand type(s) for !=: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'Vect2D'")

    def __repr__(self) ->str:
        return"Vect2d(%s, %s)" % (self.x, self.y)

    def __add__(self,other:("Vect2D" or tuple[float,float]))->"Vect2D":
        if type(other)==Vect2D:
            return Vect2D(self.x+other.x,self.y+other.y)
        elif type(other)==tuple:
            if len(other)==2:
                return Vect2D(self.x+other[0],self.y+other[1])
            else:
                raise Exception("The tuple is not two dimensionnal")
        else:
            raise TypeError("unsupported operand type(s) for +: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'Vect2D' or 'tuple'")

    def __sub__(self,other:("Vect2D" or tuple[float,float]))->"Vect2D":
        if type(other)==Vect2D:
            return Vect2D(self.x-other.x,self.y-other.y)
        elif type(other)==tuple:
            if len(other)==2:
                return Vect2D(self.x-other[0],self.y-other[1])
            else:
                raise Exception("The tuple is not two dimensionnal")
        else:
            raise TypeError("unsupported operand type(s) for -: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'Vect2D'or 'tuple' ")
    
    def __mul__(self,other:float)->"Vect2D":
        if type(other)==float or type(other)==int:
            return Vect2D(self.x*other,self.y*other)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'float'")
    
    def __truediv__(self,other:float)->"Vect2D":
        if type(other)==float or type(other)==int:
            if other !=0:
                return Vect2D(self.x/other,self.y/other)
            else:
                raise ZeroDivisionError("What is wrong with u?")
        else:
            raise TypeError("unsupported operand type(s) for /: 'Vect2D' and "+str(type(other))+"\n Excpected 'Vect2D' and 'float'")
        
    def __radd__(self,other:("Vect2D" or tuple[float,float]))->"Vect2D":
        if type(other)==Vect2D:
            return Vect2D(self.x+other.x,self.y+other.y)
        elif type(other)==tuple:
            if len(other)==2:
                return Vect2D(self.x+other[0]+self.y+other[1])
            else:
                raise Exception("The tuple is not two dimensionnal")
        else:
            raise TypeError("unsupported operand type(s) for +: "+str(type(other))+" and 'Vect2D'"+"\n Excpected 'Vect2D' or 'tuple' and 'Vect2D' ")

    def __rsub__(self,other:("Vect2D" or tuple[float,float]))->"Vect2D":
        if type(other)==Vect2D:
            return Vect2D(self.x-other.x,self.y-other.y)
        elif type(other)==tuple:
            if len(other)==2:
                return Vect2D(self.x-other[0],self.y-other[1])
            else:
                raise Exception("The tuple is not two dimensionnal")
        else:
            raise TypeError("unsupported operand type(s) for -: "+str(type(other))+" and 'Vect2D'"+"\n Excpected 'Vect2D' or 'tuple' and 'Vect2D' ")
    
    def __rmul__(self,other:float)->"Vect2D":
        if type(other)==float or type(other)==int:    
            return Vect2D(self.x*other,self.y*other)
        else:
            raise TypeError("unsupported operand type(s) for *: "+str(type(other))+" and 'Vect2D'"+"\n Excpected 'float' and 'Vect2D' ")
    
    def __rtruediv__(self,other:float)->"Vect2D":
        if type(other)==float or type(other)==int:
            if other !=0:
                return Vect2D(self.x/other,self.y/other)
            else:
                raise ZeroDivisionError("What is wrong with u?")
        else:
            raise TypeError("unsupported operand type(s) for /: "+str(type(other))+" and 'Vect2D'"+"\n Excpected 'float' and 'Vect2D' ")


    @property
    def magnitude(self)->float:
        return math.sqrt(self.x**2+self.y**2)
    
    @property
    def angle(self)->float:
        if self==Vect2D(0,0):
            return 0
        else:
            return math.acos(self.x/self.magnitude)


    def normal(self)->"Vect2D":
        if self==Vect2D(0,0):
            raise Exception("The null vector has infintely many normals")
        else:
            return Vect2D(-self.y,self.x)

    def normalise(self)->"Vect2D":
        if self==Vect2D(0,0):
            raise Exception("The null vector cannot be normalised")
        else:
            return Vect2D(self.x/self.magnitude,self.y/self.magnitude)

    def normal_normalise(self)->"Vect2D":
        if self==Vect2D(0,0):
            raise Exception("Choose your poison for the null vector")
        return Vect2D(-self.y/self.magnitude,self.x/self.magnitude)

    def cross(self, other:"Vect2D") -> float:
        if type(other)==Vect2D:
            return (self.x*other.y-self.y*other.x)
        else:
            raise TypeError("The cross product is only supported with  another 'Vect2D' not with "+str(type(other)))
    
    def dot(self, other:"Vect2D") -> float:
        if type(other)==Vect2D:
            return (self.x*other.x+self.y*other.y)
        else:
            raise TypeError("The dot product is only supported with another 'Vect2D' not with " +str(type(other)))


    def get_distance(self, other:("Vect2D" or tuple[float,float])) -> float:
        if type(other)==Vect2D:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        else:
            raise TypeError("The distance is only supported for 'Vect2D' or 'tuple' not "+str(type(other)))

    def get_linking_vector(self,other:"Vect2D")->"Vect2D":
        if type(other)==Vect2D:
            return Vect2D(other.x-self.x,other.y-self.y)
        else:
            raise TypeError("The linking vector is only supported for 'Vect2D' not "+str(type(other)))

    def rotate(self,angle:float)->"Vect2D":
        if type(angle)==(float or int):
            if(self!=Vect2D(0,0)):            
                return Vect2D(self.magnitude*math.cos(self.angle+angle),self.magnitude*math.sin(self.angle+angle))
            else:
                raise Exception("Cannot rotate the null vector")
        else:
            raise TypeError("Can only rotate a vector by a 'float' not by "+str(type(angle)))
    
    
    def tuple(self)->tuple:
        return (self.x,self.y)
    
    def list(self)->list:
        return [self.x,self.y]
    
    def complex(self)->complex:
        return complex(self.x,self.y)
    
    def polar_form(self):
        return (self.magnitude,self.angle)


    @staticmethod
    def null()->"Vect2D":
        return Vect2D(0,0)
    
    @staticmethod
    def unitx()->"Vect2D":
        return Vect2D(1,0)
    
    @staticmethod
    def unity()->"Vect2D":
        return Vect2D(0,1)

    @staticmethod
    def unit()->"Vect2D":
        return Vect2D(1,1)