import sys
import os
import pack.download as download
import psycopg2
import pgsql.pgsql as pgsql


# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# a = None
# if not a:
#     print('ss')
#
# print(os.path.abspath("."))
# print(os.path.abspath('.').index('U'))
# print(os.path.abspath('.').rindex('U'))
# print(type('s'))
# print(type(1))
# print(isinstance(2, bool))
# print(isinstance(A(), A))
# print(isinstance(B(), A))
pgsql.connect(password="123456")
pgsql.update("delete from test where id=8")
pgsql.update("insert into test(text) values ('666')")
pgsql.update("update test set text='asasdasd' where id=12")
pgsql.commit()
print(pgsql.select("select * from test order by id asc"))
pgsql.connect_close()

# conn.commit()
# array = os.path.abspath('.').split('/')
# sysPath = sys.path
# for x in array:
#     if x not in '':
#         print(x + ' ', end='')
# print('\n')
# for x in sysPath:
#     subPaths = x.split('/')
#     for sub in subPaths:
#         if sub not in '':
#             print(sub + ' ', end='')
#     print()
# print()
# download.download('/Users/HTH/Desktop/爬图片')
