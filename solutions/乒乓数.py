#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：
    乒乓序列从1开始计数，并且始终向上或向下计数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。
    乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
    1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

    定义一个函数 pingpong ，传入一个正整数参数 n ，返回第 n 个乒乓数
"""


def pingpong(n, k):
    pass


assert pingpong(7, 7) == 7
assert pingpong(8, 8) == 8
assert pingpong(55, 6) == 3
assert pingpong(100, 9) == 0
print('运行完毕')
