# -*- coding: utf-8 -*-
"""
python 脚本,自动刷王者荣耀冒险模式金币
"""
import os
import sys
import shutil
import time
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


def _image_pos(name):
    """
    查找指定图片在背景图中的位置
    """
    pull_screenshot()
    imsrc = ac.imread('bg.png')
    imobj = ac.imread('images/0{}.PNG'.format(name))
    # find the match position
    pos = ac.find_template(imsrc, imobj, 0.8)
    circle_center_pos = None
    if pos != None:
        circle_center_pos = pos['result']
        # print('找到图片坐标[{},{}]'.format(circle_center_pos[0],circle_center_pos[1]))
    return circle_center_pos


def tap(pos):
    S.tap(750 - pos[1], pos[0])


def main():
    """
    主函数
    """
    count = 1
    while True:
        # 查找“闯关”按钮，并点击
        while True:
            pos = _image_pos('1')
            if pos != None:
                print('开始第{}次闯关'.format(count))
                tap(pos)
                break
            time.sleep(5)
        # 查找“点击屏幕继续”文字，并点击
        while True:
            pos = _image_pos('4')
            if pos != None:
                tap(pos)
                print('本次闯关完成，共获得[{}]金币'.format(count * 56))
                print('点击屏幕继续')
                break
            # 查找“跳过”或“自动”按钮，并点击
            pos = _image_pos('2')
            if pos != None:
                tap(pos)
                print('自动跳过对话')
                time.sleep(1)
            pos = _image_pos('3')
            if pos != None:
                tap(pos)
                print('开始自动闯关')
            time.sleep(3)
        # 查找“再次挑战按钮”，并点击
        while True:
            pos = _image_pos('5')
            if pos != None:
                time.sleep(2)
                pos_upper = _image_pos('6')
                if pos_upper != None:
                    # 金币达到上限
                    print('检测到金币达到上限,脚本自动退出!')
                    C.home()
                    sys.exit()
                tap(pos)
                print('再次挑战')
                break
            time.sleep(3)
        # 闯关次数+1
        count = count + 1


if __name__ == '__main__':
    main()
