# coding=utf-8
'''
實作交換排序法函數 `exchange_sort()`，並且有一個參數可以決定要遞增或遞減排序
Author: XXX
'''

def exchange_sort(x, reverse = False):
    '交換排序法函數'
    if reverse == False:
        for i in range(len(__) - 1):
            for j in range((__ + 1), len(__)):
                if x[i] __ x[j]:
                    x[i], x[j] = x[j], x[i]
        return x
    else:
        for i in range(len(__) - 1):
            for j in range((__ + 1), len(__)):
                if x[i] __ x[j]:
                    x[i], x[j] = x[j], x[i]
        return x