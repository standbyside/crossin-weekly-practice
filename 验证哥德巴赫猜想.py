#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实现一段代码，输入一个大于 2 的偶数 k，输出两个质数 m、n，满足 m + n == k
"""

import math

# 100以内质数
prime_nums = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
)


def goldbach(k):
    if not isinstance(k, int) or k <= 2 or k % 2 != 0:
        raise ValueError("%s 不是大于2的偶数" % str(k))

    nums = list(prime_nums)
    if k > 97:
        nums = nums + [x for x in range(97, k) if x % 2 != 0]

    for num1 in nums:
        num2 = k - num1
        if num2 <= 0:
            break
        if is_prime(num2):
            return num1, num2
    return None, None


def is_prime(num):
    if num in prime_nums:
        return True
    if num <= prime_nums[-1]:
        return False
    # 遍历２以上，Ｎ的平方根以下的，每一个整数或奇数
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


assert goldbach(123456) == (7, 123449)
assert goldbach(12345678) == (31, 12345647)
