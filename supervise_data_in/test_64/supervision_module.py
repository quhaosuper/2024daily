import allure
import pymysql
import pytest
import yaml
import copy
from .datetimetr import *


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
    key_dic['PURCHASE_AGENT_CODE'] = '采购机构代码qh'
    key_dic['PURCHASE_AGENT_NAME'] = '采购机构代码qh'
    # 采购机构类型 1 采购服务站 2 队属采购机构 9 其他
    key_dic['AGENT_TYPE'] = '2'
    key_dic['AGENT_MANAGEMENT_DEPT'] = 'QHTEST'
    key_dic['AGENT_MANAGEMENT_DEPT_CODE'] = 'QHTEST'
    key_dic['REQUIRE_SUBMIT_TIME'] = dateplus_day_hms(0)
    key_dic['PURCHASE_FINISH_TIME'] = dateplus_min(5)
    key_dic['DELIVER_TIME'] = dateplus_day_hms(10)
    # 计划状态 0 已取消 1 正常下达 2 取消中
    key_dic['PLANNED_STATUS'] = '1'
    # 采购分类 1 物资类 2 服务类 3 工程类
    key_dic['PROJECT_TYPE'] = '2'
    # 项目属性 1 一般采购项目 2 重点采购项目 3 重大项目 4 其他 5 规划项目(一类) 6 规划项目（二类） 7 规划项目（三类） 8 规划项目（四类）
    key_dic['PROJECT_ATTRIBUTE'] = '1'
    # 合并标记 0 未被合并的 1 被合并的 2 合并后的
    key_dic['MERGE_FLAG'] = '2'
    # 提报方式 1 按建制渠道提报 2 跨保障区域提报
    key_dic['REPORTING_METHOD'] = '1'
    key_dic['BASIS_CODE'] = '依据文号test'
    # 是否关联购置计划 1 是 0 否
    key_dic['IS_PURCHASE_PLAN'] = '0'
    key_dic['GZJHBH'] = '购置计划编号' + datenow_hms()
    # 项目通用性 1 专用 2 通用
    key_dic['IS_COMMON'] = '2'
    # 是否下达 1 是 0 否
    key_dic['RELEASE_IF'] = '0'
    # 下达时间
    key_dic['DELIVERY_TIME'] = dateplus_min(15)
    # 数据状态 -1 删除 0 生效 1 作废
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '物资交易系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['EDITOR'] = '编写人1'
    key_dic['EDITOR_TELEPHONE'] = '编写人联系电话1'
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    key_dic['CREATE_USER'] = 'QHTEST'
    key_dic['CREATE_TIME'] = dateplus_min(1)
    key_dic['MODI_USER_ID'] = 'QHTEST'
    key_dic['MODI_USER'] = 'QHTEST'
    key_dic['MODI_TIME'] = dateplus_min(1)
    key_dic['RELATIVE_ATTACHMENT'] = ('[{"ATTACHMENT_TYPE":"PURCHASE_PLAN_YEAR_PDF",'
                                      '"ATTACHMENT_NAME":"年度总体计划提报信息的附件资料1",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"YEAR_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"年度总体计划确认下达1",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"YEAR_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"年度总体计划确认下达2",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]')
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
    key_dic = {}
    key_dic['ID'] = 'ID' + time_id()
    key_dic['PID'] = 'PID' + time_id()
    key_dic['QUAR_PROJECT_ID'] = 'QHQPID' + datenow_hmsf()
    key_dic['YEAR_PROJECT_ID'] = 'QHQYID' + datenow_hmsf()
    key_dic['ORIGIN_QUAR_PROJECT_ID'] = 'OQPID' + datenow_hmsf()
    key_dic['PURCHASE_UNIT_NAME'] = '测试采购单位'
    key_dic['PURCHASE_UNIT_CODE'] = '测试采购单位QH'
    key_dic['PURCHASER_MANAGEMENT_DEPT'] = '测试采购单位采管部门'
    key_dic['PURCHASER_MANAGEMENT_DEPT_CODE'] = '测试采购单位采管部门QH'
    # 规划项目编码
    key_dic['PLANNED_PROJECT_CODE'] = 'PLPC' + datenow_hmsf()
    key_dic['PLAN_YEAR'] = time_now_year()
    key_dic['PLAN_QUARTER'] = '3'
    key_dic['PLAN_MONTH'] = '1'
    key_dic['PLAN_QUAR_PROJECT_CODE'] = 'PQPC' + datenow_hmsf()
    key_dic['PLAN_QUAR_PROJECT_NAME'] = 'qh物资采购季度计划' + datenow_hmsf()
    key_dic['REQUIRE_INTRODUCTION'] = '需求概况'
    key_dic['PROJECT_BUDGET'] = '5000000.2222'
    key_dic['PURCHASE_AGENT_CODE'] = '测试采购机构CODE'
    key_dic['PURCHASE_AGENT_NAME'] = '测试采购机构NAME'
    key_dic['AGENT_TYPE'] = '2'
    key_dic['AGENT_MANAGEMENT_DEPT'] = '测试采购机构采管部门'
    key_dic['AGENT_MANAGEMENT_DEPT_CODE'] = '测试采购机构采管部门CODE'
    key_dic['REQUIRE_SUBMIT_TIME'] = dateplus_day_hms(0)
    key_dic['REQUIRE_SUBMIT_DAY'] = '1'
    key_dic['PURCHASE_FINISH_TIME'] = dateplus_min(-1)
    key_dic['PURCHASE_FINISH_DAY'] = '2'
    key_dic['DELIVER_TIME'] = dateplus_min(0)
    key_dic['DELIVER_DAY'] = '3'
    key_dic['PLAN_CHANGE_REASON'] = '计划调整情况及理由'
    # 计划状态 0 已取消 1 正常下达 2 取消中
    key_dic['PLANNED_STATUS'] = '1'
    key_dic['PROJECT_TYPE'] = '2'
    # 项目属性 1 一般采购项目 2 重点采购项目 3 重大项目 4 其他 5 规划项目(一类) 6 规划项目（二类） 7 规划项目（三类） 8 规划项目（四类）
    key_dic['PROJECT_ATTRIBUTE'] = '2'
    key_dic['PROJECT_ATTRIBUTE_DESC'] = '项目属性描述'
    key_dic['IS_PURCHASE_PLAN'] = '0'
    key_dic['GZJHBH'] = '购置计划编号1' + datenow_hmsf()
    key_dic['MERGE_FLAG'] = '2'
    # 提报方式 1 按建制渠道提报 2 跨保障区域提报
    key_dic['REPORTING_METHOD'] = '1'
    # 统筹调控方式 1 集中归并打包 2 按照项目群集中推送
    key_dic['REGULATORY_METHOD'] = '1'
    key_dic['DATA_STATUS'] = '0'
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = '物资交易系统'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['RELEASE_IF'] = '0'
    # 下达时间
    key_dic['DELIVERY_TIME'] = dateplus_min(15)
    key_dic['EDITOR'] = '编写人1'
    key_dic['EDITOR_TELEPHONE'] = '编写人联系电话1'
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    key_dic['CREATE_USER'] = 'QHTEST'
    key_dic['CREATE_TIME'] = dateplus_min(0)
    key_dic['MODI_USER_ID'] = 'QHTEST'
    key_dic['MODI_USER'] = 'QHTEST'
    key_dic['MODI_TIME'] = dateplus_min(1)
    key_dic['RELATIVE_ATTACHMENT'] = ('[{"ATTACHMENT_TYPE":"PURCHASE_PLAN_QUAR_PDF",'
                                      '"ATTACHMENT_NAME":"季度总体计划提报信息的附件资料",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"季度明细计划确认下达1",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"季度明细计划确认下达2",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]')
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
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
    # 功能环节
    key_dic['FUNCTIONAL_LINKS'] = '功能环节1'
    key_dic['PARTICULARS'] = '详情1'
    key_dic['RELATIVE_ATTACHMENT'] = ('[{"ATTACHMENT_TYPE":"YEAR_PLAN_COMMIT",'
                                      '"ATTACHMENT_NAME":"年度总体计划编制上报",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"YEAR_PLAN_REPORT",'
                                      '"ATTACHMENT_NAME":"年度总体计划汇总上报",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"YEAR_PLAN_CANCEL",'
                                      '"ATTACHMENT_NAME":"年度总体计划取消",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"YEAR_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"年度总体计划确认下达",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_COMMIT",'
                                      '"ATTACHMENT_NAME":"季度明细计划编制上报",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_REPORT”",'
                                      '"ATTACHMENT_NAME":"季度明细计划汇总上报",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_CANCEL",'
                                      '"ATTACHMENT_NAME":"季度总体计划取消",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_RELEASE",'
                                      '"ATTACHMENT_NAME":"季度明细计划确认下达",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_ADJUST",'
                                      '"ATTACHMENT_NAME":"季度明细计划调整",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"QUARTER_PLAN_REGULATE",'
                                      '"ATTACHMENT_NAME":"季度明细计划统筹调控",'
                                      '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]')
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    key_dic['DATA_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    key_dic['DATA_STATUS'] = '0'
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
    return key_dic['PLAN_APPROVAL_ID']


# （新增）建设计划信息
def construction_plan_approval_in(dic_a):
    key_dic = {}
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    # 建设计划信息
    key_dic['CONSTRUCTION_PLAN_ID'] = 'CONPL_ID' + datenow_hms()
    # 年 / 季度明细计划ID
    key_dic['PLAN_PROJECT_ID'] = 'PL_Pro'
    # 建设计划编号
    key_dic['CONSTRUCTION_PLAN_CODE'] = 'CONPL_CODE' + datenow_hms()
    # 计划名称
    key_dic['PLAN_NAME'] = '建设计划名称' + datenow_hms()
    # 计划类型 - 1 年度采购计划, 2 季度明细计划
    key_dic['PLAN_TYPE'] = '1'
    # 计划专业
    key_dic['PLAN_SPECIALTY'] = '计划专业1'
    # 计划年度
    key_dic['PLAN_YEAR'] = '计划年度1'
    # 计划总经费
    key_dic['PLAN_TOTAL_EXPENDITURE'] = 100000
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    # 创建人
    key_dic['CREATE_USER'] = 'QHTEST'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'QHTEST'
    # 更新人
    key_dic['MODI_USER'] = 'QHTEST'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    key_dic['DATA_STATUS'] = '0'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'construction_plan_approval'
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
    return key_dic['CONSTRUCTION_PLAN_ID'], key_dic['CONSTRUCTION_PLAN_CODE'], key_dic['PLAN_NAME']


# （新增）建设计划明细信息
def construction_plan_detail_approval_in(dic_a):
    # 初始化字典
    key_dic = {}
    # 自动生成ID
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    # 建设计划明细信息ID
    key_dic['CONSTRUCTION_PLAN_DETAIL_ID'] = 'CON_PL_DT_ID' + datenow_hms()
    # 建设计划信息ID
    key_dic['CONSTRUCTION_PLAN_ID'] = 'CONPL_ID'
    # 建设计划编号
    key_dic['CONSTRUCTION_PLAN_CODE'] = 'CONPL_CODE'
    # 计划名称
    key_dic['PLAN_NAME'] = '建设计划名称'
    # 建设计划明细编号
    key_dic['CONSTRUCTION_PLAN_DETAIL_CODE'] = 'CON_PL_DT_CODE' + datenow_hms()
    # 物资品种码
    key_dic['MATERIAL_BREED_CODE'] = '物资品种码1'
    # 物资名称
    key_dic['MATERIAL_NAME'] = '物资名称1'
    # 组套编号
    key_dic['STACK_CODE'] = '组套编号1'
    # 组套名称
    key_dic['STACK_NAME'] = '组套名称1'
    # 规格型号
    key_dic['SPECIFICATION_MODEL'] = '规格型号1'
    # 采购渠道
    key_dic['PURCHASE_CHANNEL'] = '采购渠道1'
    # 计量单位
    key_dic['UNIT'] = '计量单位1'
    # 数量
    key_dic['QUANTITY'] = 100
    # 单价（元）
    key_dic['UNIT_PRICE'] = 10000
    # 建设经费（元）
    key_dic['CONSTRUCTION_EXPENDITURE'] = 1000000
    # 计划交货日期
    key_dic['PLAN_DELIVERY_DATE'] = dateplus_min(0)
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    # 创建人
    key_dic['CREATE_USER'] = 'QHTEST'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'QHTEST'
    # 更新人
    key_dic['MODI_USER'] = 'QHTEST'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    key_dic['DATA_STATUS'] = '0'
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    # 数据变更时间戳
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    # 构建SQL语句
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'construction_plan_detail_approval'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
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
               'ORIGIN_REQUIRE_ID': 'REQUIRE_ID', 'DATA_CHANGE_TIMESTAMP': dateplus_min(5),
               'BUDGET_TYPE': '1'}
    key_dic['ORIGIN_REQUIRE_ID'] = key_dic['REQUIRE_ID']
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
               'INTENTION_NOTICE_ID': 'INTD' + datenow_hmsf(), 'SUBMIT_ORDER': 1, 'REQUIRE_ID': 'REID20230828165334',
               'DISCLOSURE_METHOD': '3', 'DISCLOSURE_METHOD_NAME': '需要在互联网公开，或脱密后再互联网公开3',
               'TITLE': '采购意向公告附件', 'IS_SOLICITATION': '0', 'REPORTING_METHOD': '1',
               'IS_PUBLIC_CONTACT': '0', 'LINK_MAN': '测试联系人', 'LINK_PHONE': '13728374384', 'PUBLIC_DAYS': '14',
               'REASONS': '测试主要理由', 'PUBLIC_TIME': dateplus_min(-10), 'PUBLIC_END_TIME': dateplus_min(30),
               'PID': 'PID' + time_id(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0), 'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"INTENTION_NOTICE_ALL",'
                   '"ATTACHMENT_NAME":"意见公开相关附件",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_PART",'
                   '"ATTACHMENT_NAME":"意向公开简化程序核准表",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_PDF",'
                   '"ATTACHMENT_NAME":"采购意向公告附件",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_NONE",'
                   '"ATTACHMENT_NAME":"不需意向公开有关说明或其他补充文件","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"INTENTION_NOTICE_BM",'
                   '"ATTACHMENT_NAME":"采购需求意向公告BM审查表","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"PURCHASE_OPINION_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"采购单位采购机构意见","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['INTENTION_NOTICE_ID']


