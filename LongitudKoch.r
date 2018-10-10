 
#Si se considera de nuevo la primera figura, 
#notamos que para pasar de una línea a la siguiente 
#se remplaza tres segmentos por cuatro de igual longitud,
#o sea que la longitud total es multiplicada por 4/3. 
#Después de n pasos iterativos en la construcción 
#recursiva la longitud de la curva es 3·(4/3)n, 
#el límite de la sucesión geométrica anterior de
#razón 4/3 es obviamente infinito, lo que significa 
#que la figura final tiene una longitud infinita 
#(lo que Mandelbrot denomina infinito interno). 
#Esto está relacionado con el hecho de que la curva 
#frontera del copo de Koch no es rectificable y tiene 
#una dimensión fractal d > 1.



CalcularLongitud <- function(iteraciones, longitudI){
    longitud <- longitudI*((4/3)^iteraciones)
    return(longitud)
    }

iteraciones <- 10

for (i in 1:iteraciones){
    x <- CalcularLongitud(i, 3)
    print(x)
    }
