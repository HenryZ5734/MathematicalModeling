# 实际使用需修改：积分函数f，积分区间[a,b]，精度epsilon

import numpy as np
from sympy import *

# 判断哪个问题
def get_func(Q):
    x = symbols('x')
    if Q == 1:
        expr = x**2 * exp(x)
    elif Q == 2:
        expr = sin(x) * exp(x)
    elif Q == 3:
        expr = 4/(1+x**2)
    elif Q == 4:
        expr = 1/(x+1)
    else: 
        return   
    return lambdify(x, expr, "numpy")

# 返回T[0][0]的值
def T_0_0(f, a, b):
    return 0.5*(b-a)*(f(a)+f(b))

# 初始化T[0][i]
def init(T, f, h, a, i):
    T[0][i] = 0.5*T[0][i-1]
    for k in range(1, 2**(i-1)+1):
        T[0][i] += 0.5 * h * f(a+(k-1/2)*h)
    return T

# 龙贝格积分
def Romberg(Q, a, b, epsilon=1e-6):
    i = 0 
    h = b-a
    f = get_func(Q)
    T = np.zeros(shape=(10,10))
    T[0][0] = T_0_0(f, a, b)
    loss = 100
    while(loss > epsilon):
        i += 1
        T = init(T, f, h, a, i)
        for m in range(1, i+1):
            T[m][i-m] = (4**m * T[m-1][i-m+1] - T[m-1][i-m]) / (4**m-1)
        loss = np.abs(T[m][0] - T[m-1][0])
        h = (b-a) / 2**i
    return T, i

# 打印数表T
def print_res(T, i):
    for j in range(i+1):
        for k in range(i-j+1):
            print("%.16f"%T[j][k], end=' ')
        print("")

def main():
    print("*********问题1.1*********")
    print_res(*Romberg(Q=1, a=0, b=1))
    print("*********问题1.2*********")
    print_res(*Romberg(Q=2, a=1, b=3))
    print("*********问题1.3*********")
    print_res(*Romberg(Q=3, a=0, b=1))
    print("*********问题1.4*********")
    print_res(*Romberg(Q=4, a=0, b=1))

if __name__ == "__main__":
    main()