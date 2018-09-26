#Calcula el area de los fragmentos
Area = function(base,altura){
    return  (base*altura)}

#Sigma
#la imagen de la formula se encuentra adjunta
DistribucionN = function(s, u, x){
    valor <- (1/(s * sqrt(2*pi))) * exp((-0.5*((x-u)/s)**2))
    return (valor)}

#Sumas de las areas fragmentadas
Sreinman = function(inferior, superior, x, sigma, u){
    acercamiento <- 0
    while (inferior < superior){
        acercamiento <- acercamiento + Area(x,DistribucionN(inferior + (x/2), sigma, u))
        inferior <- inferior + x}
    return (acercamiento)}
    
print(Sreinman(-20,0,1,1,0))

