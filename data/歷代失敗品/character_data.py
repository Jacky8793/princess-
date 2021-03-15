from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from character import *

class character_data(object):
    '''角色資料'''
    def __init__(self,master=None,pos=None):
        self.root = master
        self.pos = pos
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
        self.createPage()
        self.root.mainloop()

    def createPage(self):
        '''設定頁面模板'''
        self.page = Frame(self.root)
        self.page.pack()
        '''字型'''
        self.main_button_font=tkFont.Font(size=13,weight="bold")
        self.character_name_font=tkFont.Font(size=18,weight="bold")
        self.introduction_font=tkFont.Font(size=12,weight="bold")
        self.grading_font=tkFont.Font(size=12,weight="bold")
        '''背景圖片'''
        image = Image.open("lastpage/page3_background.gif")
        self.yellowstone = ImageTk.PhotoImage(image)
        Label(self.page,image=self.yellowstone).pack()
        '''回上一頁'''
        self.main_button＿pic = PhotoImage(file="lastpage/third_button.gif")
        Button(self.page,text="回上一頁",image= self.main_button＿pic,compound=CENTER,font=self.main_button_font,command=self.goto_character).place(x=10,y=10,width=100,height=30)
        self.character_data()

    def character_data(self,row=None):
        '''顯示角色資料'''
        #頭像圖片與位置 圖片大小請設置100*100
        self.img_for_character = ImageTk.PhotoImage(file="lastpage/character.gif") #設置角色圖片
        character_pic = Label(self.page,image=self.img_for_character)
        character_pic.place(x=100,y=100,width=100,height=100)
        #名字顯示與位置
        character_name= StringVar()
        character_name.set("可可羅")
        text_for_character_name= Label(self.page, textvariable= character_name, font= self.character_name_font )
        text_for_character_name.place(x=250,y=135)
        #介紹文字
        introduction= StringVar()
        introduction.set("いいい、いらっしゃいませ～！あ、あわわ、転ぶぅぅ！？")
        text_for_introduction= Label(self.page, textvariable= introduction,bg="yellow",font= self.introduction_font )
        text_for_introduction.place(x=100,y=230)
        #評分簡介 (左側標題)
        grade= StringVar()
        grade.set("評等分數:")
        text_for_grade= Label(self.page, textvariable= grade, font= self.grading_font )
        text_for_grade.place(x=100,y=300)
        position= StringVar()
        position.set("定位:")
        text_for_position= Label(self.page, textvariable= position, font= self.grading_font )
        text_for_position.place(x=100,y=350)
        fit= StringVar()
        fit.set("關卡適合度:")
        text_for_fit= Label(self.page, textvariable= fit, font= self.grading_font )
        text_for_fit.place(x=100,y=400)
        explanation= StringVar()
        explanation.set("簡易評價:")
        text_for_explanation= Label(self.page, textvariable= explanation, font= self.grading_font )
        text_for_explanation.place(x=100,y=450)
        #評分簡介 (右側內容)
        grade_content= StringVar()
        grade_content.set("9.0/10分")
        text_for_grade_content= Label(self.page, textvariable= grade_content, font= self.grading_font )
        text_for_grade_content.place(x=200,y=300)
        position_content= StringVar()
        position_content.set("支援型")
        text_for_position_content= Label(self.page, textvariable= position_content, font= self.grading_font )
        text_for_position_content.place(x=200,y=350)
        fit_content= StringVar()
        fit_content.set("冒險適合度 競技場適合度")
        text_for_fit_content= Label(self.page, textvariable= fit_content, font= self.grading_font )
        text_for_fit_content.place(x=200,y=400)
        explanation_content= StringVar()
        explanation_content.set("【優勢】\n・必殺技可以大幅度恢復己方1名血量\n・使單一敵人的物理防禦力下降\n・提升己方全體的物理攻擊力\n【弱點】\n・由於必殺技才能回血的關係不太能頻繁施放")
        text_for_explanation_content= Label(self.page, textvariable= explanation_content, font=self.grading_font,justify="left" )
        text_for_explanation_content.place(x=200,y=450)
        #右側大圖 圖片大小請設置500*280
        self.img_for_character_rightside_big = ImageTk.PhotoImage(file = "lastpage/page3_character_big_pic.gif") #設置角色圖片
        character_pic = Label(self.page, image = self.img_for_character_rightside_big)
        character_pic.place(x=625,y=200,width=500,height=280)

    def goto_character(self):
        '''跳轉至前衛、中衛、後衛選單介面'''
        self.page.destroy()
        character(self.root,self.pos)