from Test.Tool import devices
import unittest
from time import sleep



class test_001(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)

        sleep(5)

    def test_case_liaotian(self):
        driver=self.driver

        sleep(8)
        el1 = driver.find_element_by_id("com.yidejia.yim.test:id/cl_item")
        el1.click()
        sleep(5)

        el2 = driver.find_element_by_id("com.yidejia.yim.test:id/et_chat_input")
        el2.click()
        sleep(5)
        text2 = "hahahahah哈哈哈哈哈"
        # text3="hehehe"
        el2.send_keys(text2)
        sleep(5)
        el3 = driver.find_element_by_id("com.yidejia.yim.test:id/iv_send")
        el3.click()
        sleep(4)
        el4 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
        print(el4)
        self.assertEqual(el4,text2)



    def tearDown(self):
        self.driver.quit()


