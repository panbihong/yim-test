from Test.Tool import devices
import unittest
from time import sleep
import time

from appium.webdriver.common.touch_action import TouchAction


class TestXiaoxi4(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)
        sleep(2)


    def test_case_zhuanfa_zhutiao(self):
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

            # 收起键盘
            driver.hide_keyboard()

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss1 = el5.text
            TouchAction(driver).long_press(el5, duration=3000).wait(2000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]")
            el6.click()
            sleep(3)
            el7 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[3]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el7.click()
            el8 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[4]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el8.click()

            sleep(3)
            el10 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_by_one")
            el10.click()
            sleep(3)
            el11 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el11.click()
            sleep(3)
            el12 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_right")
            el12.click()
            sleep(3)

            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left")
            el13.click()
            sleep(5)

            el14 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el14.click()
            sleep(8)

            el15 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            el16 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"
            self.assertEqual(el15, el16)

        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)


    def test_case_zhuanfa_hebing(self):
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

            # 收起键盘
            driver.hide_keyboard()

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss1 = el5.text
            TouchAction(driver).long_press(el5, duration=3000).wait(2000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]")
            el6.click()
            sleep(3)
            el7 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[3]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el7.click()
            el8 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[4]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el8.click()

            sleep(3)
            el10 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_by_merge")
            el10.click()
            sleep(3)
            el11 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el11.click()
            sleep(3)
            el12 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_right")
            el12.click()
            sleep(3)

            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left")
            el13.click()
            sleep(5)

            el14 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "丢你咩")]')
            el14.click()
            sleep(8)

            el15 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_title")
            el16 = el15.text
            exp1 = "张英波超长超大超和陈洪秀349哈的聊天记录"
            self.assertEqual(el16, exp1)

        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)


    def test_case_zhuanfa_shoucang(self):
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

            # 收起键盘
            driver.hide_keyboard()

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss1 = el5.text
            TouchAction(driver).long_press(el5, duration=3000).wait(2000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]")
            el6.click()
            sleep(3)
            el7 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[3]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el7.click()
            el8 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup"
                "/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                ".RelativeLayout[4]/android.widget.FrameLayout[1]/android.widget.ImageView")
            el8.click()

            sleep(3)
            el10 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_by_collect")
            el10.click()
            sleep(3)

            el11 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_add_more")
            el11.click()
            sleep(3)
            el12 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "收藏")]')
            el12.click()
            sleep(3)
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_title").text
            el14 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_time").text

            exp1 = "张英波超长超大超和陈洪秀349哈的聊天记录"
            exp2 = time.strftime("%H:%M", time.localtime())
            self.assertEqual(el13, exp1)
            self.assertEqual(el14, exp2)


        # except:
        #     print("false")
        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)

    def test_case_shoucang(self):
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

            # 收起键盘
            driver.hide_keyboard()

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            ss1 = el5.text
            TouchAction(driver).long_press(el5, duration=2000).wait(1000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[6]")
            el6.click()
            sleep(3)

            el11 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_add_more")
            el11.click()
            sleep(3)
            el12 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "收藏")]')
            el12.click()
            sleep(3)
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_content").text
            el14 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_time").text

            exp1 = text2
            exp2 = time.strftime("%H:%M", time.localtime())
            self.assertEqual(el13, exp1)
            self.assertEqual(el14, exp2)


        # except:
        #     print("false")
        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)
    def test_case_shanchu(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "张英波")]')
            el1.click()
            sleep(5)


            el3 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
            el3.click()
            sleep(2)
            text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈 "

            el3.send_keys(text2)
            sleep(2)
            el4 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
            el4.click()
            sleep(2)

            # 收起键盘
            driver.hide_keyboard()

            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")

            TouchAction(driver).long_press(el5, duration=3000).wait(2000).perform()
            sleep(3)
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                ".widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[7]")
            el6.click()
            sleep(3)
            el7 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text")
            exp1 = el7.text
            # self.assertEqual(text2, exp1)
            # 已经删除了，所以他们俩不相等是正确的，用assertNotEqual
            self.assertNotEqual(text2, exp1)



        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)

    def tearDown(self):
        self.driver.quit()
