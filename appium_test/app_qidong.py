#!/usr/bin/python
# -*- coding: gb18030 -*-
# -*- coding: UTF-8 -*-


from appium import webdriver
import time
desired_caps = {
                'platformName':'Android',
                'deviceName':'192.168.18.101:5555',
                'platformVersion':'6.0',
                #'deviceName':'Galaxy S8',
                #'app':'C:\Users\Administrator\Desktop\com.haitao_5.9.1_591.apk',
                'appPackage':'com.haitao',
                'appActivity':'com.haitao.activity.SplashActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
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
#���������
#��1
#driver.find_element_by_id("com.haitao:id/layoutSearch").click()
#��2
loc_text = 'new UiSelector().text("����")'
t = driver.find_element_by_android_uiautomator(loc_text).get_attribute('name')
print(t)
driver.find_element_by_android_uiautomator(loc_text).click()

driver.find_element_by_id('com.haitao:id/etSearch').send_keys(u'Ůװ')
time.sleep(5)
driver.find_element_by_id("com.haitao:id/tvRight").click()

time.sleep(2)
print('d')
driver.quit()