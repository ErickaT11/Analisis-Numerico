#include <bits/stdc++.h>

using namespace std;

double evaluar(double p[]){
    int a,b,c;
    double r;
    a = p[0];
    b = p[1];
    c = p[2];
    
    int interiorRaiz = pow(b,2)-4*(a*c);
 
    double primeraSolucion = 0;
    double segundaSolucion = 0;
 
    if(interiorRaiz < 0)
    {
        std::cout << "Esta ecuacion no tiene solucion en los numeros reales." << endl;
    }
    else
    {
        primeraSolucion = (-b+sqrt(interiorRaiz))/(2*a);
        segundaSolucion = (-b-sqrt(interiorRaiz))/(2*a);
        if(primeraSolucion == segundaSolucion)
        {
            std::cout << "La unica solucion es:" << primeraSolucion;
        }
        else
        {
            std::cout << "La primera solucion es: " << primeraSolucion << std::endl;
            std::cout << "La segunda solucion es: " << segundaSolucion << std::endl;
            std::cout << std:: endl;
        }
    }
}

int main()
{
   cout<<"El volumen de la caja estarC! dado por: "<<endl;
   cout<<"V = (32 - 2x)*(24 - 2x)x"<<endl;
   cout<<"x representa el lado del cuadro que serC! cortado"<<endl;
   cout<<"Tenemos entonces que el volumen es: "<<endl;
   cout<<"V = 4x^3 - 112x^2 + 768x"<<endl;
   cout<<"Ahora encontramos los maximos y los minimos. Para eso derivamos"<<endl;
   
   double p[2];
   p[0] = 12;
   p[1] = -224;
   p[2] = 768;
   
   evaluar(p);
  
    return 0;
}
