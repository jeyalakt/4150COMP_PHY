from numpy import *
import time as time
import sys
import matplotlib.pyplot as plt
from numba import jit


@jit
def Integrand(u1, theta1, phi1, u2, theta2, phi2):
    cos_val = ((cos(theta1) * cos(theta2)) + sin(theta1) * sin(theta2) * cos(phi1 - phi2))
    r1r2 = sqrt(abs((u1 * u1) + (u2 * u2) - (2.0 * u1 * u2 * cos_val)))
    epsil = 1.0E-7
    if (r1r2 <= epsil):
        return 0
    else:
        fvalue = u1 * u1 * u2 * u2 * sin(theta1) * sin(theta2) * exp(-3 * (u1 + u2)) / r1r2
        return fvalue


@jit
def gauleg(x1, x2, x, w, n):
    itr = 0
    ZERO = 1.0E-10
    m = (n + 1) / 2
    xm = (0.5 * (x2 + x1))
    xl = (0.5 * (x2 - x1))
    for i in range(0, int(ceil(m))):
        z = cos(pi * (i + 0.75) / (n + 0.5))
        z1 = 0
        while (abs(z - z1) > ZERO):
            p1 = 1.0
            p2 = 0.0
            for j in range(n):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j + 1.0) * z * p2 - j * p3) / (j + 1.0)
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
        x[i] = xm - xl * z
        x[n - 1 - i] = xm + xl * z
        w[i] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
        w[n - 1 - i] = w[i]
    # print("legrende",x,w)
    return x, w


@jit
def gauss_laguerre(x, w, n, alf):
    # tol=1e-10
    ZERO = 1.0E-10
    EPS = 1.0E-8
    MAXIT = 10
    pi = 3.14159265359
    MAXIT = 10
    z1 = 0
    # print("n",n)
    for i in range(1, n + 1):

        if (i == 1):
            z = (1.0 + alf) * (3.0 + 0.92 * alf) / (1.0 + 2.4 * n + 1.8 * alf)
            # print("z",z)
        elif (i == 2):
            z += (15.0 + 6.25 * alf) / (1.0 + 0.9 * alf + 2.5 * n)
            # print("z",z)
        else:
            ai = i - 2
            z += ((1.0 + 2.55 * ai) / (1.9 * ai) + 1.26 * ai * alf / (1.0 + 3.5 * ai)) * (z - x[i - 2]) / (
                        1.0 + 0.3 * alf)
            # print("z",z)
        for its in range(1, MAXIT + 1):
            while (abs(z - z1) > ZERO):
                p1 = 1.0
                p2 = 0.0
                for j in range(1, n + 1):
                    p3 = p2
                    p2 = p1
                    p1 = ((2 * j - 1 + alf - z) * p2 - (j - 1 + alf) * p3) / j

                pp = (n * p1 - (n + alf) * p2) / z
                z1 = z
                z = z1 - p1 / pp
            x[i] = z
            # print("xi",x[i])
            w[i] = -exp(gammln(alf + n) - gammln(double(n))) / (pp * n * p2)
    # print("laguerre",x,w)
    return x, w


@jit
def gammln(xx):
    # cof=zeros(6)
    cof = [76.18009172947146, -86.50532032941677,
           24.01409824083091, -1.231739572450155,
           0.1208650973866179e-2, -0.5395239384953e-5]
    # print ("coeff", cof)
    y = x = xx
    tmp = x + 5.5
    tmp -= (x + 0.5) * log(tmp)
    ser = 1.000000000190015
    for j in range(0, 6):
        ser += cof[j] / ++y
        out = -tmp + log(2.5066282746310005 * ser / x)
        # print ("out", out)
        return out


outf = open('gauss lagaurre.txt', 'w+')
outf.write("n \t\t lagaurre_res\t\t exact_result\t\t realtive error\t\t exe time_lagaurre\n")
outf.close()


def main():
    tol = 1e-10
    ZERO = 1.0E-10
    EPS = 1.0E-8
    MAXIT = 10
    pi = 3.14159265359
    int_gauss_laguerre = 0.0;
    exact_integral = 5 * pi * pi / 256;
    temp = 0
    x = zeros(n)
    w = zeros(n)
    itr = 0
    laguerre_start_time = time.time()
    rg1 = zeros(n + 1)
    wg1 = zeros(n + 1)
    gauss_laguerre(rg1, wg1, n, 0.0)

    theta = zeros(n)
    w1 = zeros(n)
    gauleg(0, pi, theta, w1, n)

    phi = zeros(n)
    w2 = zeros(n)
    gauleg(0.0, 2 * pi, phi, w2, n)

    # print("lag, legtheta,legphi",w1, w2, wg1)
    # print ("wg befor loop",wg1)
    for i in range(1, n + 1):
        for k in range(0, n):
            for m in range(0, n):
                for j in range(1, n + 1):
                    for l in range(0, n):
                        for m2 in range(0, n):
                            tot_wt = wg1[i] * wg1[j] * w1[k] * w1[l] * w2[m] * w2[m2]
                            # print(tot_wt)
                            temp = Integrand(rg1[i], theta[k], phi[m], rg1[j], theta[l], phi[m2])
                            int_gauss_laguerre += temp * tot_wt
                            # print("temp",temp)
    print("int_gauss _laguerre ")
    print(int_gauss_laguerre)
    laguerre_finish_time = time.time()
    laguarre_exe_time = laguerre_finish_time - laguerre_start_time
    print("laguarre exe time", laguarre_exe_time)
    relatative_error = abs(int_gauss_laguerre - exact_integral) / exact_integral
    print("exact integral")
    print(exact_integral)
    print("relatative_error")
    print(relatative_error)
    outf = open('gauss lagaurre.txt', 'a')
    outf.write(str(n))
    outf.write("\t\t")
    outf.write("{:.6f}".format(int_gauss_laguerre))
    outf.write("\t\t")
    outf.write("{:.6f}".format(exact_integral))
    outf.write("\t\t")
    outf.write("{:.6f}".format(relatative_error))
    outf.write("\t\t")
    outf.write("{:.6f}".format(laguarre_exe_time))
    outf.write("\n")
    outf.close()

for i in range(10, 45, 5):
    n = i
    if __name__ == "__main__":
        main()
