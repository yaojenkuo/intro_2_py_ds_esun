# coding=utf-8
'''
投擲一枚公正的骰子，總共出現三個六才能停下來，請印出投擲總次數與投擲軌跡
Author: XXX
'''

from random import choice

dice = range(__, __)
flip_result = []

while flip_result.count(__) < __:
    flip_result.append(choice(dice))

print "總共投擲 %i 次" % len(flip_result)
print flip_result