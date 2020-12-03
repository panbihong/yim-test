import unittest
from time import sleep
from Test.Tool import devices


class test_sousuo1(unittest.TestCase):

    def setUp(self):
        # 调用设备方法，启动app
        devices.shebei2(self)

    def test_case_sousuo(self):
        driver = self.driver
        # 找到搜索框点击一下
        el1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "搜索")]')
        el1.click()
        sleep(2)
        # 输入张剑锋
        el2 = driver.find_element_by_id("com.yidejia.yim.test:id/et_search")
        el2.send_keys("张剑锋")
        sleep(2)
        # 点击搜索结果中的张剑锋头像
        el3 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_avatar")
        el3.click()
        sleep(2)
        # 给张剑锋发个消息text2
        el4 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
        el4.click()
        sleep(2)
        text2 = "hahahahah哈哈哈哈哈"
        el4.send_keys(text2)
        sleep(2)
        el5 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
        el5.click()
        # 获取该会话头真名text
        el6 = driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_subtitle").text
        user = "张剑锋"
        # 对比这个人是不是张剑锋
        self.assertEqual(el6, user)

    def tearDown(self):
        self.driver.quit()
