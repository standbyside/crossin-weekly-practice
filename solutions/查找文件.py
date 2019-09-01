#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹
"""

import fnmatch
import os


def search_file_1(file_path, txt_list=None):
    """解法1."""
    if txt_list is None:
        txt_list = []
    for f in os.listdir(file_path):
        abs_path = os.path.join(file_path, f)
        if os.path.isdir(abs_path):
            search_file_1(abs_path, txt_list)
        elif os.path.splitext(abs_path)[1] == '.txt':
            txt_list.append(f)
    return txt_list


def search_file_2(input_dir):
    """解法2."""
    txt_list = []
    for parent, dir_names, file_names in os.walk(input_dir):
        for file_name in file_names:
            txt_list.append(file_name)
    return fnmatch.filter(txt_list, '*.txt')


L = search_file_1(r"D:\workspace")
print(L)

L = search_file_2(r"D:\workspace")
print(L)
