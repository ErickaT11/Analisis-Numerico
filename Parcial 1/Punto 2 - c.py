import math

def evaluarFuncion(x):
    return math.log(x +2)

def calcularError(apr, exact):
    return ((apr - exact)/ exact)*100

evaluadoA = 0
x = 0
while calcularError(evaluadoA , 1.6314435) < 0.0000001:
    evaluadoA =  x+1 + evaluarFuncion(x)*((x-(x-1))/(evaluarFuncion(x))-(evaluarFuncion(x-1)))
    x+=0.0000001
