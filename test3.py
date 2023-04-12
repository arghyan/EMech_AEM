from sympy.physics.mechanics import *
from sympy import symbols
from math import pi, radians, sqrt

psi=symbols('psi')

N=ReferenceFrame('N')
O=Point('O')
O.set_vel(N,0*N.x)
N1=N.orientnew('N1','Axis',[psi,N.z])
N1.set_ang_vel(N,2*pi*N.z)
N2=N1.orientnew('N2','Axis',[radians(60),N1.x])
N2.set_ang_vel(N1,0*N1.x)
N3=N2.orientnew('N3','Axis',[0,N2.z])
N3.set_ang_vel(N2,4*pi*N2.z)

A=O.locatenew('A',10*N2.z+5*N2.y)
vA=A.v2pt_theory(O,N,N3)
aA=A.a2pt_theory(O,N,N3)
