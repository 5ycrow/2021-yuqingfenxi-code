from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from Jieba145.jieba145 import sortdata

mask=np.array(Image.open('monkey.png'))

text=open('145.txt','r',encoding='utf-8').read()
font=r'c:\Windows\Fonts\simfang.ttf'
#print(data)
wc=WordCloud(width=800, height=600,font_path=font,background_color='white',mask=mask).generate_from_frequencies(sortdata)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('Jieba145.jpg')