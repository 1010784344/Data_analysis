# -*- coding: UTF-8 -*-
import numpy
if __name__ == '__main__':

    vector = numpy.arange(15)
    print type(vector)

    # 快速构造 ndarray 数据
    vector1 = numpy.arange(15).reshape(3,5)
    print vector1

    # 快速构造 ndarray 数据 递加(步数)
    vector2 = numpy.arange(5,80,5).reshape(3, 5)
    print vector2

    # 打印数据结构
    print vector1.shape
    # 打印数据维度(一维，二维)
    print vector1.ndim
    # 当前一共是有多少个元素的
    print vector.size
    # 构造全0矩阵
    print numpy.zeros((3,4))
    # 构造全1矩阵
    print numpy.ones((3,4))
    #生成随机数
    print numpy.random.random((3,4))
    # 前2个参数分别是起点和终点，在1到100之间取5个值，并且这些值是平均分配的
    print numpy.linspace(1,100,5)

    vector3 = numpy.array([20,30,40,50])
    vector4 = numpy.arange(4)
    # 维度一样  减法
    vector5 = vector3 - vector4
    print vector5
    # 维度不一样  减法
    vector6 = vector3 - 1
    print vector6
    # 乘方
    print vector4**2
    #大小判断
    print vector3 < 35














