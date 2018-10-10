CalcularLongitud <- function(iteraciones, longitudI){
  longitud <- longitudI*((4/3)^(iteraciones-1))
  return(longitud)
}

errorPerimetro<-function (n,aprox){
  real= 3*(4/3)^(n-1)
  error = abs(real-aprox)
  return (error)
}

valorTeorico<-function (n){
  return (3*(4/3)^(n-1))
}

distancia<-function(x1, y1, x2, y2){
  return (sqrt ( (x2-x1)^2 + (y2-y1)^2 ) )
}

curvaKoch<-function(n){
  vertices <- koch(side = 1, niter = n)
  text <- bquote(bold(paste("Curva de Koch con n = ", .(n))))
  plot(vertices[, 1], vertices[, 2], type = "l", asp = TRUE, main = text, xlab = "x", ylab = "y", col = "black")
  segments(vertices[nrow(vertices), 1], vertices[nrow(vertices), 2], vertices[1, 1], vertices[1, 2], col = "black")
}

graficar<-function(n){
  curvaKoch(n)
  total=0
  x=koch(side = 1, n = n)
  for(i in 2:nrow(x)){
    x1=x[i-1,1]
    y1=x[i-1,2]
    x2=x[i,1]
    y2=x[i,2]
    total=total+distancia (x1, y1, x2, y2)
  }
  x1=x[nrow(x),1]
  y1=x[nrow(x),2]
  x2=x[1,1]
  y2= x[1,2]
  total=total+distancia (x1, y1, x2, y2)
  cat("El perimetro de la curva de Koch con n = ", n, " es: ", format(round(total,4), nsmall=4), "y el valor teorico es ",format(round(valorTeorico(n),4), nsmall=4), "(Error de",format(round(errorPerimetro(n,total),4))," )")
}
graficar(4)
