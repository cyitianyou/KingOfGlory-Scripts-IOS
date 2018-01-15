# -*- coding: utf-8 -*-
"""
python 脚本,自动刷王者荣耀冒险模式金币
"""
import os
import shutil
import time
import random
import wda
import aircv as ac

C = wda.Client()
S = C.session()

SCREENSHOT_BACKUP_DIR = 'screenshot_backups/'
if not os.path.isdir(SCREENSHOT_BACKUP_DIR):
    os.mkdir(SCREENSHOT_BACKUP_DIR)


def pull_screenshot():
    """
    截图
    """
    C.screenshot('bg.png')


def backup_screenshot():
    """
    为了方便失败的时候 debug
    """
    ts = int(time.time())
    if not os.path.isdir(SCREENSHOT_BACKUP_DIR):
        os.mkdir(SCREENSHOT_BACKUP_DIR)
    shutil.copy('bg.png', '{}{}.png'.format(SCREENSHOT_BACKUP_DIR, ts))


def find_image_pos(name):
    """
    查找指定图片在背景图中的位置
    """
    pull_screenshot()
    imsrc = ac.imread('bg.jpg')
    imobj = ac.imread(name)
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    circle_center_pos = pos['result']
    return circle_center_pos


def main():
    """
    主函数
    """
    while True:

        time.sleep(random.uniform(1, 1.1))


if __name__ == '__main__':
    main()
