#Meriam Kraige 6th edition 7/47 - Method 2
from sympy.physics.vector import Point, ReferenceFrame, cross
from sympy import symbols
from math import radians

N = ReferenceFrame('N')
O = Point('O')
O.set_vel(N,0*N.x)
N1 = N.orientnew('N1', 'Axis', [0, N.z])
Om=symbols('Om')
N1.set_ang_vel(N,1/2*N1.z)
N2 = N1.orientnew('N2', 'Axis', [-radians(30), N1.y])
N2.set_ang_vel(N1,-1/4*N1.y)
rho=8*N2.y+2*N2.z
P=O.locatenew('P',rho)

vP_rel=cross(-1/4*N1.y,rho)
aP_rel=cross(-1/4*N1.y,vP_rel)
P.set_vel(N1,vP_rel)
P.set_acc(N1,aP_rel)

vP=P.v1pt_theory(O,N,N1)
aP=P.a1pt_theory(O,N,N1)


