import allure
import pymysql
import pytest
import yaml
import copy
from .datetimetr import *
from .bus_active import *


# 采购需求初核
def purchase_requirment_first_approval_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 需求初核ID
    key_dic['REQUIRMENT_FIRST_APPROVAL_ID'] = 'RFA_ID' + datenow_hmsf()
    # 配套系统需求ID
    key_dic['ORIGIN_REQUIRE_ID'] = 'OREID' + datenow_hmsf()
    # 代录需求ID
    key_dic['REQUIREMENT_PROXY_ID'] = 'RP_ID' + datenow_hmsf()
    # 需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 任务性质
    key_dic['TASK_NATURE'] = '任务性质1'
    # 初核时间
    key_dic['FIRST_APPROVAL_COMPLETED_TIME'] = dateplus_min(5)
    # 初核结论 1 通过 0 不通过，退回采购需求
    key_dic['FIRST_APPROVAL_CONCLUSION'] = '1'
    # 承办人
    key_dic['OPERATOR_NAME'] = '承办人'
    # 承办人联系电话
    key_dic['OPERATOR_PHONE'] = '承办人联系电话'
    # 初核的采购机构
    key_dic['PURCHASE_AGENT_NAME'] = '初核的采购机构'
    # 采购机构代码
    key_dic['PURCHASE_AGENT_CODE'] = '采购机构代码'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    key_dic['FIRST_APPROVAL_COMPLETED_TIME'] = dateplus_day_hms(key_dic['FIRST_APPROVAL_COMPLETED_TIME'])
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_requirment_first_approval'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['REQUIRMENT_FIRST_APPROVAL_ID'], key_dic['ORIGIN_REQUIRE_ID'], key_dic['REQUIREMENT_PROXY_ID']


# 采购需求初核内容
def purchase_requirment_first_approval_content(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 初核内容ID
    key_dic['FIRST_APPROVAL_CONTENT_ID'] = 'RFA_ID' + datenow_hmsf()
    # 需求初核ID
    key_dic['REQUIRMENT_FIRST_APPROVAL_ID'] = 'RFA_ID'
    # 序号
    key_dic['ORDER_NO'] = 1
    # 初核内容
    key_dic['FIRST_APPROVAL_CONTENT'] = '初核内容'
    # 初核情况 1 通过 0 不通过
    key_dic['FIRST_APPROVAL_RESULT'] = '1'
    # 不通过说明
    key_dic['FAIL_DESC'] = '不通过说明'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_requirment_first_approval_content'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 任务分配
def purchase_task_assign_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 业务主键
    key_dic['TASK_ASSIGN_ID'] = 'TA_ID' + datenow_hmsf()
    # 配套系统需求ID
    key_dic['ORIGIN_REQUIRE_ID'] = 'RFA_ID'
    # 代录需求ID
    key_dic['REQUIREMENT_PROXY_ID'] = 'RFA_ID'
    # 负责制类型 1 项目负责制负责 2 分段负责制
    key_dic['MANAGING_TYPE'] = '1'
    # 负责人类型 1 需求复核负责人 2 项目负责人 3 采购文件编制负责人 4 公告负责人 5 开标负责人 6 评审负责人 7 合同履约负责人 8.采购需求审核负责人
    key_dic['MANAGER_TYPE'] = '1'
    # 负责人ID
    key_dic['MANAGER_ID'] = '负责人ID1'
    # 负责人名称
    key_dic['MANAGER_NAME'] = '负责人名称1'
    # 负责人电话
    key_dic['MANAGER_PHONE'] = '负责人电话1'
    # 负责人证件号
    key_dic['MANAGER_ID_NO'] = '负责人证件号1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_task_assign'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购需求复核信息
def purchase_requirment_review_approval_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 需求复核ID
    key_dic['REQUIRMENT_REVIEW_APPROVAL_ID'] = 'RFA_ID' + datenow_hmsf()
    # 配套系统需求ID
    key_dic['ORIGIN_REQUIRE_ID'] = 'RFA_ID'
    # 代录需求ID
    key_dic['REQUIREMENT_PROXY_ID'] = 'RFA_ID'
    # 需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 复核时间
    key_dic['REVIEW_APPROVAL_COMPLETED_TIME'] = dateplus_min(5)
    # 需求复核方式 1 内部评估 2 专家论证 3 采购平台公开征求意见 9 其他方式
    key_dic['REVIEW_TYPE'] = '1'
    # 需求复核发现的问题
    key_dic['REVIEW_QUESTION'] = '需求复核发现的问题1'
    # 意见建议
    key_dic['REVIEW_ADVICE'] = '意见建议1'
    # 复核结论_采购单位是否需要调整采购需求 1 是 0 否
    key_dic['REVIEW_RESULT'] = '0'
    # 承办人
    key_dic['OPERATOR_NAME'] = '承办人1'
    # 承办人联系电话
    key_dic['OPERATOR_PHONE'] = '承办人联系电话1'
    # 复核的采购机构
    key_dic['PURCHASE_AGENT_NAME'] = '复核的采购机构1'
    # 采购机构代码
    key_dic['PURCHASE_AGENT_CODE'] = '采购机构代码1'
    # 复核部门
    key_dic['REVIEW_DEPT_NAME'] = '复核部门1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    key_dic['REVIEW_APPROVAL_COMPLETED_TIME'] = dateplus_day_hms(key_dic['REVIEW_APPROVAL_COMPLETED_TIME'])
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_requirment_review_approval'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['REQUIRMENT_REVIEW_APPROVAL_ID']


# 采购需求复核内容
def purchase_requirment_review_approval_content_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 复核内容ID
    key_dic['REVIEW_APPROVAL_CONTENT_ID'] = 'RAC_ID' + datenow_hmsf()
    # 需求复核ID
    key_dic['REQUIRMENT_REVIEW_APPROVAL_ID'] = 'RRA_ID'
    # 序号
    key_dic['ORDER_NO'] = 1
    # 复核内容分组
    key_dic['REVIEW_APPROVAL_CONTENT_GROUP'] = '复核内容分组'
    # 复核内容
    key_dic['REVIEW_APPROVAL_CONTENT'] = '复核内容'
    # 复核情况 1 通过 0 不通过
    key_dic['REVIEW_APPROVAL_RESULT'] = '1'
    # 不通过说明
    key_dic['FAIL_DESC'] = '不通过说明'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_requirment_review_approval_content'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 征求意见公告
def purchase_opinion_announcement_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 主键
    key_dic['OPINION_ANNOUNCEMENT_ID'] = 'OPA_ID' + datenow_hmsf()
    # 配套系统需求ID
    key_dic['ORIGIN_REQUIRE_ID'] = 'ORE_ID'
    # 代录需求ID
    key_dic['REQUIREMENT_PROXY_ID'] = 'REP_ID'
    # 公告标题
    key_dic['ANNOUNCEMENT_TITLE'] = '公告标题1'
    # 公示时间起
    key_dic['ANNOUNCEMENT_START_TIME'] = dateplus_min(15)
    # 公示时间止
    key_dic['ANNOUNCEMENT_END_TIME'] = dateplus_min(-15)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_opinion_announcement'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['OPINION_ANNOUNCEMENT_ID']


# 征求意见公告反馈内容
def annoucement_feedback_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 复核内容ID
    key_dic['OPINION_ANNOUNCEMENT_FEEDBACK_ID'] = 'OPAF_ID' + datenow_hmsf()
    # 征求意见公告ID
    key_dic['OPINION_ANNOUNCEMENT_ID'] = 'OPA_ID'
    # 序号
    key_dic['ORDER_NO'] = 1
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 统一社会信用代码
    key_dic['SUPPLIER_CODE'] = '统一社会信用代码1'
    # 联系人
    key_dic['CONTACT'] = '联系人1'
    # 联系电话
    key_dic['INFORMATION'] = '13263745743'
    # 意见反馈
    key_dic['CONTENT'] = '意见反馈1'
    # 反馈时间
    key_dic['FEEDBACK_TIME'] = dateplus_min(5)
    # 附件
    key_dic['FILE_URL'] = 'http://10.0.168.64/supervision-web/#/login'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_opinion_announcement_feedback'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


def purchase_project_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 配套系统需求ID
    key_dic['ORIGIN_REQUIRE_ID'] = '2'
    # 代录需求ID
    key_dic['REQUIREMENT_PROXY_ID'] = 'REID' + datenow_hmsf()
    # 采购项目编号
    key_dic['PURCHASE_PROJECT_CODE'] = 'PP_CODE' + datenow_hmsf()
    # 采购项目名称
    key_dic['PURCHASE_PROJECT_NAME'] = 'QH测试' + datenow_hmsf() + '项目'
    # 采购项目类型 1 物资类 2 服务类 3 工程类
    key_dic['PURCHASE_PROJECT_TYPE'] = '1'
    # 采购内容
    key_dic['PURCHASE_PROJECT'] = '采购内容' + datenow_hmsf()
    # 是否SM 1 SM项目 0 非SM项目
    key_dic['SECRET_IF'] = '1'
    # 医疗设备状态 0 否 1 是
    key_dic['MEDICAL_EQUIPMENT_STATUS'] = '0'
    # 项目组织模式 1 内网本地模式 2 内网本地(不见面)模式[灰的] 3 内网云平台模式 4 内网云平台(不见面)模式[灰的] 5外网云平台模式
    key_dic['MEDICAL_EQUIPMENT_STATUS'] = '1'
    # 采购单位名称
    key_dic['PURCHASE_UNIT_NAME'] = '测试采购单位名称QH'
    # 采购单位代码
    key_dic['PURCHASE_UNIT_CODE'] = 'qhtest'
    # 采购单位项目负责人
    key_dic['PURCHASE_UNIT_MANAGER'] = 'qhtestunit'
    # 采购单位项目负责人联系方式
    key_dic['PURCHASE_UNIT_MANAGER_TEL'] = '13723743743'
    # 采购方式 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源采购 9 其他
    key_dic['PURCHASE_MODE'] = '2'
    # 采购组织形式 1 集中采购 2 部队采购
    key_dic['PURCHASE_ORGANIZE_FORM'] = '1'
    # 供应商征集形式 1 公开征集（资格后审） 2有限竞争 3有限竞争、公开征集（资格预审） 9 其他
    key_dic['SUPPLIER_COLLECT_FORM'] = '1'
    # 采购机构名称
    key_dic['PURCHASE_AGENT_NAME'] = '测试采购机构名称'
    # 采购机构代码
    key_dic['PURCHASE_AGENT_CODE'] = '测试采购机构CODE'
    # 采购机构类型 1 采购服务站 2队属采购机构
    key_dic['AGENT_TYPE'] = '1'
    # 采购机构联系人
    key_dic['PURCHASE_AGENT_CONTACT'] = 'qhtestagent'
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['PURCHASE_PROJECT_ID'], key_dic['PURCHASE_PROJECT_NAME'], key_dic['PURCHASE_PROJECT_CODE']


def purchase_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 采购包编号
    key_dic['PURCHASE_SECTION_CODE'] = 'QH-' + datenow_hmsf()
    # 采购包名称
    key_dic['PURCHASE_SECTION_NAME'] = '测试采购包' + datenow_hmsf()
    # 采购包类别 1 物资类 2 服务类 3 工程类 9 其他
    key_dic['PURCHASE_SECTION_TYPE'] = '1'
    # 预算汇总形式 1 清单汇总（标的有预算） 2 包预算（标的不设预算）
    key_dic['BUDGET_TOTAL_MODE'] = '1'
    # 报价价款形式代码 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 采购包预算
    key_dic['PURCHASE_SECTION_BUDGET'] = 3000000
    # 采购包最高限价（元）
    # key_dic['LIMITED_PRICE'] = 90000000
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['PURCHASE_SECTION_ID'], key_dic['PURCHASE_SECTION_CODE']]


