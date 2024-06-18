import pymysql
from test_0630.supervise_data_in.test_64.datetimetr import *


# 合同建议方案拟制
def contract_edit_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID' + datenow_hmsf(),
        'PURCHASE_PROJECT_ID': 'PP_ID' + datenow_hmsf(),
        'PURCHASE_SECTION_ID': 'PS_ID' + datenow_hmsf(),
        'PURCHASE_PROJECT_CODE': 'PP_CODE' + datenow_hmsf(),
        'PURCHASE_PROJECT_NAME': 'QH测试' + datenow_hmsf() + '项目',
        'PURCHASE_SECTION_CODE': 'QH-' + datenow_hmsf(),
        'PURCHASE_SECTION_NAME': '测试采购包' + datenow_hmsf(),
        'DRAFTING_UNIT': '起草单位',
        'DRAFTPERSON': '起草人',
        'PURCHASE_AGENT_CODE': '采购机构代码',
        'PURCHASE_AGENT_NAME': '采购机构名称',
        'PURCHASE_UNIT_CODE': '采购单位代码',
        'PURCHASE_UNIT_NAME': '采购单位名称',
        'DRAFTING_BEGIN_TIME': dateplus_min(5),
        'DRAFTING_TIME': dateplus_min(5),
        # 1 物资服务电子招投标系统 2 工程电子招投标系统 3 线下项目登记系统 4 A系统(预先采购结果) 5 应急采购(战略合作协议) 6 自行采购平台
        # 7 手工录入
        'PURCHASE_RESULT_SOURCE': '1',
        'PURCHASE_RESULT': '是',
        'PROJECT_YEAR': '2024',
        # 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源 6 执行采购结果 7 网上采购 8 其它 9 直接面向市场采购
        'PROCUREMENT_METHOD': '1',
        # 1 采购服务站集中采购 2 采购单位队属力量组织 3 委托第三方采购代理机构组织 4 其它
        'ORGANIZATIONAL_FORM': '1',
        # 1 物资类 2 服务类 3 工程类
        'MATERIAL_CATEGORY': '1',
        # 1 集中采购 2 自行采购
        'PROCUREMENT_TYPE': '1',
        'TIME_OF_NOTICE': dateplus_min(5),
        'PROTOCOL_NAME': '合同/协议名称' + datenow_hmsf(),
        'PROTOCOL_NUMBER': '合同/协议编号' + datenow_hmsf(),
        # 合同/协议有无具体金额 0 否 1 是
        'EXACT_AMOUNT_IF': '1',
        'EXACT_AMOUNT': '1000000',
        # 合同/协议有无具体金额 0 否 1 是
        'AGREEMENT_REVIEW_IF': '1',
        # 有无杂用费 0 否 1 是
        'FREIGHT_IF': '1',
        'PARTY_CODE': '甲方单位编码' + datenow_hmsf(),
        'PARTY_NAME': '甲方单位',
        'PARTY_LEGALER': '甲方法定代表人',
        'PARTY_ENTRUSTER': '甲方委托代理人',
        'PARTY_ENTRUSTER_TELPHONE': '甲方委托代理人联系方式',
        'PARTY_PROXY': '甲方联系人',
        'PARTY_TELPHONE': '甲方联系电话',
        'PARTY_ADDRESS': '甲方通讯地址',
        'PARTY_POSTAL_CODE': '甲方通讯地址',
        'PARTY_ACCOUNT_NAME': '甲方开户名称',
        'PARTY_BANK_NAME': '甲方开户银行',
        'PARTY_BANK_NO': '甲方开户银行',
        'PARTY_SUPPLIER_CODE': '甲方统一社会信用代码',
        'SUPPLIER_CODE': '乙方单位编码',
        'SUPPLIER_NAME': '乙方单位',
        'SUPPLIER_LEGALER': '乙方法定代表人',
        'SUPPLIER_ENTRUSTER': '乙方委托代理人',
        'SUPPLIER_ENTRUSTER_TELPHONE': '乙方委托代理人联系方式',
        'SUPPLIER_PROXY': '乙方联系人',
        'SUPPLIER_TELPHONE': '乙方联系电话',
        'SUPPLIER_ADDRESS': '乙方通讯地址',
        'SUPPLIER_POSTAL_CODE': '乙方邮政编码',
        'SUPPLIER_ACCOUNT_NAME': '乙方开户名称',
        'SUPPLIER_BANK_NAME': '乙方开户名称',
        'SUPPLIER_BANK_NO': '乙方银行账号',
        'SUPPLIER_PARTY_CODE': '乙方统一社会信用代码',
        # 合同创建方式 1 通过系统拟制 2 线下拟制上传系统
        'CONTRACT_CREATE_METHOD': '1',
        # 约定方式 1 限期完成履约 2 固定期限履约 3 分阶段性 / 分周期性履约 4 其他方式
        'SELECT_STIPULATED_FORM': '1',
        # 是否需要中标供应商确认 0 否 1 是
        'IS_WINNING_SUPPLIER_CONFIRMATION': '1',
        'FORWARDING_TIME': dateplus_min(5),
        'SUPPLIER_CONFIRMATION_TIME': dateplus_min(5),
        # 1 分阶段付款 2 一次性支付 3 无支付款项 4 其它
        'SETTLEMENT_MODES': '1',
        # 版本类型 V1 旧版 ZK 紫光 V2 新版
        'VERSION_TYPE': 'V1',
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"DRAFT_CONTRACT_DOCUMENT","ATTACHMENT_NAME":"合同草案文件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_DRAFTING_DATA","ATTACHMENT_NAME":"合同拟制依据资料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PROJECT_REPORT_FORM","ATTACHMENT_NAME":"采购项目情况报告表",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"OTHER_FILES","ATTACHMENT_NAME":"其它文件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PROTOCOL_PROPOSAL","ATTACHMENT_NAME":"合同/协议建议方案",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PROTOCOL_PROPOSAL_SEAL","ATTACHMENT_NAME":"合同/协议建议方案盖章",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"TENDER_FILE","ATTACHMENT_NAME":"招标文件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"SUPPLIER_TENDER_FILE","ATTACHMENT_NAME":"供应商招标文件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"REVIEW_FILE","ATTACHMENT_NAME":"评审过程资料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"BID_WINNING_NOTICE","ATTACHMENT_NAME":"BID_WINNING_NOTICE",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_edit'
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
    return key_dic['CONTRACT_EDIT_ID']


