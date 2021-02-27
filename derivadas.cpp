#include <iostream>
#include <functional>
#include <cmath>
#include <fstream>

using namespace std;

double derivative(const function<double(double)>& f, double x0, double h) {
  double h2 = h / 2;
  double lo = x0 - h2;
  double hi = x0 + h2;
  return (f(hi) - f(lo)) / h;
}

double Second_derivative(const function<double(double)>& f, double x0, double h) {
  double h2 = 2*h;
  double lo = x0 - h2;
  double hi = x0 + h2;
  return (f(hi) -2*f(x0) + f(lo)) / (4*pow(h,2));
}


double g(double x) {
  return x-sin(x);
}

double dg(double x) {
  return sin(x);
}


int main() {
  double x = 0;
  double h = 0.05;
  double ans = 1-cos(x); // 
  double err1 = 0;
  cout.precision(10);
  int n = 0;
  while (n < 1) {
    double app = derivative(g, x, h);
    double errlocal1 = ans - app;
    if (errlocal1<0) { err1 = -errlocal1; }
    double errglobal1;
    errglobal1 = errlocal1/ans;
    cout << "With h ==" << h << " estimate f'(" << x << ") is " << app << " error local ==" << err1 << " error global =="<< errglobal1 << endl;
    n = n+1;  
  }
  
  double x_inter [] = {-1,  -0.95, 	-0.9,	-0.85,	-0.8,	-0.75,	-0.700000000000001,	-0.650000000000001,	-0.600000000000001,	-0.550000000000001,	-0.500000000000001,	-0.450000000000001,	-0.400000000000001,	-0.350000000000001,	-0.300000000000001,	-0.250000000000002,	-0.200000000000002,	-0.150000000000002,	-0.100000000000002,	-0.050000000000002,	-1.99840144432528E-15, 0.049999999999998,	0.099999999999998,	0.149999999999998,	0.199999999999998,	0.249999999999998,	0.299999999999997,	0.349999999999997,	0.399999999999997,	0.449999999999997,	0.499999999999997,	0.549999999999997,	0.599999999999997,	0.649999999999997,	0.699999999999997,	0.749999999999996,	0.799999999999996,	0.849999999999996,	0.899999999999996,	0.949999999999996,	1};
  
  double err2 = 0;
  double errglobal =0;
  double err3 , err4 = 0;
  
  ofstream archivo;
  archivo.open("datosderivada.txt", ios::out);

  
  for (int i=0; i<=40; i++)
  {
	
	double y = g(x_inter[i]);  //Evaluar funcion  f(x)=x-sin(x)
  	double y_prima = 1-cos(x_inter[i]); // Evaluar derivada analitica
  	double y_prima_prima=sin(x_inter[i]); // Evaluar segunda derivada analítica 
  	double dy = derivative(g, x_inter[i], h); // primera derivada central
  	double ddy = derivative(dg, x_inter[i], h); // derivada de la primera derivada 
  	double ddy_sd = Second_derivative(g, x_inter[i], h); // segunda derivada central 
	double errlocal2 = y_prima - dy; // Error local 1 derivada
	double errlocal3 = ddy - y_prima_prima; // Error local 2 derivada
 	double errlocal4 = ddy_sd - y_prima_prima;
	if (errlocal2<0) { err2 = -errlocal2; }
  	if (errlocal3<0) { err3 = -errlocal3; }
  	if (errlocal4<0) { err4 = -errlocal4; }
  	double suma_analitica = 0;
  	double suma_err = 0;
  	suma_err = suma_err +  pow(err2,2);
  	suma_analitica = suma_analitica + pow(y_prima,2);
  	
  	double errglobal = pow((suma_err/suma_analitica),0.5);
  	cout << x_inter[i] << " " << y << " " << dy << " " << y_prima << " " << err2 << " " << errglobal << " " << err3 << " " << err4 << endl;
  	archivo << x_inter[i] << " " << y << " " << dy << " " << y_prima << " " << err2 << " " << errglobal << " "<< err3 << " " << err4 << endl;
  }
  	
  
  archivo.close();
  return 0;
}
