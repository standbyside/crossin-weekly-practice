#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：统计出《三国演义》书中被提及最多的角色
【附加题】：在统计分词的基础上，发挥更多的想象力：图表可视化、生成词云、分析人物的关联性、人物出场分布等等。
"""

import jieba
import os.path
from collections import Counter


def analysis_sanguo(file_path):
    content = open(file_path).read()
    # 切词
    cut_list = jieba.lcut(content)
    # 去掉无效的词
    valid_list = valid_words(cut_list)
    # 对词进行统计
    return Counter(valid_list).most_common(10)


def valid_words(old_list):
    new_list = []
    exclude_list = [
        "将军", "却说", "二人", "不可", "荆州", "不能", "如此", "商议", "如何", "军士", "左右", "次日",
        "大喜", "引兵", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "主公", "军马", "陛下", "人马",
        "都尉", "一人", "不知", "汉中", "都尉", "众将", "只见", "后主", "蜀兵", "大叫", "都督", "上马"
    ]
    person_names = [
        ["诸葛亮", "孔明", "卧龙"],
        ["关羽", "云长", "关公"],
        ["刘备", "玄德", "刘皇叔"],
        ["曹操", "孟德", "曹丞相"],
    ]
    for word in old_list:
        if len(word) < 2:
            continue
        if word in exclude_list:
            continue
        if word.endswith("曰"):
            word = word[:-1]
        for person in person_names:
            for name in person:
                if name in word:
                    word = person[0]
        new_list.append(word)
    return new_list


def get_file_path():
    # 当前目录
    base_path = os.path.dirname(__file__)
    # 目录替换
    return base_path.replace('solutions', 'files/三国.txt')


print(analysis_sanguo(get_file_path()))

