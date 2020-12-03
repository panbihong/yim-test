from appium.webdriver.common.touch_action import TouchAction

from Test.Tool import devices
import unittest
from time import sleep


class TestXiaoxiFasong1(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)

        sleep(5)

    def test_case_txt(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
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
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertEqual(el5, text2)

        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)

    def test_case_tupian(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
            el1.click()
            sleep(8)
            for i in range(1, 5):
                el33 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
                el33.click()
                sleep(2)
                text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"

                el33.send_keys(text2)
                sleep(2)
                el44 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
                el44.click()
                sleep(2)

            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_add_more")
            el2.click()
            sleep(2)
            el3 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "相册")]')
            el3.click()
            sleep(2)
            el4 = driver.find_element_by_id("com.yidejia.yim.test:id/tvCheck")
            el4.click()
            sleep(2)
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/picture_send")
            el5.click()
            sleep(2)
            sou = driver.find_element_by_id("com.yidejia.yim.test:id/tv_img")
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertIsNotNone(sou)

            # 收起键盘
            # driver.hide_keyboard()


        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_shipin(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
            el1.click()
            sleep(8)
            for i in range(1, 5):
                el33 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
                el33.click()
                sleep(2)
                text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"

                el33.send_keys(text2)
                sleep(2)
                el44 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
                el44.click()
                sleep(2)

            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_add_more")
            el2.click()
            sleep(2)
            el3 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "拍摄")]')
            el3.click()
            sleep(2)
            el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                                               ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout["
                                               "2]/android.view.View[2]")

            TouchAction(driver).long_press(el4, duration=8000).wait(3000).perform()
            sleep(3)
            el5 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View[2]")
            el5.click()
            sleep(3)
            sou2 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_duration")
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertIsNotNone(sou2)


        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_yuyin(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
            el1.click()
            sleep(8)
            for i in range(1, 5):
                el33 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
                el33.click()
                sleep(2)
                text2 = "这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈这是一条自动留言哈哈哈哈哈"

                el33.send_keys(text2)
                sleep(2)
                el44 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
                el44.click()
                sleep(2)
            # 收起键盘
            driver.hide_keyboard()
            sleep(2)
            el2 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_voice")
            el2.click()
            sleep(2)
            el4 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_voice_input")
            TouchAction(driver).long_press(el4, duration=8000).wait(3000).perform()
            sleep(3)

            sou2 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_voice")
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertIsNotNone(sou2)


        finally:
            sleep(5)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(5)

    def test_case_emoji(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
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
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_emoji_board")
            el5.click()

            el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.RelativeLayout/android.view"
                                               ".ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.widget.LinearLayout/android"
                                               ".widget.HorizontalScrollView/android.widget.LinearLayout/androidx"
                                               ".appcompat.app.ActionBar.Tab["
                                               "1]/android.widget.LinearLayout/android.widget.ImageView")
            el6.click()

            el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.RelativeLayout/android.view"
                                               ".ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                               ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                               "1]/android.widget.ImageView")
            el7.click()
            sleep(1)
            el7.click()
            sleep(1)
            el7.click()
            sleep(1)
            el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.RelativeLayout/android.view"
                                               ".ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                               ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                               "2]/android.widget.ImageView")

            el8.click()
            sleep(1)
            el8.click()
            sleep(1)
            el8.click()
            sleep(2)
            el9 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
            el9.click()
            sleep(2)
            # 点击一下输入框再收起键盘
            el33 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_voice")
            el33.click()
            sleep(2)


            el10 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.RelativeLayout/android.view"
                                                ".ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup"
                                                "/android.view.ViewGroup/android.widget.RelativeLayout["
                                                "5]/android.widget.LinearLayout/android.widget.RelativeLayout/android"
                                                ".widget.TextView")
            el11 = el10.text
            text2 = "[微笑][微笑][微笑][撇嘴][撇嘴][撇嘴]"

            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertEqual(el11, text2)

        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)

    def test_case_biaoqing(self):
        try:
            driver = self.driver
            el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "智能云官方交流群")]')
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
            el5 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_emoji_board")
            el5.click()

            el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.RelativeLayout/android.view"
                                               ".ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.widget.LinearLayout/android"
                                               ".widget.HorizontalScrollView/android.widget.LinearLayout/androidx"
                                               ".appcompat.app.ActionBar.Tab["
                                               "2]/android.widget.LinearLayout/android.widget.ImageView")
            el6.click()
            el7 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.ImageView")
            el7.click()

            sleep(2)
            # 收起键盘
            driver.hide_keyboard()

            el10 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_img")
            el13 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_read")
            self.assertIsNotNone(el13)
            self.assertIsNotNone(el10)

        finally:
            sleep(2)
            driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_left").click()
            sleep(2)

    def tearDown(self):
        self.driver.quit()
