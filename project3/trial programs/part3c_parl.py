
import numpy as np
import time as time
import sys
import matplotlib.pyplot as plt
from scipy.stats import uniform
import multiprocessing as mp
# monte carlo brute force method using uniform distribution
tol=1e-10
outf = open('monte carlo brute_par.txt', 'w+')
outf.write("n \t a\t  b\t  MCbrute_resutlt\t exact_result\t realtive error\t sigma\t exe time_MC_bruteforce\n")
outf.close()
"""
def func_6D(x1,y1,z1,x2,y2,z2):
    alpha=2
    func_val=0
    r1=sqrt(x1*x1+y1*y1+z1*z1)
    r2=sqrt(x2**2+y2**2+z2**2)
    r1r2=sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    if (r1r2>=tol):
        func_val=exp(-2*alpha*(r1+r2))/r1r2
    else
        func_val=0
    return func_val
        print("func_cal",func_val)
        #out_que.put(func_val)
        #return_dict[k]=func_val
        return (func_val)
    else:
        return 0
        #return_dict[k]=0
        #out_que.put(0)    
#Que=Queue()
"""

def main():
    for i, data in enumerate (dataloader):
        a=-5
        b=5
        d=6
        jacobi_det = (b - a) ** d
        sum_sigma=0
        integral_MC = 0
        sigma=0
        func_res=0
        print("n",n)
        out_que=0
        pros=[]
        #exact_integral=5*3.14*3.14/256
       # MC_start_time = time.time()
        #results.append(p.apply_async(MC, (n,)))
        #MC_finish_time = time.time()
        #MC_exe_time = MC_finish_time - MC_start_time
        #print("MC exe time", MC_exe_time)
        for j in range (n):

            x1 = np.random.uniform(a,b)
            x2 = np.random.uniform(a,b)
            y1=  np.random.uniform(a,b)
            y2= np. random.uniform(a,b)
            z1= np.random.uniform(a,b)
            z2= np.random.uniform(a,b)
            print(x1,y1,z1,x2,y2,z2)
            func_res=func_6D(x1,y1,z1,x2,y2,z2)
            #print("return dict",return_dict[k])
            integral_MC = integral_MC+func_val
            print("integral mc",integral_MC)
            sum_sigma+=func_val*func_val
            return integral_MC, sum_sigma
if __name__=='__main__':
   #A=[100000,1000000,10000000]
    
    A=[10]
    main()
    """
    for i in range (len(A)):
        p=Pool(5)
        results=[]
        n=A[i]
        a=-5
        b=5
        d=6

        integral_MC=0
        out=0
        sum_sigma=0

        #print("int_MC")
        #print(int_MC)
    for res in results:
        val=res.get()
        integral_MC = integral_MC+val
        print("integral mc",integral_MC)
        sum_sigma+=val*val
    integral_MC /=  n
    sum_sigma /=  n
    variance = sum_sigma - integral_MC*integral_MC
    integral_MC *= jacobi_det
    sigma = jacobi_det*sqrt(variance/n)
    exact_integral=5*3.14*3.14/256
    relative_error = abs(integral_MC-exact_integral)/exact_integral;
    print("int_MC")
    print(integral_MC)

        #print("exact integral")
        #print(exact_integral)

        #print("relatative_error")
        #print(relative_error)

    outf=open('monte carlo brute_par.txt', 'a')
    outf.write(str(n))
    outf.write("\t")
    outf.write(str(a))
    outf.write("\t")
    outf.write(str(b))
    outf.write("\t")
    outf.write("{:.6f}".format(integral_MC))
    outf.write("\t")
    outf.write("{:.6f}".format(exact_integral))
    outf.write("\t")
    outf.write("{:.6f}".format(relative_error))
    outf.write("\t")
    outf.write("{:.6f}".format(sigma))
    outf.write("\t")
    outf.write("{:.6f}".format(MC_exe_time))
    outf.write("\n")
    outf.close()
"""