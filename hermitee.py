from sympy import sympify

def Hermite(punto,val,derivada):
    '''llenamos la tabla con 0'''
    tabla = [[0 for i in range(len(val)*2)] for j in range(len(val)*2)]
    for i in range(len(val)):
        tabla[i*2][0] = val[i]
        tabla[i*2+1][0] = val[i]
        tabla[i*2][1] = derivada[i]
    
    for i in range(1,len(tabla)-1,2):
        tabla[i][1] = (tabla[i+1][0] - tabla[i][0])/(punto[(1+i)//2] - punto[i//2])
    
    for j in range(2,len(tabla)):
        for i in range(len(tabla)-j):
            tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1])/(punto[(j + i)//2] - punto[i//2])
    strPoly = ""
    for i in range(len(tabla[0])):
        if i != len(tabla[0]) - 1:
            strPoly = strPoly + str(tabla[0][i])  + agregar(i,punto) + " + "
        else :
            strPoly = strPoly + str(tabla[0][i]) + agregar(i,punto)
        
    print(strPoly)
    print()
    poly = sympify(strPoly)
    print(poly)
    return poly
