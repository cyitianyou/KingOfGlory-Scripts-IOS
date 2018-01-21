# -*- coding: utf-8 -*-
"""
截图
"""
import wda
C = wda.Client()
S = C.session()

if __name__ == '__main__':
    S.tap(5,5)
