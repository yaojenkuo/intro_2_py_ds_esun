# coding=utf-8
'''
實作樣本標準差的函數 `my_sd()`，可以使用 `math.sqrt()` 或前一題自訂的 `my_sqrt()
Author: XXX
'''
import math

def my_sd(x):
    '樣本標準差的函數'
    def my_len(x):
        '序列長度的函數'
        cnt = 0
        for i in x:
            cnt += 1
        return cnt
    
    def my_sum(x):
        '序列總和的函數'
        summation = 0
        for i in x:
            summation += i
        return summation
    
    def my_mean(x):
        '序列平均的函數'
        return float(my_sum(x) / my_len(x))
    
    N_minus_one = my_len(__) - 1
    x_bar = my_mean(__)
    sse = 0
    for i in x:
        sse += (i - __)**2
    return math.sqrt(sse / N_minus_one)