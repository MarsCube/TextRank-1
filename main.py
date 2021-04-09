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

with open('statics/1.txt') as f:
    # text=f.read()
    text=''.join([i.strip() for i in f.readlines()])
print(text)

T = textRank.TextRank(text,pr_config={'alpha': 0.85, 'max_iter': 100})

# 提取前10个关键词
res=T.get_n_keywords(50)
for i in res:
    print(i)

# 提取3个句子
res2=T.get_n_sentences(3)
for i in res2:
    print(i)


def cloud_pic(TList):
    """
    :param TList: 传入列表
    :return:
    """
    raw_signature_string = ''.join(TList)
    text = jieba.cut(raw_signature_string, cut_all=True)
    wl_space_split = ' '.join(text)

    alice_coloring = np.array(Image.open('./2.jpg'))  # 原图

    my_wordcloud = WordCloud(# background_color="white",  # 背景色
                             max_words=200,  # 字数上限
                             mask=alice_coloring,  # 形状
                             max_font_size=150,  # 字体大小
                             random_state=50,  # 随机数量
                             font_path='C:/Windows/Fonts/simhei.ttf').generate(wl_space_split)  # 中文字体
    image_color = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_color))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()


#####绘制词云图
cloud_pic(''.join([i[0] for i in res]))