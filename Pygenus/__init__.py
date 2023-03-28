from .Physic_solver import *
from .Integration_methods import *

add_method("EEM",EEM)
add_method("SIE",SIE)
add_method("Verlet",Verlet)
add_method("IE",IE)
add_method("IEM",IEM)
add_method("Midpoint",Midpoint)
add_method("RK4",RK4M)


