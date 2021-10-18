import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Testhuadong():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion']='6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        #desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        #desired_caps['appPackage'] = 'com.android.launcher3'
        #desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        #desired_caps['appActivity'] = 'com.android.launcher3.uioverrides.QuickstepLauncher'
        desired_caps['skipServerInstallation']='true'
        #desired_caps['skipDeviceInitialization']='true'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        #cn.kmob.screenfingermovelock/com.samsung.ui.MainActivity

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_touchaction(self):
        print("点击手势密码锁")
        self.driver.find_element_by_accessibility_id("手势密码锁").click()
        self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/patternTxt").click()
        # time.sleep(3)
        print("滑动用例")
        action=TouchAction(self.driver)
        action.press(x=908,y=253).wait(200).move_to(x=551,y=262).wait(200).move_to(x=168,y=298).wait(200).move_to(x=170,y=646).release().perform()
        time.sleep(4)

