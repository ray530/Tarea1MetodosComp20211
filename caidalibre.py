import numpy as np
import matplotlib.pyplot as plt

#Tiempo 

t=np.linspace(0,10)

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
 
V=velo(V0,t)
Y=posi(Y0,V0,t)
 
plt.subplot(2,1,1)
plt.plot(t,V,'ro')
plt.subplot(2,1,2)
plt.plot(t,Y, 'g')
plt.show()


#for i in range(len(t)):
#	if Y[i]==0 and i!=0:
#		print("Tiempo de vuelo ideal es ", t[i])
	
	
	




 	