# 采购意向项目明细
def insert_purchase_intention_detail_new(dic_a):
    # 初始化字典
    key_dic = {}
    # 自动生成ID
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    # 意向项目明细ID
    key_dic['INTENTION_NOTICE_DETAIL_ID'] = 'IN_NO_DT_ID' + datenow_hmsf()
    # 采购意向ID
    key_dic['INTENTION_NOTICE_ID'] = 'INTENTION_NOTICE_ID'
    # 对应需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 明细顺序
    key_dic['ORDER_NO'] = 1
    # 项目品种名称
    key_dic['PRODUCT_NAME'] = '项目品种名称1'
    # 计划采购日期
    key_dic['PLAN_PURCHASE_TIME'] = dateplus_min(0)
    # 预算金额（元）
    key_dic['TOTAL_BUDGET'] = 1000000
    # 采购数量
    key_dic['PURCHASE_NUM'] = 100
    # 计量单位
    key_dic['ITEM_UNIT'] = '计量单位1'
    # 采购内容
    key_dic['PURCHASE_CONTENT'] = '采购内容1'
    # 主要功能或目标
    key_dic['FUNCTION_TARGET'] = '主要功能或目标1'
    # 需满足的要求
    key_dic['DEMAND'] = '需满足的要求1'
    # 初步技术参数
    key_dic['PRE_TECH_PARAMETER'] = '初步技术参数1' + time_id()
    # 意向公开备注
    key_dic['REMARK'] = '意向公开备注' + time_id()
    # 数据状态
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'QHTEST'
    # 创建人
    key_dic['CREATE_USER'] = 'QHTEST'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'QHTEST'
    # 更新人
    key_dic['MODI_USER'] = 'QHTEST'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    # 数据变更时间戳
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    # 构建SQL语句
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_intention_detail_new'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['INTENTION_NOTICE_DETAIL_ID']


