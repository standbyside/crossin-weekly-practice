#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：

    在 python 中有 hashlib 和 base64 两大加密模块，
    将一串字符串先经过 hashlib.md5 加密，然后再经过 base64 加密，最后得到一串字符：
    'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'

    在此给出 4 个选项

        我们在一起吧
        我选择原谅你
        别说话，吻我
        多喝热水

    请各位大侦探们使用科学的方法算出我说的什么吧！
"""

import hashlib
import base64


def decrypt():
    password = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA='
    answers = ['我们在一起吧', '我选择原谅你', '别说话，吻我', '多喝热水']
    for answer in answers:
        md5_str = hashlib.md5(answer.encode('utf-8')).hexdigest()
        base64_byte = base64.b64encode(md5_str.encode('utf-8'))
        if str(base64_byte, 'utf-8') == password:
            return answer
    raise ValueError("can't find answer")


assert decrypt() == '多喝热水'
