#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Liu Mingchun
# @date：2018/10/06

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import stats

from matplotlib.ticker import MaxNLocator

import seaborn as sns
import re
import numpy as np
from wordcloud import WordCloud


#，第四题，计算斯皮尔曼相关系数
def corr():
#测试数据
    src1 = '/Users/liumingchun/【1】科研+实验室/4-科研项目/RateMyProfessor/rate_my_professors/rate_my_professor_40.csv'
    src = '/Users/liumingchun/PycharmProjects/pythonbook/RateMyProfessor/RMP.csv'

    df = pd.read_csv(src)
    df = df[(df['star_rating'] >= 1.0 ) & (df['diff_index'] >= 1.0)]
    # df = df.sample(1000) #随机选取数据
    star_rating = df['star_rating']
    diff_index  = df['diff_index']
    print('diff_index 数据条目:',diff_index.count())
    print('star_rating数据条目:',star_rating.count())

    p = stats.pearsonr(star_rating, diff_index)
    print('diff_index与star_rating的相关系数是：%.4f, p值是：%s' % p)

    data = df[['diff_index', 'star_rating']]
    data = data.rename(index=str,columns={'diff_index':'difficulty index','star_rating':'star rating'})

    # 计算回归方程
    regression = stats.linregress(diff_index, star_rating)
    print("R square", regression[2] ** 2)
    R_square = regression[2] ** 2
    print('线性回归方程是 Y= %.3fX + %.3f,rvalue是%.3f,pvalus是%s,标准误是%s' % regression)

    g = sns.set("paper",font_scale =1.3)
    g = sns.set_style("white")

    # g = sns.jointplot('difficulty index','star rating', data=data,height=6,ratio=7, kind="kde", xlim=(1,5), ylim=(1.0, 5.0),space=0.1,color='b')
    g = sns.jointplot('difficulty index','star rating', data=data,height=6,ratio=7, kind="kde", xlim=(1,5), ylim=(1.0, 5.0),space=0.1,
                      color='b',cbar_kws=dict(use_gridspec=False,location="right", anchor=(1.5, 0),shrink=0.9,ticks=None,),cbar=True,)

    # pl = sns.regplot(data['difficulty index'], data['star rating'], scatter=False, ax=g.ax_joint)
    # pl.text(1.1,1.8, "Y=-0.55X+5.25", horizontalalignment='left', size='small', color='black', weight='semibold')
    # pl.text(1.1,1.6, r'$R^2$=0.25', horizontalalignment='left', size='small', color='black', weight='semibold')

    #展示回归线及R方
    plt.text(-3.5,1.5, r"Y=-0.55X+5.25",fontsize=12)
    plt.text(-3.5,1.2, r'$R^2$=0.25',fontsize=12)

    # ax = plt.subplot()
    # im = ax.imshow(data.values)
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    # plt.colorbar(im, cax=cax)


# plt.text(60, .025, r'$\mu=100,\ \sigma=15$') 平均数和方差

#2、将老师分为demand组 和easy组
    # list = df['diff_index'].tolist()
    # tag_list = []
    # for i in list:
    #     if 0.9 < i < 3:
    #         tag_list.append('easy-going')
    #     elif 3 < i < 5.1:
    #         tag_list.append('demand')
    #
    # df['professor'] = pd.DataFrame(tag_list)
    # # print(df['professor'])
    # #小提琴图
    # data = df[['professor','star_rating']][:1000]
    # g = sns.violinplot('professor',"star_rating",data=data,scale='count')

    # #3、纺锤图
    # data = df[['diff_index','star_rating']][:1000]
    # # # print(data)
    # rank = ['1.0','2.0','3.0','4.0','5.0']
    # g = sns.scatterplot('diff_index','star_rating',data=data,hue='diff_index',hue_order=rank)
    plt.pause(0)  #防止图闪退

