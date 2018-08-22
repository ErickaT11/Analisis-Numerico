#Arma la tabla simplex
def inicializarTabla(objetivo, restricciones, constantes):
   tabla = [row[:] + [x] for row, x in zip(restricciones, constantes)]
   tabla.append([i for i in objetivo] + [0])
   return tabla

def columna(A, j):
   return [row[j] for row in A]

#Saca la transpuesta de una matriz
def transpuesta(A):
   return [columna(A, j) for j in range(len(A[0]))]

#Verifica si un valor es finito
def esPivote(columna):
   return (len([i for i in columna if i == 0]) == len(columna) - 1) and sum(columna) == 1

def variablePivote(tabla, columna):
   filaPivote = [i for (i, x) in enumerate(columna) if x == 1][0]
   return tabla[filaPivote][-1]

#Con las columnas pivotes veremos cuales variables son usadas
def primalSolution(tabla):
   columnas = transpuesta(tabla)
   indices = [j for j, col in enumerate(columnas[:-1]) if esPivote(col)]
   return [(columIndex, variablePivote(tabla, columnas[columIndex]))
            for columIndex in indices]

def vObjetivo(tabla):
   return -(tabla[-1][-1])

#Verifica si aún se puede seguir máximizano la función
def continua(tabla):
   uFila = tabla[-1]
   return any(x > 0 for x in uFila[:-1])

def indicePivote(tabla):
   # seleccionar el índice positivo minimo de la última fila
   columnas_elegidas = [(i,x) for (i,x) in enumerate(tabla[-1][:-1]) if x > 0]
   columna = min(columnas_elegidas, key=lambda a: a[1])[0]

   # Verifica si tiebe limites
   if all(row[columna] <= 0 for row in tabla):
      raise Exception('')

   # más de un denominador en os cocientes
   cociente = [(i, r[-1] / r[columna])
      for i,r in enumerate(tabla[:-1]) if r[columna] > 0]

   # escoger el indice de fila minimizando el cociente
   fila = min(cociente, key=lambda x: x[1])[0]

   return fila, columna

def pivotAbout(tabla, pivot):
   i,j = pivot

   pivotDenom = tabla[i][j]
   tabla[i] = [x / pivotDenom for x in tabla[i]]

   for k,row in enumerate(tabla):
      if k != i:
         pivotRowMultiple = [y * tabla[k][j] for y in tabla[i]]
         tabla[k] = [x - y for x,y in zip(tabla[k], pivotRowMultiple)]


def simplex(c, A, b):
   tableau = inicializarTabla(c, A, b)
   print(tableau)
   

   while continua(tableau):
      pivot = indicePivote(tableau)
      print("indice pivote=%d,%d \n" % pivot)
      pivotAbout(tableau, pivot)
      for row in tableau:
         print(row)
      print()

   return tableau, primalSolution(tableau), vObjetivo(tableau)



objetivo = [200, 150, 440]
restricciones = [[20, 25, 23], [46, 70, 40], [30, 50, 28], [10, 250, 10]]
constantes = [1000, 3000, 1700, 500]


# se añade la matriz identidad de forma manual 
restricciones[0] += [1,0,0,0]
restricciones[1] += [0,1,0,0]
restricciones[2] += [0,0,1,0]
restricciones[3] += [0,0,0,-1]
objetivo += [0,0,0,0]

t, s, v = simplex(objetivo, restricciones, constantes)
print(s)
print(v)
