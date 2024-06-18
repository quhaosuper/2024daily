import allure
import pymysql
import pytest
import yaml
import copy
from datetimetr import *
from bus_active import *


def plan_year_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + time_id()
    key_dic['PID'] = 'PID' + time_id()
    key_dic['YEAR_PROJECT_ID'] = 'QHQYID' + datenow_hms()
    key_dic['PURCHASE_UNIT_NAME'] = '测试采购单位'
    key_dic['PURCHASE_UNIT_CODE'] = '测试采购单位QH'
    key_dic['PURCHASER_MANAGEMENT_DEPT'] = '测试采购单位采管部门'
    key_dic['PURCHASER_MANAGEMENT_DEPT_CODE'] = '测试采购单位采管部门QH'
    key_dic['PLAN_YEAR'] = time_now_year()
    key_dic['PLAN_YEAR_PROJECT_CODE'] = 'PYPC' + time_id()
    key_dic['PLAN_YEAR_PROJECT_NAME'] = 'qh物资采购年度计划' + datenow_hms()
    key_dic['REQUIRE_INTRODUCTION'] = '需求概况'
    key_dic['PROJECT_BUDGET'] = '4999999'
    key_dic['REQUIRE_SUBMIT_TIME'] = dateplus_day_hms(0)
    key_dic['PURCHASE_FINISH_TIME'] = dateplus_min(5)
    key_dic['DELIVER_TIME'] = dateplus_day_hms(10)
    # 采购分类 1 物资类 2 服务类 3 工程类
    key_dic['PROJECT_TYPE'] = '2'
    key_dic['BASIS_CODE'] = '依据文号test'
    # 是否关联购置计划 1 是 0 否
    key_dic['IS_PURCHASE_PLAN'] = '0'
    key_dic['GZJHBH'] = '购置计划编号' + datenow_hms()
    # 项目通用性 1 专用 2 通用
    key_dic['IS_COMMON'] = '2'
    # 数据状态 -1 删除 0 生效 1 作废
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '物资交易系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['PURCHASE_AGENT_CODE'] = '采购机构代码qh'
    key_dic['PURCHASE_AGENT_NAME'] = '采购机构代码qh'
    # 采购机构类型 1 采购服务站 2 队属采购机构 9 其他
    key_dic['AGENT_TYPE'] = '2'
    key_dic['AGENT_MANAGEMENT_DEPT'] = 'QHTEST'
    key_dic['AGENT_MANAGEMENT_DEPT_CODE'] = 'QHTEST'
    # 合并标记 0 未被合并的 1 被合并的 2 合并后的
    key_dic['MERGE_FLAG'] = '2'
    key_dic['CREATE_TIME'] = dateplus_min(1)
    # 是否下达 1 是 0 否
    key_dic['RELEASE_IF'] = '0'
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    key_dic['CREATE_USER'] = 'QHTEST'
    key_dic['MODI_USER_ID'] = 'QHTEST'
    key_dic['MODI_USER'] = 'QHTEST'
    key_dic['MODI_TIME'] = dateplus_min(1)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_plan_year_new'
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
    return key_dic['YEAR_PROJECT_ID']