#第5题，比较评论单词字数和长度
def len_comment():
    print('评论长度比较～～～～～～～～～～')

    src1 = '/Users/liumingchun/【1】科研+实验室/4-科研项目/RateMyProfessor/rate_my_professors/rate_my_professor_40.csv'
    src = '/Users/liumingchun/PycharmProjects/pythonbook/RateMyProfessor/RMP.csv'

    df = pd.read_csv(src)
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()

    # 按照1-2星及4-5星分为2组，然后进行比较两者差异，独立样本T检验，方差齐性检验
    df2 = df[(df['star_rating'] <= 2) & (df['star_rating'] >= 1)]  # 低分组
    df3 = df[(df['star_rating'] >= 4) & (df['star_rating'] <= 5)]  # 高分组

    low_len_comment = df2['len_comment']
    high_len_comment= df3['len_comment']

    #方差齐性检验，看是否满足检验要求
    leven_test = stats.levene(high_len_comment,low_len_comment,center='median')
    print('len_comment的方差齐性检验是：%s, p值是：%s' % leven_test)

    low_mean = df2['len_comment'].mean() #平均数
    low_std = df2['len_comment'].std()   #标准差
    low_size = df2['len_comment'].count()#数量

    high_mean = df3['len_comment'].mean() #平均数
    high_std = df3['len_comment'].std()   #标准差
    high_size = df3['len_comment'].count()#数量

    low_rvs  =stats.norm.rvs(loc=low_mean,scale= low_std,size = low_size)
    high_rvs = stats.norm.rvs(loc=high_mean,scale=high_std,size =high_size)

    p = stats.ttest_ind(high_rvs,low_rvs,equal_var=True)
    print('高分组的len_comment平均数是%f，标准差是%f,样本量是%s' % (high_mean,high_std,high_size))
    print('低分组的len_comment平均数是%f，标准差是%f,样本量是%s' % (low_mean,low_std,low_size))
    print('len两组的T检验是：%s，p值是：%s' % p)



    # 评价词云
    list = df3['professor_all_comments'].dropna().tolist()
    text = ' '.join(str(x) for x in list).strip()
    text = text.lower()
    print(text)

    wc = WordCloud(
        background_color='white',  # 设置背景颜色
        max_font_size=150,  # 设置字体最大值
        random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.generate_from_text(text)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    plt.pause(0)

def word_comment():
    print('评论单词个数比较～～～～～～～～～～')

    df = pd.read_csv('/Users/liumingchun/PycharmProjects/pythonbook/RateMyProfessor/RMP.csv')
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    # 按照1-2星及4-5星分为2组，然后进行比较两者差异，独立样本T检验，方差齐性检验
    df2 = df[(df['star_rating'] <= 2) & (df['star_rating'] >= 1)]  # 低分组
    df3 = df[(df['star_rating'] >= 4) & (df['star_rating'] <= 5)]  # 高分组

    #计算单词个数
    low_words_comment  = df2['words_comment']
    high_words_comment = df3['words_comment']

    #方差齐性检验
    leven_words_test = stats.levene(high_words_comment,low_words_comment,center='median')
    print('words的方差齐性检验%s, p值是：%s' % leven_words_test)

    low_words_mean = df2['words_comment'].mean() #平均数
    low_words_std = df2['words_comment'].std()   #标准差
    low_words_size = df2['words_comment'].count()#样本

    high_words_mean = df3['words_comment'].mean() #平均数
    high_words_std = df3['words_comment'].std()   #标准差
    high_words_size = df3['words_comment'].count()#数量

    low_words_rvs =stats.norm.rvs(loc=low_words_mean,scale= low_words_std,size = low_words_size)
    high_words_rvs = stats.norm.rvs(loc=high_words_mean,scale=high_words_std,size =high_words_size)
    p_words = stats.ttest_ind(high_words_rvs,low_words_rvs,equal_var=True)

    print('高分组的words_comment 平均数是%f，标准差是%f,样本数%s' % (high_words_mean,high_words_std,high_words_size))
    print('低分组的words_comment 平均数是%f，标准差是%f,样本数%s' % (low_words_mean,low_words_std,low_words_size))
    print('words_comment两组T检验是%s,p值是%s ' % p_words)


#第一题 ，tag分析
def tag():
    src = "/Users/liumingchun/PycharmProjects/pythonbook/RateMyProfessor/RMP.csv"

    df = pd.read_csv(src)

    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    df2 = df[(df['star_rating'] >= 4 ) & (df['star_rating'] <= 5)]  # 高分组4-5
    df3 = df[(df['star_rating'] <= 2 ) & (df['star_rating'] >= 1)]  # 低分组1-2

    #去除统计数字及重新计算tag的频率及次数
    print('高分组评论～～～～～～～～～～～')
    high_rate_list = df2['tag_professor'].dropna().tolist()
    new_high_list=[]
    for i in high_rate_list:
        pattern = re.split('\(\d+\)',i)
        for j in pattern:
            new_high_list.append(j.strip())
    # print(new_list)
    df4 = pd.DataFrame(new_high_list, columns=['tag'])
    print(df4['tag'].value_counts(ascending=False,normalize=True))
    print('高分教授个数',df4['tag'].count())

    print('低分组评论～～～～～～～～～～～')
    low_rate_list = df3['tag_professor'].dropna().tolist()
    new_low_list=[]
    for i in low_rate_list:
        pattern = re.split('\(\d+\)',i)
        for j in pattern:
            new_low_list.append(j.strip())
    # print(new_list)
    df5 = pd.DataFrame(new_low_list, columns=['tag'])
    print(df5['tag'].value_counts(ascending=False,normalize=True))
    print('低分教授个数',df5['tag'].count())

    df6 = pd.DataFrame(columns=['High rate professors','Low rate professors'])
    df6['High rate professors'] = df4['tag'].value_counts()
    df6['Low rate professors'] =  df5['tag'].value_counts()

    print(df6)
    leven_words_test = stats.levene(df6['High rate professors'], df6['Low rate professors'],center='median')
    print('tag方差齐性检验%s, p值是：%s' % leven_words_test)

    p = stats.chisquare(df6,axis=1)
    print('卡方值："%s,"，p值：%s' % p,end='')

    df4['tag'].to_csv('high_tag.csv')
    df5['tag'].to_csv('low_tag.csv')


def wordcloud():
    # tag词云
    df = pd.read_csv('high_tag.csv')

    list = df['tag'].dropna().tolist()
    # print(list)

    text = ' '.join(str(x) for x in list).strip()
    text = text.lower()

    tag = re.sub('[^a-zA-Z]', ' ', text)

    print(tag)
    newlist = tag.split(' ')
    print(newlist)
    newtext = ' '.join(newlist)


    wc = WordCloud(
        background_color='white',  # 设置背景颜色
        max_font_size=200,  # 设置字体最大值
        random_state=40, # 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.generate_from_text(newtext)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    plt.pause(0)

def main():
    # corr()
    # len_comment()
    # word_comment()
    # tag()
    wordcloud()

if __name__ == '__main__':
    main()