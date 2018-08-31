"""
@Auther: HeTongHao
@Date: 18/8/31 14:23
@Description: 访问MySql 封装
"""
import pymysql

connection = None
cursor = None


def connect(database="test", user="root", password="123456", host="127.0.0.1", port="3306"):
    global connection
    global cursor
    try:
        connection = pymysql.connect(db=database, user=user, passwd=password, host=host, port=int(port))
        cursor = connection.cursor()
        print("MySql------连接成功")
        return connection
    except pymysql.Error:
        print("MySql------连接失败")


def select(sql):
    """
    传入查询sql，返回所有查询到的结果
    :param sql:
    :return:
    """
    global cursor
    try:
        print("MySql------Select : ", sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except pymysql.Error as e:
        print("MySql------执行sql异常:", e.args)


def update(sql):
    """
    传入更新sql，返回受影响行数
    :param sql:
    :return:
    """
    global cursor
    try:
        print("MySql------Update : ", sql)
        cursor.execute(sql)
        return cursor.rowcount
    except pymysql.Error as e:
        print("MySql------执行sql异常 : ", e.args)


def commit():
    global connection
    print("MySql------事物已提交")
    connection.commit()


def connect_close():
    global connection
    print("MySql------连接已关闭")
    connection.close()
