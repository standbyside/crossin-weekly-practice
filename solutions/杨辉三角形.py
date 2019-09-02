#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：传入正整数参数 M、N，返回杨辉三角形第 M 行，左起第 N 个数字（M，N都从0开始计算）
【附加题】：传入整数参数 M < 1000，生成前 M 行杨辉三角形
"""


def base_yh(m, n):
    if m < 0 or n < 0 or not isinstance(m, int) or not isinstance(n, int) or n > m:
        raise ValueError('非法入参')
    last_line = []
    for i in range(0, m + 1):
        cur_line = [1]
        if i > 0:
            for j in range(0, len(last_line) - 1):
                cur_line.append(last_line[j] + last_line[j + 1])
            cur_line.append(1)
        last_line = cur_line
    return last_line[n]


def generate_yh(m):
    if m < 0 or m > 1000 or not isinstance(m, int):
        raise ValueError('请输入大于0小于1000的正整数')
    last_line = []
    for i in range(0, m + 1):
        cur_line = [1]
        if i > 0:
            for j in range(0, len(last_line) - 1):
                cur_line.append(last_line[j] + last_line[j + 1])
            cur_line.append(1)
        print(cur_line)
        last_line = cur_line


assert base_yh(1, 1) == 1
assert base_yh(3, 2) == 3

generate_yh(10)
print('运行完毕')
