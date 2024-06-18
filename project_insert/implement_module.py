import allure
import pymysql
import pytest
import yaml
import copy
from datetimetr import *
from bus_active import *


def purchase_project_in(dic_a):
        key_dic = {}
        key_dic['ID'] = 'ID' + datenow_hms()
        key_dic['PID'] = 'PID' + datenow_hms()
        key_dic['DATA_STATUS'] = '0'
        key_dic['DATA_SOURCE_CODE'] = 'GO-001'
        key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
        key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
        key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
        # 采购项目ID
        key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hms()
        # 配套系统需求ID
        key_dic['ORIGIN_REQUIRE_ID'] = '2'
        # 代录需求ID
        key_dic['REQUIREMENT_PROXY_ID'] = 'REID' + datenow_hms()
        # 采购项目编号
        key_dic['PURCHASE_PROJECT_CODE'] = 'PP_CODE' + datenow_hms()
        # 采购项目名称
        key_dic['PURCHASE_PROJECT_NAME'] = 'QH测试' + datenow_hms() + '项目'
        # 采购项目类型 1 物资类 2 服务类 3 工程类
        key_dic['PURCHASE_PROJECT_TYPE'] = '1'
        # 采购单位名称
        key_dic['PURCHASE_UNIT_NAME'] = '测试采购单位名称QH'
        # 采购单位代码
        key_dic['PURCHASE_UNIT_CODE'] = 'qhtest'
        # 采购单位项目负责人
        key_dic['PURCHASE_UNIT_MANAGER'] = 'qhtest'
        # 采购单位项目负责人联系方式
        key_dic['PURCHASE_UNIT_MANAGER_TEL'] = '13723743743'
        # 采购方式 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源采购 9 其他
        key_dic['PURCHASE_MODE'] = '2'
        # 采购组织形式 1 集中采购 2 部队采购
        key_dic['PURCHASE_ORGANIZE_FORM'] = '1'
        # 供应商征集形式 1 公开征集 2有限竞争 9 其他
        key_dic['SUPPLIER_COLLECT_FORM'] = '1'
        # 采购机构名称
        key_dic['PURCHASE_AGENT_NAME'] = '测试采购机构名称'
        # 采购机构代码
        key_dic['PURCHASE_AGENT_CODE'] = '测试采购机构CODE'
        # 采购机构类型 1 采购服务站 2队属采购机构
        key_dic['AGENT_TYPE'] = '1'
        # 采购机构联系人
        key_dic['PURCHASE_AGENT_CONTACT'] = 'qhtest'
        # 采购机构联系电话
        key_dic['PURCHASE_AGENT_INFORMATION'] = '138293843743'
        # 是否远程异地评标 1 是 0 否
        key_dic['IS_REMOTE_EVALUATION'] = '0'
        # 是否不见面开标1 是 0 否
        key_dic['IS_REMOTE_OPENING'] = '0'
        # 资格审查方式 1 资格预审 2 资格后审
        key_dic['QUALIFICATION_MODE'] = '2'
        # 是否重新采购 1 是 0 否
        key_dic['IS_REBID'] = '0'
        # 重新采购原采购项目ID
        key_dic['LAST_PURCHASE_PROJECT_ID'] = ''
        # 采购项目创建时间
        key_dic['CREATE_TIME'] = dateplus_min(0)
        # 数据更新时间
        key_dic['MODI_DATE'] = dateplus_min(0)
        for key in dic_a:
            key_dic[key] = dic_a[key]
        tup_key = tuple(list(key_dic.keys()))
        tup_value = tuple(list(key_dic.values()))
        tab_name = 'purchase_project'
        sql_1 = f"INSERT INTO {tab_name}{tup_key}"
        sql_2 = sql_1.replace("'", "`")
        sql_3 = f" VALUES {tup_value}"
        sql_end = sql_2 + sql_3
        db = pymysql.connect(host='10.0.168.47',
                             port=3306, user='root',
                             password='123qwe!@#',
                             database='gld_ods_govp_new')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            # 执行sql语句
            cursor.execute(sql_end)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        db.close()
        return key_dic['PURCHASE_PROJECT_ID'], key_dic['PURCHASE_PROJECT_NAME'],  key_dic['PURCHASE_PROJECT_CODE']