# purchase_contract_edit_in({'DATA_STATUS': '0'})


# 合同履约期限
def contract_object_detail_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_OBJECT_DETAIL_ID': 'CON_OBDT_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'PUR_CATALOG_CODE': 'PU_CAL_ID' + datenow_hmsf(),
        'PUR_CATALOG_NAME': 'PU_CAL_NAME' + datenow_hmsf(),
        'PRODUCT_NAME': '货物名称/产品名称',
        'UNIT': '计量单位',
        'PURCHASE_NUM': 100,
        'PRICE': 100000,
        'TOTLE_PRICE': 100000000,
        'BRAND': '品牌',
        'SPEC': '规格型号',
        'GOOD_CODE': '统一编目码',
        'REMARK': '备注',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_object_detail'
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


# purchase_contract_object_detail_in({'DATA_STATUS': '0'})


# 合同履约期限
def contract_archive_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_ARCHIVE_ID': 'CON_ACV_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'SPECIFIC_REQUIREMENTS': '具体要求1111111231313131313131',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_archive'
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


# purchase_contract_archive_in({'DATA_STATUS': '0'})


# 合同交付验收
def contract_delivery_acceptance_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_ARCHIVE_ID': 'CON_ACV_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        # 1 本单位自行组织 2 邀请相关专业专家组织 3 委托代理机构或军队专业检验机构组织 4 委托地方专业校验机构组织 5 其它
        'ORGANIZATION_TYPE': '1',
        # 1 物资采购合同-组织首次或首批检验 2 物资采购合同-出厂检验 3 物资采购合同-到货检验 4 物资采购合同-分批检验 5 物资采购合同-安装调试检验
        # 6 物资采购合同-配套服务检验 7 物资采购合同-其它 8 服务采购合同-分期考核 9 服务采购合同-不定期抽检评估 10 服务采购合同-其它
        # 11 工程采购合同-按照行业规定组织竣工验收 12 工程采购合同-其它
        'QUALITY_REQUIREMENT': '1',
        'SPECIFIC_DELIVERY_ACCEPTANCE_CLAUSE': '具体交付验收条款',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_delivery_acceptance'
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


