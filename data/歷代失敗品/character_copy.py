from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from urllib.request import urlopen
import io
import csv

class character(object):
    '''前衛、中衛、後衛選單介面'''
    def __init__(self,master=None,pos=None):
        self.root = master
        self.pos = pos
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
        self.character_dict()
        self.createPage()
        self.root.mainloop()
    
    def character_dict(self):
        '''角色字典'''
        columns = []
        with open('character.csv','r',encoding='utf-8') as f: 
            reader = csv.reader(f)
            for row in reader:
                if columns:
                    for i, value in enumerate(row):
                        columns[i].append(value)
                else:
                    columns = [[value] for value in row]
        '''建立字典'''
        self.dat = {c[0] : c[1:] for c in columns}

    def createPage(self):
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
        self.canvas=Canvas(self.page,width=898,height=490,scrollregion=(0,0,1000,800),bd=0,bg='#f9ca7c')
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

    def createButton(self,head=None,key=None):
        if (head != None and key != None):
            print(head)
            img = urlopen(head).read()
            data_stream = io.BytesIO(img)
            pil_img = Image.open(data_stream)
            self.head = ImageTk.PhotoImage(pil_img)
            # self.front_p1_pic = PhotoImage(file='front_head/pic_1.gif')
            label = Label(self.page, image=self.head, bg='brown')
            label.pack(padx=5, pady=5)
            Button(self.canvas,image=self.head,command=lambda key=key:self.goto_character_data(key))
            

    def frontPage(self):
        '''前衛介面選單'''
        name = tuple(self.dat.keys())
        y = 80
        for col in range(len(self.dat.keys())):
            for row in range(6):
                img = urlopen(self.dat[name[row]][1]).read()
                data_stream = io.BytesIO(img)
                pil_img = Image.open(data_stream)
                self.head = ImageTk.PhotoImage(pil_img)
                self.canvas.create_window((120+130*row,y),window=Button(self.canvas,image=self.head)) #,command=lambda key=name[row]:self.goto_character_data(key)
            y += 130
        
        # self.front_p1_pic = PhotoImage(file='front_head/pic_1.gif') # 按鈕圖示
        # self.front_p1 = Button(self.canvas,image=self.front_p1_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,80),window=Button(self.canvas,image=self.front_p1_pic,command=self.goto_character_data))
        
        # self.front_p2_pic = PhotoImage(file='front_head/pic_2.gif') # 按鈕圖示
        # self.front_p2 = Button(self.canvas,image=self.front_p2_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,80),window=self.front_p2)
        
        # self.front_p3_pic = PhotoImage(file='front_head/pic_3.gif') # 按鈕圖示
        # self.front_p3 = Button(self.canvas,image=self.front_p3_pic,command=self.goto_character_data)
        # self.canvas.create_window((380,80),window=self.front_p3)
        
        # self.front_p4_pic = PhotoImage(file='front_head/pic_4.gif') # 按鈕圖示
        # self.front_p4 = Button(self.canvas,image=self.front_p4_pic,command=self.goto_character_data)
        # self.canvas.create_window((510,80),window=self.front_p4)
        
        # self.front_p5_pic = PhotoImage(file='front_head/pic_5.gif') # 按鈕圖示
        # self.front_p5 = Button(self.canvas,image=self.front_p5_pic,command=self.goto_character_data)
        # self.canvas.create_window((640,80),window=self.front_p5)
        
        # self.front_p6_pic = PhotoImage(file='front_head/pic_6.gif') # 按鈕圖示
        # self.front_p6 = Button(self.canvas,image=self.front_p6_pic,command=self.goto_character_data)
        # self.canvas.create_window((770,80),window=self.front_p6)
        
        # #按鈕第2行
        # self.front_p7_pic = PhotoImage(file='front_head/pic_7.gif') # 按鈕圖示
        # self.front_p7 = Button(self.canvas,image=self.front_p7_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,210),window=self.front_p7)
        
        # self.front_p8_pic = PhotoImage(file='front_head/pic_8.gif') # 按鈕圖示
        # self.front_p8 = Button(self.canvas,image=self.front_p8_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,210),window=self.front_p8)
        
        # self.front_p9_pic = PhotoImage(file='front_head/pic_9.gif') # 按鈕圖示
        # self.front_p9 = Button(self.canvas,image=self.front_p9_pic,command=self.goto_character_data)
        # self.canvas.create_window((380,210),window=self.front_p9)
        
        # self.front_p10_pic = PhotoImage(file='front_head/pic_10.gif') # 按鈕圖示
        # self.front_p10 = Button(self.canvas,image=self.front_p10_pic,command=self.goto_character_data)
        # self.canvas.create_window((510,210),window=self.front_p10)
        
        # self.front_p11_pic = PhotoImage(file='front_head/pic_11.gif') # 按鈕圖示
        # self.front_p11 = Button(self.canvas,image=self.front_p11_pic,command=self.goto_character_data)
        # self.canvas.create_window((640,210),window=self.front_p11)
        
        # self.front_p12_pic = PhotoImage(file='front_head/pic_12.gif') # 按鈕圖示
        # self.front_p12 = Button(self.canvas,image=self.front_p12_pic,command=self.goto_character_data)
        # self.canvas.create_window((770,210),window=self.front_p12)
        
        # #按鈕第3行
        # self.front_p13_pic = PhotoImage(file='front_head/pic_13.gif') # 按鈕圖示
        # self.front_p13 = Button(self.canvas,image=self.front_p13_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,340),window=self.front_p13)
        
        # self.front_p14_pic = PhotoImage(file='front_head/pic_14.gif') # 按鈕圖示
        # self.front_p14 = Button(self.canvas,image=self.front_p14_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,340),window=self.front_p14)
        
        # self.front_p15_pic = PhotoImage(file='front_head/pic_15.gif') # 按鈕圖示
        # self.front_p15 = Button(self.canvas,image=self.front_p15_pic,command=self.goto_character_data)
        # self.canvas.create_window((380,340),window=self.front_p15)
        
        # self.front_p16_pic = PhotoImage(file='front_head/pic_16.gif') # 按鈕圖示
        # self.front_p16 = Button(self.canvas,image=self.front_p16_pic,command=self.goto_character_data)
        # self.canvas.create_window((510,340),window=self.front_p16)
        
        # self.front_p17_pic = PhotoImage(file='front_head/pic_17.gif') # 按鈕圖示
        # self.front_p17 = Button(self.canvas,image=self.front_p17_pic,command=self.goto_character_data)
        # self.canvas.create_window((640,340),window=self.front_p17)
        
        # self.front_p18_pic = PhotoImage(file='front_head/pic_18.gif') # 按鈕圖示
        # self.front_p18 = Button(self.canvas,image=self.front_p18_pic,command=self.goto_character_data)
        # self.canvas.create_window((770,340),window=self.front_p18)
        
        # #按鈕第4行
        # self.front_p19_pic = PhotoImage(file='front_head/pic_19.gif') # 按鈕圖示
        # self.front_p19 = Button(self.canvas,image=self.front_p19_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,470),window=self.front_p19)
        
        # self.front_p20_pic = PhotoImage(file='front_head/pic_20.gif') # 按鈕圖示
        # self.front_p20 = Button(self.canvas,image=self.front_p20_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,470),window=self.front_p20)
        
        # self.front_p21_pic = PhotoImage(file='front_head/pic_21.gif') # 按鈕圖示
        # self.front_p21 = Button(self.canvas,image=self.front_p21_pic,command=self.goto_character_data)
        # self.canvas.create_window((380,470),window=self.front_p21)
        
        # self.front_p22_pic = PhotoImage(file='front_head/pic_22.gif') # 按鈕圖示
        # self.front_p22 = Button(self.canvas,image=self.front_p22_pic,command=self.goto_character_data)
        # self.canvas.create_window((510,470),window=self.front_p22)
        
        # self.front_p23_pic = PhotoImage(file='front_head/pic_23.gif') # 按鈕圖示
        # self.front_p23 = Button(self.canvas,image=self.front_p23_pic,command=self.goto_character_data)
        # self.canvas.create_window((640,470),window=self.front_p23)
        
        # self.front_p24_pic = PhotoImage(file='front_head/pic_24.gif') # 按鈕圖示
        # self.front_p24 = Button(self.canvas,image=self.front_p24_pic,command=self.goto_character_data)
        # self.canvas.create_window((770,470),window=self.front_p24)
        
        # #按鈕第5行
        # self.front_p25_pic = PhotoImage(file='front_head/pic_25.gif') # 按鈕圖示
        # self.front_p25 = Button(self.canvas,image=self.front_p25_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,600),window=self.front_p25)
        
        # self.front_p26_pic = PhotoImage(file='front_head/pic_26.gif') # 按鈕圖示
        # self.front_p26 = Button(self.canvas,image=self.front_p26_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,600),window=self.front_p26)
        
        # self.front_p27_pic = PhotoImage(file='front_head/pic_27.gif') # 按鈕圖示
        # self.front_p27 = Button(self.canvas,image=self.front_p27_pic,command=self.goto_character_data)
        # self.canvas.create_window((380,600),window=self.front_p27)
        
        # self.front_p28_pic = PhotoImage(file='front_head/pic_28.gif') # 按鈕圖示
        # self.front_p28 = Button(self.canvas,image=self.front_p28_pic,command=self.goto_character_data)
        # self.canvas.create_window((510,600),window=self.front_p28)
        
        # self.front_p29_pic = PhotoImage(file='front_head/pic_29.gif') # 按鈕圖示
        # self.front_p29 = Button(self.canvas,image=self.front_p29_pic,command=self.goto_character_data)
        # self.canvas.create_window((640,600),window=self.front_p29)
        
        # self.front_p30_pic = PhotoImage(file='front_head/pic_30.gif') # 按鈕圖示
        # self.front_p30 = Button(self.canvas,image=self.front_p30_pic,command=self.goto_character_data)
        # self.canvas.create_window((770,600),window=self.front_p30)
        
        # #按鈕第6行
        # self.front_p31_pic = PhotoImage(file='front_head/pic_31.gif') # 按鈕圖示
        # self.front_p31 = Button(self.canvas,image=self.front_p31_pic,command=self.goto_character_data)
        # self.canvas.create_window((120,730),window=self.front_p31)
        
        # self.front_p32_pic = PhotoImage(file='front_head/pic_32.gif') # 按鈕圖示
        # self.front_p32 = Button(self.canvas,image=self.front_p32_pic,command=self.goto_character_data)
        # self.canvas.create_window((250,730),window=self.front_p32)

    def middlePage(self):
        '''中衛介面選單'''
        #按鈕第一行
        self.middle_p1_pic = PhotoImage(file='middle_head/pic_1.gif') # 按鈕圖示
        self.middle_p1 = Button(self.canvas,image=self.middle_p1_pic,command=self.goto_character_data)
        self.canvas.create_window((120,80),window=self.middle_p1)
        
        self.middle_p2_pic = PhotoImage(file='middle_head/pic_2.gif') # 按鈕圖示
        self.middle_p2 = Button(self.canvas,image=self.middle_p2_pic,command=self.goto_character_data)
        self.canvas.create_window((250,80),window=self.middle_p2)
        
        self.middle_p3_pic = PhotoImage(file='middle_head/pic_3.gif') # 按鈕圖示
        self.middle_p3 = Button(self.canvas,image=self.middle_p3_pic,command=self.goto_character_data)
        self.canvas.create_window((380,80),window=self.middle_p3)
        
        self.middle_p4_pic = PhotoImage(file='middle_head/pic_4.gif') # 按鈕圖示
        self.middle_p4 = Button(self.canvas,image=self.middle_p4_pic,command=self.goto_character_data)
        self.canvas.create_window((510,80),window=self.middle_p4)
        
        self.middle_p5_pic = PhotoImage(file='middle_head/pic_5.gif') # 按鈕圖示
        self.middle_p5 = Button(self.canvas,image=self.middle_p5_pic,command=self.goto_character_data)
        self.canvas.create_window((640,80),window=self.middle_p5)
        
        self.middle_p6_pic = PhotoImage(file='middle_head/pic_6.gif') # 按鈕圖示
        self.middle_p6 = Button(self.canvas,image=self.middle_p6_pic,command=self.goto_character_data)
        self.canvas.create_window((770,80),window=self.middle_p6)
        
        #按鈕第2行
        self.middle_p7_pic = PhotoImage(file='middle_head/pic_7.gif') # 按鈕圖示
        self.middle_p7 = Button(self.canvas,image=self.middle_p7_pic,command=self.goto_character_data)
        self.canvas.create_window((120,210),window=self.middle_p7)
        
        self.middle_p8_pic = PhotoImage(file='middle_head/pic_8.gif') # 按鈕圖示
        self.middle_p8 = Button(self.canvas,image=self.middle_p8_pic,command=self.goto_character_data)
        self.canvas.create_window((250,210),window=self.middle_p8)
        
        self.middle_p9_pic = PhotoImage(file='middle_head/pic_9.gif') # 按鈕圖示
        self.middle_p9 = Button(self.canvas,image=self.middle_p9_pic,command=self.goto_character_data)
        self.canvas.create_window((380,210),window=self.middle_p9)
        
        self.middle_p10_pic = PhotoImage(file='middle_head/pic_10.gif') # 按鈕圖示
        self.middle_p10 = Button(self.canvas,image=self.middle_p10_pic,command=self.goto_character_data)
        self.canvas.create_window((510,210),window=self.middle_p10)
        
        self.middle_p11_pic = PhotoImage(file='middle_head/pic_11.gif') # 按鈕圖示
        self.middle_p11 = Button(self.canvas,image=self.middle_p11_pic,command=self.goto_character_data)
        self.canvas.create_window((640,210),window=self.middle_p11)
        
        self.middle_p12_pic = PhotoImage(file='middle_head/pic_12.gif') # 按鈕圖示
        self.middle_p12 = Button(self.canvas,image=self.middle_p12_pic,command=self.goto_character_data)
        self.canvas.create_window((770,210),window=self.middle_p12)
        
        #按鈕第3行
        self.middle_p13_pic = PhotoImage(file='middle_head/pic_13.gif') # 按鈕圖示
        self.middle_p13 = Button(self.canvas,image=self.middle_p13_pic,command=self.goto_character_data)
        self.canvas.create_window((120,340),window=self.middle_p13)
        
        self.middle_p14_pic = PhotoImage(file='middle_head/pic_14.gif') # 按鈕圖示
        self.middle_p14 = Button(self.canvas,image=self.middle_p14_pic,command=self.goto_character_data)
        self.canvas.create_window((250,340),window=self.middle_p14)
        
        self.middle_p15_pic = PhotoImage(file='middle_head/pic_15.gif') # 按鈕圖示
        self.middle_p15 = Button(self.canvas,image=self.middle_p15_pic,command=self.goto_character_data)
        self.canvas.create_window((380,340),window=self.middle_p15)
        
        self.middle_p16_pic = PhotoImage(file='middle_head/pic_16.gif') # 按鈕圖示
        self.middle_p16 = Button(self.canvas,image=self.middle_p16_pic,command=self.goto_character_data)
        self.canvas.create_window((510,340),window=self.middle_p16)
        
        self.middle_p17_pic = PhotoImage(file='middle_head/pic_17.gif') # 按鈕圖示
        self.middle_p17 = Button(self.canvas,image=self.middle_p17_pic,command=self.goto_character_data)
        self.canvas.create_window((640,340),window=self.middle_p17)
        
        self.middle_p18_pic = PhotoImage(file='middle_head/pic_18.gif') # 按鈕圖示
        self.middle_p18 = Button(self.canvas,image=self.middle_p18_pic,command=self.goto_character_data)
        self.canvas.create_window((770,340),window=self.middle_p18)
        
        #按鈕第4行
        self.middle_p19_pic = PhotoImage(file='middle_head/pic_19.gif') # 按鈕圖示
        self.middle_p19 = Button(self.canvas,image=self.middle_p19_pic,command=self.goto_character_data)
        self.canvas.create_window((120,470),window=self.middle_p19)
        
        self.middle_p20_pic = PhotoImage(file='middle_head/pic_20.gif') # 按鈕圖示
        self.middle_p20 = Button(self.canvas,image=self.middle_p20_pic,command=self.goto_character_data)
        self.canvas.create_window((250,470),window=self.middle_p20)
        
        self.middle_p21_pic = PhotoImage(file='middle_head/pic_21.gif') # 按鈕圖示
        self.middle_p21 = Button(self.canvas,image=self.middle_p21_pic,command=self.goto_character_data)
        self.canvas.create_window((380,470),window=self.middle_p21)
        
    def lastPage(self):
        '''後衛介面選單'''
        #按鈕第一行
        self.last_p1_pic = PhotoImage(file='last_head/pic_1.gif') # 按鈕圖示
        self.last_p1 = Button(self.canvas,image=self.last_p1_pic,command=self.goto_character_data)
        self.canvas.create_window((120,80),window=self.last_p1)
        
        self.last_p2_pic = PhotoImage(file='last_head/pic_2.gif') # 按鈕圖示
        self.last_p2 = Button(self.canvas,image=self.last_p2_pic,command=self.goto_character_data)
        self.canvas.create_window((250,80),window=self.last_p2)
        
        self.last_p3_pic = PhotoImage(file='last_head/pic_3.gif') # 按鈕圖示
        self.last_p3 = Button(self.canvas,image=self.last_p3_pic,command=self.goto_character_data)
        self.canvas.create_window((380,80),window=self.last_p3)
        
        self.last_p4_pic = PhotoImage(file='last_head/pic_4.gif') # 按鈕圖示
        self.last_p4 = Button(self.canvas,image=self.last_p4_pic,command=self.goto_character_data)
        self.canvas.create_window((510,80),window=self.last_p4)
        
        self.last_p5_pic = PhotoImage(file='last_head/pic_5.gif') # 按鈕圖示
        self.last_p5 = Button(self.canvas,image=self.last_p5_pic,command=self.goto_character_data)
        self.canvas.create_window((640,80),window=self.last_p5)
        
        self.last_p6_pic = PhotoImage(file='last_head/pic_6.gif') # 按鈕圖示
        self.last_p6 = Button(self.canvas,image=self.last_p6_pic,command=self.goto_character_data)
        self.canvas.create_window((770,80),window=self.last_p6)
        
        #按鈕第2行
        self.last_p7_pic = PhotoImage(file='last_head/pic_7.gif') # 按鈕圖示
        self.last_p7 = Button(self.canvas,image=self.last_p7_pic,command=self.goto_character_data)
        self.canvas.create_window((120,210),window=self.last_p7)
        
        self.last_p8_pic = PhotoImage(file='last_head/pic_8.gif') # 按鈕圖示
        self.last_p8 = Button(self.canvas,image=self.last_p8_pic,command=self.goto_character_data)
        self.canvas.create_window((250,210),window=self.last_p8)
        
        self.last_p9_pic = PhotoImage(file='last_head/pic_9.gif') # 按鈕圖示
        self.last_p9 = Button(self.canvas,image=self.last_p9_pic,command=self.goto_character_data)
        self.canvas.create_window((380,210),window=self.last_p9)
        
        self.last_p10_pic = PhotoImage(file='last_head/pic_10.gif') # 按鈕圖示
        self.last_p10 = Button(self.canvas,image=self.last_p10_pic,command=self.goto_character_data)
        self.canvas.create_window((510,210),window=self.last_p10)
        
        self.last_p11_pic = PhotoImage(file='last_head/pic_11.gif') # 按鈕圖示
        self.last_p11 = Button(self.canvas,image=self.last_p11_pic,command=self.goto_character_data)
        self.canvas.create_window((640,210),window=self.last_p11)
        
        self.last_p12_pic = PhotoImage(file='last_head/pic_12.gif') # 按鈕圖示
        self.last_p12 = Button(self.canvas,image=self.last_p12_pic,command=self.goto_character_data)
        self.canvas.create_window((770,210),window=self.last_p12)
        
        #按鈕第3行
        self.last_p13_pic = PhotoImage(file='last_head/pic_13.gif') # 按鈕圖示
        self.last_p13 = Button(self.canvas,image=self.last_p13_pic,command=self.goto_character_data)
        self.canvas.create_window((120,340),window=self.last_p13)
        
        self.last_p14_pic = PhotoImage(file='last_head/pic_14.gif') # 按鈕圖示
        self.last_p14 = Button(self.canvas,image=self.last_p14_pic,command=self.goto_character_data)
        self.canvas.create_window((250,340),window=self.last_p14)
        
        self.last_p15_pic = PhotoImage(file='last_head/pic_15.gif') # 按鈕圖示
        self.last_p15 = Button(self.canvas,image=self.last_p15_pic,command=self.goto_character_data)
        self.canvas.create_window((380,340),window=self.last_p15)
        
        self.last_p16_pic = PhotoImage(file='last_head/pic_16.gif') # 按鈕圖示
        self.last_p16 = Button(self.canvas,image=self.last_p16_pic,command=self.goto_character_data)
        self.canvas.create_window((510,340),window=self.last_p16)
        
        self.last_p17_pic = PhotoImage(file='last_head/pic_17.gif') # 按鈕圖示
        self.last_p17 = Button(self.canvas,image=self.last_p17_pic,command=self.goto_character_data)
        self.canvas.create_window((640,340),window=self.last_p17)
        
        self.last_p18_pic = PhotoImage(file='front_head/pic_18.gif') # 按鈕圖示
        self.last_p18 = Button(self.canvas,image=self.last_p18_pic,command=self.goto_character_data)
        self.canvas.create_window((770,340),window=self.last_p18)
        
        #按鈕第4行
        self.last_p19_pic = PhotoImage(file='last_head/pic_19.gif') # 按鈕圖示
        self.last_p19 = Button(self.canvas,image=self.last_p19_pic,command=self.goto_character_data)
        self.canvas.create_window((120,470),window=self.last_p19)
        
        self.last_p20_pic = PhotoImage(file='last_head/pic_20.gif') # 按鈕圖示
        self.last_p20 = Button(self.canvas,image=self.last_p20_pic,command=self.goto_character_data)
        self.canvas.create_window((250,470),window=self.last_p20)
        
        self.last_p21_pic = PhotoImage(file='last_head/pic_21.gif') # 按鈕圖示
        self.last_p21 = Button(self.canvas,image=self.last_p21_pic,command=self.goto_character_data)
        self.canvas.create_window((380,470),window=self.last_p21)
        
        self.last_p22_pic = PhotoImage(file='last_head/pic_22.gif') # 按鈕圖示
        self.last_p22 = Button(self.canvas,image=self.last_p22_pic,command=self.goto_character_data)
        self.canvas.create_window((510,470),window=self.last_p22)
        
        self.last_p23_pic = PhotoImage(file='last_head/pic_23.gif') # 按鈕圖示
        self.last_p23 = Button(self.canvas,image=self.last_p23_pic,command=self.goto_character_data)
        self.canvas.create_window((640,470),window=self.last_p23)
        

    def goto_character_data(self,key):
        '''跳轉至角色介紹'''
        print(self.dat[key])
        # self.page.destroy()
        # self.createPage_character_data()

    def createPage_character_data(self):
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
        self.character_data()

    def character_data(self,row=None):
        '''顯示角色資料'''
        #頭像圖片與位置 圖片大小請設置100*100
        self.img_for_character = ImageTk.PhotoImage(file='lastpage/character.gif') #設置角色圖片
        character_pic = Label(self.page,image=self.img_for_character)
        character_pic.place(x=100,y=100,width=100,height=100)
        #名字顯示與位置
        character_name= StringVar()
        character_name.set('可可羅')
        text_for_character_name= Label(self.page, textvariable= character_name, font= self.character_name_font )
        text_for_character_name.place(x=250,y=135)
        #介紹文字
        introduction= StringVar()
        introduction.set('いいい、いらっしゃいませ～！あ、あわわ、転ぶぅぅ！？')
        text_for_introduction= Label(self.page, textvariable= introduction,bg='yellow',font= self.introduction_font )
        text_for_introduction.place(x=100,y=230)
        #評分簡介 (左側標題)
        text_for_grade= Label(self.page, text='評等分數:', font= self.grading_font )
        text_for_grade.place(x=100,y=300)

        text_for_position= Label(self.page, text='定位:', font= self.grading_font )
        text_for_position.place(x=100,y=350)
        
        text_for_fit= Label(self.page, text='關卡適合度:', font= self.grading_font )
        text_for_fit.place(x=100,y=400)

        text_for_explanation= Label(self.page, text='簡易評價:', font= self.grading_font )
        text_for_explanation.place(x=100,y=450)
        #評分簡介 (右側內容)
        grade_content= StringVar()
        grade_content.set('9.0/10分')
        text_for_grade_content= Label(self.page, textvariable= grade_content, font= self.grading_font )
        text_for_grade_content.place(x=200,y=300)
        position_content= StringVar()
        position_content.set('支援型')
        text_for_position_content= Label(self.page, textvariable= position_content, font= self.grading_font )
        text_for_position_content.place(x=200,y=350)
        fit_content= StringVar()
        fit_content.set('冒險適合度 競技場適合度')
        text_for_fit_content= Label(self.page, textvariable= fit_content, font= self.grading_font )
        text_for_fit_content.place(x=200,y=400)
        explanation_content= StringVar()
        explanation_content.set('【優勢】\n・必殺技可以大幅度恢復己方1名血量\n・使單一敵人的物理防禦力下降\n・提升己方全體的物理攻擊力\n【弱點】\n・由於必殺技才能回血的關係不太能頻繁施放')
        text_for_explanation_content= Label(self.page, textvariable= explanation_content, font=self.grading_font,justify='left' )
        text_for_explanation_content.place(x=200,y=450)
        #右側大圖 圖片大小請設置500*280
        self.img_for_character_rightside_big = ImageTk.PhotoImage(file = 'lastpage/page3_character_big_pic.gif') #設置角色圖片
        character_pic = Label(self.page, image = self.img_for_character_rightside_big)
        character_pic.place(x=625,y=200,width=500,height=280)

    def goto_character(self):
        '''跳轉至前衛、中衛、後衛選單介面'''
        self.page.destroy()
        character(self.root,self.pos)