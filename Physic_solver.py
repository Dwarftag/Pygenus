from Body import *
from Mesh import *
from Joint import *
from Vectors2D import Vect2D as vec
import Collision_detection as check
import math
import Quarky_math_unit as math2
import Integration_methods as Im

class Monde:
    CONFIG = {
        "world_type":"circle",
        "deload_radius":20,
        "cap_speed":500,
        "n_substeps":1,
        
        "rect_config":{
            "dimension":vec(200,200)
        },

        "circle_config":{
            "center":vec(50,50),
            "radius":50,
        },

        "integration_method":"Verlet",
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
            if (object.position.get_linking_vector(self.CONFIG["circle_config"].get("center"))).magnitude>=self.CONFIG["circle_config"].get("radius")+self.CONFIG.get("deload_radius"):
                self.remove_object(object,shape)
        else:
            raise Exception("Unknown 'world_type' in CONFIG")
        return
    
    def apply_constraints(self,body,shape):
        if self.CONFIG.get("world_type")=="circle":
            to_object= self.CONFIG["circle_config"].get("center")-body.position
            radius=self.CONFIG["circle_config"].get("radius")
            if to_object.magnitude>=radius:
                n = vec.normalise(to_object)
                impulse=((-(1+body.restitution)*body.linear_velocity).dot(n))/(n.dot(n*1/body.mass))
                body.linear_velocity= body.linear_velocity+(impulse/body.mass)*n
                body.position += n*(to_object.magnitude-(radius-shape.radius))
        
        if self.CONFIG.get("world_type")=="rectangle":
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
                object[1].actualise_pos()
                self.apply_constraints(object[0],object[1])
                self.deload_object(object[0],object[1])
            check.resolve_collisions(self.Objects)
    
    def resolve_linear_motion(self,body,t):
        body.force += self.gravity*body.mass
        body.acceleration= body.force/body.mass
        
        Integration=self.CONFIG.get("integration_method")
        if Integration=="EEM":
            Im.EEM(body,t)
        elif Integration=="IEM":
            Im.IEM(body,t)
        elif Integration=="SIE":
            Im.SIE(body,t)
        elif Integration=="IE":
            Im.IE(body,t)
        elif Integration=="Verlet":
            Im.Verlet(body,t)
        elif Integration=="RK4":
            Im.RK4(body,t)
        elif Integration=="Midpoint":
            Im.Mdpoint(body,t)
        else:
            raise Exception("Unrecognised integration method in CONFIG")
        
        body.force=vec.null()
        if body.linear_velocity.magnitude>=500:
            body.linear_velocity = body.linear_velocity*(500/body.linear_velocity.magnitude)
        return