# 采购意向公开供应商意见建议
def insert_purchase_intention_advice(dic_a):
    key_dic = {}
    # 定义字段含义并赋值
    # 自动生成ID
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    # 供应商意向建议ID
    key_dic['INTENTION_ADVICE_ID'] = 'IN_ADV_ID' + datenow_hmsf()
    # 采购意向ID
    key_dic['INTENTION_NOTICE_ID'] = 'INTENTION_NOTICE_ID'
    # 对应需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 参与供应商名称
    key_dic['SUPPLIER_NAME'] = '供应商名称1'
    # 参与供应商代码 (法人和其他组织统一社会信用代码编码)
    key_dic['SUPPLIER_CODE'] = '供应商代码1'
    # 参与供应商联系人
    key_dic['CONTACT_PERSON'] = '供应商联系人1'
    # 参与供应商联系人联系电话
    key_dic['TELEPHONE'] = '供应商联系人联系电话1'
    # 反馈内容
    key_dic['ANSWER_CONTENT'] = '反馈内容'
    # 反馈时间
    key_dic['ADVICE_TIME'] = dateplus_min(0)
    # 数据状态 (-1 删除, 0 生效, 1 作废)
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'CREATE_USER_ID'
    # 创建人
    key_dic['CREATE_USER'] = 'CREATE_USER'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'MODI_USER_ID'
    # 更新人
    key_dic['MODI_USER'] = 'MODI_USER'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 相关附件
    key_dic[
        'RELATIVE_ATTACHMENT'] = ('[{"ATTACHMENT_TYPE":"INTENTION_ADVICE_ATTACHMENT",'
                                  '"ATTACHMENT_NAME":"供应商反馈意见1",'
                                  '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'
                                  )
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    # 数据变更时间戳
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    # 构建SQL语句
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_intention_advice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['INTENTION_ADVICE_ID']