# print(purchase_section_in({'PRICE_FORM_CODE': '1'}))


def section_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购包明细ID
    key_dic['PURCHASE_SECTION_DETAIL_ID'] = 'PSD_ID' + datenow_hmsf()
    # 需求包明细ID
    key_dic['REQUIRE_SECTION_DETAIL_ID'] = 'RSD_ID' + datenow_hmsf()
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
    # 是否核心产品 1 是 0 否
    key_dic['IS_CORE_PRODUCT'] = '1'
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['PURCHASE_SECTION_DETAIL_ID']


# print(section_detail_in({'PRODUCT_SPECIFICATION': '规格说明'}))

# 采购文件
def purchase_file_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID' + datenow_hmsf()
    # 公告（邀请书）ID 更正公告/邀请书时，传更正公告/邀请书的ID
    key_dic['NOTICE_ID'] = 'NT_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808183757'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183757'
    # 文件名称
    key_dic['DOC_NAME'] = 'qh测试文件'
    # 文件类型 1 首次 2 更正
    key_dic['PURCHASE_FILE_TYPE'] = '1'
    # 评审标准模板引用情况 1 原有模板 2 修改 3 新增
    key_dic['STANDARD_EVAL_RULE_MODI'] = '1'
    # 评审标准模板调整所涉条款
    key_dic['MODI_RULES'] = '评审标准模板调整所涉条款'
    # 采购文件编写人员
    key_dic['EDITOR'] = 'qhtest'
    # 采购文件编写人联系电话
    key_dic['EDITOR_PHONE'] = '13823743743'
    # 采购服务站审核人
    key_dic['AUDITOR'] = '审核人'
    # 是否标前答疑会 0 否 1 是
    key_dic['IS_ANSWER_QUESTION'] = '0'
    # 采购文件生成时间
    key_dic['SUBMIT_TIME'] = dateplus_min(500)
    # 数据更新时间
    key_dic['MODI_DATE'] = dateplus_min(5)
    # 采购文件URL
    key_dic['PURCHASE_FILE_URL'] = 'http://10.0.168.64/supervision-web/#/login'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_file'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    # 如果发生错误则回滚
    db.rollback()
    db.close()
    return key_dic['PURCHASE_FILE_ID']


