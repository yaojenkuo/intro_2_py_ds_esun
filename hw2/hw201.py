# coding=utf-8
'''
實作質數判斷函數 `is_prime()`，可以判斷輸入的數字是否為質數
Author: XXX
'''

def is_prime(x):
    '判斷輸入的數字是否為質數'
    factor_list = []
    i = __
    while len(__) < __:
        if x % i == 0:
            factor_list.append(i)
            i += 1
        i += 1
    if factor_list[__] == __:
        return "%i 是質數" % x
    else:
        return "%i 不是質數" % x