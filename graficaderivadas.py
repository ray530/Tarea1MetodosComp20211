import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('datosderivada.txt')

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.scatter(data[:,0],data[:,1],label="F(x)=x-sin(x)", color="blue")
plt.scatter(data[:,0],data[:,3],label="F'(x) númerico", color="black")
plt.plot(data[:,0],data[:,2],label="F'(x) análitico", color="red")
plt.xlabel("X")
plt.legend()
plt.subplot(1,3,2)
plt.plot(data[:,0],data[:,-2],label="Error Local", color="green")
plt.xlabel("X")
plt.legend()
plt.subplot(1,3,3)
plt.plot(data[:,0],data[:,-1],label="Error global", color="black")
plt.xlabel("X")
plt.legend()
plt.savefig("Grafica_derivada_errorlocal.png")
plt.show()



