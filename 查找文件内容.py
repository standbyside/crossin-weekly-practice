#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹
在此基础上列出这个文件夹（含所有子文件夹）里，所有文件内容包括指定搜索文本的文件
"""

import os


def search_file_content(input_dir, key_word):
    """解法1."""
    txt_list = []
    for parent, dir_names, file_names in os.walk(input_dir):
        for file_name in file_names:
            abs_path = os.path.join(parent, file_name)
            if os.path.splitext(abs_path)[1] != '.txt':
                continue
            with open(abs_path, 'r', encoding='utf-8') as f:
                if key_word in f.read():
                    txt_list.append(file_name)
    return txt_list


L = search_file_content(r"D:\workspace\my-python", '查找')
print(L)
