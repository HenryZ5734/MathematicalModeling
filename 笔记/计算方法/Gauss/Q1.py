# 实际使用需修改：main函数中{A，B的值以及Gauss函数传入的参数}

import numpy as np
np.set_printoptions(precision=16)

def Gauss(A, B, X, r=4, c=4, flag=True):
    # 获得上三角系数矩阵
    for i in range(r-1):

        max = i

        # 获得列绝对值最大元素的行标
        for p in range(i+1, r):
            if np.abs(A[max][i]) < np.abs(A[p][i]):
                max = p

        # 奇异矩阵
        if A[max][i] == 0:
            flag = False 
            break

        # 交换两行
        if max != i:
            row = np.arange(r)
            row[max] += row[i]
            row[i] = row[max] - row[i]
            row[max] = row[max] - row[i]
            A = A[row, :]
            B = B[row]

        # 更新
        for j in range(i+1, r): 

            # 更新系数矩阵
            m = A[j][i] / A[i][i]
            for k in range(i, c):
                A[j][k] -= m * A[i][k] 

            # 更新B
            B[j] -= m * B[i]

    if flag==True:
        for i in range(r-1, -1, -1):
            X[i] += B[i]
            for j in range(i+1, c):
                X[i] -= A[i][j]*X[j] 
            X[i] /= A[i][i]
        print(X)
    else:
        print("FAIL")

def main():

    # 问题 1.1
    print("问题 1.1")
    A = np.array([
        [0.4096, 0.1234, 0.3678, 0.2943],
        [0.2246, 0.3872, 0.4015, 0.1129],
        [0.3645, 0.1920, 0.3781, 0.0643],
        [0.1784, 0.4002, 0.2786, 0.3927]
    ])
    B = np.array([1.1951, 1.1262, 0.9989, 1.2499])
    X = np.zeros(4)
    Gauss(A, B, X)

    # 问题 1.2
    print("问题 1.2")
    A = np.array([
        [136.01, 90.860, 0, 0],
        [90.860, 98.810, -67.590, 0],
        [0, -67.590, 132.01, 46.260],
        [0, 0, 46.260, 177.17]
    ])
    B = np.array([226.87, 122.08, 110.68, 223.43])
    X = np.zeros(4)
    Gauss(A, B, X)

    # 问题 1.3
    print("问题 1.3")
    A = np.array([
        [1, 1/2, 1/3, 1/4],
        [1/2, 1/3, 1/4, 1/5],
        [1/3, 1/4, 1/5, 1/6],
        [1/4, 1/5, 1/6, 1/7]
    ])
    B = np.array([25/12, 77/60, 57/60, 319/420])
    X = np.zeros(4)
    Gauss(A, B, X)

    # 问题 1.4
    print("问题 1.4")
    A = np.array([
        [10, 7, 8, 7],
        [7, 5, 6, 5],
        [8, 6, 10, 9],
        [7, 5, 9, 10]
    ], dtype=np.float64)
    B = np.array([32, 23, 33, 31], dtype=np.float64)
    X = np.zeros(4)
    Gauss(A, B, X)

if __name__=="__main__":
    main()