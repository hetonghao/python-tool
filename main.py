"""
@Auther: HeTongHao
@Date: 18/8/29 17:18
@Description: 测试启动模块
"""
import sys
import os
import reptile.todayHead as download
import mysql.mysql as mysql
from school.people import People, Student
import pgsql.pgsql as pg_sql
from export_table.export_markdown import ExportMarkDown
from export_table.export_word import ExportWord

test_path = '/Users/HTH/Desktop/docx/'
git_project_docs_path = '/Users/HTH/IdeaProject/docs/backend/数据库表设计/'


def main():
    try:
        pg_sql.connect('bull', 'bull', 'vvAFXHrxKe672Rc*Y43T*Fv4wPkrxTiV', 'pgm-wz9006t1oky2042t3o.pg.rds.aliyuncs.com',
                       3432)  # 开启连接
        export_markdown = ExportMarkDown(test_path)
        export_word = ExportWord(test_path)
        export_markdown.export()
        export_word.export()
    finally:
        pg_sql.connect_close()


def school_show():
    p = People("何同昊", 22)
    p.show()
    p = Student("何同昊", 22, 1)
    p.show()


# school_show()


def mysql_function():
    mysql.connect()
    # print(mysql.update("insert into test(text) values('测试数据2')"))
    # mysql.commit()
    data = mysql.select("select id,text from test")
    for item in data:
        print("id:%d\t text: %s" % (item[0], item[1]))
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
    pg_sql.connect(password="123456")
    pg_sql.update("delete from test where id=8")
    print(pg_sql.update("insert into test(text) values ('666')"))
    print(pg_sql.update("update test set text='asasdasd' where id=12"))
    pg_sql.commit()
    print(pg_sql.select("select * from test order by id asc"))
    pg_sql.connect_close()


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


main()
