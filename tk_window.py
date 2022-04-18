# -*- encoding : utf-8 -*-
"""
@Time : 2022年04月18日 10:16
@Contact : hfhzzdx@hotmail.com
@File : tk_window.py
@SoftWare : PyCharm
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022-04-18 10:16   hfh      1.0         None
"""

import tkinter as tk
from wallhavenapi import *
from tkinter.filedialog import askdirectory
import os
import tkinter.messagebox
import sys
from decimal import *
from datetime import datetime

win = tk.Tk()  
win.title("Wallhaven Downloader")  
win.geometry('750x400')  
canvas = tk.Canvas(win, height=200, width=500) 
img_file = tk.PhotoImage(file='welcome.gif')  
image = canvas.create_image(30, 0, anchor='nw', image=img_file) 
canvas.pack(side='top') 

tk.Label(win, text='请输入个人Api Key ').place(x=50, y=150) 
var_app_key = tk.StringVar() 
entry_app_key = tk.Entry(win, textvariable=var_app_key, width=40)
entry_app_key.place(x=200, y=150)


# l = tk.Label(win, bg='yellow', width=50, height=2, text='empty')
# l.pack()
tk.Label(win, text='请选择要爬取的类别:').place(x=50, y=180)

category = tk.StringVar()


def select_category():
    print("您要爬取的类型是:" + category.get())


general = tk.Radiobutton(
    win, text='普通', variable=category, value=Category.general, command=select_category)
general.pack()
general.place(x=200, y=180)
anime = tk.Radiobutton(
    win, text='动漫', variable=category, value=Category.anime, command=select_category)
anime.pack()
anime.place(x=300, y=180)
people = tk.Radiobutton(
    win, text='人物', variable=category, value=Category.people, command=select_category)
people.pack()
people.place(x=400, y=180)
category.set(Category.general)





win.mainloop()
