#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：

    把一段字符串用"右起竖排"的古文格式输出，并且拿竖线符号作为每一列的分割符。
    比如这段文字："静夜思 李白 床前明月光，疑似地上霜。举头望明月，低头思故乡。"
    输出结果：
        低┊举┊疑┊床┊静
        头┊头┊似┊前┊夜
        思┊望┊地┊明┊思
        故┊明┊上┊月┊
        乡┊月┊霜┊光┊李
        。┊，┊。┊，┊白
"""

import re


def vertical_poetry(content):
    if not content or not isinstance(content, str):
        raise ValueError("非法入参")
    title, author, poetry = check_poetry(content.split(" "))
    # 分割后保留分隔符
    arr = re.split("(，|。)", poetry)
    arr = ["".join(i) for i in zip(arr[0::2], arr[1::2])]
    arr.insert(0, title + ' ' + author)

    width = len(arr)
    height = len(arr[0]) if len(arr[0]) > len(arr[-1]) else len(arr[-1])

    for i in range(0, height):
        row = []
        for j in range(width - 1, -1, -1):
            word = arr[j][i:i+1]
            # 字数不够时以全角空格补充
            if not word:
                word = '　'
            row.append(word)
        print('┊'.join(row))


def check_poetry(arr):
    title = None
    author = None
    poetry = None
    if len(arr) == 1:
        poetry = arr[0]
    elif len(arr) == 2:
        title = arr[0]
        poetry = arr[2]
    elif len(arr) == 3:
        title = arr[0]
        author = arr[1]
        poetry = arr[2]
    return title, author, poetry


vertical_poetry('静夜思 李白 床前明月光，疑似地上霜。举头望明月，低头思故乡。')
