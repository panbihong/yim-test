import time
import unittest
import HTMLTestRunner
import threading


def Atest1():
    # 测试用例存放路径
    case_path = 'E:/yim-test/Test/Case'
    # 筛选测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_xiaoxi_qunliao*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    # 运行测试用例
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'e:/report/' + 'APP功能第二轮测试结果' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='Report_description'
    )
    runner.run(suite)
    fp.close()
    # for i in range(1, 5):
    #     time.sleep(1)
    #     print(i)


def Atest2():
    # 测试用例存放路径
    case_path = 'E:/yim-test/Test/Case'
    # 筛选测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_xiaoxi_siliao*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    # 运行测试用例
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'e:/report/' + 'APP功能第二轮测试结果' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='Report_description'
    )
    runner.run(suite)
    fp.close()
    # for i in range(5, 10):
    #     time.sleep(1)
    #     print(i)


# 创建新线程
thread1 = threading.Thread(target=Atest1)
thread2 = threading.Thread(target=Atest2)

# 开始线程
thread2.start()
thread1.start()

# 等待线程结束
thread1.join()
thread2.join()
