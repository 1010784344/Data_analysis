# -*- coding: UTF-8 -*-
import numpy as np
if __name__ == '__main__':
    A = np.array([[1,1],[0,1]])
    B = np.array([[2, 0],[3, 4]])
    # 星乘
    print A*B
    # 点乘（这两个相同）
    print A.dot(B)
    print np.dot(A,B)


    a = np.floor(10*np.random.random((3,4)))
    print a
    # 将多维矩阵，降为一维向量
    print a.ravel()
    # 矩阵转换的另一种方法
    # a.shape = (6,2)
    a.shape = (6,-1)
    print a
    #转置（行列转换）
    print a.T


    #拼接
    c = np.floor(10*np.random.random((2,2)))
    d = np.floor(10 * np.random.random((2, 2)))
    print np.hstack((c,d))#横拼
    print np.vstack((c,d))#竖拼

    #切分
    e = np.floor(10 * np.random.random((2, 12)))
    f = np.floor(10 * np.random.random((12, 2)))
    print e
    print np.hsplit(e, 3)  # 横切
    print f
    print np.vsplit(f, 3)  # 竖切






























