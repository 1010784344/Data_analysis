# -*- coding: UTF-8 -*-
# numpy 的基本操作


import numpy
if __name__ == '__main__':
    # 用 numpy 打开一个数据
    data = numpy.genfromtxt('test.txt',delimiter=',',dtype=int)
    print type(data)
    print data

    # 取ndarray具体某一个值
    print data[2,1]

    # 取ndarray具体某一行的值
    print data[2:3]

    # ':'选取所有的行，逗号隔开然后取列
    # 取ndarray具体某一列的值
    print data[:, 1]

    # 取ndarray具体某几列的值
    print data[:, 4:5]

    # 取ndarray具体某几行某几列的值
    print data[2:4, 4:5]

    # 将python 中的 list转换为 ndarray
    data_list = numpy.array([5,7,9,3,8])
    data_list2 = numpy.array([[5,7,9,3,8],[15,87,9,23,18]])
    print data_list
    print type(data_list)
    # 打印矩阵的数据结构(几行几列)
    print data_list.shape
    print data_list2.shape
    # 打印矩阵的数据类型
    print data_list.dtype





















