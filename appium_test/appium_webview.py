#!/usr/bin/python
# -*- coding: gb18030 -*-
# -*- coding: UTF-8 -*-


from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': '192.168.18.101:5555',
    'platformVersion': '6.0',
    #'deviceName':'Galaxy S8',
    #'app':'C:\Users\Administrator\Desktop\com.haitao_5.9.1_591.apk',
    'appPackage': 'com.haitao',
    'appActivity': 'com.haitao.activity.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True
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


# #向上滑动屏幕
# size = driver.get_window_size()
# def swipeUp(driver,t = 500,n = 1):
#     l = size
#     x1 = l['width']*0.5
#     y1 = l['height']*0.75
#     y2 = l['height']*0.25
#     for i in range(n):
#         driver.swipe(x1,y1,x1,y2,t)
#
# if __name__ == '__main__':
#     swipeUp(driver,n = 2)
#     print('d')




# #进入首页第二个banner
# s = driver.find_elements_by_class_name('android.widget.ImageView')
# s[1].click()
# #获取页面所有环境
# contexts = driver.contexts
# print(contexts)
# #切换到webview
# driver.switch_to.context(contexts[1])
# now = driver.current_context
# print(now)
# #切换到native
# driver.switch_to.context("NATIVE_APP")
# #driver.switch_to.context(contexts[0])



#用xpath定位元素
driver.find_element_by_xpath('//*[@text="邀请好友"]').click()
print("df")

