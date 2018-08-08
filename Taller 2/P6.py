iteraciones = 0
print ("Punto 6\nIngrese n: ")
numero = int(input())
while numero > 0:
    iteraciones += 1
    residuo = numero % 2
    numero = numero//2
    print("Residuo: ", residuo)
print ("Iteraciones: ", iteraciones)
