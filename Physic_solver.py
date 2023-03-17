from Body import *
from Mesh import *
from Joint import *
from Vectors2D import Vect2D as vec
import Collision_detection as check
import math
import Quarky_math_unit as math2

class Monde:
    CONFIG = {
        "world_type":"rectangle",
        "deload_radius":20,
        "cap_speed":500,
        "n_substeps":1,
        
        "rect_config":{
            "dimension":vec(200,200)
        },

        "circle_config":{
            "center":vec(250,250),
            "radius":250,
        },

        "integration_method":"EM",
        "collision_detection":"brute",

    }
    
    def __init__ (self):
        
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

    def remove_object(self,body,shape):
        self.Objects.pop(self.Objects.index([body,shape]))
        return


    def add_joints(self,joint):
        self.Joints.append(joint)
        
    def remove_joint(self,joint):
        self.Joints.remove(self.joints.index(joint))

    def append_joints(self,list:list):
        for joint in len(list):
            self.Joints.append(joint)
        return


    def deload_object(self,object,shape):
        if self.CONFIG.get("world_type")=="rectangle":
            if object.position.x>(self.CONFIG["rect_config"].get("dimension")).x+self.CONFIG.get("deload_radius") or object.position.x<-self.CONFIG.get("deload_radius") or object.position.y>(self.CONFIG["rect_config"].get("dimension")).y+self.CONFIG.get("deload_radius") or object.position.y<-self.CONFIG.get("deload_radius"):
                self.remove_object(object,shape)
        elif self.CONFIG.get("world_type") == "circle":
            if (object.position.get_linking_vector(self.CONFIG["circle_config"].get("center"))).magnitude>=self.radius+self.deload_radius:
                self.remove_object(object,shape)
        else:
            raise Exception("Unknown 'world_type' in CONFIG")
        return
    
    def apply_constraints(self,body,shape):
        if self.CONFIG.get("world_type")=="circle":
            to_object= self.CONFIG["circle_config"].get("center")-body.position
            if to_object.magnitude>=self.CONFIG["circle_config"].get("radius"):
                n = vec.normalise(to_object)
                impulse=((-(1+body.restitution)*body.linear_velocity).dot(n))/(n.dot(n*1/body.mass))
                body.linear_velocity= body.linear_velocity+(impulse/body.mass)*n
                body.position += n*(to_object.magnitude-(self.radius-shape.radius))
        
        if self.CONFIG.get("world_type")=="rectangle":
            #The following formulas are derived from the impulse formula
            if body.position.x>(self.CONFIG["rect_config"].get("dimension")).x:
                body.linear_velocity.x -= (1+body.restitution)*body.linear_velocity.x
            
            if body.position.x<0:
                body.linear_velocity.x -= (1+body.restitution)*body.linear_velocity.x

            if body.position.y>(self.CONFIG["rect_config"].get("dimension")).y:
                body.linear_velocity.y -= (1+body.restitution)*body.linear_velocity.y
            
            if body.position.y<0:
                body.linear_velocity.y -= (1+body.restitution)*body.linear_velocity.y
        
        return

class Gravity_Monde(Monde):
    def __init__(self,gravity):
        super().__init__()
        self.gravity=gravity

    def update(self,t):
        N=self.CONFIG.get("n_substeps")
        for i in range (0,N):
            for joint in self.Joints:
                joint.solve_joint()
            for object in self.Objects:
                self.resolve_linear_motion(object[0],t/N)
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