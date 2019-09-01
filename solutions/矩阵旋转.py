#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：给定一个 N * N 的矩阵（N >= 0），将其顺时针旋转 90°．输出处理之后的矩阵。举例：
                1    2    3       7    4    1

                4    5    6   →   8    5    2

                7    8    9       9    6    3

【附加题】：在不创建新矩阵的情况下做变换，即所有的修改都在原矩阵上直接进行。
"""


def ratate(matrix):
    """
    : type matrix : List(List(Int))
    : rtype: List(List(Int))
    """
    # your code here


m1 = [[]]
m2 = [[1]]
m3 = [[i for i in range(3)] for j in range(3)]
m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

assert ratate(m1) == [[]]
assert ratate(m2) == [[1]]
assert ratate(m3) == [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
assert ratate(m4) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
