
#include <bits/stdc++.h>

#define PRECISION 10
#define MAX_ITERACIONES 100
#define INTERVALOS 6

using namespace std;

void tabula(double a, double b, int intervalos);
double f(double x);
double f_derivada(double x); 
void newton(double x0, double tolerancia, int max_interaciones);	


int main()
{
	double a;
	double b;
	double tolerancia;
	double x0; 
	
	cout << setprecision(PRECISION);
	cout << "\nIngrese el intervalo inicial [a,b]:" << endl;
	//Intervalos
	cout << "\na = ";
	cin >> a;
	cout << "b = ";
	cin >> b;

	tabula(a, b, INTERVALOS);
	
	// Se pide elegir una aproximacion inicial. Se escoge uno de los dos vaores en donde cambia el signo
	cout << "\nEscoja el punto inicial adecuado:   x0 = ";
	cin >> x0;
	cout << "Tolerancia = ";
	cin >> tolerancia;
	newton(x0, tolerancia, MAX_ITERACIONES);
	
	cin.get();
	cin.get();
	return 0;
}


void tabula(double a, double b, int intervalos)
{
	int puntos = intervalos + 1;
	double ancho = (b - a) / intervalos;
	
	cout << "\n\tx\t\tf(x) " << endl;
	for (int i = 0; i < puntos; i++) {
		cout << "\t" << a << "\t\t" << f(a) << endl;
		a = a + ancho;
	}
}


double f(double x)
{
	return cos(3*x) + exp(x);
}


double f_derivada(double x)
{
	return -3*sin(3*x) + exp(x);
}


void newton(double x0, double tolerancia, int max_iteraciones)
{
	double x1; 
	double error;
	int iteracion; 
	bool converge = true;
	
	cout << "\nAproximacion inicial:\n";
	cout << "x0 = " << x0 << "\n"
		<< "f(x0) = " << f(x0) << "\n"
		<< "f'(x0) = " << f_derivada(x0) << endl;
	
	iteracion = 1;
	do {
	
		if (iteracion > max_iteraciones) {
			converge = false;
			break;
		
		} else {
			x1 = x0 - f(x0) / f_derivada(x0); // Se calcula la siguiente aproximacion
			error = fabs(x1 - x0);	// El error es la diferencia entre dos aproximaciones sucesivas
			
	
			cout << "\a";
		
			cout << "\n\nIteracion #" << iteracion << endl;
			cout << "\nx" << iteracion << "     = " << x1 << "\n"
				<< "f(x" << iteracion << ")  = " << f(x1) << "\n"
				<< "f'(x" << iteracion << ") = " << f_derivada(x1) << "\n"
				<< "error  = " << error << endl;
			
			if (error <= tolerancia) { // CondiciC3n de terminaciC3n
				converge = true;
				break;
			} else {
				x0 = x1;
				iteracion++;
			}
		}
	
	} while (1);
	
	//Respuesta
	cout << "\a";

	if (converge) {
		cout << "\n\nPara una tolerancia de " << tolerancia << " la raiz aproximada de f es = " << x1 << endl;
	
	} else {
		cout << "\n\nSe sobrepasa la maxima cantidad de iteraciones permitidas" << endl;
	}
}


//Referencia de Algoritmos y+