# 意向公开信息查看
def insert_intent_public_info_check(dic_a):
    key_dic = {}
    # 自动生成ID
    key_dic['ID'] = 'ID' + datenow_hms()
    key_dic['PID'] = 'PID' + datenow_hms()
    # 意向查看ID
    key_dic['INTENTION_VIEW_ID'] = 'IN_VI_ID' + datenow_hmsf()
    # 操作日期
    key_dic['OPERATION_DATE'] = dateplus_min(0)
    # 经办人ID
    key_dic['OPERATOR_ID'] = 'OPERATOR_ID'
    # 经办人
    key_dic['OPERATOR'] = 'OPERATOR'
    # 操作类型
    key_dic['OPERATION_TYPE'] = '操作类型1'
    # 记录
    key_dic['RECORD'] = '记录1'
    # 数据状态 (-1 删除, 0 生效, 1 作废)
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'CREATE_USER_ID'
    # 创建人
    key_dic['CREATE_USER'] = 'CREATE_USER'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'MODI_USER_ID'
    # 更新人
    key_dic['MODI_USER'] = 'MODI_USER'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'GO-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'quhaotestname'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    # 数据变更时间戳
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'intention_public_information_check'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()


def require_survey_in(dic_a):
    key_dic = {'ID': 'ID' + time_id(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': '配套业务管理系统', 'DATA_TIMESTAMP': dateplus_min(5),
               'CREATE_TIME': dateplus_min(0), 'REQUIRE_SURVEY_ID': 'RSID' + time_id(), 'SUBMIT_ORDER': '1',
               'QUAR_PROJECT_ID': 'QHQPID20230810164439', 'REQUIRE_ID': 'REID20230828165334', 'IS_DEMAND_SURVEY': '0',
               'NOT_SURVEY_REASON': '不需调查的理由', 'SURVEY_TIME': dateplus_min(-9), 'PID': 'PID' + time_id(),
               'REASEARCH_MEMBER': '测试调查小组成员', 'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0), 'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"REQUIRE_SURVEY_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"需求调查报告","ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
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
               'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"REQRESEARCH_DETAIL_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"调查对象其他资料1",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"REQRESEARCH_DETAIL_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"调查对象其他资料2",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"REQRESEARCH_DETAIL_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"调查对象其他资料3",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
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
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"DEMONSTRATION_REPORT",'
                                      '"ATTACHMENT_NAME":"专项论证报告1","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"DEMONSTRATION_REPORT",'
                                      '"ATTACHMENT_NAME":"专项论证报告2","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
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
               'SUBMIT_ORDER': 1,
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
               'CEILING_PRICE_IF': '1', 'LIMITED_PRICE': 100000, 'EDIT_UNIT': '需求编制单位1',
               'EDIT_TIME': dateplus_day_hms(
                   -8),
               'PURCHASE_AGENT_CODE': '采购机构代码1', 'PURCHASE_AGENT_NAME': '采购机构名称1', 'AGENT_TYPE': '2',
               'PROJECT_INTRODUCTION': '项目概况1', 'FEE_CHANNEL': '经费结算渠道1', 'PURCHASE_MODE': '2',
               'PURCHASE_MODE_REASON': '此种采购方式的理由1', 'PROJECT_TYPE': '2',
               'PROJECT_TYPE_NAME': '需求产品分类名称1', 'IMPORTANT_TYPE': '2', 'IMPORTANT_TYPE_NAME': '一般重要',
               'STAGE_TYPE': '1', 'STAGE_TYPE_NAME': '任务阶段名称1', 'COMPLETION_TYPE': '1',
               'COMPLETION_TYPE_NAME': '完成要求名称1', 'ORGANIZATION_TYPE': '1', 'IF_SITE_SURVEY': '1',
               'ORGANIZATION_TYPE_NAME': '组织方式名称1', 'GOODS_RESOURCE_TYPE': '2',
               'GOODS_RESOURCE_TYPE_NAME': '货物来源名称1', 'ENSURE_TYPE': '1', 'ENSURE_TYPE_NAME': '保障任务性质名称1',
               'OTHER_TYPES': '01', 'OTHER_TYPES_NAME': '专业领域名称1', 'OPERATION_TYPE': '1', 'OPERATION_TYPE_NAME':
                   '分阶段招投标名称', 'PROJECT_NATURE_TOTAL': '任务性质1',
               'CHECK_ITEM': '合同验收交付要求1', 'DEFAULT_ITEM': '违约责任1', 'DISPUTE_ITEM': '争议处理1',
               'PATENT_ITEM': '保密和专利权要求1', 'SAFETY_ITEM': '安全保密措施1',
               'OTHER_SITUATION': '其他需要说明的情况1', 'DATA_STATUS': '0', 'PID': 'PID' + datenow_hmsf(),
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'CREATE_TIME': dateplus_min(0),
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"REQUIREMENT_DOC",'
                                      '"ATTACHMENT_NAME":"采购需求文件1","ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
               'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QH配套业务管理系统',
               'DATA_TIMESTAMP': dateplus_min(0), 'DATA_CHANGE_TIMESTAMP': dateplus_min(5), 'BUDGET_TYPE': '1'}
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
               'ORIGIN_SECTION_ID': 'ORIGIN_SECTION_ID', 'DATA_CHANGE_TIMESTAMP': dateplus_min(5), 'IF_SITE_SURVEY':
                   '1'}
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
    key_dic = {'ID': 'ID' + datenow_hmsf(),
               'DATA_STATUS': '0',
               'DATA_SOURCE_CODE': 'RE-001',
               'DATA_SOURCE_NAME': 'QH配套业务管理系统',
               'DATA_TIMESTAMP': dateplus_min(0),
               'CREATE_TIME': dateplus_min(0),
               'REQUIRE_SECTION_DETAIL_ID': 'RSD_ID' + datenow_hmsf(),
               'SUBMIT_ORDER': 1,
               'REQUIRE_SECTION_ID': 'RS_ID' + datenow_hmsf(),
               'ORDER_NO': 1,
               'OBJECT_NAME': '标的名称1',
               'SINGLE_PRICE': 10000,
               'PURCHASE_NUM': 50,
               'ITEM_UNIT': '个',
               'TOTAL_PRICE': 500000,
               'UNIFIED_CODE': '编目码',
               'PURCHASE_ITEM_CODE': '采购品目编码' + datenow_hmsf(),
               'PURCHASE_ITEM_NAME': '采购品目名称1',
               'SECTION_DETAIL_TYPE': '1',
               'IS_SPECIAL_PRODUCT': '1',
               'SPECIAL_PRODUCT_BASIS': '专用产品依据和标准规范',
               'IS_PROVIDE_SAMPLE': '1',
               'SAMPLE_REQUIRE': '样品要求与相关事项',
               'IS_CORE': '1',
               'PID': 'PID' + time_id(),
               'CREATE_USER_ID': 'QHTEST',
               'CREATE_USER': 'QHTEST',
               'MODI_USER_ID': 'QHTEST',
               'MODI_USER': 'QHTEST',
               'MODI_TIME': dateplus_min(0),
               'ORIGIN_SECTION_DETAIL_ID': 'ORIGIN_SECTION_DETAIL_ID',
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
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.rollback()
    db.close()
    return key_dic['REQUIRE_SECTION_DETAIL_ID']


# 采购需求-技术要求（标的技术参数）
def insert_purchase_tech_parameter(dic_a):
    key_dic = {}
    # 自动生成ID
    key_dic['ID'] = 'ID' + datenow_hmsf()
    key_dic['PID'] = 'PID' + datenow_hmsf()
    # 标的技术参数ID
    key_dic['OBEJECT_TECH_PARAMETER_ID'] = 'OB_TE_PA_ID' + datenow_hmsf()
    # 需求拟制_分包标的明细ID
    key_dic['REQUIRE_SECTION_DETAIL_ID'] = 'REQUIRE_SECTION_DETAIL_ID'
    # 对应需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 参数序号
    key_dic['ORDER_NO'] = 1
    # 参数名称
    key_dic['PARAMETER_NAME'] = '参数名称1'
    # 参数值
    key_dic['PARAMETER_VALUE'] = '参数值1'
    # 技术要求类型 (1 无标识, 2 星号标识（实质性要求）, 3 三角标识（重点要求）)
    key_dic['STANDARD_TYPE'] = '1'
    # 数据状态 (-1 删除, 0 生效, 1 作废)
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'CREATE_USER_ID'
    # 创建人
    key_dic['CREATE_USER'] = 'CREATE_USER'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'MODI_USER_ID'
    # 更新人
    key_dic['MODI_USER'] = 'MODI_USER'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'RE-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'QH配套业务管理系统'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    columns = ', '.join(key_dic.keys())
    values = ', '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in key_dic.values()])
    sql_insert = f"INSERT INTO PURCHASE_TECH_PARAMETER ({columns}) VALUES ({values})"
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_insert)
    db.commit()
    db.close()
    return key_dic['OBEJECT_TECH_PARAMETER_ID']


