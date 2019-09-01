#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：统计一部英文小说里单词的出现次数（忽略大小写），按出现次数显示最高的 100 个单词
【附加题】：多统计几个不同作家的作品，挑选一些特征词汇的次数画在图表上，展示不同作家的风格区别。
"""

from collections import Counter


def count_words(file_path):
    text = open(file_path).read()
    common_words = Counter(text.split(' ')).most_common(100)
    return common_words


print(count_words(r'/Users/zn/Downloads/word-cloud-text.txt'))