# contract_delivery_acceptance_in({'DATA_STATUS': '0'})

# 合同支付与结算
def contract_pay_closing_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_PAY_CLOSING_ID': 'CON_PCL_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'MAIN_STAGES_AND_PAYMENT_REQUIREMENTS': '主要阶段及支付要求1111111',
        'PAYMENT_RATIO': 0.12,
        'PAYMENT_AMOUNT': 100000,
        # 1 预付款 2 质保金 3 阶段付款
        'TYPE': '1',
        'SPECIFIC_PAYMENT_TERMS': '具体支付条款',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_pay_closing'
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


# contract_pay_closing_in({'DATA_STATUS': '0'})

# 合同支付与结算
def contract_proposal_approval_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_PROPOSAL_APPROVAL_ID': 'CON_PAP_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'TRADE_STEP': '核验环节',
        'COMMITTER_NAME': '操作人姓名',
        'COMMITTER_ID': '操作人证件ID',
        'COMMITTER_UNIT': '操作人所在单位',
        'COMMITTER_UNIT_CODE': '操作人所在单位代码',
        # 1 采购服务站 2 采购单位
        'EDIT_DEPT_TYPE': '1',
        'COMMITTER_DEPT': '操作人所在部门',
        'COMMITTER_DEPT_CODE': '操作人所在部门代码',
        'COMMIT_TIME': dateplus_min(0),
        # 1 发起 2 撤回 3 审核通过 4 审核不通过
        'COMMIT_TYPE': '1',
        # 0 不同意 1 同意
        'APPROVAL_RESULT': '1',
        'APPROVAL_OPINION': '审批意见',
        'RECORD': '记录11111111111',
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"CONTRACT_PROPOSAL_APPROVAL","ATTACHMENT_NAME":"合同建议方案审核单",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_PROPOSAL_REVIEW_SHEET","ATTACHMENT_NAME":"合同方案意见审核单",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"DRAFT_CONTRACT_DOCUMENT","ATTACHMENT_NAME":"合同草案文件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_proposal_approval'
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


# contract_proposal_approval_in({'DATA_STATUS': '0'})


# 合同订立
def contract_conclusion_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_PLAN_ID': 'CON_PLA_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'PROTOCOL_NAME': '合同/协议名称1',
        'PROTOCOL_NUMBER': '合同/协议编号1',
        'EXACT_AMOUNT': '1000000',
        # 项目信息是否存在变更 0 存在变更 1 一致
        'IS_PROJECT_CHANGE': '1',
        'PROJECT_EXPLAIN': '项目信息变更说明1',
        # 合同标的是否存在变更 0 存在变更 1 一致
        'IS_OBJECT_CHANGE': '1',
        'OBJECT_EXPLAIN': '合同标的变更说明',
        # 当事人信息是否存在变更 0 存在变更 1 一致
        'IS_PARTIES_CHANGE': '1',
        'PARTIES_EXPLAIN': '当事人信息变更说明',
        # 合同条款是否存在变更 0 存在变更 1 一致
        'IS_CLAUSE_CHANGE': '1',
        'SIGN_TIME': dateplus_min(5),
        # 约定方式 1 限期完成履约 2 固定期限履约 3 分阶段性/分周期性履约 4 其他方式
        'SELECT_STIPULATED_FORM': '1',
        # 付款及结算方式 1 分阶段付款 2 一次性支付 3 无支付款项 4 其它
        'SETTLEMENT_MODES': '1',
        'CONCLUSION_END_TIME': dateplus_min(5),
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"DULY_SEALED_CONTRACT","ATTACHMENT_NAME":"正式盖章合同1",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"DULY_SEALED_CONTRACT","ATTACHMENT_NAME":"正式盖章合同2",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"DULY_SEALED_CONTRACT","ATTACHMENT_NAME":"正式盖章合同3",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_conclusion'
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
    return key_dic['CONTRACT_PLAN_ID']


