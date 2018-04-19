#!/usr/bin/python
# -*- coding: gb18030 -*-
# -*- coding: UTF-8 -*-


from appium import webdriver
#import time
desired_caps = {
    'platformName': 'Android',
    # 'deviceName': '192.168.18.101:5555',
    # 'platformVersion': '6.0',
    # #'deviceName':'Galaxy S8',
    # 'appPackage': 'com.sec.android.app.popupcalculator',
    # 'appActivity': 'com.sec.android.app.popupcalculator.Calculator'

    'deviceName': 'Android Emulator',
    'platformVersion': '4.2',
    'app':'C:\Windows\System32\node_modules\appium\sample-code\apps\ContactManager',
    'appPackage': 'com.example.android.contactmanager',
    'appActivity': '.ContactManager'


    #'unicodeKeyboard': True,
    #'resetKeyboard': True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

