from time import sleep

def sousuoModule(self, step1, step2,step3,step4,step5,name1):
    driver = self.driver
    # 找到搜索框点击一下
    el1 = driver.find_element_by_xpath(step1)
    el1.click()
    sleep(2)
    # 输入name1
    el2 = driver.find_element_by_id(step2)
    el2.send_keys(name1)
    sleep(2)
    # 点击搜索结果中的name1头像
    el3 = driver.find_element_by_id(step3)
    el3.click()
    sleep(2)
    # 给name1发个消息name1
    el4 = driver.find_element_by_id(step4)
    el4.click()
    sleep(2)

    el4.send_keys(name1)
    sleep(2)
    el5 = driver.find_element_by_id(step5)
    el5.click()




