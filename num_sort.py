# -*- coding: UTF-8 -*-

#
import numpy as np

if __name__ == '__main__':
    # 索引最大值的位置
    data = np.sin(np.arange(20).reshape(4,5))
    print data
    # 获取每一列索引最大值的位置
    da_index = data.argmax(axis=0)
    print da_index
    data_value = data[da_index,range(data.shape[1])]
    print data_value


    #扩展
    A = np.arange(0,40,10)
    print A
    B = np.tile(A,(3,5))
    print B

    # 排序
    a = np.array([[4,3,5],[1,2,4]])
    print a
    b = np.sort(a,axis=1)
    print b
    a.sort(axis=1)
    print a
    # argsort 返回由小到大的下标
    d = np.array([4,7,5,2])
    c = d.argsort()
    print c
    # 下标取值法
    print d[c]












