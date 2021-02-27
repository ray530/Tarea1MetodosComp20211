import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('datosderivada.txt')

plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
plt.scatter(data[:,0],data[:,1],label="F(x)=x-sin(x)", color="blue")
plt.scatter(data[:,0],data[:,3],label="F'(x) númerico", color="black")
plt.plot(data[:,0],data[:,2],label="F'(x) análitico", color="red")
plt.xlabel("X")
plt.legend()
plt.subplot(2,2,2)
plt.plot(data[:,0],data[:,-4],label="Error Local", color="green")
plt.xlabel("X")
plt.legend()
plt.subplot(2,2,3)
plt.plot(data[:,0],data[:,-3],label="Error global", color="black")
plt.xlabel("X")
plt.legend()
plt.subplot(2,2,4)
plt.plot(data[:,-2],data[:,-1], color="black")
plt.xlabel("Error segunda derivada de primera derivada central ")
plt.ylabel("Error segunda derivada central ")
plt.legend()
plt.show()



