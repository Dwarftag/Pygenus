from Vectors2D import Vect2D as vec
from Quarky_math_unit import Clamp

class RigidBody:
    
    def __init__(self,mass:float,angular_inertia:float,restitution=1,static_friction=0,dynamic_friction=0):
        self.position= vec.null()
        self.old_position= vec.null()
        self.linear_velocity= vec.null()
        self.force= vec.null()
        self.mass=mass
        
        self.angle=0
        self.angular_velocity=0
        self.torque=0
        self.inertia=angular_inertia

        self.restitution=Clamp(restitution,0,1)
        self.static_friction=static_friction
        self.dynamic_friction=dynamic_friction
        
        return
    
    @property
    def linear_momentum(self):
        return self.mass*self.linear_velocity
    
    @property
    def kinetic_energy(self):
        return (1/2)*self.mass*(self.linear_velocity.magnitude)**2
    
    @property
    def angular_momentum(self):
        return self.inertia*self.angular_velocity
    
    @property
    def angular_energy(self):
        return (1/2)*self.inertia*(self.angular_velocity)**2
    
    



