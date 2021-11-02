# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 5:53 下午
# @Author  : rainbowzhouj
# @FileName: test_contact.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.common.by import By


class TestContact:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator",
            "emulator": "uiautomator2",
            "appPackage": "com.larksuite.suite",
            "appActivity": "com.ss.android.lark.main.app.MainActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def testcontact(self):
        self.driver.find_element(By.ID, "com.larksuite.suite:id/contact_tab").click()
        self.driver.find_element(By.ID, "com.larksuite.suite:id/tv_department_header").click()
        # self.driver.find_element(By.ID,"com.larksuite.suite:id/tv_department_header").click()
        self.driver.find_element_by_id("com.larksuite.suite:id/tv_contact_department_invite").click()

        self.driver.find_element(By.XPATH, "//*[@text='输入手机号']").click()
        self.driver.find_element_by_id("com.larksuite.suite:id/immMobileInputEt").send_keys('13700000002')
        self.driver.find_element_by_id("com.larksuite.suite:id/immNameInputEt").send_keys('test_zhouj')
        self.driver.find_element_by_id("com.larksuite.suite:id/immInviteMembersBtn").click()
        assert "邀请已发送" in self.driver.page_source

    def teardown(self):
        self.driver.quit()
