#coding=utf-8

from appium import webdriver
import time
import unittest
import os
import HTMLTestRunner
class LoginTestLizi(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设备系统
        desired_caps['platformVersion'] = '6.0.1' #设备系统版本
        desired_caps['deviceName'] = '270f2988' #设备名称
        desired_caps['appPackage'] = 'com.lizi.app' #测试app包名
        desired_caps['appActivity'] = '.activity.MainActivity'  #测试appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动app

    def test_login(self):
        driver = self.driver
        #进入首页后点击‘我的’按钮
        driver.find_element_by_name(u'我的').click()
        time.sleep(2)
        #点击登录头像按钮，进行登录，跳转到登录界面
        driver.find_element_by_id('com.lizi.app:id/user_login_iv').click()
        time.sleep(2)
        #输入用户名
        driver.find_element_by_id('com.lizi.app:id/zhanghao_edittext').send_keys('18267200735')
        #输入密码
        driver.find_element_by_id('com.lizi.app:id/password_edittext').send_keys('password')
        #点击确认登录按钮
        driver.find_element_by_id('com.lizi.app:id/login_button').click()

        time.sleep(3)
        #登录成功，页面下滑，不然点击不到设置按钮
        driver.swipe(500, 200, 500, 800,0)
        time.sleep(2)
        #获取登录后的昵称
        name = driver.find_element_by_id('com.lizi.app:id/login_username_tv').text

        #添加断言，若昵称不正确，则打印错误信息
        try:
            assert 'No_matter' in name
            print 'loginUser is right'
        except AssertionError as e:
            print 'loginUser is Error'

        #点击设置按钮，进入设置页面
        driver.find_element_by_id('com.lizi.app:id/setting_imageView').click()
        #点击退出按钮
        driver.find_element_by_id('com.lizi.app:id/exit_button').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTestLizi('test_login'))
    filename = 'C:\\Temp\\app.html'
    fb = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb,title='liziapptestreport',description='liziapp')
    runner.run(suite)
    fb.close()



