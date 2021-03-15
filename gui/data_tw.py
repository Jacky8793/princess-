import requests
import bs4
import pandas as pd
import time
import wget
import os
from PIL import Image
import glob

def tw():
        '''連上網頁'''
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        # res = requests.get('https://gamewith.tw/pricone-re/article/show/87390',headers=headers)
        # content = res.content.decode()
        url = 'https://gamewith.tw/pricone-re/article/show/87390'
        tsmchtml = requests.get(url)
        objSoup = bs4.BeautifulSoup(tsmchtml.text, 'html.parser')

        '''開始'''
        print('連接完成.....')

        '''建立字典'''
        df = {}
        '''輸入資料'''
        print('資料輸入中.....')
        table = objSoup.select('.sorttable')
        re = False

        for tb in table:
        all_tr = tb.find_all('tr')
        for tr in all_tr:
                '''角色名稱'''
                name = tr.get('data-col1')
                '''角色站位'''
                sop = tr.get('data-col3')

                if (name != None and 'NEW！' in name):
                name = name.replace('NEW！','')
                if name == '綾音(聖誕節)':
                        if re == True:
                                continue
                        re = True
                
                '''角色介紹連結和圖片'''
                td = tr.find('td')
                if td != None:
                        info = td.find('a').get('href')
                        head =  td.find('a').find('img')
                        if head.get('data-original') != None:
                                head = head.get('data-original')
                        else:
                                head = head.get('src')

                        '''角色介紹'''
                        print('目前正抓取 {} 的角色資料....'.format(name))
                        df[name] = []

                        '''角色站位'''
                        df[name].append(sop)

                        '''角色頭貼下載'''
                        filename = name + '.png'
                        if os.path.isdir('./head/png'):
                                filepath = os.path.join('./head/png',filename)
                        if not os.path.isfile(filepath):
                                wget.download(head,filepath)
                                '''轉檔'''
                                frames = []
                                imgs = glob.glob(os.path.join('./head/png',(name + '.png')))
                                for i in imgs:
                                        new_frame = Image.open(i)
                                        frames.append(new_frame)
                                
                                frames[0].save(os.path.join('./head/gif',(name + '.gif')), format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)

                        tsmchtml_ = requests.get(info)
                        objSoup_ = bs4.BeautifulSoup(tsmchtml_.text, 'html.parser')

                        '''角色立繪下載'''
                        src = objSoup_.find('div',class_='pcr_img_charatop').find('img').get('src')
                        filename = name + '.png'
                        if os.path.isdir('./people/png'):
                                filepath = os.path.join('./people/png',filename)
                        if not os.path.isfile(filepath):
                                wget.download(src,filepath)
                                '''轉檔'''
                                frames = []
                                imgs = glob.glob(os.path.join('./people/png',(name + '.png')))
                                for i in imgs:
                                        new_frame = Image.open(i)
                                        frames.append(new_frame)
                                
                                frames[0].save(os.path.join('./people/gif',(name + '.gif')), format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)

                        '''角色台詞'''
                        tips = objSoup_.find('div',class_="puri_tips").find('p').text
                        df[name].append(tips)

                        '''抓取角色評分、定位、關卡適合度、評價'''
                        table = objSoup_.find('div',class_='puri_hyouka_table').find_all('td')

                        for text in table:
                                if text.find('img') != None:
                                        '''定位圖示'''
                                        df[name].append(text.find('img').get('src'))
                                df[name].append(text.text.replace(' ',''))
                        time.sleep(1)


        '''建立資料表'''
        print('正在建立資料表.....')
        df = pd.DataFrame(df)
        df.to_csv('character.csv', index=False)
        print('建立完成!!')