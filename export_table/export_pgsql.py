"""
@author HeTongHao
@date 2019/4/1 11:00
@description  
"""
import pgsql.pgsql as pgsql


def list_all_table_detail():
    # 调用postgresSql
    results = pgsql.select('''
    SELECT table_name
    ,(select description
        from pg_description
        join pg_class on pg_description.objoid = pg_class.oid
        where relname = table_name and objsubid=0)
    FROM INFORMATION_SCHEMA.tables 
    WHERE table_schema='public' AND table_type IN ('BASE TABLE')
    ''')
    return results


def list_column_detail(pg_table_name):
    # 调用postgresSql
    results = pgsql.select('''
    SELECT column_name, data_type, is_nullable
    ,(SELECT col_description((select oid from pg_class where relname=table_name), ordinal_position))
    FROM information_schema.columns as base
    WHERE table_name = \'''' + pg_table_name + '''\'
    ''')
    return results


def group_name_handle(grep_name):
    if grep_name == 'de' or grep_name == 'dev':
        return 'device'
    elif grep_name == 'pk':
        return 'parking'
    elif grep_name == 'cg':
        return 'charge'
    elif grep_name == 'sys':
        return 'system'
    elif grep_name == 'code':
        return 'common'
    else:
        return grep_name


def value_handle(value):
    if value == 'None':
        return ''
    elif value == 'bigint':
        return 'int8'
    elif value == 'integer':
        return 'int4'
    elif value == 'character varying':
        return 'varchar'
    elif value == 'timestamp without time zone':
        return 'timestamp'
    else:
        return value


def list_group_result():
    """
    获取所有数据表分组之后的结果，以表开头的前缀分组
    :return: 字典，组名:表详情对象(表名、表描述)
    """
    module_greps = {}
    for table_detail in list_all_table_detail():
        table_name = table_detail[0]
        grep_name = group_name_handle(table_name[:table_name.find('_')])  # 获取第一个_之前为组名
        if not module_greps.__contains__(grep_name):
            module_greps[grep_name] = []
        module_greps[grep_name].append(table_detail)
    return module_greps
