import math

def areaRectangulo(b,h):
    return  b*h

def areaTriangulo(b,h):
    return b*h/2
    
def areaTrapecio(p1,p2,b):
    ht = abs(p2-p1)
    if p1 > p2 :
        hr = p2 
    else: 
        hr = p1 
    return areaRectangulo(b,hr) + areaTriangulo(b,ht)

def areaEntreCurvas(limA, limB, pSize):
    total = 0
    while limA < limB :
        if f(limA) > g(limA) :
            total = total + areaTrapecio(f(limA),f(limA+pSize),pSize) - areaTrapecio(g(limA),g(limA+pSize),pSize)
        elif f(limA) < g(limA) :
            total = total - areaTrapecio(f(limA),f(limA+pSize),pSize) + areaTrapecio(g(limA),g(limA+pSize),pSize)
        limA += pSize
    
    return total
    
def f(x):
    return x**2

def g(x):
    return 1-x**2

print(areaEntreCurvas(-1/math.sqrt(2),1/math.sqrt(2),0.01))
print(areaEntreCurvas(-1,1,0.01))
