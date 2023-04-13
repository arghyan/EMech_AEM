#Meriam Kraige 6th edition Sample problem 7/3
from sympy.physics.mechanics import *
from sympy import symbols, solve 
from math import atan, degrees, radians, sqrt, sin, cos

psi_d,theta_d,omega_2=symbols('psi_d,theta_d,omega_2')

N=ReferenceFrame('N')
psi=atan(50/100)
theta=atan(100/sqrt(50**2+100**2))

O=Point('O')
O.set_vel(N,0*N.x)
N1=N.orientnew('N1','Axis',[-psi,N.z])
N1.set_ang_vel(N,-psi_d*N.z)
N2=N1.orientnew('N2','Axis',[theta,N1.x])
N2.set_ang_vel(N1,theta_d*N1.x)
B=O.locatenew('B',0*N.x)
B.set_vel(N,600*N.x)
A=B.locatenew('A',50*N.x+100*N.y+100*N.z)
vA=A.v2pt_theory(B,N,N2)

eqn1=dot((vA-50*omega_2*N.y),N.x)
eqn2=dot((vA-50*omega_2*N.y),N.y)
eqn3=dot((vA-50*omega_2*N.y),N.z)
sol=solve([eqn1,eqn2,eqn3],psi_d,theta_d,omega_2)
angvel=N2.ang_vel_in(N).simplify().express(N)
angvel=angvel.subs({psi_d:sol[psi_d],theta_d:sol[theta_d]})

