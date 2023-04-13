#Meriam Kraige 6th edition 7/47 - Method 1
from sympy.physics.vector import Point, ReferenceFrame
from sympy import symbols
from math import radians

N = ReferenceFrame('N')
O = Point('O')
O.set_vel(N,0)
N1 = N.orientnew('N1', 'Axis', [0, N.z])
Om=symbols('Om')
N1.set_ang_vel(N,1/2*N1.z)
N2 = N1.orientnew('N2', 'Axis', [-radians(30), N1.y])
N2.set_ang_vel(N1,-1/4*N1.y)
P=O.locatenew('P',8*N2.y+2*N2.z)
vP=P.v2pt_theory(O,N,N2)
aP=P.a2pt_theory(O,N,N2)
