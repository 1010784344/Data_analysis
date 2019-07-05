# -*- coding: UTF-8 -*-
# numpy 布尔类型的相关判断

import numpy
if __name__ == '__main__':

    vector = numpy.array([[5, 10, 15, 20],[1, 2, 3, 4]])

    equal_to_ten = (vector == 10)

    print equal_to_ten

    print vector[equal_to_ten]

    # 逻辑判断（与）
    ten = (vector == 10) & (vector == 30)
    print ten

    # 数据类型转换
    vector_copy = vector.astype(float)
    print vector_copy
    # 取最大最小值
    print vector.min()
    print vector.max()
    # 按行求和，按列求和
    print vector.sum(axis=1)
    print vector.sum(axis=0)























