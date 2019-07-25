# -*- coding: UTF-8 -*-
import pandas
import sys
defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
if __name__ == '__main__':
    food_info = pandas.read_csv('food_info.csv')
    print (type(food_info))
    print (food_info.dtypes)