# 采购文件_包关系
def purchase_file_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 明细ID
    key_dic['ITEM_ID'] = 'ITEM_ID' + datenow_hmsf()
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183757'
    # 评审方法 1 综合评审法 2 质量优先法 3 最低价法 9 其他
    key_dic['BID_EVALUATION_METHOD'] = '1'
    # 文件领取方式 1 线上领取 2 线下领取
    key_dic['FILE_RECEIVE_METHOD'] = '1'
    # 评审因素 多种评审因素间用半角分号隔开
    # 100023003 技术部分（明标） 100023014 技术部分（暗标） 100023005 商务评审 100023017 样品评审 100023018 样品比测 100023007 价格分
    key_dic['BID_EVALUATION_FACTOR'] = '100023003'
    # 设定总分
    key_dic['SET_SCORE'] = 100
    # 客观分值
    key_dic['OBJECTIVE_SCORE'] = 60
    # 主观分值
    key_dic['SUBJECTIVE_SCORE'] = 40
    # 是否允许分项超限价 1 是 0 否
    key_dic['IS_ALLOW_SUBITEM_LIMIT_PRICE'] = '1'
    # 是否有样品评审 1 是 0 否
    key_dic['IS_SAMPLE_REVIEW'] = '1'
    # 是否有现场踏勘 1 是 0 否
    key_dic['IS_SITE_SURVEY'] = '1'
    # 推荐候选人数量确认方式 1 根据评审结果推荐（适用于协议入围业务） 2 有限数量
    key_dic['CANDIDATE_SUBMIT_METHOD'] = '1'
    # 推荐候选人有限数量
    key_dic['CANDIDATE_NUM'] = 6
    # 中标人数量确认方式 1 是 0 否
    key_dic['BIDDER_SUBMIT_METHOD'] = '1'
    # 中标人有限数量
    key_dic['BIDDER_NUM'] = 3
    # 中标（成交）金额是否预分配 1 预分配 0 不预分配
    key_dic['IS_PRE_ALLOCATION'] = '1'
    # 最低有效供应商数量
    key_dic['MINIMUM_SUPPLIER_NUM'] = 4
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_file_section'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购包评审条款大类
def purchase_section_clause_type_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 一级评审项ID
    key_dic['EVAL_LEVEL1_ID'] = 'EV_LV1_ID' + datenow_hmsf()
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183757'
    # 序号
    key_dic['CLAUSE_SEQUENCE'] = 1
    # 一级评审项名称
    key_dic['EVAL_LEVEL1_NAME'] = '一级评审项名称1'
    # 100023003 技术部分（明标） 100023014 技术部分（暗标） 100023005 商务评审 100023017 样品评审 100023018 样品比测
    # 100023007 价格分
    key_dic['CLAUSE_TYPE'] = '100023003'
    # 评审类型 1分值 2合格 3折扣率 4价格 5数量  9 其他
    key_dic['SCORE_TYPE'] = '1'
    # 一级评审项总分
    key_dic['EVAL_LEVEL1_SCORE'] = 80
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section_clause_type'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['EVAL_LEVEL1_ID']


# 采购包评审条款小类
def purchase_section_clause_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 二级评审项ID
    key_dic['EVAL_LEVEL2_ID'] = 'EV_LV2_ID' + datenow_hmsf()
    # 一级评审项ID
    key_dic['EVAL_LEVEL1_ID'] = 'EV_LV1_ID' + datenow_hmsf()
    # 评审因素
    key_dic['EVAL_LEVEL2_ITEM'] = '评审因素1'
    # 序号
    key_dic['CLAUSE_SEQUENCE'] = 1
    # 是否客观项 1 有 0 无
    key_dic['IS_OBJECTIVE'] = '1'
    # 是否扣分项 1 是 0 否
    key_dic['IS_DEDUCTION_ITEM'] = '0'
    # 二级评审项分数
    key_dic['EVAL_LEVEL2_SCORE'] = 60
    # 标准分值
    key_dic['STANDARD_SCORE'] = 60
    # 评分项权重
    key_dic['EVAL_ITEM_RATE'] = 11
    # 评审标准
    key_dic['EVAL_LEVEL2_DETAIL'] = '评审标准'
    # 评审标准模板引用情况 1 原有模板 2 修改 3 新增
    key_dic['STANDARD_EVAL_RULE_QUOTE'] = '1'
    # 修改前二级评审项内容
    key_dic['LAST_EVAL_LEVEL2'] = '修改前二级评审项内容1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section_clause'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购包技术要求
def section_technical_requirement_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 技术要求ID
    key_dic['TECHNICAL_REQUIREMENT_ID'] = 'TEC_REQ_ID' + datenow_hmsf()
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID'
    # 采购标的名称
    key_dic['PURCHASE_OBJECT_NAME'] = '采购标的名称1'
    # 序号
    key_dic['CLAUSE_SEQUENCE'] = 1
    # 参数类型 1 无标识 2 星号标识 3 三角标识
    key_dic['PARAM_TYPE'] = '1'
    # 技术参数与性能指标
    key_dic['CONTENT'] = '技术参数与性能指标1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section_technical_requirement'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购包特殊资格条款
def section_special_qualification_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 技术要求ID
    key_dic['SPECIAL_QUALIFICATION_CLAUSE_ID'] = 'TEC_REQ_ID' + datenow_hmsf()
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID'
    # 序号
    key_dic['CLAUSE_SEQUENCE'] = 1
    # 评审点要求概况
    key_dic['OVERVIEW'] = '评审点要求概况1'
    # 评审点具体描述
    key_dic['CONTENT'] = '评审点具体描述1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_section_special_qualification_clause'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购文件编制审批流信息
def purchase_doc_approval_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 采购文件编制审批信息ID
    key_dic['DOC_APPROVAL_ID'] = 'DA_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 采购文件ID
    key_dic['PURCHASE_FILE_ID'] = 'PF_ID20230808183757'
    # 文件类型 1 首次 2 更正
    key_dic['PURCHASE_FILE_TYPE'] = '1'
    # 核验环节 1 采购机构编制文件 2 采购机构确认文件 3 采购单位核验文件
    key_dic['TRADE_STEP'] = '1'
    # 操作人姓名
    key_dic['COMMITTER_NAME'] = '操作人姓名1'
    # 操作人ID
    key_dic['COMMITTER_ID'] = '操作人ID1'
    # 操作人所在单位
    key_dic['COMMITTER_UNIT'] = '操作人所在单位1'
    # 操作人所在单位代码
    key_dic['COMMITTER_UNIT_CODE'] = '操作人所在单位代码1'
    # 操作人所在单位类型 1 采购服务站 2 采购单位
    key_dic['EDIT_DEPT_TYPE'] = '1'
    # 操作人所在部门
    key_dic['COMMITTER_DEPT'] = '操作人所在部门1'
    # 操作人所在部门代码
    key_dic['COMMITTER_DEPT_CODE'] = '操作人所在部门代码1'
    # 接收时间
    key_dic['RECEIVE_TIME'] = dateplus_min(50)
    # 操作时间
    key_dic['COMMIT_TIME'] = dateplus_min(50)
    # 操作类型 1 发起 2 撤回 3 审核通过 4 审核不通过
    key_dic['COMMIT_TYPE'] = '1'
    # 意见
    key_dic['CONTENT'] = '意见1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    key_dic['COMMIT_TIME'] = dateplus_day_hms(key_dic['COMMIT_TIME'])
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_doc_approval'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['DOC_APPROVAL_ID']


