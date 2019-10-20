
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
def func_6D(x1,y1,z1,x2,y2,z2,q):
    alpha=2
    func_val=0
    r1=np.sqrt(x1*x1+y1*y1+z1*z1)
    r2=np.sqrt(x2**2+y2**2+z2**2)
    r1r2=np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    if (r1r2>=tol):
        q.put(np.exp(-2*alpha*(r1+r2))/r1r2)
    else:
        q.put(0)
if __name__=='__main__':
    mp.set_start_method('spawn')
    # MC_start_time = time.time()
    # results.append(p.apply_async(MC, (n,)))
    # MC_finish_time = time.time()
    # MC_exe_time = MC_finish_time - MC_start_time
    # print("MC exe time", MC_exe_time)
    #A=[100000,1000000,10000000]
    A=[10]
    for i in range (len(A)):
        n=A[i]
        print("n", n)
        a = -5
        b = 5
        d = 6
        Integral_MC = 0
        sum_sigma = 0
        jacobi_det = (b - a) ** d
        exact_integral=5*3.14*3.14/256
        for j in range(0,n):
            x1 = np.random.uniform(a, b)
            x2 = np.random.uniform(a, b)
            y1 = np.random.uniform(a, b)
            y2 = np.random.uniform(a, b)
            z1 = np.random.uniform(a, b)
            z2 = np.random.uniform(a, b)
            #print(x1, y1, z1, x2, y2, z2)
            q = mp.Queue()
            p = mp.Process(target=func_6D, args=(x1,y1,z1,x2,y2,z2,q))
            p.start()
            func_res=(q.get())
            #print("func_res",func_res)
            Integral_MC = Integral_MC + func_res
            sum_sigma += func_res * func_res
            p.join()
            #print(i)
            #print("integral mc",Integral_MC)
        Integral_MC /=  n
        sum_sigma /=  n
        variance = sum_sigma - Integral_MC*Integral_MC
        Integral_MC *= jacobi_det
        sigma = jacobi_det*np.sqrt(variance/n)
        exact_integral=5*3.14*3.14/256
        relative_error = abs(Integral_MC-exact_integral)/exact_integral;
        print("int_MC")
        print(Integral_MC)
        print("exact integral")
        print(exact_integral)
        print("relatative_error")
        print(relative_error)
        outf=open('monte carlo brute_par.txt', 'a')
        outf.write(str(n))
        outf.write("\t")
        outf.write(str(a))
        outf.write("\t")
        outf.write(str(b))
        outf.write("\t")
        outf.write("{:.6f}".format(Integral_MC))
        outf.write("\t")
        outf.write("{:.6f}".format(exact_integral))
        outf.write("\t")
        outf.write("{:.6f}".format(relative_error))
        outf.write("\t")
        outf.write("{:.6f}".format(sigma))
        #outf.write("\t")
        #outf.write("{:.6f}".format(MC_exe_time))
        outf.write("\n")
        outf.close()