import requests
from bs4 import BeautifulSoup as bs
import pymysql


def saveTopic(topicname, imgUrl, content, contentUrl, hotValue):
    # pymysql.connect(数据库url,用户名,密码,数据库名 )
    db = pymysql.connect(host="localhost", user="root", password="root", database="newsanalysis", charset='utf8')
    cursor = db.cursor()
    try:
        # print("db-ok")
        cursor.execute("INSERT INTO zhihu(topic,imgUrl,content,contentUrl,hotValue) VALUES(%s,%s,%s,%s,%s)",
                       (topicname, imgUrl, content, contentUrl, hotValue))
        db.commit()
    except:
        db.rollback()
    db.close()


url = "https://www.zhihu.com/hot"
hd = {
    'cookie': '_zap=22e60910-78b8-48bf-99d3-6413362c9ec8; d_c0="AHCRBF8uXRGPTpC2sx0tYWK5wz3-8HqH_Dg=|1591091056"; _ga=GA1.2.1184934007.1591091057; z_c0="2|1:0|10:1609578203|4:z_c0|92:Mi4xSnd0VkF3QUFBQUFBY0pFRVh5NWRFU1lBQUFCZ0FsVk4yNFRkWUFCQjRab0hTRlgxTFc3MUI0V0duM3ZLSXBCWm9B|735f3b05037078581f56544bbb468e985e3923c85e253a226e6d3fb0000a1c1f"; tst=r; _xsrf=Y1yKFsYiSUApCgt3q0TTAoS8D7N7pWnD; q_c1=6d36759238504a44a5c50e5c5b9c1560|1615279714000|1594365608000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1616935636,1617003275,1617084024,1617084039; KLBRSID=e42bab774ac0012482937540873c03cf|1617675493|1617675491',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
r = requests.get(url, headers=hd)
rh = str(r.content, "utf-8")
soup = bs(rh, "html.parser")
topic_list = soup.find_all('section', class_="HotItem")
for each in topic_list:
    topic = each.find('h2', class_="HotItem-title").text
    if each.find('p', class_="HotItem-excerpt"):
        questionContent = each.find('p', class_="HotItem-excerpt").get_text()
    else:
        questionContent = 'None'
    if each.find('a', class_="HotItem-img"):
        img_url = each.find('a', class_="HotItem-img").select('img')[0].get('src')
    else:
        img_url = "None"
    content_url = each.find('div', class_='HotItem-content').select('a')[0]['href']
    hot_value = each.find('div', class_="HotItem-metrics").get_text()
    print(topic)
    print(questionContent)
    print(img_url)
    print(content_url)
    print(hot_value)
    saveTopic(topic, img_url, questionContent, content_url, hot_value)
# print(topic_list)