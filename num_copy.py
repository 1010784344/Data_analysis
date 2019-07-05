# -*- coding: UTF-8 -*-
import numpy as np
if __name__ == '__main__':
    # 赋值
    a = np.arange(12)
    b = a
    print a is b
    b.shape = (3,4)
    print a.shape
    print id(a)
    print id(b)

    #view(浅拷贝)
    # id 不一致，shape 不一致，但就是值一致
    c = a.view()
    print c is a
    c.shape = (2,6)
    print a.shape
    c[0,4] = 1234
    print a
    print id(a)
    print id(c)

    # copy（深拷贝）
    # id 不一致，shape 不一致，值也不一致
    d = a.copy()
    print d is a
    d[0,3] = 999
    print a
    print id(a)
    print id(c)











