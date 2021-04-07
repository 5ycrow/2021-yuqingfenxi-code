import pymysql
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def search():
    db = pymysql.connect("localhost", "root", "root", "newsanalysis", charset = 'utf8')
    cursor = db.cursor()
    try:
        # print("db-ok")
        cursor.execute("SELECT content FROM cucnews")
        res = cursor.fetchall()
        with open('cucnewscontent.txt','w+',encoding='utf-8') as f:
                f.writelines(str(res)+'\n')
    except:
        db.rollback()
    db.close()

search()
with open('cucnewscontent.txt', 'r', encoding='utf-8') as f:
    gov = f.read()
jieba.load_userdict("AIDict.txt")
seg_list = jieba.cut(gov, cut_all=False)
#print(list(seg_list))

tf = {}
for seg in seg_list:
    if seg in tf:
        tf[seg] += 1
    else:
        tf[seg] = 1
print(len(tf))

ci = list(tf.keys())
# print(ci)
with open('stopword.txt', 'r',encoding='utf-8') as ft:
    stopword = ft.read()

for seg in ci:
    if tf[seg] < 10 or len(seg) < 2 or seg in stopword or '一' in seg:
        tf.pop(seg)

print(len(tf))
ci = list(tf.keys())
num = list(tf.values())
data = []

for i in range(len(tf)):
    data.append((num[i], ci[i]))

data.sort()
data.reverse()
# print(data)
f = open("cucnewsresult.txt", "w+",encoding='utf-8')
for i in range(len(data)):
    f.write(data[i][1] + "," + str(data[i][0]) + "\r\n")
f.close()

sortdata = {}
for d in data:
    sortdata[d[1]] = d[0]
print(sortdata)

mask=np.array(Image.open('monkey.png'))

text=open('145.txt','r',encoding='utf-8').read()
font=r'c:\Windows\Fonts\simfang.ttf'
#print(data)
wc=WordCloud(width=800, height=600,font_path=font,background_color='white',mask=mask).generate_from_frequencies(sortdata)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('Jiebacucnews.jpg')

