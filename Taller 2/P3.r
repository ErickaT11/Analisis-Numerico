root <- function(n,E,x) {
	y <- 1/2*(x+n/x)
	while (abs(x - y) > E) {
		x <- y
		y <- 1/2*(x+n/x)
	}
	y
}


root(7,1.e-4,4)
