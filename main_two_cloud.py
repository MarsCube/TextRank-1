'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-04-08 21:37:49
LastEditTime: 2021-04-09 19:34:00
'''
"""
主函数，用来提取关键词 、及主题句子
"""
import textRank
##########生成词云所用的库##########
import matplotlib.pyplot as plt
import PIL.Image as Image
import jieba
import numpy as np
import os
from wordcloud import WordCloud,ImageColorGenerator
##################################

with open('statics/1.txt','r',encoding='utf-8') as f:
    data=[i for i in f.readlines()]
    text=''.join(data)
# print(text)

Tdata=[]  #存放正方文本
Fdata=[]  #存放反方文本
title=data[0]  # 辩题

for i in data:
    if i.startswith('正方'):
        Tdata.append(i.split('：')[1])
    elif i.startswith('反方'):
        Fdata.append(i.split('：')[1])
    else:
        pass
# print(Tdata)
# print(Fdata)
# print(title)



def get_words_and_sentences(text):
    """

    :param text: 传入列表  可以传入Tata 和 Fdata
    :return:
    """
    # 正方选手
    T = textRank.TextRank(''.join(text), pr_config={'alpha': 0.85, 'max_iter': 100})
    # 提取正方选手前80个关键词，用于生成词云
    Tres = T.get_n_keywords(80)
    # for i in Tres:
    #     print(i)
    # 提取正方选手    3个句子
    Tres2 = T.get_n_sentences(3)
    # for i in Tres2:
    #     print(i)
    return Tres,Tres2



def cloud_pic(TList,T=True):
    """
    :param TList: 传入列表
    T 参数用于选择图片，其中默认为True
    :return:
    """
    raw_signature_string = ''.join(TList)
    text = jieba.cut(raw_signature_string, cut_all=True)
    wl_space_split = ' '.join(text)

    if T:
        alice_coloring = np.array(Image.open('./1.jpg'))  # 原图
    else:
        alice_coloring = np.array(Image.open('./2.jpg'))  # 原图

    my_wordcloud = WordCloud(background_color="white",  # 背景色
                             max_words=200,  # 字数上限
                             mask=alice_coloring,  # 形状
                             max_font_size=150,  # 字体大小
                             random_state=50,  # 随机数量
                             font_path='C:/Windows/Fonts/simhei.ttf').generate(wl_space_split)  # 中文字体
    image_color = ImageColorGenerator(alice_coloring)

    return my_wordcloud.recolor(color_func=image_color),my_wordcloud




#####绘制词云图
# cloud_pic(''.join([i[0] for i in res]))




def draw_cloud_pic(title,T,F):
    """
    重新更改后的cloud_pic
    title: 辩题
    T: 正方 关键词
    F： 反方 关键词
    :return:
    """
    Tcloud,Tword=cloud_pic(TList=T,T=True)
    Fcloud,Fword=cloud_pic(TList=F,T=False)
    plt.rcParams['figure.figsize'] = (18, 10)  # 画布大小
    # 防止中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 父标题
    plt.suptitle(title, fontsize=30, color='g', fontweight='bold')

    # 正方词云
    plt.subplot(1, 2, 1)  # 1行2列 1号位置
    plt.title('正方选手', fontsize=20, color='red')  # 标题设置
    plt.imshow(Tcloud)
    plt.imshow(Tword)
    plt.axis("off")


    # 反方词云
    plt.subplot(1, 2, 2)  # 1行2列 1号位置
    plt.title('反方选手', fontsize=20,color='blue')  # 标题设置
    plt.imshow(Fcloud)
    plt.imshow(Fword)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    #  正方
    Twords,Tsentences=get_words_and_sentences(text=Tdata)
    print("获取正方选手的关键词(前80个)")
    print(Twords)
    print("获取正方选手的关键句子（前3个）")
    for i in Tsentences:
        print(i)
    # 反方
    Fwords, Fsentences = get_words_and_sentences(text=Fdata)
    print("获取正方选手的关键词(前80个)")
    print(Fwords)
    print("获取正方选手的关键句子（前3个）")
    for i in Fsentences:
        print(i)

    # 绘制词云图
    cloudT=''.join([i[0] for i in Twords])
    cloudF = ''.join([i[0] for i in Fwords])
    draw_cloud_pic(title, T=cloudT, F=cloudF)