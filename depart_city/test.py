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


province=['河北','山西','内蒙古','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']



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


fp = open("city_real_name", "r")
source_lines = ""
try:
    source_lines = fp.read()
finally:
    fp.close()
city_name = json.loads(source_lines)



# train_date = []
# load_data()
# print (train_date)

# X = np.array([[-1, -1,2], [-2, -1,3], [-3, -2,4], [1, 1,5], [2, 1,6], [3, 2,7]])

X = np.array(train_date)
# ipca = IncrementalPCA(n_components=1, batch_size=300)
# kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(X)
kmeans_model =   KMeans(n_clusters=50, max_iter=3000, random_state=9).fit(X)
labels = kmeans_model.labels_



 # 数组输出
zu = {}
tmp_count = 0
for  i  in  labels:
    if str(i) not in zu:
        zu[str(i)] = []
    if city_name[tmp_count]  in  province:
        tmp_count +=1
        continue
    zu[str(i)].append(city_name[tmp_count])
    tmp_count +=1



show_str =  json.dumps( zu )
print (show_str)
# for  i in range(0,40):
#     i = str(i)
#     print (i+"\n",end=' ')
#     for j in zu[i]:
#         print ("\t"+j+"\t",end=' ')
#     print ("\n",end=' ')





# digits_proj = TSNE().fit_transform(X)    #将X降到2维
# scatter(digits_proj, labels)
# tmp_count = 0
# for a,b in digits_proj:
#     plt.text(a,b+0.1,city_name[tmp_count]+"_"+str(labels[tmp_count]),ha = 'center',va = 'bottom',fontsize=7)
#     tmp_count+=1
# plt.show()


