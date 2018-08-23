import sys
import os
import pack.download as download


class A:
    pass


class B(A):
    pass


a = None
if a:
    print('ss')

print(os.path.abspath("."))
print(os.path.abspath('.').index('U'))
print(os.path.abspath('.').rindex('U'))
print(type('s'))
print(type(1))
print(isinstance(2, bool))
print(isinstance(A(), A))
print(isinstance(B(), A))

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
