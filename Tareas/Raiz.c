#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main()
{
    double x;
    double raiz = sqrt(7.0);
    cout<<raiz<<endl;
    cin>>x;
    
    double aprox = ((1.0/2.0)*(x+(7.0/x)));
    double xError = fabs(raiz-aprox);
    cout<<aprox<<endl;
    while(xError > 0.0001)
    {
        aprox = ((1.0/2.0)*(aprox+(7.0/aprox)));
        cout<<aprox<<endl;
        xError = fabs(raiz-aprox);
        
    }
    xError = fabs((raiz-aprox)/raiz)*100.0;
    cout<<xError<<endl;
}
