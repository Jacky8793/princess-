from tkinter import *

def num_name(num):
    '''列印num'''
    print(num)

root = Tk()
name = ['11','22','33']
'''用for迴圈印出獨立按鈕，並列印出各自結果'''
for i in range(len(name)):
    Button(root,text=name[i],command= lambda num=i:num_name(num)).pack()
root.mainloop()