def plan_quar_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'PID': 'PID' + time_id(), 'QUAR_PROJECT_ID': 'QHQPID' + datenow_hmsf(),
               'YEAR_PROJECT_ID': 'QHQYID' + datenow_hmsf(), 'PURCHASE_UNIT_NAME': '测试采购单位',
               'PURCHASE_UNIT_CODE': '测试采购单位QH', 'PURCHASER_MANAGEMENT_DEPT': '测试采购单位采管部门',
               'PURCHASER_MANAGEMENT_DEPT_CODE': '测试采购单位采管部门QH', 'PLAN_YEAR': time_now_year(),
               'PLAN_QUARTER': '3', 'PLAN_MONTH': '1', 'PLAN_QUAR_PROJECT_CODE': 'PQPC' + time_id(),
               'PLAN_QUAR_PROJECT_NAME': 'qh物资采购季度计划' + datenow_hmsf(), 'REQUIRE_INTRODUCTION': '需求概况',
               'PROJECT_BUDGET': '5000000.2222', 'PURCHASE_AGENT_CODE': '测试采购机构CODE',
               'PURCHASE_AGENT_NAME': '测试采购机构NAME', 'AGENT_TYPE': '2',
               'AGENT_MANAGEMENT_DEPT': '测试采购机构采管部门',
               'AGENT_MANAGEMENT_DEPT_CODE': '测试采购机构采管部门CODE', 'REQUIRE_SUBMIT_TIME': dateplus_day_hms(0),
               'REQUIRE_SUBMIT_DAY': '1', 'PURCHASE_FINISH_TIME': dateplus_min(-1), 'PURCHASE_FINISH_DAY': '2',
               'DELIVER_TIME': dateplus_min(0), 'DELIVER_DAY': '3', 'PLAN_CHANGE_REASON': '计划调整情况及理由',
               'PROJECT_TYPE': '2', 'PROJECT_ATTRIBUTE_DESC': '项目属性描述', 'IS_PURCHASE_PLAN': '0',
               'GZJHBH': '购置计划编号1' + datenow_hmsf(), 'MERGE_FLAG': '2', 'DATA_STATUS': '0',
               'DATA_SOURCE_CODE': 'GO-001', 'DATA_SOURCE_NAME': '物资交易系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'RELEASE_IF': '0', 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(1),
               'ORIGIN_QUAR_PROJECT_ID': 'OQPID' + datenow_hmsf(), 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_plan_quar_new'
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
    return key_dic['PLAN_QUAR_PROJECT_NAME'], key_dic['QUAR_PROJECT_ID'], key_dic['PURCHASE_AGENT_CODE'], \
        key_dic['PURCHASE_AGENT_NAME'], key_dic['PURCHASE_UNIT_NAME'], key_dic['PURCHASE_UNIT_CODE']


def purchase_plan_approval_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    key_dic['PLAN_APPROVAL_ID'] = 'PLAID' + datenow_hms()
    # 1 年度计划 2 季度计划
    key_dic['PLAN_TYPE'] = '2'
    # 年度、季度计划的ID
    key_dic['OBJECT_ID'] = 'QHQPID20230823093221'
    key_dic['TRADE_STEP'] = '大单位采管部门审核'
    key_dic['COMMITTER_NAME'] = 'QHTEST'
    key_dic['COMMITTER_ID'] = 'QHTEST'
    key_dic['COMMITTER_UNIT'] = 'GLD'
    key_dic['COMMITTER_UNIT_CODE'] = 'quhaotest'
    # 操作人所在单位类型 1 采购单位需求部门 2 采购单位采购管理部门 3 大单位采管部门 9 其他
    key_dic['COMMITTER_UNIT_TYPE'] = '3'
    key_dic['COMMIT_TIME'] = dateplus_min(0)
    # 操作类型 1 发起 2 撤回 3 审核通过 4 审核不通过
    key_dic['COMMIT_TYPE'] = '3'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_plan_approval'
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


def require_compilation_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'SUBMIT_ORDER': 1, 'REQUIRE_ID': 'REID' + datenow_hmsf(),
               'QUAR_PROJECT_ID': 'QPID' + datenow_hmsf(),
               'REQUIRE_PROJECT_NAME': 'quhao' + datenow_hmsf() + '测试项目',
               'PROJECT_TYPE': '1', 'PROJECT_TYPE_NAME': 'qhtest', 'DIVIDED_IF': '1', 'PROGRAM_BUDGET': 4999999,
               'PLAN_CODE': 'PLCO' + datenow_hmsf(), 'PLAN_YEAR': time_now_year(), 'PLAN_DELIVER_MONTH': time_now_mon(),
               'PURCHASE_UNIT_CODE': 'RE-001', 'PURCHASE_UNIT_NAME': 'QHTEST' + datenow_hmsf(),
               'PURCHASE_AGENT_CODE': 'PAC' + datenow_hmsf(), 'PURCHASE_AGENT_NAME': 'PAN' + datenow_hmsf(),
               'LINK_MAN': 'QHTEST', 'LINK_PHONE': '13723743643', 'REQUIRE_CREATE_TIME': dateplus_min(2),
               'PID': 'PID' + datenow_hmsf(), 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'ORIGIN_REQUIRE_ID': 'OREID' + datenow_hmsf(), 'DATA_CHANGE_TIMESTAMP': dateplus_min(5),
               'BUDGET_TYPE': '1'}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_compilation_new'
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
    return key_dic['REQUIRE_ID'], key_dic['ORIGIN_REQUIRE_ID'], key_dic['REQUIRE_PROJECT_NAME']


