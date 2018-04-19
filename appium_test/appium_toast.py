#!/usr/bin/python
# -*- coding: gb18030 -*-
# -*- coding: UTF-8 -*-


from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName': 'Android',
    'deviceName': '192.168.18.101:5555',
    'platformVersion': '6.0',
    #'deviceName':'Galaxy S8',
    #'app':'C:\Users\Administrator\Desktop\com.haitao_5.9.1_591.apk',
    'appPackage': 'com.haitao',
    'appActivity': 'com.haitao.activity.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    #'automationName':'Uiautomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)

driver.find_element_by_id('android:id/button1').click()
time.sleep(5)
driver.find_element_by_id('com.haitao:id/rbDev').click() #选择dev环境
time.sleep(3)
driver.find_element_by_id('com.haitao:id/btnSubmit').click()
time.sleep(5)
driver.find_element_by_id('com.haitao:id/ib_close').click() #去掉引导页
time.sleep(15)
driver.find_element_by_id('com.haitao:id/btnClose').click()



#获取toast提示语
def is_toast_exsit(driver,text,timeout=30,poll_frequency=0.5):
    # '''is toast exist, return True or False
    # :Agrs:
    #  - driver - 传driver
    #  - text   - 页面上看到的文本内容
    #  - timeout - 最大超时时间，默认30s
    #  - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    # :Usage:
    #  is_toast_exist(driver, "看到的内容")
    # '''

    try:
        toast_loc = ("xpath",".//*[contains(@text,'%s')]"%text)
        WebDriverWait(driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False

if __name__ =='__main__':
    #按返回
    driver.back()
    print(is_toast_exsit(driver,'再按一次退出程序'))
    print('aa')