# contract_conclusion_in({'DATA_STATUS': '0'})


# 合同履约计划
def contract_project_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_PROJECT_ID': 'CON_PRO_ID' + datenow_hmsf(),
        'CONTRACT_PLAN_ID': 'CON_PLA_ID',
        'PLAN_TIME': dateplus_min(0),
        'SPECIFIC_REQUIREMENTS': '具体要求asdadadsasdsadad2387819839849719841984109',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_project'
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


# contract_project_in({'DATA_STATUS': '0'})

# 合同交付验收计划
def contract_delivery_project_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_DELIVERY_PROJECT_ID': 'CON_DL_PRO_ID' + datenow_hmsf(),
        'CONTRACT_PLAN_ID': 'CON_PLA_ID',
        'PLAN_TIME': dateplus_min(0),
        # 组织方式 1 本单位自行组织 2 邀请相关专业专家组织 3 委托代理机构或军队专业检验机构组织 4 委托地方专业校验机构组织 5 其它
        'ORGANIZATION_TYPE': '1',
        # 验收方式 1 物资采购合同-组织首次或首批检验 2 物资采购合同-出厂检验 3 物资采购合同-到货检验 4 物资采购合同-分批检验 5 物资采购合同-安装调试检验
        # 6 物资采购合同-配套服务检验 7 物资采购合同-其它 8 服务采购合同-分期考核 9 服务采购合同-不定期抽检评估 10 服务采购合同-其它
        # 11 工程采购合同-按照行业规定组织竣工验收 12 工程采购合同-其它
        'QUALITY_REQUIREMENT': '1',
        'SPECIFIC_DELIVERY_ACCEPTANCE_CLAUSE': '具体交付验收条款1',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_delivery_project'
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


# contract_delivery_project_in({'DATA_STATUS': '0'})

# 合同支付与结算计划
def contract_pay_project_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_PAY_PROJECT_ID': 'CON_PY_PRO_ID' + datenow_hmsf(),
        'CONTRACT_PLAN_ID': 'CON_PLA_ID',
        'PLAN_TIME': dateplus_min(0),
        'MAIN_STAGES_AND_PAYMENT_REQUIREMENTS': '主要阶段及支付要求1',
        'PAYMENT_RATIO': 0.23,
        'PAYMENT_AMOUNT': 1000000,
        # 类型 1 预付款 2 质保金 3 阶段付款
        'TYPE': '1',
        'SPECIFIC_PAYMENT_TERMS': '具体支付条款1',
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_pay_project'
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


# contract_pay_project_in({'DATA_STATUS': '0'})

