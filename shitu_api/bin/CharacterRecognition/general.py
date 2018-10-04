#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 20:32
# @User    : zhunishengrikuaile
# @File    : 通用文字识别.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: MeBlog
'''
百度识图，通用文字识别，网络图片文字识别
'''
import os
import base64
import requests


class ORC_Images(object):

    def __init__(self, IMG, API_KEY, SECRET_KEY, URLS):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.img = IMG
        self.urls = URLS

    def get_token(self):
        '''
        获取access_token
        :param API_KEY:
        :param SECRET_KEY:
        :return:
        '''
        access_token_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(
            self.API_KEY, self.SECRET_KEY)
        access_token = requests.post(access_token_url)
        return access_token.json()['access_token']

    def postOrcImg(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}?access_token={}".format(self.urls, self.get_token())
        if os.path.isfile(self.img):
            with open(self.img, 'rb') as img_file:
                imgs = base64.b64encode(img_file.read())
            data = {'image': imgs}
        else:
            data = {'url': self.img}
        result = requests.post(url, headers=header, data=data)
        return result
