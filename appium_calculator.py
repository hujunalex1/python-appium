#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android' #设备系统
desired_caps['platformVersion'] = '4.2' #设备系统版本
desired_caps['deviceName'] = 'Android Emulator' #设备名称
desired_caps['appPackage'] = 'com.android.calculator2' #测试app包名
desired_caps['appActivity'] = '.Calculator'  #测试appActivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动app

time.sleep(5) #启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素

driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("=").click()

time.sleep(10)
driver.quit()





