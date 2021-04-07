import jieba

with open('145.txt', 'r', encoding='utf-8') as f:
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
f = open("result.txt", "w",encoding='utf-8')
for i in range(len(data)):
    f.write(data[i][1] + "," + str(data[i][0]) + "\r\n")
f.close()

sortdata = {}
for d in data:
    sortdata[d[1]] = d[0]
print(sortdata)