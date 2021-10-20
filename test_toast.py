import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName']='emulator-5554'
        desired_caps['automationName']='uiautomator2'
        desired_caps['appPackage']='io.appium.android.apis'
        desired_caps['appActivity']=".view.PopupMenu1"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        #self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        #toast 定位1：xpath方式：
        #current_name=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        #定位2：contains 包含
        current_name=self.driver.find_element_by_xpath("//*[contains(@text,'Clicked popup')]").text
        print(current_name)
        # current_name=self.driver.find_element_by_class_name("android.widget.Toast").text
        #assert current_name=="Clicked popup menu item Search"