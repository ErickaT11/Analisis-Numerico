#R version 3.3.2 

f<-function(fcn,x,y){
  return(eval(fcn))
}

calcular <- function(x,y){
  h <- 0.1
  m <- 20
  i <- x
  
  for(i  in 1:m){
    k1 <- f(expression(x+y+1-(x*x)),x[i],y[i])
    k2 <- f(expression(x+y+1-(x*x)),(x[i] + h),(y[i] + k1))
    y[i+1] <- y[i] + 0.5 *(k1 + k2)
    x[i+1] <- x[i] + h 
    cat("X:", x, "Y: ", y, "K1 : " , k1, "K2:" , k2, "\n");
  }
}

calcular(0,1);
