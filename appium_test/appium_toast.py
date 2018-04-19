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
driver.find_element_by_id('com.haitao:id/rbDev').click() #ѡ��dev����
time.sleep(3)
driver.find_element_by_id('com.haitao:id/btnSubmit').click()
time.sleep(5)
driver.find_element_by_id('com.haitao:id/ib_close').click() #ȥ������ҳ
time.sleep(15)
driver.find_element_by_id('com.haitao:id/btnClose').click()



#��ȡtoast��ʾ��
def is_toast_exsit(driver,text,timeout=30,poll_frequency=0.5):
    # '''is toast exist, return True or False
    # :Agrs:
    #  - driver - ��driver
    #  - text   - ҳ���Ͽ������ı�����
    #  - timeout - ���ʱʱ�䣬Ĭ��30s
    #  - poll_frequency  - �����ѯʱ�䣬Ĭ��0.5s��ѯһ��
    # :Usage:
    #  is_toast_exist(driver, "����������")
    # '''

    try:
        toast_loc = ("xpath",".//*[contains(@text,'%s')]"%text)
        WebDriverWait(driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False

if __name__ =='__main__':
    #������
    driver.back()
    print(is_toast_exsit(driver,'�ٰ�һ���˳�����'))
    print('aa')





