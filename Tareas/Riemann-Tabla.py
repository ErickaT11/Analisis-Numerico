import math
from decimal import Decimal

#Calcula el area de los fragmentos
def Area(base,altura):
    return base*altura

#Sigma
#la imagen de la formula se encuentra adjunta
def DistribucionN (x, s, u):
    valor = (1/(s * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-u)/s)**2))
    return valor

def z(x):
    return (1/math.sqrt(2*math.pi)) * math.e **(-0.5*((x)**2))
    
#Sumas de las areas fragmentadas
def Sreinman (inferior, superior, x, sigma, u):
    acercamiento = 0
    while inferior < superior:
        acercamiento = acercamiento + Area(x,DistribucionN(inferior + (x/2), sigma, u))
        inferior = inferior + x
    return acercamiento
    
print(Sreinman(-20,0,1,1,0))

def reinmanZ(inferior, superior, x):
    acercamiento = 0
    while inferior < superior:
        acercamiento += Area(x,z(inferior + (x/2)))
        inferior += x
    return acercamiento

#Impresion de la tabla
print("0.000 || ", end="")
for i in range(0,10):
  print("0.00" + str(i),end = " | ")

print("\n")
x = 0
cont = 0
print("0.000 | ", end="")
while x < 1:
    y = Decimal(reinmanZ(-10,x,0.001))
   
    print(round(y,3), end="|")
    cont += 1
    if(cont== 10):
        max = Decimal(x+0.001)
        print()
        print(str(round(max,3))+" | ", end="|")
        cont = 0
    x += 0.001
