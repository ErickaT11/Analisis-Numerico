import numpy as np  
import matplotlib.pyplot as plt
from sympy import sympify

def graph(formula, x_range, dots, values):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y, 'b',dots,values,'ro')  
    plt.show()
    
def interpolHermite(xPun,xVal,xDer):

    tabla = [[0 for x in range(len(xVal)*2)] for y in range(len(xVal)*2)]

    for x in range(len(xVal)):
        tabla[x*2][0] = xVal[x]
        tabla[x*2+1][0] = xVal[x]
        tabla[x*2][1] = xDer[x]

    for x in range(1,len(tabla)-1,2):
        tabla[x][1] = (tabla[x+1][0] - tabla[x][0])/(xPun[(1+x)//2] - xPun[x//2])

    

    for y in range(2,len(tabla)):
        for x in range(len(tabla)-y):
            tabla[x][y] = (tabla[x+1][y-1] - tabla[x][y-1])/(xPun[(y + x)//2] - xPun[x//2])

    

    strPoly = ""
    for x in range(len(tabla[0])):
        if x != len(tabla[0]) - 1:
            strPoly = strPoly + str(tabla[0][x])  + agregarHermite(x,xPun) + " + "
        else :
            strPoly = strPoly + str(tabla[0][x]) + agregarHermite(x,xPun)
        
    print(strPoly)
    print()
    poly = sympify(strPoly)
    graph(strPoly,range(0,20),xPun,xVal)
    plt.show()
    print(poly)
    return poly

def agregarHermite(x,xPun):

    if x == 0:
        string = ""
        return string
    elif x % 2 == 1 :
        string = "*(x-"+str(xPun[((x+1)//2)-1])+")"    
        return string + agregarHermite(x-1,xPun)
    else : 
        string = "*((x-"+str(xPun[((x+1)//2)-1])+")**2)"     
        return string + agregarHermite(x-2,xPun)
    
def interpolNewton(xPun,xVal):

    tabla = [[0 for x in range(len(xVal))] for y in range(len(xVal))]

    for x in range(len(xVal)):
        tabla[x][0] = xVal[x]
    
    for y in range(1,len(tabla)):
        for x in range(len(tabla)-y):
            tabla[x][y] = (tabla[x+1][y-1] - tabla[x][y-1])/(xPun[y+x] - xPun[x])
   
    strPoly = ""
    for x in range(len(tabla[0])):
        if x != len(tabla[0]) - 1:
            strPoly = strPoly + str(tabla[0][x])  + agregarNewton(x,xPun) + " + "
        else :
            strPoly = strPoly + str(tabla[0][x]) + agregarNewton(x,xPun)
    print(strPoly)
    poly = sympify(strPoly)
    graph(strPoly,range(0,20),xPun,xVal)
    return poly

def agregarNewton(x,xPun):

    if x == 0:
        string = ""
        return string
    else :
        string = "*(x-"+str(xPun[x-1])+")"    
        return string + agregarHermite(x-1,xPun)
    
#interpolHermite([1.3,1.6,1.9],[0.6200860,0.4554022,0.2818186],[-0.5220232,-0.5698959,-0.5811571])
interpolNewton([1.3,1.6,1.9],[0.6200860,0.4554022,0.2818186])    
