#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int cont;
double horner(double p[], int n, double x){
    cont = 0;
    double y = p[0];
    int i;
    for(i = 0; i<n; i++){
        y = x*y + p[i];
        cont +=2;
    }
    return y;
}
double eval(double p[], int n, double x){
    cont = 0;
    double s = 0;
    int i;
    for(i = 0; i<n; i++){
        s = s + p[i]* pow(x, n-i-1);
        cont += 4;
    }
    return s;
}

int main()
{
    cout<<"Polinomio: "<<"7x^5 + 6x^4 - 6x^3 + 3x - 4"<<endl;
    int x =  3;
    int n = 5;
    int n2 = 4;
    double result = 0;
    double p[5];
    double pd[4];
    p[0] = 7;
    p[1] = 6;
    p[2] = -6;
    p[3] = 0;
    p[4] = 3;
    p[5] = 4;
    
    pd[0] = 35;
    pd[1] = 24;
    pd[2] = 18;
    pd[3] = 0;
    pd[4] = 3;
    
    cout<<"El metodo se evalua por Horner y de manera directa para hacer la comparacion"<<endl;
    cout<<"Primero se aplica para el polinomio sin derivar "<<endl;
    cout<<"Resultados: "<<endl;
    cout<<"Horner: "<<endl;
    result = horner(p, n, x);
    cout<<result<<endl;
    cout<<"Numero de operaciones: "<<cont<<endl;
    cout<<"Metodo directo: "<<endl;
    eval(p, n, x);
    cout<<"Numero de operaciones: "<<cont<<endl;
    
    cout<<"El polinomio fue derivado anteriormente"<<endl;
    cout<<"Polinomio derivado: "<<endl;
    cout<<"Horner: "<<endl;
    result = horner(pd, n2, x);
    cout<<result<<endl;
    cout<<"Numero de operaciones: "<<cont<<endl;
    cout<<"Metodo directo: "<<endl;
    eval(pd, n2, x);
    cout<<"Numero de operaciones: "<<cont<<endl;
    
    cout<<endl;
    cout<<"Analisis: "<<endl;
    cout<<"El algoritmo de Horner al solo requerir una n sumas y n productos, requiere unicamente 2n operaciones"<<endl;
    cout<<"Para evaluar el polinomio de manera directa teniendo en cuenta los coeficientes tenemos: "<<endl;
    cout<<"(n^2 + 3n)/2"<<endl;
}
