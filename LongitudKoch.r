CalcularLongitud <- function(iteraciones, longitudI){
  longitud <- longitudI*((4/3)^(iteraciones-1))
  return(longitud)
}

distancia<-function(x1, y1, x2, y2){
  return (sqrt ( (x2-x1)^2 + (y2-y1)^2 ) )
}
graficar<-function(n){
  snowflake(n)
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
  total=total+distanciaPuntos (x1, y1, x2, y2)
  cat("Longitud:", CalcularLongitud(n,3))
}
graficar(4)
