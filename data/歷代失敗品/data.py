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

'''資料欄位'''
df =  {"頭像":[],"角色名稱":[],"★數":[],"站位":[],"定位":[],"評價分數":[],"連結":[]}

'''輸入資料'''
print("資料輸入中.....")
table = objSoup.select(".sorttable")

for tb in table:
    all_tr = tb.find_all("tr")
    for tr in all_tr:
        '''抓取資料:頭像、角色名稱、★數、站位、定位、評價分數、連結'''

        '''確認是否重複(頭像)'''
        head_count = 0

        '''抓取角色名稱'''
        all_td = tr.find("td")
        if all_td != None:
            for td in all_td:
                if td.text != 'NEW！':
                    df["角色名稱"].append(td.text)

        '''抓取★數'''
        star = tr.get("data-col2")
        if star != None:
            df["★數"].append(star)

        '''抓取站位'''
        postion = tr.get("data-col3")
        if postion != None:
            df["站位"].append(postion)

        '''抓取定位'''
        Attributes = tr.get("data-col4")
        if Attributes != None:
            df["定位"].append(Attributes)

        '''抓取評價分數'''
        score = tr.get("data-col5")
        if score != None:
            df["評價分數"].append(score)

        '''抓取頭像、連結'''
        all_character = tr.find_all("td")
        for character in all_character:
            all_a = character.find_all("a")
            for a in all_a:
                '''抓取連結'''
                href = a.get("href")
                df["連結"].append(href)

                '''抓取頭像'''
                if (a.find("img").get("data-original") != None and head_count < 1):
                    head_count += 1
                    img = a.find("img").get("data-original")
                else:
                    head_count = 0
                    img = a.find("img").get("src")
                df["頭像"].append(img)
                
            

'''建立資料表'''
print("正在建立資料表.....")
df = pd.DataFrame(df)
df.to_excel("character.xlsx", index=False)
print("建立完成!!")