def purchase_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hms()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hms()
    # 采购包编号
    key_dic['PURCHASE_SECTION_CODE'] = 'QH-' + datenow_hms()
    # 采购包名称
    key_dic['PURCHASE_SECTION_NAME'] = '测试采购包' + datenow_hms()
    # 预算汇总形式 1 清单汇总（标的有预算） 2 包预算（标的不设预算）
    key_dic['BUDGET_TOTAL_MODE'] = '1'
    # 报价价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 采购包预算
    key_dic['PURCHASE_SECTION_BUDGET'] = 3000000
    # 采购包最高限价（元）
    key_dic['LIMITED_PRICE'] = 90000000
    # 是否重新采购 1 是 0 否
    key_dic['IS_REBID'] = '0'
    # 采购包重新采购次数
    key_dic['PURCHASE_SECTION_TENDER_TIME'] = 0
    # 重新采购上一次采购包ID
    key_dic['FORMER_PURCHASE_SECTION_ID'] = ''
    # 数据更新时间
    key_dic['MODI_DATE'] = dateplus_min(0)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return [key_dic['PURCHASE_SECTION_ID'], key_dic['PURCHASE_SECTION_CODE']]

# print(purchase_section_in({'PRICE_FORM_CODE': '1'}))


def section_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购包明细ID
    key_dic['PURCHASE_SECTION_DETAIL_ID'] = 'PSD_ID' + datenow_hms()
    # 需求包明细ID
    key_dic['REQUIRE_SECTION_DETAIL_ID'] = 'RSD_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183757'
    # 采购标的序号
    key_dic['PURCHASE_OBJECT_ORDER_NO'] = 2
    # 采购标的名称
    key_dic['PURCHASE_OBJECT_NAME'] = '包1的明细'
    # 采购品目编码
    key_dic['PURCHASE_ITEM_CODE'] = 'bag0001'
    # 采购品目名称
    key_dic['PURCHASE_ITEM_NAME'] = '采购品目名称test2'
    # 采购数量
    key_dic['ITEM_NUM'] = 100
    # 计量单位
    key_dic['ITEM_UNIT'] = '个'
    # 采购明细预算金额（元）
    key_dic['ITEM_BUDGET'] = 4999999
    # 采购标的单价（元）
    key_dic['ITEM_UNIT_PRICE'] = 50000
    # 采购标的总价（元）
    key_dic['PURCHASE_OBJECT_AMOUNT'] = 5000000
    # 采购标的最高限价（元）
    key_dic['LIMITED_PRICE'] = 50000
    # 是否进口产品 1 是 0 否
    key_dic['IS_IMPORT_PRODUCT'] = '1'
    # 规格说明
    key_dic['PRODUCT_SPECIFICATION'] = '规格说明'
    # 数据更新时间
    key_dic['MODI_DATE'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['PURCHASE_SECTION_DETAIL_ID']


# print(section_detail_in({'PRODUCT_SPECIFICATION': '规格说明'}))


def purchase_open_bid_record(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 开标记录ID
    key_dic['OPEN_BID_ID'] = 'OBid' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hms()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hms()
    # 开标地点
    key_dic['BID_OPENING_ADDRESS'] = '开标地点test2'
    # 开标开始时间
    key_dic['BID_OPENING_START_TIME'] = dateplus_min(0)
    # 开标结束时间
    key_dic['BID_OPENING_END_TIME'] = dateplus_min(0)
    # 开标方式 1 线下开标 2 不见面开标
    key_dic['BID_OPEN_MODE'] = '2'
    # 参与开标供应商家数
    key_dic['SUPPLIER_NUM'] = 3
    # 开标合格进入评审供应商家数
    key_dic['QUALIFIED_SUPPLIER_NUM'] = 3
    # 是否双信封招标  1 是 0 否
    key_dic['IS_DOUBLE_ENVELOPE'] = '0'
    # 第二信封开标时间
    key_dic['SECTION_ENVELOPE_START_TIME'] = dateplus_min(0)
    # 开标结论 1 开标结束，进入评审环节 2 流标
    key_dic['BID_OPEN_RESULT'] = '2'
    # 流标原因
    key_dic['FLOW_BID_REASON'] = '流标原因1'
    # 开标流标原因类型 101 符合专业条件的供应商或者对招标文件作实质响应的供应商不足三家的
    # 102 出现影响采购公正的违法、违规行为的
    # 103 投标人的报价均超过了采购预算，采购人不能支付的
    # 104 因重大变故，采购任务取消的
    # 105 其他
    # 106 评标
    key_dic['FLOW_BID_REASON_TYPE'] = '101'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_open_bid_record'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['OPEN_BID_ID']


def purchase_supplier_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 开标记录ID
    key_dic['SUPPLIER_LIST_ID'] = 'SLid' + datenow_hms()
    # 开标记录ID
    key_dic['OPEN_BID_ID'] = 'OBid' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称3'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商名称3'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 供应商负责人
    key_dic['SUPPLIER_MANAGER'] = 'QH供应商负责人' + datenow_hms()
    # 供应商负责人联系电话
    key_dic['SUPPLIER_MANAGER_TEL'] = '13827382732'
    # 是否判定本次投标无效 1 是 0 否
    key_dic['IS_INVALID'] = '1'
    # 无效原因
    key_dic['INVALID_REASON'] = '无效原因1'
    # 投标工期描述
    key_dic['TIME_LIMIT_CONTENT'] = '一个月'
    # 投标文件解密状态 1 解密成功 2 解密失败
    key_dic['DECRY_STATUS_DOC'] = '1'
    # 投标文件解密时间
    key_dic['DECRY_DATE_DOC'] = dateplus_min(0)
    # 价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 投标报价金额（元）
    key_dic['BID_PRICE'] = 500000
    # 其他形式报价结果
    key_dic['OTHER_BID_PRICE'] = '无其他形式报价结果'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_supplier_list'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['SUPPLIER_LIST_ID']


def supplier_score_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 供应商评审汇总ID
    key_dic['SUPPLIER_SCORE_DETAIL_ID'] = 'SSD_ID' + datenow_hms()
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称3'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商名称3'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 是否无效投标 1 是 0 否
    key_dic['IS_INVALID'] = '0'
    # 无效原因
    key_dic['INVALID_REASON'] = '无效原因1'
    # 价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 最终总价形式报价（元）
    key_dic['BID_PRICE'] = 5000000
    # 其他形式最终报价结果
    key_dic['OTHER_BID_PRICE'] = '最终报价结果'
    # 技术文件的评分
    key_dic['EVALUATION_DOC_SCORE'] = 10
    # 商务文件的评分
    key_dic['BUSINESS_DOC_SCORE'] = 10
    # 投标报价得分
    key_dic['TENDER_OFFER_SCORE'] = 10
    # 信用分
    key_dic['CREDIT_SCORE'] = 40
    # 其它因素得分
    key_dic['OTHER_FACTOR_SCORE'] = 10
    # 评审结果得分
    key_dic['TOTAL_SCORE'] = '80'
    # 评审结果排序
    key_dic['SORT'] = 1
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_supplier_score_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['SUPPLIER_SCORE_DETAIL_ID']


def purchase_file_info_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 投标文件特征码ID
    key_dic['FILE_INFO_ID'] = 'FL_id' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称3'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商名称3'
    # 投标文件制作客户端安装序号
    key_dic['CLIENT_SERIAL_NUM'] = '11111110'
    # 投标（报价）文件哈希值
    key_dic['BID_FILE_HAS'] = '投标（报价）文件哈希值'
    # 投标（报价）电脑CPU序列号
    key_dic['CPU_ID'] = '电脑CPU序列号13827382732'
    # 投标（报价）电脑硬盘序列号
    key_dic['HARD_DISK_SERIAL_NUM'] = '电脑硬盘序列号21230'
    # 投标（报价）电脑网卡MAC地址
    key_dic['MAC_ADDRESS'] = '电脑网卡MAC地址21230'
    # 投标（报价）上传IP地址
    key_dic['NET_ID'] = '10.10.10l.1'
    # 投标文件大小(单位：MB)
    key_dic['FILE_SIZE'] = 112
    # 投标文件作者
    key_dic['FILE_EDITOR'] = 'atlas'
    # 投标文件页数
    key_dic['FILE_PAGES'] = 22
    # 供应商投标联系人
    key_dic['SUPPLIER_CONTACT'] = '供应商投标联系人1'
    # 投标联系人联系方式
    key_dic['SUPPLIER_CONTACT_PHONE'] = '1392938476384'
    # 投标联系人身份证件号
    key_dic['SUPPLIER_CONTACT_ID'] = '1392938476384'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_file_info'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['FILE_INFO_ID']


def evaluation_report_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 投标文件特征码ID
    key_dic['EVALUATION_EVAL_REPORT_ID'] = 'EER_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 评审方式 0结果录入 1电子统分 2线上评审 3线下评标 4远程异地评审
    key_dic['EVLUATION_MODE'] = '3'
    # 评审方法 1 综合评审法 2 质量优先法 3 最低价法
    key_dic['BID_EVALUATION_METHOD'] = '1'
    # 评审开始时间
    key_dic['BEGIIN_TIME'] = dateplus_min(-5)
    # 评审结束时间
    key_dic['END_TIME'] = dateplus_min(5)
    # 预中标供应商确定方式 1 评审委员会确定 2 采购单位确定
    key_dic['CANDIDATE_DEFINE_MODE'] = '1'
    # 评审结果 1 成功 0 失败
    key_dic['EVALUATION_RESULT'] = '1'
    # 是否修改过评审结果 1 是 0 否
    key_dic['RESULT_MODIFY_IF'] = '0'
    # 修改评审结果的原因 01资格性审查错误 02符合性审查错误 03分值汇总计算错误 04分项评分超出评分标准范围 05客观评审因素评分错误
    key_dic['RESULT_MODIFY_REASON'] = '01'
    # 重评原因类型 01评审委员会组成不符合规定 02回避评审专家未能回避 03评审专家违反工作纪律 04评审委员会及其成员独立评审受到非法干预
    key_dic['REEVALUATION_REASON'] = '01'
    # 重评原因描述
    key_dic['REEVALUATION_REASON_DETAIL'] = '重评原因test'
    # 终止评审原因 201符合专业条件的供应商或者对采购文件作实质响应的供应商不足法定数量 202出现影响采购公正的违法、违规行为 203报价均超过了采购人预算，采购人不能支付
    # 204因重大变故采购人任务取消 205文件存在不合理条款或者招标程序不符合规定 206其他
    key_dic['BID_FAILURE_REASONS'] = '201'
    # 失败原因
    key_dic['INVALID_REASON'] = '失败原因test'
    # 评审报告生成时间
    key_dic['SUBMIT_TIME'] = dateplus_min(-5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_evaluation_report'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['EVALUATION_EVAL_REPORT_ID']


def expert_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 主键
    key_dic['EXPERT_LIST_ID'] = 'EP_ID' + datenow_hms()
    # 投标文件特征码ID
    key_dic['EVAL_COMMITTEE_ID'] = 'EC_ID' + datenow_hms()
    # 评审委员会ID
    key_dic['EVAL_COMMITTEE_ID'] = 'EC_ID202308091020'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 专家（评委）类别 126002 专家 126003 采购单位代表 126005 采购机构人员
    key_dic['EXPERT_TYPE_ORIGIN'] = '126002'
    # 专家专业分类 6 物资技术 7 工程技术 8 服务技术 9 物资服务经济 10 工程经济
    key_dic['EXPERT_CLASSIFY_TYPE_ORIGIN'] = '10'
    # 专家来源 1 专家抽取系统 2 评标系统补录
    key_dic['EXPERT_SOURCE'] = '2'
    # 专家隶属 1 军队 2 地方 3库外
    key_dic['EXPERT_SUBORDINATE'] = '1'
    # 专家（评委）姓名
    key_dic['EXPERT_NAME'] = '工程经济专家1'
    # 专家（评委）身份证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['ID_CARD_TYPE'] = '2'
    # 专家（评委）身份证件号
    key_dic['ID_CARD'] = '110101198003071992'
    # 专家（评委）工作单位
    key_dic['EXPERT_UNIT'] = '专家（评委）工作单位1'
    # 专家（评委）工作单位代码
    key_dic['EXPERT_UNIT_CODE'] = '专家（评委）工作单位代码1'
    # 专家（评委）专业代码
    key_dic['EXPERT_PROFESSION_CODE'] = '专家（评委）专业代码1'
    # 专家（评委）专业名称
    key_dic['EXPERT_PROFESSION_NAME'] = '专家（评委）专业名称1'
    # 是否为评审组长 1 是 0 否
    key_dic['IS_CHAIR_MAN'] = '1'
    # 专家签到时间
    key_dic['EXPERT_CHECKIN_TIME'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_expert_list'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['EVAL_COMMITTEE_ID']


def score_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 打分细项ID
    key_dic['SCORE_DETAIL_ID'] = 'SD_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 专家姓名
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 专家身份证件号
    key_dic['ID_CARD'] = '110101198003071992'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商名称1'
    # 评审专家对技术文件的评分
    key_dic['TECHNICAL_DOC_SCORE'] = 66
    # 评审专家对商务文件的评分
    key_dic['BUSINESS_DOC_SCORE'] = 66
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_score_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['SCORE_DETAIL_ID']



def eval_committee_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 评审委员会ID
    key_dic['EVAL_COMMITTEE_ID'] = 'EC_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 委员会组建时间
    key_dic['ORG_TIME'] = dateplus_min(5)
    # 评标地点
    key_dic['EVALUATION_ADDRESS'] = 'QH评标地点1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_eval_committee'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['EVAL_COMMITTEE_ID']


def candidate_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 预中标供应商明细ID
    key_dic['CANDIDATE_ID'] = 'CD_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 预中标供应商名称
    key_dic['WINNING_CANDIDATE_NAME'] = 'QH供应商名称1'
    # 预中标供应商代码
    key_dic['WINNING_CANDIDATE_CODE'] = 'QH供应商代码1'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '1'
    # 预中标供应商排名
    key_dic['WINNING_CANDIDATE_SORT'] = 1
    # 评标价格（元）
    key_dic['BID_EVALUATION_PRICE'] = 500000
    # 价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 总价形式最终报价（元）
    key_dic['BID_PRICE'] = 500000
    # 其他形式最终报价结果
    key_dic['OTHER_BID_PRICE'] = '其他形式最终报价结果'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_candidate_list'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['CANDIDATE_ID']


def supplier_score_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 条款得分ID
    key_dic['SUPPLIER_SCORE_ITEM_ID'] = 'SS_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 专家姓名
    key_dic['EXPERT_NAME'] = '工程经济专家1'
    # 专家身份证件号
    key_dic['ID_CARD'] = '110101198003070156'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码1'
    # 评审项编号
    key_dic['EVAL_ITEM_CODE'] = '评审项编号'
    # 一级评审项/评审因素分类 100023001 资格性 100023008 符合性
    #     # 100023005 商务评审
    #     # 100023007 价格分
    #     # 100023003 技术部分（明标）
    #     # 100023014 技术部分（暗标）
    #     # 100023017 样品评审
    #     # 100023015 详细评审
    #     # 100023004 价格扣除
    #     # 100023018 样品比测
    #     # 100023010 核心产品品牌
    #     # 100023099 其他
    key_dic['EVAL_LEVEL1_ITEM'] = '100023001'
    # 二级评审项名称
    key_dic['EVAL_LEVEL2_ITEM'] = '二级评审项1'
    # 二级评审项ID
    key_dic['EVAL_LEVEL2_ID'] = '二级评审项ID1'
    # 评审打分类型 1 分值 2 合格
    key_dic['SCORE_TYPE'] = '1'
    # 二级评审项分值
    key_dic['EVAL_LEVEL2_SCORE'] = 100
    # 二级评审项是否客观评审项 1 是 0 否
    key_dic['IS_OBJECTIVE'] = '1'
    # 二级评审项得分
    key_dic['EVAL_ITEM_SCORE'] = 77
    # 二级评审项是否通过 1 通过 0 不通过
    key_dic['PASS_STATUS'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_supplier_score_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['SUPPLIER_SCORE_ITEM_ID']


def neg_offer_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 报价信息ID
    key_dic['EVALUATION_EVAL_REPORT_ID'] = 'QAM_ID20230809101807'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码1'
    # 报价轮次
    key_dic['OFFER_NUM'] = 1
    # 报价金额
    key_dic['OFFER_PRICE'] = 5000
    # 报价时间
    key_dic['OFFER_TIME'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_neg_offer'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()


def qual_after_member_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 小组成员ID
    key_dic['QUAL_AFTER_MEMBER_ID'] = 'QAM_ID' + datenow_hms()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 小组成员姓名
    key_dic['MEMBER_NAME'] = '工程经济专家1'
    # 小组成员证件号
    key_dic['MEMBER_ID_CARD'] = '110101198003071001'
    # 小组成员工作单位名称
    key_dic['MEMBER_BELONG'] = '作单位名称1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_qual_after_member'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['QUAL_AFTER_MEMBER_ID']


def win_notice_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标结果公示ID
    key_dic['WIN_NOTICE_ID'] = 'WN_ID' + datenow_hms()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 公示标题
    key_dic['WIN_NOTICE_TITLE'] = '公示标题' + datenow_hms()
    # 公示内容
    key_dic['WIN_NOTICE_CONTENT'] = '公示内容2'
    # 公示性质 1 正常公告 2 更正公告
    key_dic['WIN_NOTICE_NATURE'] = '1'
    # 公示更正次数
    key_dic['MODI_NUM'] = 2
    # 更正内容
    key_dic['MODI_CONTENT'] = '更正内容'
    # 公示发布时间
    key_dic['WIN_PUBLISH_TIME'] = dateplus_min(5)
    # 公示结束日期
    key_dic['WIN_NOTICE_END_TIME'] = dateplus_min(5)
    # 公示源URL
    key_dic['URL'] = "https://www.baidu.com/"
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_win_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['WIN_NOTICE_ID']


# print(win_notice_in({'WIN_NOTICE_CONTENT': '公示内容2'}))

def win_supplier_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标人信息ID
    key_dic['WIN_SUPPLIER_ID'] = 'WS_ID' + datenow_hms()
    # 中标结果公示ID
    key_dic['WIN_NOTICE_ID'] = 'WN_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808184758'
    # 中标（成交）供应商名称
    key_dic['WINNING_BIDDER_NAME'] = '供应商名称3'
    # 中标（成交）供应商代码
    key_dic['WINNING_BIDDER_CODE'] = '供应商代码3'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 总价形式中标价（元）
    key_dic['WIN_BID_PRICE'] = 333000
    # 其他形式中标价
    key_dic['WIN_OTHER_BID_PRICE'] = '其他形式中标价1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_win_supplier'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['WIN_SUPPLIER_ID']
    # return sql_end

# print(win_supplier_in({'WINNING_BIDDER_NAME': '供应商名称3'}))


def bid_object_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标（成交）标的明细ID
    key_dic['BID_OBJECT_DETAIL_ID'] = 'BOD_ID' + datenow_hms()
    # 中标（成交）结果公示ID
    key_dic['WIN_NOTICE_ID'] = 'WN_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808184758'
    # 中标（成交）供应商名称
    key_dic['WINNING_BIDDER_NAME'] = '供应商名称3'
    # 中标（成交）供应商代码
    key_dic['WINNING_BIDDER_CODE'] = '供应商代码3'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 标的ID
    key_dic['PURCHASE_SECTION_DETAIL_ID'] = 'PSD_ID20230815095228'
    # 标的序号
    key_dic['DORDER'] = '1'
    # 标的名称
    key_dic['GOODS_NAME'] = '标的名称1'
    # 采购品目编码
    key_dic['PUR_CATALOG_CODE'] = '采购品目编码1'
    # 品牌商标
    key_dic['BRAND'] = '品牌商标1'
    # 规格型号
    key_dic['SPEC'] = '规格型号1'
    # 统一编目码
    key_dic['GOOD_CODE'] = '统一编目码1'
    # 采购品目名称
    key_dic['PUR_CATALOG_NAME'] = '采购品目名称1'
    # 数量
    key_dic['PURCHASE_NUM'] = 20
    # 计量单位
    key_dic['UNIT'] = '个'
    # 单价（元）
    key_dic['PRICE'] = 10000
    # 总价（元）
    key_dic['TOTLE_PRICE'] = 200000
    # 标的明细要求
    key_dic['ITEM_CONTENT'] = '标的明细要求1'
    # 是否进口产品 1 是 0 否
    key_dic['IS_IMPORT_PRODUCT'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_bid_object_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['BID_OBJECT_DETAIL_ID']
    # return sql_end

# print(win_supplier_in({'WINNING_BIDDER_NAME': '供应商名称3'}))


def faliure_bid_notice_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 业务主键
    key_dic['FALIURE_BID_NOTICE_ID'] = 'FBN_ID' + datenow_hms()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808184758'
    # 废标（暂停）公示标题
    key_dic['NOTICE_TITLE'] = '废标（暂停）公示标题'
    # 废标（暂停）公示类型 1 废标 2终止采购活动 3 暂停 4 恢复
    key_dic['NOTICE_TYPE'] = '1'
    # 公示内容
    key_dic['NOTICE_CONTENT'] = '公示内容aaaaaaaaa'
    # 环节 1 开标 2 资格审查 3 评审 4 中标结果公示 9 其他
    key_dic['FALIURE_BID_LINK'] = '1'
    # 废标(暂停、取消)原因
    key_dic['FALIURE_BID_REASON'] = '废标(暂停、取消)原因'
    # 公示发布时间
    key_dic['NOTICE_START_TIME'] = dateplus_day_hms(0)
    # 公示结束时间
    key_dic['NOTICE_END_TIME'] = dateplus_day_hms(10)
    # 公示源URL
    key_dic['URL'] = 'https://www.baidu.com/'

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_faliure_bid_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['FALIURE_BID_NOTICE_ID']
    # return sql_end


# print(faliure_bid_notice_in({'URL': 'https://www.baidu.com/'}))


def rebid_project_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 流标处理ID
    key_dic['PURCHASE_REBID_ID'] = 'PR_ID' + datenow_hms()
    # 原采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 原采购项目ID
    key_dic['PURCHASE_PROJECT_CODE'] = 'PP_code'
    # 处理方式 1 重新组织采购 2 变更采购方式 3 终止
    key_dic['MANAGE_TYPE'] = '1'
    # 新采购项目ID
    key_dic['NEW_PROJECT_ID'] = 'NPJ_ID' + datenow_hms()
    # 新采购项目编号
    key_dic['NEW_PROJECT_CODE'] = 'NPJ_CODE' + datenow_hms()
    # 新采购项目名称
    key_dic['NEW_PROJECT_NAME'] = 'QH新采购项目名称' + datenow_hms()
    # 重新采购理由
    key_dic['REBID_REASON'] = '废标(暂停、取消)原因'
    # 变更的采购方式 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源采购 9 其他
    key_dic['PURCHASE_MODE_NEW'] = '2'
    # 变更理由
    key_dic['PURCHASE_MODE_REASON'] = '变更理由'
    # 终止理由
    key_dic['TERMINATION_REASON'] = '终止理由test'
    # 处理时间
    key_dic['DECIDE_DATE'] = dateplus_min(0)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_rebid_project'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['PURCHASE_REBID_ID']
    # return sql_end


# print(rebid_project_in({'TERMINATION_REASON': '终止理由test'}))


def rebid_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 流标包处理ID
    key_dic['PURCHASE_REBID_SECTION_ID'] = 'PRS_ID' + datenow_hms()
    # 流标处理ID
    key_dic['PURCHASE_REBID_ID'] = 'PR_ID'
    # 原采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_code'
    # 原采购包编号
    key_dic['PURCHASE_SECTION_CODE'] = 'PS_code'
    # 新采购包ID
    key_dic['NEW_SECTION_ID'] = 'NS_ID' + datenow_hms()
    # 新采购包编号
    key_dic['NEW_SECTION_CODE'] = 'NS_CODE' + datenow_hms()
    # 新采购包名称
    key_dic['NEW_SECTION_NAME'] = 'QH新采购包名称' + datenow_hms()
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_rebid_section'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['PURCHASE_REBID_SECTION_ID']
    # return sql_end


# print(rebid_section_in({'PURCHASE_SECTION_CODE': 'PS_code'}))


def win_note_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 通知书ID
    key_dic['WIN_NOTE_ID'] = 'WN_ID'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PS_code'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_code'
    # （未）中标通知书编号
    key_dic['NOTE_CODE'] = '（未）中标通知书编号' + datenow_hms()
    # 通知书性质 1 首次 2 更正
    key_dic['NOTE_NATURE'] = '1'
    # 采购机构名称
    key_dic['PURCHASER_AGENCY_NAME'] = '采购机构名称1'
    # 采购机构代码
    key_dic['PURCHASER_AGENCY_CODE'] = '采购机构代码1'
    # 采购单位名称
    key_dic['PURCHASE_UNIT_NAME'] = '采购单位名称1'
    # 采购单位代码
    key_dic['PURCHASE_UNIT_CODE'] = '采购单位代码1'
    # 供应商名称
    key_dic['BIDDER_NAME'] = 'QH供应商名称1'
    # 供应商代码
    key_dic['BIDDER_CODE'] = 'QH供应商名称1'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 通知书类型 1 中标通知书 0 未中标通知书
    key_dic['NOTE_TYPE'] = '1'
    # 通知书发出时间
    key_dic['ISSUE_TIME'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_win_note'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(sql_end)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()
    return key_dic['NOTE_CODE']
    # return sql_end


# print(win_note_in({'NOTE_TYPE': '1'}))