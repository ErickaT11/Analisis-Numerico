import math

def evaluar(numero):
    resultado = math.exp(-numero)- numero
    return resultado

print("Ingrese el valor inicial del intervalo: " )
punto0 = int(input())
print("Ingrese el valor final del intervalo: " )
punto1 = int(input())
punto2 = (punto1+punto0)/2
auxResta0 = punto1-punto0
auxResta1 = punto2-punto1
delta1 = (evaluar(punto1)-evaluar(punto0))/auxResta0
delta2 = (evaluar(punto2)-evaluar(punto1))/auxResta1
c1= (delta2-delta1)/(auxResta1- auxResta0)
c2 = c1*auxResta1+ delta1
c3 = evaluar(punto2)
error = abs(c1 - 0.567143/c1)
iteracion = 0
if(evaluar(punto0)* evaluar(punto1)<0):
    while error>0.30:
        punto0 = punto1
        punto1 = punto2
        iteracion+=1
        if c2 > 0:
            respuesta1 = punto2 +(2*c3/(c2+math.sqrt(c2*c2-(4*c1*c3))))
            punto2 = respuesta1 
        else:
            respuesta2 = punto2 +(2*c3/(c2-math.sqrt(c2*c2-(4*c1*c3))))
            punto2 = respuesta2
        auxResta0 = punto1-punto0
        auxResta1 = punto2-punto1
        delta1 = (evaluar(punto1)-evaluar(punto0))/auxResta0
        delta2 = (evaluar(punto2)-evaluar(punto1))/auxResta1
        c1= (delta2-delta1)/(auxResta1 +  auxResta0)
        c2 = c1*auxResta1 - delta2
        c3 = evaluar(punto2)
        error = abs(punto2 - 0.567143/punto2)
        print("Se encontró la respuesta ", punto2,"Con un error de", error, "en la iteración ", iteracion)
else:
    print("No existe raíz")
