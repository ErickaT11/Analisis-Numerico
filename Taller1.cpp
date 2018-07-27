#include <bits/stdc++.h>


using namespace std;


double m,t,v;
int cont = 0;
//------------------------------------------------------------------------
double evaluacion(double Xi ,double Xd,int nParticiones, int l)
{
  
  cont++;
  double Xe = 0;
  double resultado, resultado2;
  double siguiente = 0;
 
  Xe =  (Xd-Xi)/nParticiones;
  siguiente = Xe + Xi;


 //El vector representará la segmentación   
 vector<double> segmentos;
 
 segmentos.push_back(Xi);
 
 nParticiones =  nParticiones-1;

  while(nParticiones != 0)  {  
      segmentos.push_back(siguiente);
  
      siguiente = siguiente +  Xe;   
      nParticiones--;
 }
    
 segmentos.push_back(Xd);




 for(int i=0; i<segmentos.size()-1;i++)
   
 {
   
     resultado = (9.8*m/segmentos[i])*(1-exp(-1*(segmentos[i]/m)*t))-v;

     if(abs(resultado)<= 0.0000001) return segmentos[i]; 
     
     resultado2 = (9.8*m/segmentos[i+1])*(1-exp(-1*(segmentos[i+1]/m)*t))-v;

     if(resultado*resultado2<0)
 
		return evaluacion(segmentos[i],segmentos[i+1],nParticiones,l);
    
       
 }
    return Xd+=1;

}

//---------------------------------------------------------------------------------

int main()
{
  

// Se manejó la ecuación de la página 15. gm/c*(1-e^-((c/m)*t))-v\n
	double Xi = 0;
	double Xd = 0;
	double result = 0;
	int nParticiones;
  
    
	cout<<"La gravedad será tomada como 9.8"<<endl;
  
	cout<<"Por favor, ingrese los valores constantes"<<endl;
  
	cout<<"masa: "<<endl;
	cin>>m;
	cout<<"tiempo: "<<endl;
	cin>>t; 
	cout<<"velocidad: "<<endl;
	cin>>v;
 
 
 	cout<<" ingrese el numero de particiones: "<<endl;
   
 	cin>>nParticiones;

 
 	cout<<"límite inferior: "<<endl;
   
 	cin>>Xi;
  
  	cout<<"límite superior: "<<endl;
 
   	cin>>Xd;
    
  
 	result = evaluacion(Xi ,Xd,nParticiones,Xd);
   
	cout<<"Evaluación en: "<< result<<endl;
 	if(result > Xd)
     
  	 cout<<"Mayor a límite superior, no se encontró la solución";
  
  	else
   	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
 	cout<<"Solución (resultado final): "<<result<<endl;
   	cout<<"Número de iteraciones: "<<cont<<endl;
 	return 0;

}
