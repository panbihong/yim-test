
from time import sleep
def liaotianModule(self, step1, step2,step3,step4,jieguo1):
    driver = self.driver

    el1 = driver.find_element_by_id(step1)
    el1.click()
    sleep(5)
    el2 = driver.find_element_by_id(step2)
    el2.click()
    sleep(5)

    el2.send_keys(jieguo1)
    sleep(5)
    el3 = driver.find_element_by_id(step3)
    el3.click()
    sleep(4)


# # 退出模块
# def liaotiantuichu(self):
#     driver = self.driver
#     driver.tap([(436, 236)], 1)
#     driver.find_element_by_name(u'退出登录').click()