#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【基础题】：学习 wordcloud 基本用法，然后生成一张词云图
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_text(file_path):
    return open(file_path).read()


def get_word_cloud(text):
    cloud_generator = WordCloud(background_color='white')
    # 生成词云
    word_cloud = cloud_generator.generate(text)
    # 显示词云
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    # 保存图片
    word_cloud.to_file(r'/Users/zn/Downloads/word-cloud-image.jpg')


get_word_cloud(get_text(r'/Users/zn/Downloads/word-cloud-text.txt'))
print('运行完毕')
