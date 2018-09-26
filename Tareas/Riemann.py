import math

#Calcula el area de las particiones dentro del intervalo
def Area(base,altura):
    return  base*altura

#Sigma
#la imagen de la formula se encuentra adjunta
def DistribucionN(s, u, x):
    valor = (1/(s * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-u)/s)**2))
    return valor

#Sumas de las areas fragmentadas
def Sreinman(inferior, superior, x, sigma, u):
    acercamiento = 0
    while inferior < superior:
        acercamiento += Area(x,DistribucionN(inferior + (x/2), sigma, u))
        inferior += x
    return acercamiento
    
print(Sreinman(-20,0,1,1,0))
