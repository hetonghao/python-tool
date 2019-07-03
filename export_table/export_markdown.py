"""
@author HeTongHao
@date 2019/4/1 11:00
@description  读取所有数据表,导出MarkDown文件
"""
import os
from export_table.export_pgsql import list_group_result, list_column_detail, value_handle


class ExportMarkDown:
    def __init__(self, export_path='export_dir/'):
        self.export_path = export_path

    def export(self):
        module_greps = list_group_result()  # 分组后的结果
        if not os.path.exists(self.export_path):
            os.mkdir(self.export_path)
        for grep_name in module_greps.keys():
            file_name = 'bull_' + grep_name + '模块表结构设计.md'
            f = open(self.export_path + '/' + file_name, 'w+')
            for table_detail in module_greps[grep_name]:
                add_table(f, table_detail)
            f.close()
            print(file_name + '导出成功!')
        print('-----------所有数据表结构导出完毕!')


def add_table(markdown_file, pg_table_detail):
    pg_table_name = pg_table_detail[0]
    pg_table_dec = pg_table_detail[1] if pg_table_detail[1] is not None else ''
    columns = list_column_detail(pg_table_name)
    markdown_file.write('### ' + pg_table_name + '\n\n')
    if pg_table_dec != '':
        markdown_file.write(pg_table_dec + '\n\n')
    markdown_file.write('| 字段名 | 类型 | 是否允许为空 | 描述 | \n')
    markdown_file.write('| ----- | --- | ---------- | --- | \n')
    for column in columns:
        column_values = str(column).replace('(', '').replace(')', '').split(',')
        markdown_file.write('|')
        for column_value in column_values:
            value = column_value.replace('\'', '').strip()
            value = value_handle(value)
            markdown_file.write(' ' + value + ' |')
        markdown_file.write('\n')
    markdown_file.write('\n')
