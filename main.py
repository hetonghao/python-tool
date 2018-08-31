"""
@Auther: HeTongHao
@Date: 18/8/29 17:18
@Description: 测试启动模块
"""
import sys
import os
import reptile.todayHead as download
import pgsql.pgsql as pgsql
import mysql.mysql as mysql
import pymysql


def mysql_function():
    pymysql.connect(db="test", user="root", passwd="123456", host="127.0.0.1", port=3306)
    mysql.connect()
    print(mysql.update("insert into test(text) values('测试数据')"))
    mysql.commit()
    print(mysql.select("select * from test"))
    mysql.connect_close()


def shi_yong():
    # 实用方法
    class A:
        pass

    class B(A):
        pass

    a = None
    if not a:
        print('ss')
    print(os.path.abspath("."))
    print(os.path.abspath('.').index('U'))
    print(os.path.abspath('.').rindex('U'))
    print(type('s'))
    print(type(1))
    print(isinstance(2, bool))
    print(isinstance(A(), A))
    print(isinstance(B(), A))


def postgres():
    # 调用postgresSql
    pgsql.connect(password="123456")
    pgsql.update("delete from test where id=8")
    print(pgsql.update("insert into test(text) values ('666')"))
    print(pgsql.update("update test set text='asasdasd' where id=12"))
    pgsql.commit()
    print(pgsql.select("select * from test order by id asc"))
    pgsql.connect_close()


# postgres()


def chai_fen_path():
    # 拆分路径
    array = os.path.abspath('.').split('/')
    sysPath = sys.path
    for x in array:
        if x not in '':
            print(x + ' ', end='')
    print('\n')
    for x in sysPath:
        subPaths = x.split('/')
        for sub in subPaths:
            if sub not in '':
                print(sub + ' ', end='')
        print()
    print()


def pa_chong():
    # 调用爬虫
    download.download('/Users/HTH/Desktop/爬图片')
