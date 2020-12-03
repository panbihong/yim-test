from Test.Module import sousuo
from Test.Tool import devices
from Test.Tool import mysqlconn
import unittest
from time import sleep



class test_sousuo002(unittest.TestCase):

    def setUp(self):
        devices.shebei1(self)

        sleep(5)

    def test_case_liaotian(self):
        driver=self.driver
        sql = "select step1,step2,step3,step4,step5,expectedresults from app_case where id =2"
        results = mysqlconn.select(sql)
        step1 = results[0][0]
        step2 = results[0][1]
        step3 = results[0][2]
        step4 = results[0][3]
        step5 = results[0][4]
        name1 = results[0][5]


        sousuo.sousuoModule(self,step1,step2,step3,step4,step5,name1)

        el6=driver.find_element_by_id("com.yidejia.yim.test:id/base_tv_subtitle").text
        self.assertEqual(el6,name1)



    def tearDown(self):
        self.driver.quit()