def intention_notice_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QHQYID',
               'DATA_TIMESTAMP': dateplus_min(5), 'CREATE_TIME': dateplus_min(0),
               'INTENTION_NOTICE_ID': 'INTD' + datenow_hmsf(), 'SUBMIT_ORDER': '1', 'REQUIRE_ID': 'REID20230828165334',
               'DISCLOSURE_METHOD': '3', 'DISCLOSURE_METHOD_NAME': '需要在互联网公开，或脱密后再互联网公开3',
               'TITLE': 'QH测试公告' + datenow_hmsf(), 'IS_SOLICITATION': '0', 'REPORTING_METHOD': '1',
               'IS_PUBLIC_CONTACT': '0', 'LINK_MAN': '测试联系人', 'LINK_PHONE': '13728374384', 'PUBLIC_DAYS': '14',
               'REASONS': '测试主要理由', 'PUBLIC_TIME': dateplus_min(-10), 'PID': 'PID' + time_id(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0), 'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-1投标函",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms'
                   '//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564421702_3997.pdf&fileName=test-0809-js-1投标函.pdf"},'
                   '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-2投标函附录","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564483122_4007.pdf&fileName=test-0809-js-2投标函附录.pdf'
                   '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-3保密承诺书",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564564117_4009.pdf&fileName=test-0809-js-3保密承诺书.pdf'
                   '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-4法定代表人身份证明","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564570809_4015.pdf&fileName=test-0809-js-4'
                   '法定代表人身份证明.pdf"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-5授权委托书","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms'
                   '//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564576168_4017.pdf'
                   '&fileName=test-0809-js-5授权委托书.pdf"}]',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_intention_notice_new'
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
    return key_dic['INTENTION_NOTICE_ID']


def require_survey_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'REQUIRE_SURVEY_ID': 'RSID' + time_id(), 'SUBMIT_ORDER': '1',
               'QUAR_PROJECT_ID': 'QHQPID20230810164439', 'REQUIRE_ID': 'REID20230828165334', 'IS_DEMAND_SURVEY': '0',
               'NOT_SURVEY_REASON': '不需调查的理由', 'SURVEY_TIME': dateplus_min(-9), 'PID': 'PID' + time_id(),
               'REASEARCH_MEMBER': '测试调查小组成员', 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0), 'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-1投标函","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564421702_3997.pdf&fileName=test-0809-js-1投标函.pdf"}]',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_survey_new'
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
    return key_dic['REQUIRE_SURVEY_ID']


