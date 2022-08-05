# 实际使用需修改：目标方程、epsilon1和epsilon2的值、初始值x0、迭代次数N

from sympy import *
import numpy as np

# 获取原方程和求导后的方程
def get_func(Q):
    
    x = symbols('x')
    if Q == 11:
        expr = cos(x) - x
        f = lambdify(x, expr, "numpy")
        f_grad = lambdify(x, expr.diff(x), "numpy")
    elif Q == 12:
        expr = exp(-x) - sin(x)
        f = lambdify(x, expr, "numpy")
        f_grad = lambdify(x, expr.diff(x), "numpy")
    elif Q == 21:
        expr = x - exp(-x)
        f = lambdify(x, expr, "numpy")
        f_grad = lambdify(x, expr.diff(x), "numpy")
    elif Q == 22:
        expr = x**2 - 2*x*exp(-x) + exp(-2*x)
        f = lambdify(x, expr, "numpy")
        f_grad = lambdify(x, expr.diff(x), "numpy")
    return f, f_grad

# 牛顿迭代
def Newton(x0, N, Q, epsilon1 = 1e-6, epsilon2 = 1e-4):
    
    # 获得问题方程
    f, f_grad = get_func(Q)
    
    # 迭代过程
    for i in range(N):
        if np.abs(f(x0)) < epsilon1:
            print(f"{x0}")
            break
        elif np.abs(f_grad(x0)) < epsilon2:
            print("FAIL")
            break
        x1 = x0 - f(x0) / f_grad(x0)
        loss = np.abs(x1 - x0)
        if loss < epsilon1:
            print(f"{x1}")
            break
        else:
            x0 = x1

    # 输出错误标志
    if i>=N:
        print("FAIL")

def main():
    print("问题1.1")
    Newton(x0=np.pi/4, N=10, Q=11)
    print("问题1.2")
    Newton(x0=0.6, N=10, Q=12)
    print("问题2.1")
    Newton(x0=0.5, N=10, Q=21)
    print("问题2.2")
    Newton(x0=0.5, N=20, Q=22)

if __name__ == "__main__":
    main()