#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：
    设定一个长度为 N 的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值。

【附加题】：
    输入的数字串可以重新打乱排列，比如输入 123 ，打乱排列之后会有 132，213，231，312，321 等情况，
    其他条件不变，求最大值。
"""


def product_1(num):
    pass


assert product_1(312) == 62
assert product_1(1234) == 492
assert product_1(12345) == 6170
assert product_1(123456) == 74070


def product_2(num):
    pass


assert product_2(1234) == 1312
assert product_2(12345) == 22412
assert product_2(123456) == 342002
