from .Physic_solver import *
from .Integration_methods import *
from .Collision_detection import *
from .Body import *
from .Joint import *
from .Mesh import *
from .Quarky_math_unit import *
from .Vectors2D import Vect2D as vec

add_method("EEM",EEM)
add_method("SIE",SIE)
add_method("Verlet",Verlet)
add_method("IE",IE)
add_method("IEM",IEM)
add_method("Midpoint",Midpoint)
add_method("RK4",RK4M)


