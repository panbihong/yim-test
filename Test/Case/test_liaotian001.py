from Test.Module import liaotian
from Test.Tool import devices
import unittest
from time import sleep
from Test.Tool import mysqlconn



class test_liaotian001(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)

        sleep(5)

    def test_case_liaotian(self):
        driver=self.driver
        sql = "select step1,step2,step3,step4,expectedresults from app_case where id =1"
        results = mysqlconn.select(sql)
        step1 = results[0][0]
        step2 = results[0][1]
        step3 = results[0][2]
        step4 = results[0][3]
        # method = results[0][4]
        jieguo1 = results[0][4]

        liaotian.liaotianModule(self,step1,step2,step3,step4,jieguo1)

        el4 = driver.find_element_by_id("com.yidejia.yim.test:id/tv_text").text
        self.assertEqual(el4,jieguo1)



    def tearDown(self):
        self.driver.quit()