def survey_detail_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'REQRESEARCH_DETAIL_ID': 'RDID' + time_id(), 'SUBMIT_ORDER': '1',
               'REQUIRE_SURVEY_ID': 'REQUIRE_SURVEY_ID', 'DEMAND_SURVEY_OBJECT': '需求调查对象1',
               'DEMAND_SURVEY_METHOD_CODE': '1', 'DEMAND_SURVEY_METHOD': '需求调查方式',
               'REQUIRE_SURVEY_DATE': dateplus_min(0), 'CONTENT': dateplus_min(0), 'PID': 'PID' + time_id(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-1投标函","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564421702_3997.pdf&fileName=test-0809-js-1投标函.pdf"},'
                                      '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-2投标函附录","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564483122_4007.pdf&fileName=test-0809-js-2投标函附录.pdf'
                                      '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-3保密承诺书","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564564117_4009.pdf&fileName=test-0809-js-3保密承诺书.pdf'
                                      '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-4法定代表人身份证明","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564570809_4015.pdf&fileName=test-0809-js-4'
                                      '法定代表人身份证明.pdf"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-5授权委托书","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564576168_4017.pdf&fileName=test-0809-js-5授权委托书.pdf"}]',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_survey_detail_new'
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
        cursor.execute(sql_end)
        db.commit()
    except:
        db.rollback()
    db.close()
    return key_dic['REQRESEARCH_DETAIL_ID']


def purchase_demonstration_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'DEMONSTRATION_ID': 'DEMID' + datenow_hmsf(), 'SUBMIT_ORDER': '1',
               'QUAR_PROJECT_ID': 'QHQPID20230810164439', 'REQUIRE_ID': 'REID20230810164521', 'IS_DEMONSTRATION': '0',
               'DEMONSTRATION_TIME': dateplus_min(-8), 'NO_DEMONSTRATION_REASON': '不论证的原因',
               'PID': 'PID' + datenow_hmsf(), 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-1投标函","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564421702_3997.pdf&fileName=test-0809-js-1投标函.pdf"},'
                                      '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-2投标函附录","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564483122_4007.pdf&fileName=test-0809-js-2投标函附录.pdf'
                                      '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-3保密承诺书","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564564117_4009.pdf&fileName=test-0809-js-3保密承诺书.pdf'
                                      '"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-4法定代表人身份证明","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564570809_4015.pdf&fileName=test-0809-js-4'
                                      '法定代表人身份证明.pdf"},{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-5授权委托书","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564576168_4017.pdf&fileName=test-0809-js-5授权委托书.pdf"}]',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_demonstration_new'
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
    return key_dic['DEMONSTRATION_ID']


def demonstration_detail_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'DEMONSTRATION_DETAIL_ID': 'DEMDID' + datenow_hmsf(),
               'SUBMIT_ORDER': '1',
               'DEMONSTRATION_ID': 'DEMID20230831150219', 'DEMONSTRATION_MEMBER_CODE': '1',
               'DEMONSTRATION_MEMBER': '论证参与者', 'EXPERT_NAME': '专家名称1', 'EXPERT_ID_CODE': '28383833838383',
               'EXPERT_PHONE': '13829384374', 'SUPPLIER_NAME': '供应商名称1', 'SUPPLIER_CODE': '供应商CODE1',
               'PID': 'PID' + datenow_hmsf(), 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_demonstration_detail_new'
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
    return key_dic['DEMONSTRATION_DETAIL_ID']


def require_project_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'REQUIREMENT_ID': 'REQ_ID' + datenow_hmsf(), 'SUBMIT_ORDER': 1,
               'QUAR_PROJECT_ID': 'QHQPID20230810164439', 'REQUIRE_ID': 'REID20230810164521',
               'REQUIREMENT_PROJECT_ID': 'RP_ID' + datenow_hmsf(), 'REQUIRE_PROJECT_CODE': 'REQUIRE_PROJECT_CODE',
               'REQUIRE_PROJECT_NAME': 'REQUIRE_PROJECT_NAME', 'PURCHASE_UNIT_CODE': 'qh采购单位代码',
               'PURCHASE_UNIT_NAME': 'qh采购单位名称', 'PURCHASER_YEAR': time_now_year(), 'PROGRAM_BUDGET': 500000,
               'LIMITED_PRICE': 100000, 'EDIT_UNIT': '需求编制单位1', 'EDIT_TIME': dateplus_day_hms(-8),
               'PURCHASE_AGENT_CODE': '采购机构代码1', 'PURCHASE_AGENT_NAME': '采购机构名称1', 'AGENT_TYPE': '2',
               'PROJECT_INTRODUCTION': '项目概况1', 'FEE_CHANNEL': '经费结算渠道1', 'PURCHASE_MODE': '2',
               'PURCHASE_MODE_REASON': '此种采购方式的理由1', 'PROJECT_TYPE': '2',
               'PROJECT_TYPE_NAME': '需求产品分类名称1', 'IMPORTANT_TYPE': '2', 'IMPORTANT_TYPE_NAME': '一般重要',
               'STAGE_TYPE': '1', 'STAGE_TYPE_NAME': '任务阶段名称1', 'COMPLETION_TYPE': '1',
               'COMPLETION_TYPE_NAME': '完成要求名称1', 'ORGANIZATION_TYPE': '1',
               'ORGANIZATION_TYPE_NAME': '组织方式名称1', 'GOODS_RESOURCE_TYPE': '2',
               'GOODS_RESOURCE_TYPE_NAME': '货物来源名称1', 'ENSURE_TYPE': '1', 'ENSURE_TYPE_NAME': '保障任务性质名称1',
               'OTHER_TYPES': '01', 'OTHER_TYPES_NAME': '专业领域名称1', 'PROJECT_NATURE_TOTAL': '',
               'CHECK_ITEM': '合同验收交付要求1', 'DEFAULT_ITEM': '违约责任1', 'DISPUTE_ITEM': '争议处理1',
               'PATENT_ITEM': '保密和专利权要求1', 'SAFETY_ITEM': '安全保密措施1',
               'OTHER_SITUATION': '其他需要说明的情况1', 'DATA_STATUS': '0', 'PID': 'PID' + datenow_hmsf(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'CREATE_TIME': dateplus_min(0),
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-1投标函","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564421702_3997.pdf&fileName=test-0809-js-1投标函.pdf"}]',
               'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QH配套业务管理系统',
               'DATA_TIMESTAMP': dateplus_min(0), 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_project_new'
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
        cursor.execute(sql_end)
        db.commit()
    except:
        db.rollback()
    db.close()
    return key_dic['REQUIREMENT_ID']


def require_section_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': 'QH配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(0),
               'CREATE_TIME': dateplus_min(0), 'REQUIRE_SECTION_ID': 'RS_ID' + datenow_hmsf(), 'SUBMIT_ORDER': 1,
               'REQUIREMENT_ID': 'RE_ID' + datenow_hmsf(), 'REQUIRE_SECTION_CODE': 'RS_CODE' + datenow_hmsf(),
               'REQUIRE_SECTION_NAME': '分包名称1', 'SECTION_BUDGET': 50000, 'SECTION_LIMITED_PRICE': 500000,
               'SETTLEMENT_MODE': '1', 'SETTLEMENT_MODE_NAME': '包定价方式名称1', 'SAMPLE_IF': '1', 'SAMPLE_NUM': '30',
               'SAMPLE_REQ': '样品提交要求1', 'EVALUATION_METHOD': '1', 'CONTRACT_DIVIDED': '0', 'DIVIDE_PROPORTION': 1,
               'UNION_BID_IF': '0', 'PID': 'PID' + time_id(), 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'ORIGIN_SECTION_ID': 'ORIGIN_SECTION_ID', 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_section_new'
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
    return key_dic['REQUIRE_SECTION_ID']


def section_detail_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': 'QH配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(0),
               'CREATE_TIME': dateplus_min(0), 'REQUIRE_SECTION_DETAIL_ID': 'RSD_ID' + datenow_hmsf(),
               'SUBMIT_ORDER': 1,
               'REQUIRE_SECTION_ID': 'RS_ID' + datenow_hmsf(), 'ORDER_NO': 1, 'OBJECT_NAME': '标的名称1',
               'SINGLE_PRICE': 10000, 'PURCHASE_NUM': 50, 'ITEM_UNIT': '个', 'TOTAL_PRICE': 500000,
               'UNIFIED_CODE': '编目码', 'PURCHASE_ITEM_CODE': '采购品目编码' + datenow_hmsf(),
               'PURCHASE_ITEM_NAME': '采购品目名称1', 'SECTION_DETAIL_TYPE': '1', 'IS_SPECIAL_PRODUCT': '1',
               'SPECIAL_PRODUCT_BASIS': '专用产品依据和标准规范', 'IS_PROVIDE_SAMPLE': '1',
               'SAMPLE_REQUIRE': '样品要求与相关事项', 'IS_CORE': '1', 'PID': 'PID' + time_id(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0), 'ORIGIN_SECTION_DETAIL_ID': 'ORIGIN_SECTION_DETAIL_ID',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_section_detail_new'
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
    return key_dic['REQUIRE_SECTION_DETAIL_ID']


def require_notice_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'REQUIRE_NOTICE_ID': 'RN_ID' + datenow_hmsf(),
               'REQUIRE_ID': 'REID20230810164521', 'SUBMIT_ORDER': 1, 'IS_ORGANIZATION': '1', 'PUBLIC_TYPE_CODE': '2',
               'PUBLIC_NAME': '公示名称qhtest', 'PUBLIC_CONTEXT': '公示内容qhtest',
               'SINGLE_REASON': 'qh单一来源采购理由', 'SINGLE_SUPPLIER_NAME': 'qh单一来源供应商名称',
               'SINGLE_SUPPLIER_CODE': '单一来源供应商代码1', 'CONTEXT_FORBID': '0',
               'PUBLISH_TIME': dateplus_day_hms(-6), 'PUBLISH_ORG': '发布单位1', 'DATA_STATUS': '0',
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'CREATE_TIME': dateplus_min(0),
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0), 'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-1投标函",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms'
                   '//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564421702_3997.pdf'
                   '&fileName=test-0809-js-1投标函.pdf"}]',
               'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QH配套业务管理系统',
               'DATA_TIMESTAMP': dateplus_min(0), 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_notice_new'
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
    return key_dic['REQUIRE_NOTICE_ID']


def require_check_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'REQUIRE_CHECK_ID': 'RECID' + datenow_hmsf(),
               'REQUIRE_ID': 'REID20230828165334', 'PLAN_CODE': '计划编号test',
               'PROJECT_NAME': 'qh项目名称' + datenow_hmsf(), 'PURCHASE_UNIT_NAME': 'QH测试采购单位名称',
               'PURCHASE_AGENT_NAME': 'QH测试采购机构名称', 'EXAMINATION_TYPE': '2', 'EXAMINATION_WAY_CODE': '2',
               'EXAMINATION_WAY': '内部审查', 'EXAMINATION_MEMBER': '审查小组成员test', 'EXAMINATION_SECRET_LEVEL': '1',
               'PUBLIC_SCOPE': '1', 'PURCHASE_MODE': '2', 'IS_RESONABLE': '是否合理test', 'MARK': 'QHTEST需要说明事项',
               'EXAMINATION_TIME': dateplus_min(-5), 'PID': 'PID' + time_id(), 'SUBMIT_ORDER': '1',
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"test-0809-js-1投标函",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://119.3.244.32:20311/uploader-gpms'
                   '//download.html?url=/upload'
                   '/commoninfo/2023/8/9/1691564421702_3997.pdf'
                   '&fileName=test-0809-js-1投标函.pdf"}]', 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_check_new'
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
    return key_dic['REQUIRE_CHECK_ID']


def require_submit_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QHQYID',
               'DATA_TIMESTAMP': dateplus_min(5), 'REQUIRE_ID': 'REID20230901153643831', 'STATUS': '6',
               'OPERATE_TYPE': '需求提报', 'OPERATE_USER': 'QHTEST', 'OPERATE_TYPE_RECORD': ' ',
               'BACK_PROBLEM': '测试操作记录', 'BACK_REASON': '测试退回原因', 'REVIEW_TYPE': '3',
               'CREATE_TIME': dateplus_day_hms(-3), 'PID': 'PID' + datenow_hmsf(), 'SUBMIT_ORDER': '1',
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                                      '"ATTACHMENT_NAME":"test-0809-js-1投标函",'
                                      '"ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://119.3.244.32:20311/uploader-gpms'
                                      '//download.html?url=/upload'
                                      '/commoninfo/2023/8/9/1691564421702_3997.pdf'
                                      '&fileName=test-0809-js-1投标函.pdf"}]', 'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
    for key in dic_a:
        key_dic[key] = dic_a[key]
    key_dic['CREATE_TIME'] = dateplus_day_hms(key_dic['CREATE_TIME'])
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_submit_new'
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
