    #include <iostream>
    #include <fstream>
    #include <iomanip>
    #include <cmath>
    #include <string>
    #include <armadillo>
    #include "time.h"

    // use namespace for output and input
    using namespace std;
    using namespace arma;
ofstream ofile;

inline double f(double x) {return 100.0*exp(-10.0*x);}
inline double exact(double x) {return 1.0-(1-exp(-10))*x-exp(-10*x);}


// Begin main program
int main(int argc, char *argv[]){
  int exponent;
    string filename;
    // We read also the basic name for the output file and the highest power of 10^n we want
    if( argc <= 1 ){
          cout << "Bad Usage: " << argv[0] <<
              " read also file name on same line and max power 10^n" << endl;
          exit(1);
    }
        else{
        filename = argv[1]; // first command line argument after name of program
        exponent = atoi(argv[2]);
    }
    // Loop over powers of 10
    for (int i = 1; i <= exponent; i++){
      int  n = (int) pow(10.0,i);
      // Declare new file name
      string fileout = filename;
      // Convert the power 10^i to a string
      string argument = to_string(i);
      // Final filename as filename-i-
      fileout.append(argument);
      fileout.append(".txt");
      double h = 1.0/(n);
      double hh = h*h;
      // Set up arrays for the simple case

      // Set up vectors
      vec  d(n+1); vec solution (n+1) ; vec b(n+1); vec x(n+1); vec a(n+1) ; vec c(n+1);

     for(int k=1;k<=n-1;k++) c(k)=-1;
     for (int m=2;m<=n;m++) a(m)=-1;
     for (int p=1;p<=n;p++)  d(p)=2;


    //  vec d(n+1);  vec solution(n+1);  vec b(n+1);  vec x(n+1); vec a(n+1);vec c(n+1);
      //  setup of updated diagonal elements and enpoint values of x and b
      x(0) = 0.0; x(n) = 1.0;//solution vec
      b(0) = hh*f(x(0)); b(n) = hh*f(x(n));//function end points
      d(0) = 2.0; d(1)=2; d(n) = 2.0;//diagnal end points
      a(0)=0;a(1)=0;// coeff a
      c(0)=0;// coeff c

      /*vec d(n+1);  vec solution(n+1);  vec b(n+1);  vec x(n+1);
      // Quick setup of updated diagonal elements and enpoint values of x and b
      x(0) = 0.0; x(n) = 1.0;  b(0) = hh*f(x(0)); b(n) = hh*f(x(n)); d(0) = 2.0;  d(n) = 2.0; */


      for (int i = 1; i < n; i++){
       d(i)=d(i)-((a(i)*c(i-1))/d(i-1)); // modifying diag elements
   // d(i) = (i+1.0)/( (double) i);
        x(i) = i*h;
    b(i) = hh*f(x(i));
      }
     // Forward substitution
      clock_t start, finish;
            start = clock();
      for (int i = 2; i < n; i++)
           b(i)=b(i)-(a(i)*b(i-1)/d(i-1));
          //b(i) = b(i) + b(i-1)/d(i-1);
      // Backward substitution
      solution(n-1) = b(n-1)/d(n-1);
      for (int i = n-2; i > 0; i--)
          solution(i)=(b(i)-(c(i)*solution(i+1)))/d(i); // gen soln
          //solution(i) = (b(i)+solution(i+1))/d(i);
      finish = clock();
            double timeused = (double) (finish - start)/((double) CLOCKS_PER_SEC );
            cout << setiosflags(ios::showpoint | ios::uppercase);
                // cout << setprecision(10) << setw(20) << "Time used  for  computation=" << finish << endl;
                // cout << setprecision(10) << setw(20) << "Time used  for  computation=" << start << endl;

      // Now open file and write out results
      ofile.open(fileout);
      ofile << setiosflags(ios::showpoint | ios::uppercase);
      ofile << "       x:             approx:          exact:       relative error" << endl;
      for (int i = 1; i < n;i++) {
    double RelativeError = fabs((exact(x(i))-solution(i))/exact(x(i)));
    ofile << setw(15) << setprecision(8) << x(i);
    ofile << setw(15) << setprecision(8) << solution(i);
    ofile << setw(15) << setprecision(8) << exact(x(i));
         ofile << setw(15) << setprecision(8) << log10(RelativeError) << endl;
//cout<<log10(RelativeError)<<endl;
      }

      ofile.close();
cout << setprecision(10) << setw(20) << "Time used  for  computation=" << timeused << endl;
    }

    return 0;
}