# 采购需求拟制_分包供应商资格要求
def insert_purchase_require_supplier_qual_new(dic_a):
    key_dic = {}
    # 添加ID
    key_dic['ID'] = 'ID' + datenow_hmsf()
    # 添加PID
    key_dic['PID'] = 'PID' + datenow_hmsf()
    # 供应商资格要求ID
    key_dic['REQUIRE_SECTION_SUPPLIER_QUAL_ID'] = 'RE_SE_SP_QU_ID' + datenow_hmsf()
    # 需求拟制ID
    key_dic['REQUIREMENT_ID'] = 'REQ_ID'
    # 采购需求项目分包ID
    key_dic['REQUIRE_SECTION_ID'] = 'REQ_SEC_ID'
    # 对应需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 资格要求类型 1 供应商一般资格要求, 2 供应商特殊资格要求
    key_dic['SUPPLIER_QUAL_TYPE'] = '1'
    # 序号
    key_dic['ORDER_NO'] = 1
    # 资格要求名称
    key_dic['SUPPLIER_QUAL_NAME'] = '资格要求名称1'
    # 资格要求详细说明
    key_dic['SUPPLIER_QUAL_DETAIL'] = '资格要求详细说明1'
    # 数据状态 -1 删除, 0 生效, 1 作废
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'CREATE_USER_ID'
    # 创建人
    key_dic['CREATE_USER'] = 'CREATE_USER'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'MODI_USER_ID'
    # 更新人
    key_dic['MODI_USER'] = 'MODI_USER'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'RE-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'QH配套业务管理系统'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_supplier_qual_new'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['REQUIRE_SECTION_SUPPLIER_QUAL_ID']


