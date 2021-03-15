import requests
import bs4
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
import io
import csv

def createButton(head=None,key=None):
        if (head != None and key != None):
            print(head)
            img = urlopen('https://s3-ap-northeast-1.amazonaws.com/gamewith/article_tools/pricone-re/gacha/92903_is.png').read()
            data_stream = io.BytesIO(img)
            pil_img = Image.open(data_stream)
            head_img = ImageTk.PhotoImage(pil_img)
            # self.front_p1_pic = PhotoImage(file='front_head/pic_1.gif')
            label = Label(root, image=head_img)
            label.pack(padx=5, pady=5)
            # Button(canvas,image=head,command=lambda key=key:goto_character_data(key))

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
dat = {c[0] : c[1:] for c in columns}

root = Tk()
ls = list(dat['可可蘿'])
img = urlopen(ls[1]).read()
data_stream = io.BytesIO(img)
pil_img = Image.open(data_stream)
head_img = ImageTk.PhotoImage(pil_img)
# self.front_p1_pic = PhotoImage(file='front_head/pic_1.gif')
label = Label(root, image=head_img)
label.pack(padx=5, pady=5)
# Button(canvas,image=head,command=lambda key=key:goto_character_data(key))

root.mainloop()