# 采购合同履约
def contract_implementation_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_IMPLEMENTATION_ID': 'CON_IMP_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        # 备案类型 1 履约备案 2 交付验收 3 支付结算 4 合同中止 5 合同违约和纠纷处理 6 合同交付 7 履行评价 8 履约保证金返还 9 质量保证金返还
        # 99 其它
        'ARCHIVE_TYPE': '1',
        # 付款及结算方式 1 分阶段付款 2 一次性支付 3 无支付款项 4 其它
        'SETTLEMENT_MODES': '1',
        'STAGE_NAME': '阶段名称1',
        'PHASE_EXPLAIN': '阶段说明1',
        'PAYMENT_RATIO': 0.23,
        'PAYMENT_AMOUNT': 1000000,
        # 支付结算类型 1 预付款 2 质保金 3 阶段付款
        'TYPE': '1',
        'HAPPEN_TIME': dateplus_min(0),
        'HAPPEN_TIME_DESC': '发生日期说明1',
        'PLAN_TIME': dateplus_min(0),
        'INPUT_TIME': dateplus_min(0),
        # 删除状态 0 否 1 是
        'DELETE_STATUS': '1',
        'DELETE_REASON': '删除原因1',
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"FINANCIAL_SETTLEMENT_APPROVAL","ATTACHMENT_NAME":"财务结算审批单",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"EVIDENCE_OF_PERFORMANCE","ATTACHMENT_NAME":"履约证明资料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"DELIVERY_PLAN","ATTACHMENT_NAME":"交付验收方案",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"DELIVERY_REPORT","ATTACHMENT_NAME":"交付验收报告",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_SUSPEND","ATTACHMENT_NAME":"合同中止证明资料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CORRELATION_DATA","ATTACHMENT_NAME":"相关资料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PROOF_OF_DELIVERY","ATTACHMENT_NAME":"交付证明材料",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PER_EVAL_REGISTRATION","ATTACHMENT_NAME":"供应商合同履行评价登记表",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"PER_GUA_SETTLEMENT_APPLY","ATTACHMENT_NAME":"履约保证金结算申请手续",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"QUA_GUA_SETTLEMENT_APPLY","ATTACHMENT_NAME":"质量保证金结算申请手续",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_implementation'
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
    return key_dic['CONTRACT_IMPLEMENTATION_ID']


# contract_implementation_in({'DATA_STATUS': '0'})

# 采购合同变更
def contract_modi_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_MODI_ID': 'CON_MO_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        'MODI_TIME': dateplus_min(0),
        # 变更原因 01 变更采购内容(适用追加、追减及更换产品服务) 02 当事人信息变更 03 其它情形
        'CHANGE_REASON': '01',
        'PARTY_CODE': '甲方单位编码' + datenow_hmsf(),
        'PARTY_NAME': '甲方单位' + datenow_hmsf(),
        'PARTY_LEGALER': '甲方法定代表人',
        'PARTY_ENTRUSTER': '甲方委托代理人',
        'PARTY_ENTRUSTER_TELPHONE': '甲方委托代理人联系方式1',
        'PARTY_PROXY': '甲方联系人',
        'PARTY_TELPHONE': '甲方联系电话',
        'PARTY_ADDRESS': '甲方通讯地址',
        'PARTY_POSTAL_CODE': '甲方邮政编码',
        'PARTY_ACCOUNT_NAME': '甲方开户名称',
        'PARTY_BANK_NAME': '甲方开户银行',
        'PARTY_BANK_NO': '甲方银行账号',
        'PARTY_SUPPLIER_CODE': '甲方统一社会信用代码',
        'SUPPLIER_CODE': '乙方单位编码',
        'SUPPLIER_NAME': '乙方单位',
        'SUPPLIER_LEGALER': '乙方法定代表人',
        'SUPPLIER_ENTRUSTER': '乙方委托代理人',
        'SUPPLIER_ENTRUSTER_TELPHONE': '乙方委托代理人联系方式',
        'SUPPLIER_PROXY': '乙方联系人',
        'SUPPLIER_TELPHONE': '乙方联系电话',
        'SUPPLIER_ADDRESS': '乙方通讯地址',
        'SUPPLIER_POSTAL_CODE': '乙方邮政编码',
        'SUPPLIER_ACCOUNT_NAME': '乙方开户名称',
        'SUPPLIER_BANK_NAME': '乙方开户银行',
        'SUPPLIER_BANK_NO': '乙方银行账号',
        'SUPPLIER_PARTY_CODE': '乙方统一社会信用代码',
        'SPECIFIC_EXPLAIN': '具体说明1',
        'INPUT_TIME': dateplus_min(0),
        # 删除状态 0 否 1 是
        'DELETE_STATUS': '0',
        'DELETE_REASON': '删除原因',
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"CONTRACT_MODI_DRAW","ATTACHMENT_NAME":"合同变更协议草案",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_MODI_DRAW_APPROVAL","ATTACHMENT_NAME":"合同变更协议草案审核单",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_MODI_SCAN","ATTACHMENT_NAME":"正式变更盖章扫描件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_modi'
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
    return key_dic['CONTRACT_MODI_ID']


