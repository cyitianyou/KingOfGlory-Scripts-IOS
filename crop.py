# -*- coding: utf-8 -*-

from PIL import Image

if __name__ == '__main__':
    name = '6'
    img = Image.open('images/bg/{}.png'.format(name))
    # region = (920, 80, 1112, 150)
    # region = (1180, 680, 1310, 720)
    # region = (1220, 697, 1270, 745)
    # region = (575, 30, 758, 60)
    # region = (1020, 35, 1200, 90)
    region = (1134, 412, 1273, 430)

    # 裁切图片
    cropImg = img.crop(region)

    # 保存裁切后的图片
    cropImg.save('images/0{}.png'.format(name))
