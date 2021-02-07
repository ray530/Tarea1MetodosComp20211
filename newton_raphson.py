import numpy as np
import matplotlib.pyplot as plt

#Primera raiz
x1=1

Max_iter=100

tol=0.001

for i in range(Max_iter):
	xnew1=x1-(3*x1**5+5*x1**4-x1**3)/(15*x1**4+20*x1**3-3*x1**2)
	if abs(xnew1-x1)< tol: break
	x1=xnew1
print("la primera raiz ",xnew1,  "a ", i,  " iteraciones")


#Segunda raiz
x2=-10


for i in range(Max_iter):
	xnew2=x2-(3*x2**5+5*x2**4-x2**3)/(15*x2**4+20*x2**3-3*x2**2)
	if abs(xnew2-x2)< tol: break
	x2=xnew2
print("la segunda raiz es ",xnew2,  "a ", i,  " iteraciones")

#Tercera raiz
x3=0.01


for i in range(Max_iter):
	xnew3=x3-(3*x3**5+5*x3**4-x3**3)/(15*x3**4+20*x3**3-3*x3**2)
	if abs(xnew3-x3)<=tol/1000: break
	x3=xnew3
print("la tercera raiz es ",round(xnew3),  "a ", i,  " iteraciones")


#Grafica 

x=np.linspace(-10,10,100)
def fun(x):
	f=3*x**5+5*x**4-x**3
	return f
y=fun(x)


roots=np.array([xnew1,xnew2,round(xnew3)])
y_ceros=np.zeros(3)
plt.plot(x,y,'b',label="Función")
plt.scatter(roots,y_ceros,marker='o', color='red',label="RAICES")
plt.xlim(-2,2)
plt.ylim(-4,4)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.savefig("Grafica_Newton_Raphson.png")