# contract_modi_in({'DATA_STATUS': '0'})

# 变更明细
def contract_change_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_CHANGE_ID': 'CON_CHG_ID' + datenow_hmsf(),
        'CONTRACT_MODI_ID': 'CON_MO_ID',
        'PRODUCT_NAME': '货物名称/产品名称',
        'UNIT': '计量单位',
        'PURCHASE_NUM': 100,
        'PRICE': 10000,
        'TOTLE_PRICE': 1000000,
        'BRAND': '品牌1',
        'SPEC': '规格型号1134342425464w36',
        'GOOD_CODE': '统一编目码1asdsadasd',
        'ORIGINAL_PURCHASE_AMOUNT': '1000000',
        'ADD_SUBTRACT_AMOUNT': 5000,
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_change'
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


# contract_change_in({'DATA_STATUS': '0'})

# 采购合同解除
def contract_cancel_in(dic_a):
    key_dic = {
        'ID': 'ID' + datenow_hmsf(),
        'PID': 'PID' + datenow_hmsf(),
        'CONTRACT_CANCEL_ID': 'CON_CAL_ID' + datenow_hmsf(),
        'CONTRACT_EDIT_ID': 'CON_EID',
        # 解除原因 01 因不可抗力无法履行合同，不能实现合同目的 02 继续履行合同将损害国家或者j队利益，且无法通过合同变更或者中止方式解决
        # 03 采购任务调整或者取消，不能通过合同变更方式达成新协议 04 中标(成交)供应商明确表示或者以自己的行为表明不履行合同主要义务
        # 05 中标(成交)供应商迟延履行合同主要义务，经催告后在限定合理整改期限内仍不履行 06 中标(成交)供应商存在违规违约行为致使不能实现合同目的
        # 07 中标(成交)供应商发生控股关系、经营范围等重大实质性变化，不符合规定的合同订立主体条件国家法律法规规定或者合同约定的其他情形
        # 08 其他情形
        'CANCEL_REASON': '01',
        'CANCEL_TIME_DESC': '解除具体说明1',
        'RELATIVE_ATTACHMENT': ('[{"ATTACHMENT_TYPE":"CONTRACT_CANCEL_DRAW","ATTACHMENT_NAME":"合同解除协议草案",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"CONTRACT_CANCEL_DRAW_APPROVAL","ATTACHMENT_NAME":"合同解除协议草案审核单",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"},'
                                '{"ATTACHMENT_TYPE":"RELIEVE_STAMP_SWEEPING_PIECE","ATTACHMENT_NAME":"正式解除盖章扫描件",'
                                '"ATTACHMENT_FORM":"pdf","URL":"http://10.0.168.64/supervision-web/#/login"}]'),
        'DATA_STATUS': '0',
        'DATA_SOURCE_CODE': 'GO-001',
        'DATA_SOURCE_NAME': '物资服务电子招投标系统',
        'DATA_TIMESTAMP': dateplus_min(5),
        'DATA_CHANGE_TIMESTAMP': dateplus_min(5)
    }
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'purchase_contract_cancel'
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

# contract_cancel_in({'DATA_STATUS': '0'})
