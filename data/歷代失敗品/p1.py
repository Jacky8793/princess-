import requests
import bs4
import pandas as pd
import time
import os
import random
import wget

'''連上網頁'''
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# res = requests.get("https://gamewith.tw/pricone-re/article/show/87390",headers=headers)
# content = res.content.decode()
url = "https://gamewith.tw/pricone-re/article/show/87390"
tsmchtml = requests.get(url)
objSoup = bs4.BeautifulSoup(tsmchtml.text, 'html.parser')

'''開始'''
print("連接完成.....")

'''資料'''
table = objSoup.select(".sorttable")
df =  {"頭像":[],"角色名稱":[],"★數":[],"站位":[],"定位":[],"評價分數":[],"連結":[]}

'''輸入資料'''
print("資料輸入中.....")

print(table)

for tb in table:
    all_tr = tb.find_all('tr')
    for i,tr in enumerate(all_tr):
        head = tr.get("data-col1")
        star = tr.get("data-col2")
        postion = tr.get("data-col3")
        Attributes = tr.get("data-col4")
        score = tr.get("data-col5")
        '''頭像、角色名稱、連結'''
        if head is not None:
            df["角色名稱"].append(head)
            td = (tr.find("td")).find("a")
            href = td.get("href")
            df["連結"].append(href)
            pic = td.find("img")
            href_src = pic.get("src")
            src = 'src'
            wait = random.randint(1,10)
            print("圖片下載中....")
            time.sleep(wait)
            if not os.path.isdir(src):
                os.mkdir(src)
            
            filename = os.path.join("./src",head + '.png')
            if not os.path.isfile(filename):
                wget.download(href_src,filename)
            df["頭像"].append(href_src)

        '''★數'''
        if star is not None:
            df["★數"].append(star)
        '''站位'''
        if postion is not None:
            df["站位"].append(postion)
        '''定位'''
        if Attributes is not None:
            df["定位"].append(Attributes)
        '''評價分數'''
        if score is not None:
            df["評價分數"].append(score)

df = pd.DataFrame(df)
df.to_excel("pricone-re.xlsx", index=False)

'''建表完成'''
print("資料表建立完成")