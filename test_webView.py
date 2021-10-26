# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 2:01 下午
# @Author  : rainbowzhouj
# @FileName: test_webView.py
# @Software: PyCharm
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By



class TestChrome:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['platformVersion'] = '10'
        desired_caps['browserName'] = 'Chrome'
        # noReset 保留缓存，比如登录状态
        #desired_caps['noReset'] = True
        #desired_caps['autoAcceptAlerts'] = True
        desired_caps['chromedriverExecutable'] = "/Users/zhoujing/Documents/chromedriver"


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get("http://m.baidu.com")
        # time.sleep(5)
        print(self.driver.page_source)
        # alert=self.driver.switch_to.alert
        # alert.dismiss()
        # self.driver.find_element(MobileBy.ID,"index-kw").send_keys("test webView")
        # self.driver.find_element_by_accessibility_id("index-kw").click()
        # self.driver.find_element_by_accessibility_id("index-kw").send_keys("test webView")
        # self.driver.find_element(By.ID,"index-bn").click()
        # assert "test" in self.driver.page_source

