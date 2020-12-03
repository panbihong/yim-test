import pymysql


def select(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "test888888", "testcase")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return results
    db.close()


def insert(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "test888888", "testcase")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

def update(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "test888888", "testcase")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()
def delect(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "test888888", "testcase")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()
