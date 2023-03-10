from Vectors2D import Vect2D as vec
from Quarky_math_unit import Clamp

class RigidBody:
    
    STATIC=1
    DYNAMIC=2
    KINEMATIC=3
    
    
    def __init__(self,mass:float,angular_inertia:float,restitution=1,static_friction=0,dynamic_friction=0,body_type=None):
        self.position= vec.null()
        self.linear_velocity= vec.null()
        self.force= vec.null()
        
        self.angle=0
        self.angular_velocity=0
        self.torque=0
        self.inertia=angular_inertia

        self.body_type=body_type
        self.mass=mass

        self.restitution=Clamp(restitution,0,1)
        self.static_friction=static_friction
        self.dynamic_friction=dynamic_friction
        return
    
    @property
    def linear_momentum(self):
        return self.mass*self.linear_velocity.magnitude
    
    @property
    def kinetic_energy(self):
        return self.mass*(self.linear_velocity.magnitude**2)
    
    



