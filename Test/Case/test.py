# import time
#
# from Test.Tool import mysqlconn
#
#
# # sql="select * from app_case where id >0"
# #
# #
# # a=mysqlconn.select(sql)
# #
# # for row in a:
# #     print(row)
# # 格式化成2016-03-20 11:45:39形式
# print (time.strftime("%H:%M", time.localtime()))

from pywinauto.application import Application
app = Application(backend="uia").start("notepad.exe")


# sql = "select step1,step2,step3,step4,method_id,expectedresults from app_case where id =1"
# results = mysqlconn.select(sql)
# step1 = results[0][0]
# step2 = results[0][1]
# step3 = results[0][2]
# step4 = results[0][3]
# method = results[0][4]
# exp1 = results[0][5]
#
# print(step1)
# print(step2)
# print(step3)
# print(step4)
# print(method)
# print(exp1)