# 采购公告
def purchase_tender_notice_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 公告ID
    key_dic['TENDER_NOTICE_ID'] = 'TN_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 公告标题
    key_dic['NOTICE_TITLE'] = '公告标题1'
    # 公告内容
    key_dic['NOTICE_CONTENT'] = '公告内容1'
    # 公告性质 1 首次公告 2 更正公告
    key_dic['NOTICE_NATURE'] = '1'
    # 公告更正次数
    key_dic['MODI_NUM'] = 0
    # 更正内容
    key_dic['MODI_CONTENT'] = ' '
    # 公告发布时间
    key_dic['NOTICE_PUBLISH_TIME'] = dateplus_min(5)
    # 投标截止时间
    key_dic['TENDER_END_TIME'] = dateplus_min(900)
    # 文件申领开始日期
    key_dic['FILE_RECEIVE_START_TIME'] = dateplus_min(5)
    # 文件申领结束日期
    key_dic['FILE_RECEIVE_END_TIME'] = dateplus_min(900)
    # 文件领取方式 1 线上领取 2 线下领取
    key_dic['FILE_RECEIVE_METHOD'] = '1'
    # 采购机构联系人
    key_dic['PROJECT_CONTACT'] = '采购机构联系人1'
    # 采购机构联系方式
    key_dic['PROJECT_INFORMATION'] = '采购机构联系方式1'
    # 公告源URL
    key_dic['URL'] = 'http://10.0.168.64/supervision-web/#/login'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_tender_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['TENDER_NOTICE_ID']


# 公告明细
def purchase_tender_notice_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 公告明细ID
    key_dic['TENDER_NOTICE_SECTION_ID'] = 'TNS_ID' + datenow_hmsf()
    # 公告ID
    key_dic['TENDER_NOTICE_ID'] = 'TN_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hmsf()
    # 是否允许联合体投标 1 是 0 否
    key_dic['SYNDICATED_FLAG'] = '1'
    # 文件获取开始时间
    key_dic['DOC_SELL_START_TIME'] = dateplus_min(500)
    # 文件获取截止时间
    key_dic['DOC_SELL_END_TIME'] = dateplus_min(50)
    # 文件获取地址
    key_dic['DOC_SELL_ADRESS'] = '文件获取地址1'
    # 文件获取方式
    key_dic['DOC_SELL_METHOD'] = '文件获取方式1'
    # 开标时间
    key_dic['BID_OPEN_TIME'] = dateplus_min(5)
    # 开标地点
    key_dic['BID_OPEN_SITE'] = '开标地点1'
    # 投标文件/响应文件递交截止时间
    key_dic['BID_CLOSING_TIME'] = dateplus_min(50)
    # 是否收取投标保证金 1 是 0 否
    key_dic['MARGIN_COLLECT'] = '1'
    # 投标保证金缴纳方式 1转账 2 支票 3 保函 4 汇票 9 其他
    key_dic['MARGIN_PAY_TYPE'] = '1'
    # 投标保证金金额
    key_dic['MARGIN_AMOUNT'] = 50000
    # 是否缴纳履约保证金 1 是 0 否
    key_dic['IS_COMMIT_PERFORM_MARGIN'] = '0'
    # 履约保证金缴纳比例
    key_dic['PERFORM_MARGIN_PERCENT'] = ''
    # 是否双信封招标 1 是 0 否
    key_dic['IS_DOUBLE_ENVELOPE'] = '0'
    # 简要技术要求、服务和安全要求
    key_dic['SERVICE_SECURITY'] = '简要技术要求、服务和安全要求'
    # 申请人的一般资格要求
    key_dic['APPLICANT_REQUIRE'] = '申请人的一般资格要求'
    # 申请人的特殊资格要求
    key_dic['APPLICANT_SPECIAL_REQUIRE'] = '申请人的特殊资格要求'
    # 是否有样品展示 1 是 0 否
    key_dic['IS_SAMPLES_SHOW'] = '0'
    # 交货地点或服务地点
    key_dic['SERVICE_LOCATION'] = '交货地点或服务地点'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_tender_notice_section'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 采购文件下载
def purchase_file_download_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 文件下载ID
    key_dic['FILE_DOWNLOAD_ID'] = 'FD_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hmsf()
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商' + datenow_hmsf()[-10:]
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码' + datenow_hmsf()[-10:]
    # 供应商报名时间
    key_dic['SUPPLIER_SIGN_TIME'] = dateplus_min(0)
    # 采购文件下载时间
    key_dic['FILE_DOWNLOAD_TIME'] = dateplus_min(5)
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '1'
    # 供应商联系人
    key_dic['SUPPLIER_CONTACT'] = '供应商联系人' + datenow_hmsf()[-10:]
    # 供应商联系电话
    key_dic['SUPPLIER_CONTACT_TEL'] = '1' + datenow_hmsf()[-10:]
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_file_download'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['FILE_DOWNLOAD_ID']


