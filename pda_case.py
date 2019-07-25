# -*- coding: utf-8 -*-
# 经典泰坦尼克竞赛题

import pandas as pd
import numpy as np

if __name__ == '__main__':
    train_info = pd.read_csv('train.csv')
    print(train_info.head())

    # 单取年龄这一列的前10条数据
    age = train_info['Age']
    print(age.loc[0:10])
    # 判断缺失值
    age_is_null = pd.isnull(age)
    print(age_is_null)
    #用True 或者 False 当成我们的一个索引传进来
    # 就会帮我们把只有Ture 的留下来，False 都过滤回去
    age_null_true = age[age_is_null]
    print(age_null_true)
    # 打印为 Ture 的长度
    print(len(age_null_true))
    # 求年龄的平均值
    # age_is_null 默认是只输出True，输出False 需进行指定
    age_sur = train_info['Age'][age_is_null == False]
    correct_age = sum(age_sur)/len(age_sur)
    print(correct_age)
    #pd 自带函数，求有缺失值的均值的方法
    print(train_info['Age'].mean())
    # 仓位等级有：1，2，3.求每个仓位等级的平均船票价格是多少

















