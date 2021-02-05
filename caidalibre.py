import numpy as np
import matplotlib.pyplot as plt

#Tiempo 

t=np.linspace(0.0,30,200)


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

#Tiempo de vuelo ideal

for i in range(len(t)):
	g=9.81
	if Yideal[i]<=0 and i!=0:
		print("El tiempo de vuelo ideal es ",t[i])
		if t[i+1]>=((V0*2)/g):
			break






plt.subplot(2,1,1)
plt.plot(t,Videal,'ro')
plt.xlim(0,10.5)
plt.ylim(-50,50)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.subplot(2,1,2)
plt.plot(t,Yideal, 'g')
plt.xlim(0,10.5)
plt.ylim(0,150)
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")
plt.savefig('Caso_ideal.png')
plt.close()

################################CASO REAL ###############

#Variables 
C_d=0.8 #Coeficiente de drag
R=0.05 #radio en m
A=np.pi*R**2
rho=1.225 #Densidad del aire kg/m³
m=1.0 #masa en kg
gamma=np.sqrt((C_d*rho*A)/(2*m))
g=9.81 

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
	

def pos(gamma_,Y0_,V0_,t_):
	g=9.81
	c1=1/gamma**2
	c2=gamma*np.sqrt(g)
	c3=(gamma*V0)/np.sqrt(g)
	if c3 > -1.0 and c3 < 1.0:
		c4=np.arctanh(c3)
	else:
		print("c3 debe estar entre -1 y 1")
	y=Y0+c1*np.log(np.cosh(c4)/np.cosh(-c2*t+c4))
	return 2*y/g

	

V=vel(gamma,V0,t)
Y=pos(gamma,Y0,V0,t)

#Tiempo de vuelo real 
for i in range(len(t)):
	if Y[i]<=0 and i!=0:
		print("El tiempo de vuelo con drag es ",t[i])
		if t[i+1]>= t[i]:
			break


plt.figure
plt.subplot(2,1,1)
plt.plot(t,V)
plt.xlim(0,28)
plt.ylim(-50,50)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.subplot(2,1,2)
plt.plot(t,Y)
plt.xlim(0,28)
<<<<<<< HEAD
plt.ylim(0,120)
=======
plt.ylim(0,110)
>>>>>>> 65bf8e911757672015f53d5c1dcc23b2e5e462d8
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")
plt.savefig('Caso_real.png')


	
	
#################### Comportamiento de C respecto al tiempo de vuelo ####################################3

#c es numero entre 0 y 1

c=np.linspace(0.1, 1, 20)


def gamma_c(c_):
	R=0.05 #radio en m
	A=np.pi*R**2
	rho=1.225 #Densidad del aire kg/m³
	m=1.0 #masa en kg
	g=9.81
	gama=np.sqrt((c*rho*A)/(2*m))
	return gama
	
#print((1/gamma)**2,"c2= ",gamma*np.sqrt(9.81), "c3= ",(gamma*V0)/np.sqrt(9.81))

Gamma=gamma_c(c)
g=9.81
c1=1/Gamma**2
c2=Gamma*np.sqrt(g)
c3=(Gamma*V0)/np.sqrt(g)



 	
