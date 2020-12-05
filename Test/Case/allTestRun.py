import time
import unittest
import HTMLTestRunner


# 获取所有测试用例
def get_allcase():
    # 测试用例存放路径
    case_path = '//Test/Case'
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_xiao*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == '__main__':
    # 运行测试用例
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'e:/report/' + 'APP功能第二轮测试结果' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='Report_description'
    )
    runner.run(get_allcase())
    fp.close()

