from Body import *
from Mesh import *
from Joint import *
from Vectors2D import Vect2D as vec
import Collision_detection as check
import math
import Quarky_math_unit as math2

class Monde:
    RECTANGULAR=1
    CIRCULAR=2
    
    def __init__ (self,rectangle:"vec",radius:float,center:"vec",deload_radius:float,type):
        
        self.rectangle=rectangle
        self.radius=radius
        self.center=center
        self.deload_radius=deload_radius
        self.type=type
        
        self.Objects=[]
        self.Joints=[]
        return

    def add_object(self,object:"RigidBody",shape:"Mesh"):
        self.Objects.append([object,shape])
        return
    
    def append_objects(self,list:list["RigidBody","Mesh"]):
        for object in len(list):
            self.Objects.append(object)
        return
    
    def remove_body(self,body):
        self.Objects[0].pop(self.Objects[0].index(body))
        return

    def remove_mesh(self,mesh):
        self.Objects[1].pop(self.Objects[1].index(mesh))

    def add_joints(self,joint):
        self.Joints.append(joint)
        
    def remove_joint(self,joint):
        self.Joints.remove(self.joints.index(joint))

    def append_joints(self,list:list):
        for joint in len(list):
            self.Joints.append(joint)
        return

    def deload_object(self,object,shape):
        if self.type== self.RECTANGULAR:
            if object.position.x>self.rectangle.x+self.deload_radius or object.position.x < -self.deload_radius or object.position.y>self.rectangle.y+self.deload_radius or object.position.y<0-self.deload_radius:
                self.remove_object(object,shape)
        elif self.type == self.CIRCULAR:
            if (object.position.get_linking_vector(self.center)).magnitude>=self.radius+self.deload_radius:
                self.remove_object(object,shape)
        return
    
    def apply_constraints(self,body,shape):
        if self.type==self.CIRCULAR:
            to_object= self.center-body.position
            if to_object.magnitude>=(self.radius-shape.radius):
                n = vec.normalise(to_object)
                impulse=((-(1+body.restitution)*body.linear_velocity).dot(n))/(n.dot(n*1/body.mass))
                body.linear_velocity= body.linear_velocity+(impulse/body.mass)*n
                body.position += n*(to_object.magnitude-(self.radius-shape.radius))
        
        if self.type==self.RECTANGULAR:
            #The following formulas are derived from the impulse formula
            if body.position.x+shape.radius>self.rectangle.x:
                body.linear_velocity.x -= (1+body.restitution)*body.linear_velocity.x
                body.position.x -= (body.position.x+shape.radius-self.rectangle.x)
            
            if body.position.x-shape.radius<0:
                body.linear_velocity.x -= (1+body.restitution)*body.linear_velocity.x
                body.position.x += (shape.radius-body.position.x)

            if body.position.y+shape.radius>self.rectangle.y:
                body.linear_velocity.y -= (1+body.restitution)*body.linear_velocity.y
                body.position.y -= (body.position.y+shape.radius-self.rectangle.y)
            
            if body.position.y-shape.radius<0:
                body.linear_velocity.y -= (1+body.restitution)*body.linear_velocity.y
                body.position.y += (shape.radius-body.position.y)
        
        return

class Newton_Monde(Monde):
    def __init__(self,rectangle:"vec",radius:float,center:"vec",deload_radius:float,type,gravity:"vec"= vec(0,20)):
        super().__init__(rectangle,radius,center,deload_radius,type)
        self.gravity=gravity

    def update(self,t):
        for joint in self.Joints:
            joint.solve_joint()
        for object in self.Objects:
            self.resolve_linear_motion(object[0],t)
            self.apply_constraints(object[0],object[1])
            #self.resolve_angular_motion(body,t)
            self.deload_object(object[0],object[1])
            object[1].actualise_pos()
        check.resolve_collisions(self.Objects)
    
    def resolve_linear_motion(self,body,t):
        body.force += self.gravity*body.mass
        body.linear_velocity += body.force*t/body.mass
        body.position += body.linear_velocity*t
        body.force=vec.null()
        if body.linear_velocity.magnitude>=500:
            body.linear_velocity = body.linear_velocity*(500/body.linear_velocity.magnitude)
        return
    
    def resolve_angular_motion(self,body,t):
        body.torque += "???"
        body.angular_velocity += body.torque*t/body.inertia
        body.angle += (body.angular_velocity*t)
        body.torque= 0
        return