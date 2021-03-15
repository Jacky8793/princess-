import requests
import bs4
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

'''使用圖片網址在tk上顯示'''
info_url = 'https://gamewith.tw/pricone-re/article/show/89768' #更動區
tsmchtml_ = requests.get(info_url)
objSoup_ = bs4.BeautifulSoup(tsmchtml_.text, 'html.parser')
root = Tk()
                
src = objSoup_.find('div',class_='pcr_img_charatop').find('img').get('src')
img = urlopen(src).read()
data_stream = io.BytesIO(img)
pil_img = Image.open(data_stream)

tk_img = ImageTk.PhotoImage(pil_img)

label = Label(root, image=tk_img, bg='brown')
label.pack(padx=5, pady=5)
root.mainloop()