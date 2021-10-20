import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestWebDriverwait:
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['automationName'] = 'uiautomator2'
        # noReset 保留缓存，比如登录状态
        #desired_caps['noReset']=True
        #不停止应用，直接运行测试用例
        desired_caps['dontStopAppOnReset']=True
        # 中文输入
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        desired_caps['appPackage'] = 'com.larksuite.suite'
        desired_caps['appActivity'] = "com.ss.android.lark.main.app.MainActivity"
        #desired_caps['appActivity'] = "com.ss.android.lark.guide.landing.general.ui.GuidePageActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        """
        1.点击搜索框，进行搜索成员
        2.选择搜索后的其中一个成员
        3.定位第二点contacts
        """
        #self.driver.find_element_by_id("com.larksuite.suite:id/startLoginBtn")
        # 第一次登录
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Log In']").click()

        # 切换语言为简体中文
        self.driver.find_element(By.ID,"com.larksuite.suite:id/tvChangeLanguage").click()
        self.driver.find_element(By.XPATH,"//*[@text='简体中文']").click()
        self.driver.find_element(By.XPATH,"//*[@text='Done']").click()
        self.driver.find_element(By.XPATH, "//*[@text='Switch']").click()

        # 用手机号方式进行登录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"phone number").send_keys("15001731170")
        # 勾选政策
        self.driver.find_element_by_id("com.larksuite.suite:id/checkBoxPolicy").click()
        # 点击下一步
        self.driver.find_element(By.ID,"com.larksuite.suite:id/tvNextStep").click()
        time.sleep(2)





