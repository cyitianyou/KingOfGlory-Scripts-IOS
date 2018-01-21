# -*- coding: utf-8 -*-
"""
查找图片位置
"""
import aircv as ac

def _image_pos(name):
    """
    查找指定图片在背景图中的位置
    """
    imsrc = ac.imread('images/bg/{}.png'.format(name[1:]))
    imobj = ac.imread('images/{}.PNG'.format(name))
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    circle_center_pos = pos['result']
    return circle_center_pos

if __name__ == '__main__':
    _image_pos('01')