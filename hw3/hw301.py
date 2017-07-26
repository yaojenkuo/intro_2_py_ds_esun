# coding=utf-8
'''
建立一個外觀 (9, 9) 的 ndarray 並且填入九九乘法表
Author: XXX
'''

# solution 1
import numpy as np

arr_1 = np.arange(1, 10).reshape(__, __)
arr_2 = np.arange(1, 10).reshape(__, __)
print np.dot(arr_1, arr_2)

# solution 2
import numpy as np

ans = np.empty(__, dtype = 'int').reshape(__, __)
nrow = ans.shape[0]
ncol = ans.shape[1]

for i in range(nrow):
    for j in range(ncol):
        ans[i, j] = __ * __

print ans