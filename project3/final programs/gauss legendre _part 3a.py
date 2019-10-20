from numpy import *
import time as time
import sys
import matplotlib.pyplot as plt
from numba import jit
tol = 1e-10
ZERO = 1.0E-10
@jit
def fun_6D(x1, y1, z1, x2, y2, z2):
    alpha = 2
    func_val = 0
    r1 = sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    r2 = sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)
    r1r2 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    if (r1r2 >= tol):
        func_val = exp(-2 * alpha * (r1 + r2)) / r1r2
        return (func_val)
    else:
        return 0
@jit
def gauleg(x1, x2, x, w, n):
    itr = 0
    m = (n + 1) / 2
    xm = (x2 + x1) / 2
    xl = (x2 - x1) / 2

    for i in range(int(ceil(m))):
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
    print(x, w)
    return x, w

outf = open('gauss legendre.txt', 'w+')
outf.write("n \t\t a\\tt  b\t\t  legrendre_resutlt\t\t exact_result\t\t realtive error\t\t exe time_legrendre\n")
outf.close()

def main():
    a = -5
    b = 5
    int_gauss = 0
    x = zeros(n)
    w = zeros(n)
    r = zeros(n)
    u = zeros(n)
    gauleg(a, b, r, u, n)

    exact_integral = 5 * 3.14 * 3.14 / 256
    legrendre_start_time = time.time()
    for i1 in range(0, n):
        for i2 in range(0, n):
            for i3 in range(0, n):
                for j1 in range(0, n):
                    for j2 in range(0, n):
                        for j3 in range(0, n):
                            temp = 1.0
                            temp = temp * fun_6D(r[i1], r[i2], r[i3], r[j1], r[j2], r[j3])
                            # print("func6d array", len(r))
                            # temp= fun_6D(r[i1],r[i2],r[i3],r[j1],r[j2],r[j3]) *u[i1]*u[i2]*u[i3]*u[j1]*u[j2]*u[j3]
                            temp = temp * u[i1] * u[i2] * u[i3] * u[j1] * u[j2] * u[j3]
                            int_gauss = temp + int_gauss
    print("int_gauss")
    print(int_gauss)
    legrendre_finish_time = time.time()
    legrendre_exe_time = legrendre_finish_time - legrendre_start_time
    # print("legrendre exe time", legrendre_exe_time)
    relatative_error = abs(int_gauss - exact_integral) / exact_integral
    # print("exact integral")
    # print(exact_integral)

    # print("relatative_error")
    # print(relatative_error)

    outf = open('gauss legendre.txt', 'a')
    outf.write(str(n))
    outf.write("\t\t")
    outf.write(str(a))
    outf.write("\t\t")
    outf.write(str(b))
    outf.write("\t\t")
    outf.write("{:.6f}".format(int_gauss))
    outf.write("\t\t")
    outf.write("{:.6f}".format(exact_integral))
    outf.write("\t\t")
    outf.write("{:.6f}".format(relatative_error))
    outf.write("\t\t")
    outf.write("{:.6f}".format(legrendre_exe_time))
    outf.write("\n")
    outf.close()


for i in range(10, 30, 5):
    n = i
    if __name__ == "__main__":
        main()