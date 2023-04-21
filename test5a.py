#Meriam Kraige 6th edition 7/48 - Method 1
from sympy.physics.mechanics import *
from sympy import symbols, solve 
from math import atan, degrees, radians, sqrt, sin, cos, pi

psi_d,theta_d,omega_1,omega_2,p,b,r=symbols('psi_d,theta_d,omega_1,omega_2,p,b,r')

N=ReferenceFrame('N')
O=Point('O')
B=O.locatenew('B',b*N.x)
O.set_vel(N,0*N.x)
N1=N.orientnew('N1','Axis',[0,N.y])
N1.set_ang_vel(N,omega_2*N.y)
N2=N1.orientnew('N2','Axis',[0,N1.x])
N2.set_ang_vel(N1,-omega_1*N1.x)
N3=N2.orientnew('N3','Axis',[0,N2.z])
N3.set_ang_vel(N2,p*N2.z)

vB=cross(omega_2*N.y,B.pos_from(O))
aB=cross(omega_2*N.y,vB)
B.set_vel(N,vB)
B.set_acc(N,aB)
A=B.locatenew('A',r*N2.y)

A.v2pt_theory(B,N,N3)
A.a2pt_theory(B,N,N3)
