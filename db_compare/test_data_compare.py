import copy
import time

import pytest
import yaml

from db_link_mo import *


class Test_compare():
    @pytest.mark.parametrize("input_db", yaml.safe_load(open("db_info_mongo.yml", encoding='utf-8')))
    def test_mongo_mysql(self, input_db):
        dbname = input_db['dbname'][0]
        tablename = input_db['tablename'][0]
        key_value = input_db['key_value'][0]
        res_mog = connect_64supervisor_one(dbname, tablename, key_value)
        com_data = copy.deepcopy(res_mog['data'])
        sql = input_db['sql'][0]
        res_my = connect_64_dh_mo(sql)[0]
        trans_dic_mog = {}
        trans_dic_mys = {}
        list_error_coleect = []
        right_num = 0
        for key in com_data:
            trans_dic_mog[key.lower()] = com_data[key]
        for key in res_my:
            if 'datetime.datetime' in str(type(res_my[key])):
                new_time = time.mktime(res_my[key].timetuple())
                str_time = str(round(new_time))
                trans_dic_mys[(key.replace("_", "")).lower()] = round(new_time)
                if len(str_time) != 13:
                    for i in range(13 - len(str_time)):
                        str_time = str_time + '0'
                trans_dic_mys[(key.replace("_", "")).lower()] = int(str_time)
            else:
                trans_dic_mys[(key.replace("_", "")).lower()] = res_my[key]
        for key in trans_dic_mog:
            if key in trans_dic_mys:
                if trans_dic_mog[key] == trans_dic_mys[key]:
                    right_num += 1
                else:
                    list_error_coleect = list_error_coleect + [{key: [trans_dic_mog[key], trans_dic_mys[key]]}]
            else:
                print(f"键{key}不存在于数仓数据库")
        print(f"正确字段数量是{right_num}")
        for key in trans_dic_mys:
            if key in trans_dic_mog:
                if trans_dic_mys[key] == trans_dic_mog[key]:
                    right_num += 1
                else:
                    list_error_coleect = list_error_coleect + [{key: [trans_dic_mog[key], trans_dic_mys[key]]}]
            else:
                print(f"键{key}未同步到Mongo数据库")
        print(f"不匹配字段为{list_error_coleect}")
        # print(trans_dic_mys)
        # assert len(list_error_coleect) == 0, f"不匹配字段为{list_error_coleect}"

    @pytest.mark.parametrize("input_db", yaml.safe_load(open("db_info_mongo.yml", encoding='utf-8')))
    def test_mysql_mongo(self, input_db):
        dbname = input_db['dbname'][0]
        tablename = input_db['tablename'][0]
        key_value = input_db['key_value'][0]
        res_mog = connect_64supervisor_one(dbname, tablename, key_value)
        com_data = copy.deepcopy(res_mog['data'])
        sql = input_db['sql'][0]
        res_my = connect_64_dh_mo(sql)[0]
        trans_dic_mog = {}
        trans_dic_mys = {}
        list_error_coleect = []
        right_num = 0
        for key in com_data:
            trans_dic_mog[key.lower()] = com_data[key]
        for key in res_my:
            if 'datetime.datetime' in str(type(res_my[key])):
                new_time = time.mktime(res_my[key].timetuple())
                str_time = str(round(new_time))
                trans_dic_mys[(key.replace("_", "")).lower()] = round(new_time)
                if len(str_time) != 13:
                    for i in range(13 - len(str_time)):
                        str_time = str_time + '0'
                trans_dic_mys[(key.replace("_", "")).lower()] = int(str_time)
            else:
                trans_dic_mys[(key.replace("_", "")).lower()] = res_my[key]
        for key in trans_dic_mys:
            if key in trans_dic_mog:
                if trans_dic_mys[key] == trans_dic_mog[key]:
                    right_num += 1
                else:
                    list_error_coleect = list_error_coleect + [{key: [trans_dic_mog[key], trans_dic_mys[key]]}]
            else:
                print(f"键{key}未同步到Mongo数据库")

