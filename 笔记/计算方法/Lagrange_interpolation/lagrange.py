# 本代码仅实现了等分插值的情况，实际使用需修改：目标方程f，等分区间[a,b]，等分次数N

from sympy import *

# 获取方程
def get_func(Q):
    x = symbols('x')
    if Q == 1:
        expr = 1 / (1+x**2)
    elif Q == 2:
        expr = exp(x) 
    elif Q == 4:
        expr = x**(0.5)
    f = lambdify(x, expr, "numpy")
    return f

# 返回插值节点的迭代器
def dataLoader(a, b, N, f):
    for n in N:
        x_list = list()
        y_list = list()
        h = (b - a) / n
        for i in range(n+1):
            x = a + h*i
            y = f(x)
            x_list.append(x)
            y_list.append(y)
        yield x_list, y_list

# 拉格朗日插值，返回估计值
def lagrange_Interpolation(x_list, y_list, X):
    Y = list()
    for x in X:
        y = 0
        n = len(x_list)
        for i in range(n):
            l = 1
            for j in range(n):
                if j == i:
                    continue
                else:
                    l *= (x - x_list[j]) / (x_list[i] - x_list[j])
            y += l*y_list[i]
        Y.append(y)
    return Y


def main():

    print("******问题1.1******")
    f = get_func(Q=1)
    X = [0.75, 1.75, 2.75, 3.75, 4.75]
    N = [5, 10, 20]
    print(f"待估计点 {X}")
    Y = [f(x) for x in X]
    print(f"真实值 {Y}")
    for x_list, y_list in dataLoader(a=-5, b=5, N=N, f=f):
        Y_hat = lagrange_Interpolation(x_list, y_list, X)
        print(f"等分次数 {len(x_list) - 1}, 估计值 {Y_hat}")

    print("******问题1.2******")
    f = get_func(Q=2)
    X = [-0.95, -0.05, 0.05, 0.95]
    N = [5, 10, 20]
    print(f"待估计点 {X}")
    Y = [f(x) for x in X]
    print(f"真实值 {Y}")
    for x_list, y_list in dataLoader(a=-1, b=1, N=N, f=f):
        Y_hat = lagrange_Interpolation(x_list, y_list, X)
        print(f"等分次数 {len(x_list) - 1}, 估计值 {Y_hat}")

    print("******问题2.1******")
    f = get_func(Q=1)
    X = [-0.95, -0.05, 0.05, 0.95]
    N = [5, 10, 20]
    print(f"待估计点 {X}")
    Y = [f(x) for x in X]
    print(f"真实值 {Y}")
    for x_list, y_list in dataLoader(a=-1, b=1, N=N, f=f):
        Y_hat = lagrange_Interpolation(x_list, y_list, X)
        print(f"等分次数 {len(x_list) - 1}, 估计值 {Y_hat}")

    print("******问题2.2******")
    f = get_func(Q=2)
    X = [-4.75, -0.25, 0.25, 4.75]
    N = [5, 10, 20]
    print(f"待估计点 {X}")
    Y = [f(x) for x in X]
    print(f"真实值 {Y}")
    for x_list, y_list in dataLoader(a=-5, b=5, N=N, f=f):
        Y_hat = lagrange_Interpolation(x_list, y_list, X)
        print(f"等分次数 {len(x_list) - 1}, 估计值 {Y_hat}")

    print("******问题4.1******")
    f = get_func(Q=4)
    X = [5, 50, 115, 185]
    Y = [f(x) for x in X]
    print(f"待估计点 {X}")
    x_list = [1, 4, 9]
    y_list = [f(x) for x in x_list]
    print(f"真实值 {Y}")
    Y_hat = lagrange_Interpolation(x_list, y_list, X)
    print(f"估计值 {Y_hat}")

    print("******问题4.2******")
    f = get_func(Q=4)
    X = [5, 50, 115, 185]
    Y = [f(x) for x in X]
    print(f"待估计点 {X}")
    x_list = [36, 49, 64]
    y_list = [f(x) for x in x_list]
    print(f"真实值 {Y}")
    Y_hat = lagrange_Interpolation(x_list, y_list, X)
    print(f"估计值 {Y_hat}")

    print("******问题4.3******")
    f = get_func(Q=4)
    X = [5, 50, 115, 185]
    Y = [f(x) for x in X]
    print(f"待估计点 {X}")
    x_list = [100, 121, 144]
    y_list = [f(x) for x in x_list]
    print(f"真实值 {Y}")
    Y_hat = lagrange_Interpolation(x_list, y_list, X)
    print(f"估计值 {Y_hat}")

    print("******问题4.4******")
    f = get_func(Q=4)
    X = [5, 50, 115, 185]
    Y = [f(x) for x in X]
    print(f"待估计点 {X}")
    x_list = [169, 196, 225]
    y_list = [f(x) for x in x_list]
    print(f"真实值 {Y}")
    Y_hat = lagrange_Interpolation(x_list, y_list, X)
    print(f"估计值 {Y_hat}")

if __name__ == "__main__":
    main()