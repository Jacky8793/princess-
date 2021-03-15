from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import pygame as py
from character import *
import data

'''背景音樂'''
py.mixer.init()                         #更改音樂檔案
Music = r"./music/bgm.mp3"               #音樂位置
py.mixer.music.load(Music)              #讀取音樂
py.mixer.music.set_volume(0.3)          #設定音量大小(0~1)
py.mixer.music.play()                   #播放

class home(object):
    '''創建首頁'''
    def __init__(self,master=None):
        self.root = master
        # 鎖定頁面
        self.root.resizable(False,False)
        # icon設定
        self.root.iconbitmap("mainpage/app_icon.ico")
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
        self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

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
        self.Language = 'JP'
        self.createPage()
        self.root.mainloop()
    
    def Language_cheak(self,Lang):
        self.Language = Lang

    def createPage(self):
        '''首頁內容'''
        self.page = Frame(self.root)
        self.page.pack()
        '''背景圖片'''
        self.yellowstone = ImageTk.PhotoImage(file="mainpage/background.gif")
        Label(self.page,image=self.yellowstone).pack()
        self.main_button_font= tkFont.Font(size=36, weight="bold")
        self.main_button＿pic = PhotoImage(file="mainpage/main_button.gif")
        '''跳轉'''
        Button(self.page,text="前衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_frontPage).place(x=150,y=300,width=260,height=90)
        Button(self.page,text="中衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_middlePage).place(x=450,y=300,width=260,height=90)
        Button(self.page,text="後衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_lastPage).place(x=750,y=300,width=260,height=90)
    
    def goto_frontPage(self):
        '''跳轉至前衛角色資料'''
        self.page.destroy()
        character(self.root,'front',self.Language)

    def goto_middlePage(self):
        '''跳轉至中衛角色資料'''
        self.page.destroy()
        character(self.root,'middle',self.Language)

    def goto_lastPage(self):
        '''跳轉至後衛角色資料'''
        self.page.destroy()
        character(self.root,'last',self.Language)
