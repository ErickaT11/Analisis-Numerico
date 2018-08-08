import math

def evaluar(numero):
    resultado = math.log1p((5*numero)-1)
    error = abs(resultado - 0.544880440159982)
    return resultado, error

numero = 0.1  
incremento = 0.15
for i in range(0,5):
    resultado, error = evaluar(numero)
    if resultado <= numero:
        print("En la iteración ", i+1, " converge y el error de truncamiento es de: ", error)
    else:
        print("En la iteración ", i+1, " se pasó de la solución y el error de truncamiento es de: ", error)
    numero = numero + incremento
