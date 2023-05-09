from sympy.physics.mechanics import *
from sympy import symbols, pi

theta=symbols('theta')
OA=symbols('OA')

theta_d=30*3.14159/180
phi_d=(200*1000/3600)/(0.920/2)

N=ReferenceFrame('N')
O=Point('O')
O.set_vel(N,0*N.x)
N1=N.orientnew('N1','Axis',[-theta,N.y])
N1.set_ang_vel(N,-theta_d*N.y)
A=O.locatenew('A',OA*N1.x)
G=O.locatenew('G',OA*N1.x+0.215*N1.z)
G.v2pt_theory(O,N,N1)
N2=N1.orientnew('N2','Axis',[0,N1.z])
N2.set_ang_vel(N1,-phi_d*N1.z)
ival=45*0.370**2


imat=inertia(N2,ival/2,ival/2,ival,0,0,0)
inertia_tuple=(imat,G)
print(imat.to_matrix(N2))
Body=RigidBody('Body',G,N2,45,inertia_tuple)

HG=Body.angular_momentum(G, N)
HA=Body.angular_momentum(A, N)