# -*- coding: utf-8 -*-

from PIL import Image

if __name__ == '__main__':
    name = '5'
    img = Image.open('images/bg/{}.png'.format(name))
    #region = (80,920,150,1112)
    #region = (680,1180,720,1310)
    #region = (697,1220,745,1270)
    #region = (30,575,60,758)
    region = (35,1020,90,1200)

    #裁切图片
    cropImg = img.crop(region)

    #保存裁切后的图片
    cropImg.save('images/0{}.png'.format(name))