# insert_purchase_require_supplier_qual_new({'DATA_STATUS':'0'})


# 采购需求拟制-经济要求
def insert_require_contract_payment(dic_a):
    key_dic = {}
    # 添加ID
    key_dic['ID'] = 'ID' + datenow_hmsf()
    # 添加PID
    key_dic['PID'] = 'PID' + datenow_hmsf()
    # 经济要求ID
    key_dic['ECO_ID'] = 'ECO_ID' + datenow_hmsf()
    # 需求拟制ID
    key_dic['REQUIREMENT_ID'] = 'REQ_ID'
    # 采购需求项目分包ID
    key_dic['REQUIRE_SECTION_ID'] = 'REQ_SEC_ID'
    # 对应需求对接轮次
    key_dic['SUBMIT_ORDER'] = 1
    # 经济要求序号
    key_dic['ECO_ORDER'] = 1
    # 经济要求性质 1 无标识 2 星号标识
    key_dic['ECO_NATURE'] = '1'
    # 经济要求类型编码 01交货时间、地点与方式 02产品包装和运输要求 03 售后服务 04 知识产权和保密要求 05 物资编目编码、打码贴签要求
    # 06付款及结算方式 07履约保证金和质量保证金 08备品备件要求 99其他
    key_dic['ECO_TYPE_CODE'] = '01'
    # 经济要求类型名称
    key_dic['ECO_TYPE_NAME'] = '经济要求类型名称1'
    # 要求说明
    key_dic['ECO_DETAIL'] = '要求说明1'
    # 付款及结算方式 1 无预付款 2 有预付款 3 分阶段付款 9 其他
    key_dic['PAYMENT_TYPE'] = '1'
    # 预付款描述
    key_dic['PRE_PAYMENT_DETAIL'] = '[{"PRE_PAY_PROPORTION":20,"PAY_LIMIT":5000000}]'
    # 分阶段付款描述
    key_dic['DIVIDED_PAYMENT_DETAIL'] = '[{"STAGE":1,"STAGE_REQ":"阶段要求","PAY_PROPORTION":30,"PAY_BASIS":"结算依据"}]'
    # 其他类型付款描述
    key_dic['OTHER_PAYMENT_DETAIL'] = '其他类型付款描述1'
    # 数据状态 -1 删除, 0 生效, 1 作废
    key_dic['DATA_STATUS'] = '0'
    # 创建人ID
    key_dic['CREATE_USER_ID'] = 'CREATE_USER_ID'
    # 创建人
    key_dic['CREATE_USER'] = 'CREATE_USER'
    # 创建时间
    key_dic['CREATE_TIME'] = dateplus_min(0)
    # 更新人ID
    key_dic['MODI_USER_ID'] = 'MODI_USER_ID'
    # 更新人
    key_dic['MODI_USER'] = 'MODI_USER'
    # 更新时间
    key_dic['MODI_TIME'] = dateplus_min(0)
    # 数据来源代码
    key_dic['DATA_SOURCE_CODE'] = 'RE-001'
    # 数据来源名称
    key_dic['DATA_SOURCE_NAME'] = 'QH配套业务管理系统'
    # 数据时间戳
    key_dic['DATA_TIMESTAMP'] = dateplus_min(0)
    key_dic['DATA_CHANGE_TIMESTAMP'] = dateplus_min(5)
    # 将传入的字段值更新到字典中
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_contract_payment'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['ECO_ID']


