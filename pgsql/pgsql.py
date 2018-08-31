"""
@Auther: HeTongHao
@Date: 18/8/29 17:18
@Description: 访问PostgresSql 封装
"""
import psycopg2

connection = None
cursor = None


def connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432"):
    global connection
    global cursor
    try:
        connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = connection.cursor()
        print("PostgresSql------连接成功")
        return connection
    except psycopg2.Error:
        print("PostgresSql------连接失败")


def select(sql):
    """
    传入查询sql，返回所有查询到的结果
    :param sql:
    :return:
    """
    global cursor
    try:
        print("PostgresSql------Select : ", sql)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("PostgresSql------执行sql异常 : ", e.args)


def update(sql):
    """
    传入更新sql，返回受影响行数
    :param sql:
    :return:
    """
    global cursor
    try:
        print("PostgresSql------Update : ", sql)
        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print("PostgresSql------执行sql异常 : ", e.args)


def commit():
    global connection
    print("PostgresSql------事物已提交")
    connection.commit()


def connect_close():
    global connection
    print("PostgresSql------连接已关闭")
    connection.close()
