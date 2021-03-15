from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import csv
import data

class character(object):
    '''前衛、中衛、後衛選單介面'''
    def __init__(self,master=None,pos=None,Language='JP'):
        self.root = master
        self.pos = pos
        self.Language = Language
        # 鎖定頁面
        self.root.resizable(False,False)
        # icon設定
        self.root.iconbitmap('mainpage/app_icon.ico')
        # 螢幕寬度
        screenWidth = self.root.winfo_screenwidth()
        # 螢幕高度
        screenHeight = self.root.winfo_screenheight()
        # 視窗寬
        w = 1200
        # 視窗高
        h = 680
        # 視窗左上角x軸位置
        x = int((screenWidth - w) / 2)
        # 視窗左上角Y軸位置
        y = int((screenHeight - h ) / 4)
        self.root.geometry('%dx%d+%d+%d' % (w,h,x,y))

        # '''建立工具列'''
        # self.menubar = Menu(self.root)
        # self.filemenu = Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label='爬蟲', menu=self.filemenu)
        # self.filemenu.add_command(label='台版', command=data.tw)
        # self.filemenu.add_command(label='日版', command=data.jp)

        # self.Language = Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label='本版', menu=self.Language)
        # self.Language.add_command(label='台版', command=lambda:self.Language_cheak('TW'))
        # self.Language.add_command(label='日版', command=lambda:self.Language_cheak('JP'))

        # self.root.config(menu=self.menubar)

        self.character_dict()
        self.createPage()
        self.root.mainloop()

    def Language_cheak(self,Lang):
        self.Language = Lang
        self.character_dict()
        # 語言判斷
        if self.Language == 'TW':
            self.scr_len = 700
        else:
            self.scr_len = 1200
        '''判斷跳轉頁面'''
        if self.pos == 'front':
            self.frontPage()
        elif self.pos == 'middle':
            self.middlePage()
        elif self.pos == 'last':
            self.lastPage()
    
    def character_dict(self):
        '''角色字典'''
        columns = []
        if self.Language == 'TW':
            path = './character.csv' 
        else:
            path = './character_jp.csv' 
        with open(path,'r',encoding='utf-8') as f: 
            reader = csv.reader(f)
            for row in reader:
                if columns:
                    for i, value in enumerate(row):
                        columns[i].append(value)
                else:
                    columns = [[value] for value in row]
        '''建立字典 角色名字:[站位、台詞、評分、類型圖示、類型、定位、優缺點]'''
        self.dat = {c[0] : c[1:] for c in columns}

    def createPage(self):
        # 語言判斷
        if self.Language == 'TW':
            self.scr_len = 700
        else:
            self.scr_len = 1200
        '''設定頁面模板'''
        self.page = Frame(self.root)
        self.page.pack()
        '''背景圖片'''
        self.yellowstone = ImageTk.PhotoImage(file='secondpage/sec.gif')
        Label(self.page,image=self.yellowstone).pack()
        '''字型'''
        self.main_button_font= tkFont.Font(size=20, weight='bold') 
        self.main_button＿pic = PhotoImage(file='secondpage/sec_button.gif')
        '''選單按鈕'''
        Button(self.page,text='前衛',image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.frontPage).place(x=225,y=20,width=150,height=50)
        Button(self.page,text='中衛',image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.middlePage).place(x=525,y=20,width=150,height=50)
        Button(self.page,text='後衛',image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.lastPage).place(x=825,y=20,width=150,height=50)
        '''視窗'''
        self.canvas=Canvas(self.page,width=898,height=490,scrollregion=(0,0,1000,self.scr_len),bd=0,bg='#f9ca7c')
        self.canvas.place(x=150,y=100)
        self.canvas_frame=Frame(self.canvas)
        self.canvas_frame.place(width=898,height=490)
        self.vbar=Scrollbar(self.canvas,orient=VERTICAL)
        self.vbar.place(x = 880,width=20,height=490)
        self.vbar.configure(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set)
        self.canvas.create_window((1000,1000), window=self.canvas_frame)
        '''判斷跳轉頁面'''
        if self.pos == 'front':
            self.frontPage()
        elif self.pos == 'middle':
            self.middlePage()
        elif self.pos == 'last':
            self.lastPage()

    def frontPage(self):
        '''前衛介面選單'''
        self.canvas.delete("all")
        self.pos = 'front'
        self.temp = []
        name = []
        # 匯入角色字典
        for dat in self.dat.keys():
            if self.dat[dat][0] == '前衛':
                name.append(dat)
        # 語言判斷
        if self.Language == 'TW':
            path = './head/gif/'
        else:
            path = './head/gif_jp/'
        # 列座標
        y = 80
        # 陣列數
        count = 0
        # 列總數
        row = len(name) % 6 
        row = 1 + int(len(name) / 6) if row != 0 else int(len(name) / 6)
        for col in range(row):
            for row in range(6):
                '''設置按鈕座標位置'''
                self.temp.append(PhotoImage(file=path+name[count]+'.gif'))
                self.canvas.create_window((120+130*row,y),window=Button(self.canvas,image=self.temp[count],command=lambda key=name[count]:self.goto_character_data(key)))
                count += 1
                if count >= len(name)-1 :
                    '''超過腳色數量時跳出'''
                    break
            y += 130

    def middlePage(self):
        '''中衛介面選單'''
        self.canvas.delete("all")
        self.pos = 'middle'
        self.temp = []
        name = []
        # 匯入角色字典
        for dat in self.dat.keys():
            if self.dat[dat][0] == '中衛':
                name.append(dat)
        # 語言判斷
        if self.Language == 'TW':
            path = './head/gif/'
        else:
            path = './head/gif_jp/'
        # 列座標
        y = 80
        # 陣列數
        count = 0
        # 列總數
        row = len(name) % 6 
        row = 1 + int(len(name) / 6) if row != 0 else int(len(name) / 6)
        for col in range(row):
            for row in range(6):
                '''設置按鈕座標位置'''
                self.temp.append(PhotoImage(file=path+name[count]+'.gif'))
                self.canvas.create_window((120+130*row,y),window=Button(self.canvas,image=self.temp[count],command=lambda key=name[count]:self.goto_character_data(key)))
                count += 1
                if count >= len(name)-1 :
                    '''超過腳色數量時跳出'''
                    break
            y += 130
        
    def lastPage(self):
        '''後衛介面選單'''
        self.canvas.delete("all")
        self.pos = 'last'
        self.temp = []
        name = []
        # 匯入角色字典
        for dat in self.dat.keys():
            if self.dat[dat][0] == '後衛':
                name.append(dat)
        # 語言判斷
        if self.Language == 'TW':
            path = './head/gif/'
        else:
            path = './head/gif_jp/'
        # 列座標
        y = 80
        # 陣列數
        count = 0
        # 列總數
        row = len(name) % 6 
        row = 1 + int(len(name) / 6) if row != 0 else int(len(name) / 6)
        for col in range(row):
            for row in range(6):
                '''設置按鈕座標位置'''
                self.temp.append(PhotoImage(file=path+name[count]+'.gif'))
                self.canvas.create_window((120+130*row,y),window=Button(self.canvas,image=self.temp[count],command=lambda key=name[count]:self.goto_character_data(key)))
                count += 1
                if count >= len(name)-1 :
                    '''超過腳色數量時跳出'''
                    break
            y += 130

    def goto_character_data(self,key):
        '''跳轉至角色介紹'''
        self.page.destroy()
        self.createPage_character_data(key)

    def createPage_character_data(self,key):
        '''設定頁面模板'''
        self.page = Frame(self.root)
        self.page.pack()
        '''字型'''
        self.main_button_font=tkFont.Font(size=13,weight='bold')
        self.character_name_font=tkFont.Font(size=18,weight='bold')
        self.introduction_font=tkFont.Font(size=12,weight='bold')
        self.grading_font=tkFont.Font(size=12,weight='bold')
        '''背景圖片'''
        image = Image.open('lastpage/page3_background.gif')
        self.yellowstone = ImageTk.PhotoImage(image)
        Label(self.page,image=self.yellowstone).pack()
        '''回上一頁'''
        self.main_button＿pic = PhotoImage(file='lastpage/third_button.gif')
        Button(self.page,text='回上一頁',image= self.main_button＿pic,compound=CENTER,font=self.main_button_font,command=self.goto_character).place(x=10,y=10,width=100,height=30)
        self.character_data(key)

    def character_data(self,key):
        '''顯示角色資料'''
        # 角色姓名
        self.name = key
        # 語言判斷
        if self.Language == 'TW':
            head_path = './head/gif/'
            people_path = './people/gif/'
            self.type_ = self.dat[self.name][4]
            self.score = self.dat[self.name][2]
        else:
            head_path = './head/gif_jp/'
            people_path = './people/gif_jp/'
            self.type_ = self.dat[self.name][0]
            self.score = self.dat[self.name][2] + ' / ' + self.dat[self.name][3] + ' / ' + self.dat[self.name][4]
        #頭像圖片與位置 圖片大小請設置100*100
        self.img_for_character = ImageTk.PhotoImage(file=head_path + key + '.gif') #設置角色圖片
        character_pic = Label(self.page,image=self.img_for_character)
        character_pic.place(x=100,y=70,width=100,height=100)
        #名字顯示與位置
        character_name= StringVar()
        character_name.set(self.name)
        text_for_character_name= Label(self.page, textvariable= character_name, font= self.character_name_font )
        text_for_character_name.place(x=250,y=105)
        #介紹文字
        introduction= StringVar()
        introduction.set(self.dat[self.name][1])
        text_for_introduction= Label(self.page, textvariable= introduction,bg='yellow',font= self.introduction_font,justify='left',wraplength = 500,anchor = 'w')
        text_for_introduction.place(x=100,y=200)
        #評分簡介 (左側標題)
        text_for_grade= Label(self.page, text='評等分數:', font= self.grading_font )
        text_for_grade.place(x=100,y=270)

        text_for_position= Label(self.page, text='定位:', font= self.grading_font )
        text_for_position.place(x=100,y=320)
        
        text_for_fit= Label(self.page, text='適合度:', font= self.grading_font )
        text_for_fit.place(x=100,y=370)

        text_for_explanation= Label(self.page, text='簡易評價:', font= self.grading_font )
        text_for_explanation.place(x=100,y=420)
        #評分簡介 (右側內容)
        '''評價分數'''
        grade_content= StringVar()
        grade_content.set(self.score)
        text_for_grade_content= Label(self.page, textvariable= grade_content, font= self.grading_font )
        text_for_grade_content.place(x=200,y=270)
        '''類型'''
        position_content= StringVar()
        position_content.set(self.type_)
        text_for_position_content= Label(self.page, textvariable= position_content, font= self.grading_font )
        text_for_position_content.place(x=200,y=320)
        '''角色趨勢'''
        fit_content= StringVar()
        fit_content.set(self.dat[self.name][5])
        text_for_fit_content= Label(self.page, textvariable= fit_content, font= self.grading_font )
        text_for_fit_content.place(x=200,y=370)
        '''優缺點'''
        explanation_content= StringVar()
        #將優缺點切出來
        re_str = self.dat[key][6].replace('【弱','\n【弱').split('【星')
        explanation_content.set(re_str[0])
        
        text_for_explanation_content= Label(self.page, textvariable= explanation_content, font=self.grading_font,justify='left',wraplength = 400,anchor = 'w')
        text_for_explanation_content.place(x=200,y=420,width=400)
        #右側大圖 圖片大小請設置500*280
        '''右側角色圖示'''
        img = Image.open(people_path + key + '.gif')
        (w,h) = img.size
        new_img = img.resize((500,300))
        self.img_for_character_rightside_big = ImageTk.PhotoImage(new_img) #設置角色圖片
        character_pic = Label(self.page, image = self.img_for_character_rightside_big)
        character_pic.place(x=625,y=200,width=500,height=280)

    def goto_character(self):
        '''跳轉至前衛、中衛、後衛選單介面'''
        self.page.destroy()
        character(self.root,self.pos)