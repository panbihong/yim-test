from Test.Tool import devices
import unittest
from time import sleep
from Test.Tool import mysqlconn
from appium.webdriver.common.touch_action import TouchAction


class TestXiaoxi3(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)

        sleep(5)

    def test_case_fuzhi(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "张英波")]')
            el1.click()
            sleep(5)
            for i in range(1, 4):
                el33 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
                el33.click()
                sleep(2)
                text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"

                el33.send_keys(text2)
                sleep(2)
                el44 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
                el44.click()
                sleep(2)

            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            TouchAction(driver).long_press(el2, duration=3000).wait(2000).perform()
            sleep(3)
            el3 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
            el3.click()
            sleep(3)
            el4 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
            el4.click()
            sleep(3)
            TouchAction(driver).long_press(el4, duration=2000).wait(2000).perform()
            sleep(3)
            TouchAction(driver).tap(x=124, y=880).perform()
            # ss = driver.getClipboardText()
            ss = el2.text
            sleep(3)
            # el4.click()
            # el4.send_keys(ss)
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
            el5.click()
            sleep(3)
            el6 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            self.assertEqual(el6, ss)
        # except:
        #     print("false")
        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_huifu(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "张英波")]')
            el1.click()
            sleep(5)

            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            TouchAction(driver).long_press(el2, duration=3000).wait(2000).perform()
            sleep(3)
            el3 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]")
            el3.click()
            sleep(3)
            el4 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
            el4.click()
            ss2 = "自动回复"
            el4.send_keys(ss2)
            sleep(3)
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
            el5.click()
            sleep(3)
            el6 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            el7 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_reply").text
            ss3 = el2.text
            self.assertEqual(el7, ss2)
            self.assertEqual(el6, ss3)

        # except:
        #     print("false")
        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_zhuanfa(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "张英波")]')
            el1.click()
            sleep(5)

            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss4 = el2.text
            TouchAction(driver).long_press(el2, duration=3000).wait(2000).perform()
            sleep(3)
            el3 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]")
            el3.click()
            sleep(3)
            el4 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el4.click()
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_right")
            el5.click()
            sleep(3)

            el6 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left")
            el6.click()
            sleep(5)

            el8 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el8.click()
            sleep(5)

            el9 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            self.assertEqual(el9, ss4)

        # except:
        #     print("false")
        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_chehui(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "张英波")]')
            el1.click()
            sleep(5)

            for i in range(1, 5):
                el3 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
                el3.click()
                sleep(2)
                text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"

                el3.send_keys(text2)
                sleep(2)
                el4 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
                el4.click()
                sleep(2)

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss7 = el5.text
            # 收起键盘
            driver.hide_keyboard()
            TouchAction(driver).long_press(el5, duration=3000).wait(2000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]")
            el6.click()
            sleep(3)
            el7 = driver.find_element_by_id('com.yidejia.yim.test:id/tv_msg_tip')
            # el7 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "重新编辑")]')
            ss8 = el7.text
            # el7.click()
            # el8 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
            # el8.click()
            # sleep(3)

            el9 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            el10 = "你撤回了一条消息 重新编辑"

            self.assertEqual(el10, ss8)
            # self.assertEqual(el9, ss7)

        # except:
        #     print("false")
        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def tearDown(self):
        self.driver.quit()
