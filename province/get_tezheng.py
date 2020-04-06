#-*- coding: utf-8 -*-
import numpy as np
import  json
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import IncrementalPCA
import seaborn as sns
# 支持中文

import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['STHeiti\ Medium']
# mpl.rcParams['font.serif'] = ['STHeiti\ Medium']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串


province = []
# province=['河北','山西','内蒙古','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']



def scatter(x, colors):
    palette = np.array(sns.color_palette("hls", 40))
 
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
                    c=palette[colors.astype(np.int)])
    # sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
    #                 c=colors)
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')



fp = open("all_city_ans_str", "r")
source_lines = ""
try:
    source_lines = fp.read()
finally:
    fp.close()
train_date = json.loads(source_lines)


fp = open("province_list.log", "r")
source_lines = ""
try:
    source_lines = fp.read()
finally:
    fp.close()
city_name = json.loads(source_lines)


fp = open("all_cutword_array_str", "r")
source_lines = ""
try:
    source_lines = fp.read()
finally:
    fp.close()
cut_word = json.loads(source_lines)









from sklearn.feature_selection import SelectKBest,f_classif

X = np.array(train_date)
y=[
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0
]


# print('before transform:\n',X)
selector=SelectKBest(score_func=f_classif,k=60)
selector.fit(X,y)
# print('scores_:\n',selector.scores_)
# print('pvalues_:',selector.pvalues_)
print('selected index:',selector.get_support(True))
# print('after transform:\n',selector.transform(X))







for  i  in  selector.get_support(True):
    if  train_date[17][i] == 0 or  train_date[24][i]==0:
        continue
    print (cut_word[i] + "\t" + str(train_date[17][i]) + "\t" + str(train_date[24][i])  )



for  i  in  selector.get_support(True):
    if  train_date[17][i] == 0 or  train_date[24][i]==0:
        continue
    tmp_ans = ""
    for j in range(0,len(train_date)):
        if j==17 or  j==24:
            tmp_ans += "__"+str(train_date[j][i])+"__" + "  "
        else:
            tmp_ans += str(train_date[j][i]) + "  "
    print (str(i)+"\t"+cut_word[i] + tmp_ans  )

print ("\n\n\n"+ str(len(train_date[0])) )







