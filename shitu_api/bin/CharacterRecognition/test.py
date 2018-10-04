#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 21:03
# @User    : zhunishengrikuaile
# @File    : test.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: MeBlog

from shitu_api.config import GENERAL_API_KEY, GENERAL_SECRET_KEY
from shitu_api.bin.CharacterRecognition.url import *

from shitu_api.bin.CharacterRecognition.general import ORC_Images
from shitu_api.bin.CharacterRecognition.idcard import Idcard
from shitu_api.bin.CharacterRecognition.banckard import Banckard
from shitu_api.bin.CharacterRecognition.driving_license import Drving_License
from shitu_api.bin.CharacterRecognition.vehicle_license import Vehicle_License
from shitu_api.bin.CharacterRecognition.license_plate import License_Plate
from shitu_api.bin.CharacterRecognition.business_license import Business_License

if __name__ == "__main__":
    # 测试通用文字识别，本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/2.png', URLS=GENERAL_URL, API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别本地：', result1.json())

    # 测试通用文字识别，url图片
    test_orc = ORC_Images(IMG='https://www.baidu.com/img/bd_logo1.png?where=super', URLS=GENERAL_URL,
                          API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('通用文字识别url: ', result.json())

    # 测试通用文字识别（含位置信息版），本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/2.png', URLS=GENERAL_High_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别（含位置信息版）本地：', result1.json())

    # 测试通用文字识别（含位置信息版），url图片
    test_orc = ORC_Images(IMG='https://www.baidu.com/img/bd_logo1.png?where=super', URLS=GENERAL_High_URL,
                          API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('通用文字识别（含位置信息版）url: ', result.json())

    # 通用文字识别（高精度含位置版），本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/2.png', URLS=GENERAL_ACCURATE_BASIC_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别（高精度含位置版）本地：', result1.json())

    # 通用文字识别（高精度含位置版），本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/2.png', URLS=GENERAL_ACCURATE_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别（高精度含位置版）本地：', result1.json())

    # 网络图片文字识别，本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/2.png', URLS=WEB_IMAGES_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('web本地：', result1.json())

    # 网络图片文字识别，url图片
    test_orc = ORC_Images(IMG='https://www.baidu.com/img/bd_logo1.png?where=super', URLS=WEB_IMAGES_URL,
                          API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('weburl: ', result.json())

    # 身份证识别，本地真实图片
    test_id = Idcard(IMG='../../testimg/sfz.jpeg', URLS=IDCARD_URL, API_KEY=GENERAL_API_KEY,
                     SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_id.postOrcImg()
    print('身份证：', result.json())

    # 银行卡识别，本地真实图片
    test_id = Banckard(IMG='../../testimg/yhk.jpeg', URLS=BANCKARD_URL, API_KEY=GENERAL_API_KEY,
                       SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_id.postOrcImg()
    print('银行卡：', result.json())

    # 驾驶证识别，测试，本地图片
    test = Drving_License(IMG='../../testimg/jsz.jpeg', URLS=DRIVING_LICENSE_URL, API_KEY=GENERAL_API_KEY,
                          SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('驾驶证：', result.json())

    # 行驶证识别，测试，本地图片
    test = Vehicle_License(IMG='../../testimg/xsz.jpg', URLS=VEHICLE_LICENSE_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('行驶证：', result.json())

    # 车牌号识别，测试，本地图片
    test = License_Plate(IMG='../../testimg/cph.jpg', URLS=LICENSE_PLATE_URL, API_KEY=GENERAL_API_KEY,
                         SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('车牌号：', result.json())

    # 营业执照识别，测试
    test = Business_License(IMG='../../testimg/yyzz.jpeg', URLS=BUSINESS_LICENSE_URL, API_KEY=GENERAL_API_KEY,
                            SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('营业执照识别：', result.json())

    # # 护照识别，测试
    # from shitu_api.bin.CharacterRecognition.passport import Passport
    # test = Passport(IMG='../../testimg/hz.jpeg', URLS=PASSPORT_URL, API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    # result = test.postOrcImg()
    # print('护照识别：', result.json())

    # 表格文字识别异步接口测试，图片
    test_orc = ORC_Images(IMG='../../testimg/hz.jpeg', URLS=GENERAL_High_URL, API_KEY=GENERAL_API_KEY,
                          SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('表格文字识别: ', result.json())

    # 通用票据识别测试，图片
    from shitu_api.bin.CharacterRecognition.receipt import Receipt

    test_orc = Receipt(IMG='../../testimg/typj.jpeg', URLS=RECEIPT_URL, API_KEY=GENERAL_API_KEY,
                       SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('通用票据识别测试: ', result.json())

    # 增值税发票识别，图片
    from shitu_api.bin.CharacterRecognition.vat_invoice import Vat_Invoice

    test = Vat_Invoice(IMG='../../testimg/zzsfp.jpeg', URLS=VAT_INVOICE_URL, API_KEY=GENERAL_API_KEY,
                       SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('增值税发票识别: ', result.json())

    # 数字识别，图片
    from shitu_api.bin.CharacterRecognition.number import Number

    test = Number(IMG='../../testimg/number.jpeg', URLS=NUMBER_URL, API_KEY=GENERAL_API_KEY,
                  SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('数字识别：', result.json())

    # 手写文字识别
    from shitu_api.bin.CharacterRecognition.handwriting import Handwriting

    test = Handwriting(IMG='../../testimg/2.png', URLS=HANDWRITING_URL, API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('手写文字识别：', result.json())
