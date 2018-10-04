#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 21:30
# @User    : zhunishengrikuaile
# @File    : idcard.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: MeBlog
'''
身份证识别
'''

import os
import base64
import requests
from shitu_api.bin.CharacterRecognition.general import ORC_Images

class Idcard(ORC_Images):
    def __init__(self, IMG, API_KEY, SECRET_KEY, URLS, detect_risk=True, id_card_side='front'):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.img = IMG
        self.urls = URLS
        self.detect_risk = detect_risk
        self.id_card_side = id_card_side

    def postOrcImg(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}?access_token={}".format(self.urls, self.get_token())
        if os.path.isfile(self.img):
            with open(self.img, 'rb') as img_file:
                imgs = base64.b64encode(img_file.read())
        else:
            return '文件路径不正确'
        data = {'image': imgs, 'detect_direction': True, 'id_card_side': self.id_card_side,
                'detect_risk':self.detect_risk}
        result = requests.post(url, headers=header, data=data)
        return result