def require_notice_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'PID': 'PID' + datenow_hmsf(), 'REQUIRE_NOTICE_ID': 'RN_ID' +
                                                                                                datenow_hmsf(),
               'REQUIRE_ID': 'REID20230810164521', 'SUBMIT_ORDER': 1, 'IS_ORGANIZATION': '1', 'PUBLIC_TYPE_CODE': '2',
               'PUBLIC_NAME': '公示名称qhtest', 'PUBLIC_CONTEXT': '公示内容qhtest',
               'SINGLE_REASON': 'qh单一来源采购理由', 'SINGLE_SUPPLIER_NAME': 'qh单一来源供应商名称',
               'SINGLE_SUPPLIER_CODE': '单一来源供应商代码1', 'CONTEXT_FORBID': '0',
               'PUBLISH_TIME': dateplus_day_hms(-6), 'PUBLISH_ORG': '发布单位1', 'DATA_STATUS': '0',
               'CREATE_USER_ID': 'QHTEST', 'CREATE_USER': 'QHTEST', 'CREATE_TIME': dateplus_min(0),
               'MODI_USER_ID': 'QHTEST', 'MODI_USER': 'QHTEST', 'MODI_TIME': dateplus_min(0),
               'RELATIVE_ATTACHMENT':
                   '[{"ATTACHMENT_TYPE":"REQUIRE_NOTICE_ATTACHMENT",'
                   '"ATTACHMENT_NAME":"需求公示相关资料",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"REQUIRE_NOTICE_BM",'
                   '"ATTACHMENT_NAME":"需求公示BM审查表",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                   '{"ATTACHMENT_TYPE":"REQUIRE_NOTICE_PDF",'
                   '"ATTACHMENT_NAME":"需求公示预览PDF文件",'
                   '"ATTACHMENT_FORM":"pdf",'
                   '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
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
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['REQUIRE_NOTICE_ID']


def require_check_in(dic_a):
    key_dic = key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'RE-001',
        'DATA_SOURCE_NAME': '配套业务管理系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'CREATE_TIME': dateplus_min(0),
        'REQUIRE_CHECK_ID': 'RECID' + datenow_hmsf(),
        'REQUIRE_ID': 'REID20230828165334',
        'PLAN_CODE': '计划编号test',
        'PROJECT_NAME': 'qh项目名称' + datenow_hmsf(),
        'PURCHASE_UNIT_NAME': 'QH测试采购单位名称',
        'PURCHASE_AGENT_NAME': 'QH测试采购机构名称',
        'EXAMINATION_TYPE': '2',
        'EXAMINATION_WAY_CODE': '2',
        'EXAMINATION_WAY': '内部审查',
        'EXAMINATION_MEMBER': '审查小组成员test',
        'EXAMINATION_SECRET_LEVEL': '1',
        'PUBLIC_SCOPE': '1',
        'PURCHASE_MODE': '2',
        'IS_RESONABLE': '是否合理test',
        'MARK': 'QHTEST需要说明事项',
        'EXAMINATION_TIME': dateplus_min(-5),
        'PID': 'PID' + time_id(),
        'SUBMIT_ORDER': '1',
        'CREATE_USER_ID': 'QHTEST',
        'CREATE_USER': 'QHTEST',
        'MODI_USER_ID': 'QHTEST',
        'MODI_USER': 'QHTEST',
        'MODI_TIME': dateplus_min(0),
        'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"REQUIRE_CHECK_ATTACHMENT","ATTACHMENT_NAME":"需求审查相关资料",'
                               '"ATTACHMENT_FORM":"pdf",'
                               '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                               '{"ATTACHMENT_TYPE":"BM_CHECK_ATTACHMENT","ATTACHMENT_NAME":"BM审查相关资料",'
                               '"ATTACHMENT_FORM":"pdf",'
                               '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_require_check_new'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['REQUIRE_CHECK_ID']


print(require_check_in({'PUBLIC_SCOPE': '1'}))


def require_submit_in(dic_a):
    key_dic = {'ID': 'ID' + datenow_hmsf(), 'DATA_STATUS': '0', 'DATA_SOURCE_CODE': 'RE-001', 'DATA_SOURCE_NAME': 'QHQYID',
               'DATA_TIMESTAMP': dateplus_min(5), 'REQUIRE_ID': 'REID20230901153643831', 'STATUS': '6',
               'OPERATE_TYPE': '需求提报', 'OPERATE_USER': 'QHTEST', 'OPERATE_USER_UNIT': '经办人所在单位',
               'OPERATE_TYPE_RECORD':
                   '操作记录',
               'BACK_PROBLEM': '测试操作记录', 'BACK_REASON': '测试退回原因', 'REVIEW_TYPE': '3',
               'CREATE_TIME': dateplus_day_hms(-4), 'PID': 'PID' + datenow_hmsf(), 'SUBMIT_ORDER': '1',
               'RELATIVE_ATTACHMENT': '[{"ATTACHMENT_TYPE":"REQUIRE_SUBMIT_LETTER",'
                                      '"ATTACHMENT_NAME":"需求提报函",'
                                      '"ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://10.0.168.64/supervision-web/#/login"},'
                                      '{"ATTACHMENT_TYPE":"REQUIRE_SUBMIT_OTHER",'
                                      '"ATTACHMENT_NAME":"需求提报其他资料",'
                                      '"ATTACHMENT_FORM":"pdf",'
                                      '"URL":"http://10.0.168.64/supervision-web/#/login"}]',
               'DATA_CHANGE_TIMESTAMP': dateplus_min(5)}
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
    # 连接数据库并执行SQL语句
    db = pymysql.connect(host='10.0.168.47', port=3306, user='root', password='123qwe!@#', database='gld_ods_govp_new')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_end)
    db.commit()
    db.close()
    return key_dic['ID']


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
    return key_dic['REQUIRMENT_FIRST_APPROVAL_ID'], key_dic['REQUIREMENT_PROXY_ID']


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
