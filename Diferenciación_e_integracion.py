import math

def evaluar(x):
    return x*math.exp(x)

def evaluarDerivada(x):
    return math.exp(x) + x*math.exp(x)

#crear formula

def formula(h, x):
    aux = []
    for i in range (0,3):
        val = ((1/(2*h))*(-3*(evaluar(x[i])) + 4*(evaluar(x[i]) + h) - evaluar(x[i]) + 2*h) + (pow(h,2)/3))
    aux.append(val)
    return aux

x = [1.8,1.9,2.0,2.1,2.2]
y = []
yd = []
h = [0.1,0.01,0.001]
val = []
#evaluacion de la funcion sin derivar
for i in range (len(x)):
    y.append(evaluar(x[i])) 
#evaluacion de la funcion derivada

for i in range (len(x)):
    y.append(evaluarDerivada(x[i])) 

#evalur por cada h


print(evaluarDerivada(2))

for i in range (0,3):
    val.append(formula(h[i], x))
print(val)    

#calcular errores 

