from time import localtime,strftime

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def cut(words):

    jieba.load_userdict("static/AIDict.txt")
    seg_list=jieba.cut(words,cut_all=False)
    #print(list(seg_list))

    tf={}
    for seg in seg_list:
        if seg in tf:
            tf[seg]+=1
        else:
            tf[seg]=1
    #print(len(tf))

    ci=list(tf.keys())
    with open('static/stopword.txt','r',encoding='utf-8') as ft:
        stopword=ft.read()

    for seg in ci:
        if tf[seg]<10 or len(seg)<2 or seg in stopword or '一' in seg:
            tf.pop(seg)

    #print(len(tf))

    ci=list(tf.keys())
    num=list(tf.values())
    data=[]

    for i in range(len(tf)):
        data.append((num[i],ci[i]))

    data.sort()
    data.reverse()
    #print(data)
    return data


def wordc(data):
    #print(data)
    wcdata={}
    for d in data:
        wcdata[d[1]]=d[0]
    #print(wcdata)
    font=r'c:\Windows\Fonts\simfang.ttf'
    wc=WordCloud(font_path=font,background_color='white').generate_from_frequencies(wcdata)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    picname='D:/SSSSTUDY/2020第二学期/舆情分析/code/frontend/cucnews_frontend/static/news.jpg'
    wc.to_file(picname)
    return picname
