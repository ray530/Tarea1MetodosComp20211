import numpy as np
import matplotlib.pyplot as plt

#Tiempo 

t=np.linspace(0,10)


####################CASO IDEAL ############################

#Velocidad análitica

V0=50.0 #Velocidad inical m/s

def velo(V0_,t_):
	g=9.81 #Aceleración m/s² 
	v=V0-g*t
	return v

#Posición vertical 

Y0=0.0 #Altura inicial m 	
 	
def posi(Y0_,V0_,t_):
	g=9.81
	y=Y0+V0*t-0.5*g*t**2
	return y
 
Videal=velo(V0,t)
Yideal=posi(Y0,V0,t)
 
plt.subplot(2,1,1)
plt.plot(t,Videal,'ro')
plt.subplot(2,1,2)
plt.plot(t,Yideal, 'g')
plt.show()


################################CASO REAL ###############

#Variables 
C_d=0.8 #Coeficiente de drag
R=0.05 #radio en m
A=np.pi*R**2
rho=1.225 #Densidad del aire kg/m³
m=1.0 #masa en kg
gamma=np.sqrt((C_d*rho*A)/(2*m))


def vel(gamma_,V0_,t_):
	g=9.81 
	c1=np.sqrt(g)/gamma
	c2=gamma*np.sqrt(g)
	c3=(gamma*V0)/np.sqrt(g)
	if c3 > -1.0 and c3 < 1.0:
		v=c1*np.tanh(-c2*t+np.arctanh(c3))
	else:
		print("c3 debe estar entre -1 y 1")
	return v
	
V=vel(gamma,V0,t)

plt.figure
plt.plot(t,V)
plt.show()


	
	
	




 	
