#Meriam Kraige 6th edition 7/26 - Cone rolling on fixed cone
from sympy.physics.mechanics import *
from sympy import symbols,trigsimp, solve
from math import pi, sqrt, asin, atan, degrees

angle=asin(1/(3*sqrt(2)))
print(degrees(angle))

psi,phi_d=symbols('psi,phi_d')

N=ReferenceFrame('N')
O=Point('O')
O.set_vel(N,0*N.x)

N1=N.orientnew('N1','Axis',[psi,N.z])
N1.set_ang_vel(N,(2*pi/4)*N.z)

N2=N1.orientnew('N2','Axis',[pi/4+angle,N1.x])
N2.set_ang_vel(N1,0*N1.x)

N3=N2.orientnew('N2','Axis',[0,N2.z])
N3.set_ang_vel(N1,phi_d*N2.z)

B=O.locatenew('B',150*N.z-150*N1.y)
vB=B.v2pt_theory(O,N,N3)

#Velocity is zero at any point on instantaneous line of zero velocity
eq1=dot(vB,N2.x).simplify()
eq2=dot(vB,N2.y).simplify()
eq3=dot(vB,N2.z).simplify()

sol=solve([eq1,eq2,eq3],phi_d)

print(sol[phi_d])

N3.set_ang_vel(N1,sol[phi_d]*N2.z)

angvelN3=N3.ang_vel_in(N).express(N2)
print(angvelN3)
angvelN3_ycomp=dot(angvelN3,N3.y)
angvelN3_zcomp=dot(angvelN3,N3.z)
print(degrees(atan(angvelN3_ycomp/angvelN3_zcomp)))

print(N3.ang_acc_in(N).express(N2))

