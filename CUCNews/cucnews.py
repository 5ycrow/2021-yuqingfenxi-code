import requests
from bs4 import BeautifulSoup as bs
import pymysql

def savenews(title,url,picurl,content):
    # pymysql.connect(数据库url,用户名,密码,数据库名 )
    db = pymysql.connect("localhost", "root", "root", "newsanalysis", charset = 'utf8')
    cursor = db.cursor()
    try:
        # print("db-ok")
        cursor.execute("INSERT INTO cucnews(title,url,picurl,content) VALUES(%s,%s,%s,%s)", (title,url,picurl,content))
        db.commit()
    except:
        db.rollback()
    db.close()

for num in range(1,50):
    print(num)
    url = 'http://www.cuc.edu.cn/news/1901/list'+(str(num))+'.htm'
    r=requests.get(url)
    rt=r.content
    rh=str(rt,"utf-8")
    # print(rh)
    soup=bs(rh,"html.parser")
    titles=soup.find_all("h3",attrs={'class','tit'})
    picurls = soup.find_all('div', class_='desc g-line')
    for (p,t) in zip(picurls,titles):
        try:
            picurl='http://www.cuc.edu.cn'+p.select('div img')[0].get('src')
        except:
            picurl="该新闻无图片"

        newsurl=t.find_all('a')
        urllen=str(newsurl[0]).find("target")

        url='http://www.cuc.edu.cn'+(str(newsurl[0])[9:urllen-2])
        r = requests.get(url)
        rt = r.content
        rh = str(rt, "utf-8")
        soup = bs(rh, "html.parser")
        contents = soup.find_all("div",attrs={'class','wp_articlecontent'})
        for c in contents:
            content = c.get_text()
        title=t.get_text()
        savenews(title,url,picurl,content)