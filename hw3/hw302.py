# coding=utf-8
'''
利用 numpy 提供的 .size 屬性、.sum() 方法、.mean() 方法與 .sqrt() 實作樣本標準差函數
Author: XXX
'''

import numpy as np

def my_sd(x):
    x = np.array(x)
    N_minus_1 = __ - 1
    x_bar = np.mean(__)
    sqe = (__ - __)**2
    sse = np.sum(__)
    return np.sqrt(__ / __)