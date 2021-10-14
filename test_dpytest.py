import pytest
from appium.webdriver import webdriver


class py():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion']='6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.mkblog.www.mkbrowser'
        desired_caps['appActivity'] = 'cn.mkblog.www.mkbrowser.WebActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_dpy(self):
        print("搜索测试用例")
        """
        1  打开学习强国助手  cn.mkblog.www.mkbrowser/cn.mkblog.www.mkbrowser.WebActivity
        2  点击搜索按钮
        3  搜索python
        4  断言返回的text 中含有python
        """
        el1 = self.driver.find_element_by_id("cn.mkblog.www.mkbrowser:id/goForward")
        el1.click()
        el2 = self.driver.find_element_by_id("cn.mkblog.www.mkbrowser:id/textUrl")
        el2.click()

if __name__ == '__main__':
    pytest.main()