# 投标文件递交
def purchase_tender_file_submit_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 投标文件递交ID
    key_dic['TENDER_FILE_SUBMIT_ID'] = 'FI_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hmsf()
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 投标文件名称
    key_dic['FILE_NAME'] = '投标文件名称1'
    # 投标文件
    key_dic['FILE_URL'] = 'http://10.0.168.64/supervision-web/#/login'
    # 投标文件递交时间
    key_dic['FILE_UPLOAD_TIME'] = dateplus_min(5)
    # 供应商来源 1 公开征集 2 定向邀请 3 随机抽取 4 系统内征集
    key_dic['SUPPLIER_ORIGIN'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_tender_file_submit'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['TENDER_FILE_SUBMIT_ID']


def purchase_open_bid_record(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 开标记录ID
    key_dic['OPEN_BID_ID'] = 'OBid' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID' + datenow_hmsf()
    # 开标地点
    key_dic['BID_OPENING_ADDRESS'] = '开标地点test2'
    # 开标开始时间
    key_dic['BID_OPENING_START_TIME'] = dateplus_min(30)
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
    # 开标结果 1 开标完成 2 流标 3 未开标 4 废标
    key_dic['BID_OPEN_RESULT'] = '1'
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['OPEN_BID_ID']


# 开标明细/供应商名单
def purchase_supplier_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 开标记录ID
    key_dic['SUPPLIER_LIST_ID'] = 'SLid' + datenow_hmsf()
    # 开标记录ID
    key_dic['OPEN_BID_ID'] = 'OBid' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商' + datenow_hmsf()[-10:]
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码' + datenow_hmsf()[-10:]
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 供应商负责人
    key_dic['SUPPLIER_MANAGER'] = 'QH供应商负责人' + datenow_hmsf()[-10:]
    # 供应商负责人联系电话
    key_dic['SUPPLIER_MANAGER_TEL'] = '1' + datenow_hmsf()[-10:]
    # 是否判定本次投标无效 1 是 0 否
    key_dic['IS_INVALID'] = '1'
    # 无效原因
    key_dic['INVALID_REASON'] = '无效原因1'
    # 投标工期描述
    key_dic['TIME_LIMIT_CONTENT'] = '一个月'
    # 投标状态 1 已投标 0 未投标
    key_dic['DECRY_STATUS'] = '1'
    # 签到状态 1 已签到 0 未签到
    key_dic['SIGN_STATUS'] = '0'
    # 签到时间
    key_dic['SIGN_TIME'] = dateplus_min(5)
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['SUPPLIER_LIST_ID']


def supplier_score_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 供应商评审汇总ID
    key_dic['SUPPLIER_SCORE_DETAIL_ID'] = 'SSD_ID' + datenow_hmsf()
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商' + datenow_hmsf()
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码' + datenow_hmsf()
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
    # 候选人排名
    key_dic['CANDIDATE_SORT'] = 1
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['SUPPLIER_SCORE_DETAIL_ID']


# 投标（报价）文件特征码
def purchase_file_info_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 投标文件特征码ID
    key_dic['FILE_INFO_ID'] = 'FL_id' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = 'QH供应商' + datenow_hmsf()
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = 'QH供应商代码' + datenow_hmsf()
    # 投标文件制作客户端安装序号
    key_dic['CLIENT_SERIAL_NUM'] = datenow_hmsf()
    # 投标（报价）文件哈希值
    key_dic['BID_FILE_HAS'] = '投标（报价）文件哈希值'
    # 投标（报价）电脑CPU序列号
    key_dic['CPU_ID'] = datenow_hmsf()
    # 投标（报价）电脑硬盘序列号
    key_dic['HARD_DISK_SERIAL_NUM'] = datenow_hmsf()
    # 投标（报价）电脑网卡MAC地址
    key_dic['MAC_ADDRESS'] = '电脑网卡MAC地址21230'
    # 投标（报价）上传IP地址
    key_dic['NET_ID'] = '10.10.10l.1'
    # 文件递交方式 1系统递交 2现场递交
    key_dic['FILE_SUBMIT_METHOD'] = '1'
    # 投标文件大小(单位：MB)
    key_dic['FILE_SIZE'] = 112
    # 投标文件作者
    key_dic['FILE_EDITOR'] = 'atlas'
    # 投标文件页数
    key_dic['FILE_PAGES'] = 22
    # 供应商投标联系人
    key_dic['SUPPLIER_CONTACT'] = '供应商投标联系人' + datenow_hms_s()
    # 投标联系人联系方式
    key_dic['SUPPLIER_CONTACT_PHONE'] = '1' + datenow_hmsf()[-10:]
    # 投标联系人身份证件号
    key_dic['SUPPLIER_CONTACT_ID'] = '1111' + datenow_hms_ss()
    # 投标客户端信息
    key_dic['MACHINE_INFO'] = '1' + datenow_hms_s()
    # 投标客户端特征码
    key_dic['MACHINE_ID'] = datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['FILE_INFO_ID']


def evaluation_report_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 投标文件特征码ID
    key_dic['EVALUATION_EVAL_REPORT_ID'] = 'EER_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 评标监督人
    key_dic['BID_EVALUATION_SUPERVISOR'] = '评标监督人1'
    # 评标经办人
    key_dic['BID_EVALUATION_MANAGER'] = '评标经办人1'
    # 是否转线下 1 是 0 否
    key_dic['TRANSFER_LINE'] = '0'
    # 是否转竞谈 1 是 0 否
    key_dic['SWITCHING_NEGOTIATION'] = '1'
    # 是否暂停评审 1 是 0 否
    key_dic['SUSPENSION_REVIEW'] = '0'
    # 评审方式 0结果录入 1电子统分 2线上评审 3线下评标 4远程异地评审
    key_dic['EVLUATION_MODE'] = '3'
    # 评审方法 1 综合评审法 2 质量优先法 3 最低价法
    key_dic['BID_EVALUATION_METHOD'] = '1'
    # 评审开始时间
    key_dic['BEGIIN_TIME'] = dateplus_min(0)
    # 评审结束时间
    key_dic['END_TIME'] = dateplus_min(86)
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
    # 评审附件
    key_dic['FILE_URL'] = ('[{"ATTACHMENT_TYPE":"QUALIFICATION_EXAMINATION","ATTACHMENT_NAME":"资格性审查附件",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                           '{"ATTACHMENT_TYPE":"COMPLIANCE_REVIEW","ATTACHMENT_NAME":"符合性审查附件",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                           '{"ATTACHMENT_TYPE":"EVLUATION_TOTAL","ATTACHMENT_NAME":"评审汇总表附件",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                           '{"ATTACHMENT_TYPE":"CORE_PRODUCT_REVIEW","ATTACHMENT_NAME":"核心产品评审附件",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                           '{"ATTACHMENT_TYPE":"EVLUATION_REPORT","ATTACHMENT_NAME":"评审报告",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                           '{"ATTACHMENT_TYPE":"PURCHASE_INVITATION_NOTICE","ATTACHMENT_NAME":"其他附件",'
                           '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]')
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['EVALUATION_EVAL_REPORT_ID'], key_dic['PURCHASE_SECTION_ID']]


def expert_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 主键
    key_dic['EXPERT_LIST_ID'] = 'EP_ID' + datenow_hmsf()
    # 投标文件特征码ID
    key_dic['EVAL_COMMITTEE_ID'] = 'EC_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['EVAL_COMMITTEE_ID']


def score_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 打分细项ID
    key_dic['SCORE_DETAIL_ID'] = 'SD_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['SCORE_DETAIL_ID']


def eval_committee_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 评审委员会ID
    key_dic['EVAL_COMMITTEE_ID'] = 'EC_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['EVAL_COMMITTEE_ID'], key_dic['PURCHASE_SECTION_ID']]


def candidate_list_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 预中标供应商明细ID
    key_dic['CANDIDATE_ID'] = 'CD_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['CANDIDATE_ID']


def supplier_score_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 条款得分ID
    key_dic['SUPPLIER_SCORE_ITEM_ID'] = 'SS_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['SUPPLIER_SCORE_ITEM_ID']


# 价格谈判轮次记录
def neg_offer_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 资格性审查表
def qualification_examination_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 资格性审查ID
    key_dic['QUALIFICATION_EXAMINATION_ID'] = 'QA_EX_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 条款
    key_dic['CLAUSE'] = '条款1'
    # 通过数量
    key_dic['PASSING_QUANTITY'] = 4
    # 未通过数量
    key_dic['UNAPPROVED_QUANTITY'] = 4
    # 通过供应商名称
    key_dic['APPROVED_SUPPLIER'] = '通过供应商名称1'
    # 未通过供应商名称
    key_dic['FAILED_SUPPLIER'] = '未通过供应商名称1'
    # 意见汇总
    key_dic['SUMMARY_OF_OPINIONS'] = '意见汇总1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_qualification_examination'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['QUALIFICATION_EXAMINATION_ID'], key_dic['PURCHASE_SECTION_ID']]


# 资格审查小组表
def qualification_panel_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 资格审查小组ID
    key_dic['QUALIFICATION_PANEL_ID'] = 'QA_PA_ID' + datenow_hmsf()
    # 资格性审查ID
    key_dic['QUALIFICATION_EXAMINATION_ID'] = 'QA_EX_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['DOCUMENT_TYPE'] = '1'
    # 专家证件号
    key_dic['ID_CARD'] = '专家证件号1'
    # 联系方式
    key_dic['CONTACT_INFORMATION'] = '13727347345'
    # 类型 2 专家 3 采购单位代表 4 采购单位监督 5 采购机构人员
    key_dic['TYPE'] = '2'
    # 专业类别 1 物资技术类 2 工程技术类 3 服务技术类 4 物资服务经济类 5 工程经济类 9其他
    key_dic['PROFESSIONAL_CATEGORY'] = '1'
    # 工作单位
    key_dic['WORK_UNIT'] = '工作单位1'
    # 职务
    key_dic['JOB'] = '职务1'
    # 专家隶属 1 军队 2 地方 3库外
    key_dic['EXPERT_SUBORDINATE'] = '1'
    # 行号
    key_dic['LINE_NUMBER'] = '行号1'
    # 正式/候补 1 正式 2 候补
    key_dic['OFFICIAL_ALTERNATE'] = '1'
    # 签到状态 1已签到 0未签到
    key_dic['SIGN_IN_STATUS'] = '1'
    # 应到时间
    key_dic['DUE_TIME'] = dateplus_min(15)
    # 签到时间
    key_dic['SIGN_IN_TIME'] = dateplus_min(5)
    # 评审状态 1正常 0异常
    key_dic['REVIEW_STATUS'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_qualification_panel'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 资格性审查明细表
def qualification_examination_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 资格性审查明细项ID
    key_dic['QUALIFICATION_EXAMINATION_DETAIL_ID'] = 'QA_EXD_ID' + datenow_hmsf()
    # 资格性审查ID
    key_dic['QUALIFICATION_EXAMINATION_ID'] = 'QA_EX_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 明细项ID
    key_dic['DETAIL_ID'] = '明细项ID'
    # 明细项名称
    key_dic['DETAIL_NAME'] = '明细项名称1'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 专家ID
    key_dic['EXPERT_ID'] = '专家ID1'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 专家身份证件号
    key_dic['ID_CARD'] = '专家身份证件号1'
    # 是否通过 1是 0否
    key_dic['PASS_OR_NOT'] = '1'
    # 不通过理由
    key_dic['REASON_FOR_REJECTION'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_qualification_examination_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 资格性审查结果表
def qualification_examination_result_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 资格性审查明细项ID
    key_dic['QUALIFICATION_EXAMINATION_RESULT_ID'] = 'QA_EXR_ID' + datenow_hmsf()
    # 资格性审查ID
    key_dic['QUALIFICATION_EXAMINATION_ID'] = 'QA_EX_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 是否通过 1是 0否
    key_dic['PASS_OR_NOT'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_qualification_examination_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 符合性审查表
def compliance_review_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 符合性审查ID
    key_dic['COMPLIANCE_REVIEW_ID'] = 'CO_RV_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PROJECT_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 条款
    key_dic['CLAUSE'] = '供应商代码1'
    # 通过数量
    key_dic['PASSING_QUANTITY'] = 4
    # 未通过数量
    key_dic['UNAPPROVED_QUANTITY'] = 4
    # 不通过原因
    key_dic['CAUSE_OF_DISQUALIFICATION'] = '不通过原因1'
    # 通过供应商名称
    key_dic['APPROVED_SUPPLIER'] = '通过供应商名称1'
    # 未通过供应商名称
    key_dic['FAILED_SUPPLIER'] = '未通过供应商名称1'
    # 意见汇总
    key_dic['SUMMARY_OF_OPINIONS'] = '意见汇总1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_compliance_review'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['COMPLIANCE_REVIEW_ID'], key_dic['PURCHASE_SECTION_ID']]


# 符合性审查小组表
def compliance_review_team_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 符合性审查小组ID
    key_dic['COMPLIANCE_REVIEW_TEAM_ID'] = 'CO_RV_TM_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 符合性审查ID
    key_dic['COMPLIANCE_REVIEW_ID'] = 'CO_RV_ID'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['DOCUMENT_TYPE'] = '1'
    # 专家证件号
    key_dic['ID_CARD'] = '专家证件号1'
    # 联系方式
    key_dic['CONTACT_INFORMATION'] = '1392834734'
    # 专家类别 126002 专家 126003 采购单位代表 126005 采购机构人员
    key_dic['EXPERT_TYPE_ORIGIN'] = '126002'
    # 专业类别 1 物资技术类 2 工程技术类 3 服务技术类 4 物资服务经济类 5 工程经济类 9其他
    key_dic['PROFESSIONAL_CATEGORY'] = '2'
    # 工作单位
    key_dic['WORK_UNIT'] = '工作单位1'
    # 职务
    key_dic['JOB'] = '职务1'
    # 专家隶属 1 军队 2 地方 3库外
    key_dic['EXPERT_SUBORDINATE'] = '1'
    # 行号
    key_dic['LINE_NUMBER'] = '行号1'
    # 正式/候补 1 正式 2 候补
    key_dic['OFFICIAL_ALTERNATE'] = '1'
    # 签到状态 1已签到 0未签到
    key_dic['SIGN_IN_STATUS'] = '1'
    # 应到时间
    key_dic['DUE_TIME'] = dateplus_min(5)
    # 签到时间
    key_dic['SIGN_IN_TIME'] = dateplus_min(5)
    # 评审状态 1正常 0异常
    key_dic['REVIEW_STATUS'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_compliance_review_team'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 符合性审查明细表
def compliance_review_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 符合性审查明细项ID
    key_dic['COMPLIANCE_REVIEW_DETAIL_ID'] = 'CO_RV_DT_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 符合性审查ID
    key_dic['COMPLIANCE_REVIEW_ID'] = 'CO_RV_ID'
    # 明细项ID
    key_dic['DETAIL_ID'] = '明细项ID1'
    # 明细项名称
    key_dic['DETAIL_NAME'] = '明细项名称1'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 专家ID
    key_dic['EXPERT_ID'] = '专家ID1'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 专家身份证件号
    key_dic['ID_CARD'] = '专家身份证件号1'
    # 是否通过 1是 0否
    key_dic['PASS_OR_NOT'] = '1'
    # 不通过理由
    key_dic['REASON_FOR_REJECTION'] = '不通过理由1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_compliance_review_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['COMPLIANCE_REVIEW_DETAIL_ID']


# 符合性审查结果表
def compliance_review_result_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 符合性审查结果ID
    key_dic['COMPLIANCE_REVIEW_RESULT_ID'] = 'CO_RV_DT_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 符合性审查ID
    key_dic['COMPLIANCE_REVIEW_ID'] = 'CO_RV_ID'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 是否通过 1是 0否
    key_dic['PASS_OR_NOT'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_compliance_review_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 核心产品评审表
def core_product_review_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 核心产品评审ID
    key_dic['CORE_PRODUCT_REVIEW_ID'] = 'CO_PR_RV_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808183021'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808183021'
    # 评审轮次
    key_dic['EVALUATION_NUM'] = 1
    # 评审结果
    key_dic['REVIEW_RESULT'] = '评审结果1'
    # 评审意见
    key_dic['REVIEW_COMMENTS'] = '评审意见1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_core_product_review'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['CORE_PRODUCT_REVIEW_ID'], key_dic['PURCHASE_SECTION_ID']]


# 核心产品评审结果表
def core_product_review_result_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 核心产品评审结果ID
    key_dic['CORE_PRODUCT_REVIEW_RESULT_ID'] = 'CO_RV_RT_ID' + datenow_hmsf()
    # 核心产品评审ID
    key_dic['CORE_PRODUCT_REVIEW_ID'] = 'CO_PR_RV_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 产品ID
    key_dic['PRODUCT_ID'] = '产品ID1'
    # 产品名称
    key_dic['PRODUCT_NAME'] = '产品名称1'
    # 评审结果
    key_dic['REVIEW_RESULT'] = '评审结果1'
    # 评审意见
    key_dic['REVIEW_COMMENTS'] = '评审意见1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_core_product_review_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 同品牌评审得分表
def core_product_review_score_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 核心产品评审得分ID
    key_dic['CORE_PRODUCT_REVIEW_SCORE_ID'] = 'CO_RV_SC_ID' + datenow_hmsf()
    # 核心产品评审ID
    key_dic['CORE_PRODUCT_REVIEW_ID'] = 'CO_PR_RV_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 产品ID
    key_dic['PRODUCT_ID'] = '产品ID1'
    # 产品名称
    key_dic['PRODUCT_NAME'] = '产品名称1'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '评审意见1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '评审意见1'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['DOCUMENT_TYPE'] = '1'
    # 专家证件号
    key_dic['ID_CARD'] = '专家证件号1'
    # 技术评分
    key_dic['TECHNICAL_SCORE'] = 30
    # 商务评分
    key_dic['BUSINESS_RATING'] = 30
    # 价格评分
    key_dic['PRICE_RATING'] = 30
    # 评分汇总
    key_dic['SCORE_SUMMARY'] = 90
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_core_product_review_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 线下委员会名单表
def offline_expert_roster_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 线下委员会名单ID
    key_dic['OFFLINE_EXPERT_ROSTER_ID'] = 'OF_EX_RO_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 专家名称
    key_dic['EXPERT_NAME'] = '产品ID1'
    # 证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['DOCUMENT_TYPE'] = '1'
    # 专家证件号
    key_dic['ID_CARD'] = '专家证件号1'
    # 联系方式
    key_dic['CONTACT_INFORMATION'] = '评审意见1'
    # 专业类别 1 物资技术类 2 工程技术类 3 服务技术类 4 物资服务经济类 5 工程经济类 9其他
    key_dic['PROFESSIONAL_CATEGORY'] = '1'
    # 工作单位
    key_dic['WORK_UNIT'] = '1'
    # 专家专业分类 6 物资技术 7 工程技术 8 服务技术 9 物资服务经济 10 工程经济
    key_dic['EXPERT_CLASSIFY_TYPE_ORIGIN'] = '6'
    # 是否组长 1是 0否
    key_dic['IS_LEADER'] = '1'
    # 签到时间
    key_dic['SIGN_IN_TIME'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_offline_expert_roster'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 线下评审得分
def offline_evaluation_score_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 线下评审得分ID
    key_dic['OFFLINE_EVALUATION_SCORE_ID'] = 'OF_EX_RO_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 技术评分
    key_dic['TECHNICAL_SCORE'] = 30
    # 商务评分
    key_dic['BUSINESS_RATING'] = 30
    # 价格评分
    key_dic['PRICE_RATING'] = 30
    # 评分汇总
    key_dic['SCORE_SUMMARY'] = 90
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_offline_evaluation_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 线下评审结果
def offline_evaluation_result_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 线下评审得分ID
    key_dic['OFFLINE_EVALUATION_RESULT_ID'] = 'OF_EV_RS_ID' + datenow_hmsf()
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 供应商代码
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 技术评分 1 总价 2 上浮 3 下浮 4 数量 5 单价 9 其他
    key_dic['PRICE_FORM_CODE'] = '1'
    # 总价形式中标价（元）
    key_dic['WIN_BID_PRICE'] = 300000
    # 其他形式中标价
    key_dic['WIN_OTHER_BID_PRICE'] = '300000'
    # 推荐时间
    key_dic['RECOMMEND_TIME'] = dateplus_min(5)
    # 评审排名
    key_dic['RECOMMEND_SORT'] = 1
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_offline_evaluation_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 专家履职评价专家评分
def performance_evaluation_score_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 专家履职评价专家评分ID
    key_dic['PERFORMANCE_EVALUATION_SCORE_ID'] = 'PE_EV_SC_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'CO_RV_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 评价时间
    key_dic['EVALUATION_TIME'] = dateplus_min(5)
    # 专家ID
    key_dic['EXPERT_ID'] = '专家ID1'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 评分得分
    key_dic['SCORE_SUMMARY'] = 30
    # 是否违规 1 是 0 否
    key_dic['IS_VIOLATION'] = '0'
    # 专家专业分类 6 物资技术 7 工程技术 8 服务技术 9 物资服务经济 10 工程经济
    key_dic['EXPERT_CLASSIFY_TYPE_ORIGIN'] = '6'
    # 是否组长 1 是 0 否
    key_dic['IS_LEADER'] = '1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_performance_evaluation_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


# 专家履职评价专家评分明细
def performance_evaluation_score_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 专家履职评价专家评分ID
    key_dic['PERFORMANCE_EVALUATION_SCORE_DETAIL_ID'] = 'PE_EV_SD_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'CO_RV_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'CO_RV_ID'
    # 专家ID
    key_dic['EXPERT_ID'] = '专家ID1'
    # 专家名称
    key_dic['EXPERT_NAME'] = '专家名称1'
    # 序号
    key_dic['DORDER'] = 1
    # 评分项分类
    key_dic['SCORE_TYPE'] = '评分项分类1'
    # 评价条款
    key_dic['SCORE_TYPE_DETAIL'] = '评价条款1'
    # 条款分值
    key_dic['CLAUSE_SCORE'] = 30
    # 是否违规 1 是 0 否
    key_dic['IS_VIOLATION'] = '0'
    # 扣分详情
    key_dic['ACTUAL_SCORE'] = 10
    # 备注说明
    key_dic['CONTENT'] = '备注说明1'
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_performance_evaluation_score_detail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


def qual_after_member_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 小组成员ID
    key_dic['QUAL_AFTER_MEMBER_ID'] = 'QAM_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['QUAL_AFTER_MEMBER_ID']


# 中标（成交）结果公示
def win_notice_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标结果公示ID
    key_dic['WIN_NOTICE_ID'] = 'WN_ID' + datenow_hmsf()
    # 采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 公示标题
    key_dic['WIN_NOTICE_TITLE'] = '公示标题' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['WIN_NOTICE_ID']


def labeling_process_log_in(dic_a):
    key_dic = {}
    key_dic['PURCHASE_LABELING_PROCESS_LOG_ID'] = 'PLPID' + datenow_hms()
    key_dic['PURCHASE_PROJECT_ID'] = 'PURCHASE_PROJECT_ID'
    key_dic['PURCHASE_PROJECT_CODE'] = 'PURCHASE_PROJECT_CODE'
    key_dic['PURCHASE_PROJECT_NAME'] = 'PURCHASE_PROJECT_NAME'
    # 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源采购 9 其他
    key_dic['PURCHASE_MODE'] = '1'
    key_dic['PROCESS_NAME'] = '采购流程名称1'
    key_dic['PROCESS_ACTIVITY_NAME'] = '采购环节名称1'
    # 0 流程发起 1 正在确认 2 确认退回 3 流程挂起 9 确认通过
    key_dic['STEP_STATUS'] = '0'
    key_dic['STEP_STATUS_NAME'] = '步骤状态名称1'
    key_dic['PROCESS_ASSIGNEE_NAME'] = '办理人1'
    key_dic['OPERATION_START_TIME'] = dateplus_min(5)
    key_dic['OPERATION_COMPLETE_TIME'] = dateplus_min(0)
    key_dic['CONTENT'] = '意见1'
    key_dic['FILE_URL'] = '附件URL地址,多种附件间用半角分号隔开'
    # 数据状态 -1 删除 0 生效 1 作废
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '物资交易系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_labeling_process_log'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.0.168.47',
                         port=3306, user='root',
                         password='123qwe!@#',
                         database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()


def win_supplier_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标人信息ID
    key_dic['WIN_SUPPLIER_ID'] = 'WS_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['WIN_SUPPLIER_ID']
    # return sql_end


# print(win_supplier_in({'WINNING_BIDDER_NAME': '供应商名称3'}))


def bid_object_detail_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 中标（成交）标的明细ID
    key_dic['BID_OBJECT_DETAIL_ID'] = 'BOD_ID' + datenow_hmsf()
    # 中标（成交）结果公示ID
    key_dic['WIN_NOTICE_ID'] = 'WN_ID'
    # 采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PP_ID20230808184758'
    # 中标（成交）供应商名称
    key_dic['WINNING_BIDDER_NAME'] = '供应商名称' + datenow_hmsf()
    # 中标（成交）供应商代码
    key_dic['WINNING_BIDDER_CODE'] = '供应商代码' + datenow_hmsf()
    # 是否联合体 1 是 0 否
    key_dic['UNION_BIDDER_IF'] = '0'
    # 标的ID
    key_dic['PURCHASE_SECTION_DETAIL_ID'] = 'PSD_ID' + datenow_hmsf()
    # 标的序号
    key_dic['DORDER'] = '1'
    # 标的名称
    key_dic['GOODS_NAME'] = '标的名称' + datenow_hmsf()
    # 采购品目编码
    key_dic['PUR_CATALOG_CODE'] = '采购品目编码' + datenow_hmsf()
    # 品牌商标
    key_dic['BRAND'] = '品牌商标1'
    # 规格型号
    key_dic['SPEC'] = '规格型号1'
    # 统一编目码
    key_dic['GOOD_CODE'] = '统一编目码' + datenow_hmsf()
    # 采购品目名称
    key_dic['PUR_CATALOG_NAME'] = '采购品目名称' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['BID_OBJECT_DETAIL_ID']
    # return sql_end


# print(win_supplier_in({'WINNING_BIDDER_NAME': '供应商名称3'}))


def faliure_bid_notice_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 业务主键
    key_dic['FALIURE_BID_NOTICE_ID'] = 'FBN_ID' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['FALIURE_BID_NOTICE_ID']
    # return sql_end


# print(faliure_bid_notice_in({'URL': 'https://www.baidu.com/'}))


def rebid_project_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 流标处理ID
    key_dic['PURCHASE_REBID_ID'] = 'PR_ID' + datenow_hmsf()
    # 原采购项目ID
    key_dic['PURCHASE_PROJECT_ID'] = 'PP_ID20230808184758'
    # 原采购项目ID
    key_dic['PURCHASE_PROJECT_CODE'] = 'PP_code'
    # 处理方式 1 重新组织采购 2 变更采购方式 3 终止
    key_dic['MANAGE_TYPE'] = '1'
    # 新采购项目ID
    key_dic['NEW_PROJECT_ID'] = 'NPJ_ID' + datenow_hmsf()
    # 新采购项目编号
    key_dic['NEW_PROJECT_CODE'] = 'NPJ_CODE' + datenow_hmsf()
    # 新采购项目名称
    key_dic['NEW_PROJECT_NAME'] = 'QH新采购项目名称' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['PURCHASE_REBID_ID']
    # return sql_end


# print(rebid_project_in({'TERMINATION_REASON': '终止理由test'}))


def rebid_section_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '配套业务管理系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 流标包处理ID
    key_dic['PURCHASE_REBID_SECTION_ID'] = 'PRS_ID' + datenow_hmsf()
    # 流标处理ID
    key_dic['PURCHASE_REBID_ID'] = 'PR_ID'
    # 原采购包ID
    key_dic['PURCHASE_SECTION_ID'] = 'PS_code'
    # 原采购包编号
    key_dic['PURCHASE_SECTION_CODE'] = 'PS_code'
    # 新采购包ID
    key_dic['NEW_SECTION_ID'] = 'NS_ID' + datenow_hmsf()
    # 新采购包编号
    key_dic['NEW_SECTION_CODE'] = 'NS_CODE' + datenow_hmsf()
    # 新采购包名称
    key_dic['NEW_SECTION_NAME'] = 'QH新采购包名称' + datenow_hmsf()
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['PURCHASE_REBID_SECTION_ID']
    # return sql_end


# print(rebid_section_in({'PURCHASE_SECTION_CODE': 'PS_code'}))


def win_note_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
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
    key_dic['NOTE_CODE'] = '（未）中标通知书编号' + datenow_hmsf()
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
    # 通知书附件
    key_dic['FILE_URL'] = 'http://10.0.168.64/supervision-web/#/login'
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['NOTE_CODE']
    # return sql_end

# print(win_note_in({'NOTE_TYPE': '1'}))
