# -*- encoding : utf-8 -*-
"""
@Time : 2022年04月15日 17:09
@Contact : hfhzzdx@hotmail.com
@File : img2char.py
@SoftWare : PyCharm
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022-04-15 17:09   hfh      1.0         None
"""

from PIL import Image as img
import os
ascii_char = list(".$@B%8&2M#*oahkbdpqwmzO0QLCJUYXvZcunxrjft/\|()1{}[]?-_+~<>i!1I;:,\"^`'")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    file_list = []
    rootpath = ''
    img_path_list = []
    file_path = input("请输入要预览的图片文件夹路径(图片文件的上一级目录)\r\n")
    for root, dirs, files in os.walk(file_path):
        file_list = files
        rootpath = root
    for filepath in file_list:
        img_path_list.append(rootpath+'/'+filepath)
    for file in img_path_list:
        # img_path = input("请输入图片地址\r\n")
        # WIDTH = 150
        # HEIGHT = 40
        im = img.open(file)
        print(im.size)
        print("图片的宽为{}px,高为{}px".format(str(im.size[0]), str(im.size[1])))
        HEIGHT = int(input("请输入要输出的像素高度\r\n"))
        WIDTH = int(HEIGHT * (im.size[0] / im.size[1]) * 3)
        im = im.resize((WIDTH,HEIGHT), img.NEAREST)
        text = ''
        for i in range(HEIGHT):
            for j in range(WIDTH):
                text += get_char(*im.getpixel((j, i)))
            text += '\n'
        print(text)
