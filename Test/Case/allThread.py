import time
import unittest
import HTMLTestRunner
import threading

exitFlag = 0


class allThresd(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        runner.run(Atest1())
        runner.run(Atest2())


def Atest1():
    # 测试用例存放路径
    case_path = 'E:/untitled1/Test/Case'
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_xiaoxi_qunliao*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


def Atest2():
    # 测试用例存放路径
    case_path = 'E:/untitled1/Test/Case'
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_xiaoxi_siliao*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    # 创建新线程
    thread1 = allThresd(1, "Thread-1", 1)
    thread2 = allThresd(2, "Thread-2", 2)

    # 运行测试用例
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'e:/report/' + 'APP功能第二轮测试结果' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='Report_description'
    )
    # 开始线程
    thread1.start()
    thread2.start()
    # 等待线程结束
    thread1.join()
    thread2.join()
    # 关闭文件
    fp.close()
