import pymongo
import pymysql


def connect_64supervisor_one(dbname, tablename, key_value):
    # 监管64库连接
    client = pymongo.MongoClient('mongodb://10.0.104.224:27017')
    db = client[dbname]
    collection = db[tablename]
    res = collection.find_one(key_value)
    # res = collection.find_one({'data.yearProjectId': 'QUTEST20230725'})
    # for i in res:
    #     list_64.append(i)
    return res


def connect_mongo_in_one_64(tablename, in_dic):
    client = pymongo.MongoClient('mongodb://10.0.104.224:27017')
    db = client['dc_20230719']
    collection = db[tablename]
    res = collection.insert_one(in_dic)
    return res


def connect_mongo_in_one_85(tablename, in_dic):
    client = pymongo.MongoClient('mongodb://10.10.10.85:27017')
    db = client['dc_20230810']
    collection = db[tablename]
    res = collection.insert_one(in_dic)
    print(res)


def connect_64supervisor_all(dbname, tablename, key_value):
    # 监管64库连接
    client = pymongo.MongoClient('mongodb://10.0.104.224:27017')
    db = client[dbname]
    collection = db[tablename]
    res = collection.find(key_value)
    # res = collection.find_one({'data.yearProjectId': 'QUTEST20230725'})
    for i in res:
        print(i)


def connect_64_dh_mo(sql):
    # 数仓连接
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql_1 = "SELECT * FROM purchase_plan_year_new where year_project_id ='QUTEST20230725'"
    cursor.execute(sql)
    all_data = cursor.fetchall()
    db.close()
    return all_data


def connect_mysql_mo(dbname, sql):
    # 数仓连接
    db = pymysql.connect(dbname)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql_1 = "SELECT * FROM purchase_plan_year_new where year_project_id ='QUTEST20230725'"
    cursor.execute(sql)
    all_data = cursor.fetchall()
    db.close()
    return all_data

def connect_mysql_dh():
    # 数仓连接
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp')
    return db



# connect_64supervisor_one('dc_20230719', 'SU_SS_T_PURCHASE_PLAN_YEAR_NEW', {'data.yearProjectId': 'QUTEST20230725'})
# print(connect_64supervisor_one('dc_20230719', 'SU_SS_T_PURCHASE_PLAN_QUAR_NEW',
#                                {'data.quarProjectId': 'E3702002313012100725'}))

# print(connect_64supervisor_one('dc_20230719', 'SU_SS_T_PURCHASE_DEMONSTRATION_NEW',
#                                {'data.createUserId': 'qh072609'}))

# print(connect_64supervisor_one('dc_20230719', 'SU_SS_T_PURCHASE_DEMONSTRATION_DETAIL_NEW',
#                                {'uid': 'c5b5938f3748e893983211ea5021bb5e'}))

# print(connect_64supervisor_one('dc_20230719', 'SU_SS_T_PURCHASE_PLAN_MERGE',
#                                {'data.id': '67c9935b819e44c1a2eb9ye223072610'}))


# sql_1 = 'SELECT * FROM purchase_plan_quar_new'
# sql_2 = "SELECT * FROM purchase_plan_year_new where year_project_id ='QUTEST20230725'"
# sql_3 = "SELECT * FROM purchase_plan_quar_new where year_project_id ='QHTEST202307251413'"
# sql_4 = "SELECT * FROM purchase_demonstration_new where id ='5'"
# sql_5 = "SELECT * FROM purchase_demonstration_detail_new where id ='2'"
# sql_6 = "SELECT * FROM purchase_plan_merge where id ='67c9935b819e44c1a2eb9ye223072610'"
# print(connect_64_dh_mo(sql_5))
