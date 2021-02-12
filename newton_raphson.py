import numpy as np
import matplotlib.pyplot as plt

# definir función

def FUNC(x):
	return 3*x**5+5*x**4-x**3
	
def DERIVATIVE(f,x,h):
	d=0.01
	if (h!=0):
		d=(f(x+h)-f(x-h))/(2*h)
	return d

def NR(f,df,xn,error,it,precision=0.0001,iterations=1000):
    h_ = 1.0e-4
    while error > precision and it < iterations:  
        try:   
            xn1 = xn - f(xn)/df(f,xn,h_) 
            error = np.abs((xn1-xn)/xn1)
            #print(xn1)
        except ZeroDivisionError:
            print("Hay division por cero")   
        xn = xn1
        it += 1
    return xn1

#Roots 

C=100 #numero de puntos
x=np.linspace(-10,10,C)

for i in x:
	roots=[NR(FUNC,DERIVATIVE,i,100,1),0]
	#print(roots, i )
	xnew=[NR(FUNC,DERIVATIVE,-2,100,1),NR(FUNC,DERIVATIVE,-0.5,100,1),NR(FUNC,DERIVATIVE,2,100,1)]
print("LAs raices son ",xnew)
y_ceros=np.zeros(len(xnew))


#Grafica 

plt.plot(x,FUNC(x),'b',label="Función")
plt.scatter(xnew,y_ceros,marker='o', color='red',label="RAICES")
plt.xlim(-2,2)
plt.ylim(-4,4)
plt.legend()
plt.xlabel("X")
plt.ylabel("F(X)")
plt.grid()
plt.savefig("Grafica_Newton_Raphson.png")

