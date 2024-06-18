from datetimetr import *
import pymysql


# 招标文件及补遗
def ce_tender_doc_in(dic_a):
    key_dic = {}
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 相关标段ID
    key_dic['section_ids'] = ''
    # 招标（补遗）文件名称
    key_dic['tender_doc_name'] = '招标（补遗）文件名称1'
    # 招标（补遗）文件内容
    key_dic['tender_doc_content'] = '招标（补遗）文件内容1'
    # 招标（补遗）文件生成时间
    key_dic['submit_time'] = dateplus_min(5)
    # 是否引用范本 1 有 0 无（如上传PDF文件）
    key_dic['standard_eval_rule_quote'] = '0'
    # 文件是否含有敏感词 1 是 0 否
    key_dic['sensitive_if'] = '1'
    # 涉敏段落
    key_dic['sensitive_para'] = '涉敏段落1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        if key == 'section_ids' and isinstance(dic_a[key], int):
            a = dic_a[key]
            while a > 0:
                key_dic[key] = key_dic[key] + 'ST_ID' + datenow_hms()
                if a - 1 == 0:
                    break
                else:
                    key_dic[key] = key_dic[key] + ';'
                a -= 1
                time.sleep(1)
        else:
            key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_doc'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['tender_doc_id'], key_dic['tender_project_id'], key_dic['section_ids']]
    # return sql_end


# print(ce_tender_doc_in({'section_ids': 3}))


# 招标（补遗）文件明细
def ce_tender_doc_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审方法 1 综合评审法 2 质量优先法 3 最低价法
    key_dic['eval_method'] = '1'
    # 开标模式 1 单信封 2 双信封
    key_dic['bid_opening_mode'] = '1'
    # 是否设置最高限价 1 是 0 否
    key_dic['control_price_if'] = '1'
    # 价款形式 1 金额 2 费率 3 比率 4 优惠率 5 合格率 6下浮率 7 折扣 8 单价 9 其他
    key_dic['price_form_code'] = '1'
    # 金额类招标控制价 单位：元
    key_dic['control_price'] = 50000
    # 其他类型招标控制价
    key_dic['other_control_price'] = '其他类型招标控制价1'
    # 中标人确定方式 1 评审委员会确定中标人 2 评审委员会推荐候选人，建设单位确定中标人 3 确定入围单位 4 非推荐中标候选人
    key_dic['candidate_define_mode'] = '1'
    # 基准价计算方法 待定
    key_dic['price_calculation'] = '1'
    # 价格分权重
    key_dic['price_weight'] = 10
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_doc_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_tender_doc_item_in({'candidate_define_mode': '1'}))


# 标段评审步骤
def ce_tender_doc_step_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['step_id'] = 'ST_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审步骤名称
    key_dic['step_name'] = '评审步骤名称1'
    # 排序
    key_dic['sequence_num'] = 1
    # 评审步骤评标（审）方式 1 打分制 2 通过/符合制 9 其他
    key_dic['step_eval_type'] = '1'
    # 评审步骤分类 工程编标无
    key_dic['step_sorts'] = '1'
    # 评审步骤总分（最高分）
    key_dic['score'] = 78.21
    # 权重
    key_dic['weight'] = 22
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_doc_step'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['step_id'], key_dic['step_name']]
    # return sql_end


# print(ce_tender_doc_step_in({'step_eval_type': '1'}))


# 标段评审因素
def ce_tender_doc_clause_in(dic_a):
    key_dic = {}
    # 条款主键
    key_dic['clause_id'] = 'CL_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审步骤ID
    key_dic['step_id'] = 'ST_ID' + datenow_hms()
    # 条款级别
    key_dic['level'] = 1
    # 父条款主键
    key_dic['parent_id'] = '父条款主键1'
    # 排序
    key_dic['sequence_num'] = 1
    # 是否评审条款组 1 是 0 否
    key_dic['clause_group'] = '1'
    # 评审因素
    key_dic['eval_factor'] = '评审因素1'
    # 评审标准
    key_dic['eval_standard'] = '评审标准1'
    # 是否主要评审项 1 是 0 否
    key_dic['main_if'] = '1'
    # 是否客观评审项 1 是 0 否
    key_dic['objective_if'] = '1'
    # 条款评标（审）方式 1 打分制 2 通过/符合制 9 其他
    key_dic['clause_eval_type'] = '1'
    # 评审因素分值
    key_dic['clause_score_original'] = 78.12
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_doc_clause'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['clause_id']
    # return sql_end


# print(ce_tender_doc_clause_in({'clause_eval_type': '1'}))


# 资格预审文件及补遗
def ce_qual_doc_in(dic_a):
    key_dic = {}
    # 资审（补遗）文件ID
    key_dic['qual_doc_id'] = 'QD_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 相关标段ID
    key_dic['section_ids'] = 'ST_IDS' + datenow_hms()
    # 资审（补遗）文件名称
    key_dic['qual_doc_name'] = '资审（补遗）文件名称1'
    # 资审（补遗）文件生成时间
    key_dic['submit_time'] = dateplus_min(5)
    # 是否引用范本 1 有 0 无（如上传PDF文件）
    key_dic['standard_eval_rule_quote'] = '1'
    # 文件是否含有敏感词 1 是 0 否
    key_dic['sensitive_if'] = '0'
    # 涉敏段落
    key_dic['sensitive_para'] = '涉敏段落1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_doc'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['qual_doc_id']
    # return sql_end


# print(ce_qual_doc_in({'sensitive_if': '1'}))

# 资审（补遗）文件明细
def ce_qual_doc_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 资审（补遗）文件ID
    key_dic['qual_doc_id'] = 'QD_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 申请有效期 单位：天
    key_dic['valid_period'] = 30
    # 审查方法 1 合格制 2 有限数量制
    key_dic['examine_type'] = '1'
    # 通过资审的申请人数量
    key_dic['passed_applicant_num'] = 10
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_doc_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_qual_doc_item_in({'examine_type': '1'}))

# 招标文件编制及复核确认流程
def ce_doc_exec_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['doc_exec_id'] = 'DE_ID' + datenow_hms()
    # 招标文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 业务环节编码 1采购单位预立项，提交信息 2 采购服务中心敏感词审核（审核通过视为文件编制开始） 3 采购代理提交文件（视为文件编制完成） 4 采购单位确认文件
    key_dic['business_step_type'] = '1'
    # 业务环节状态 0 不通过，返回修改 1 通过 2 已提交
    key_dic['audit_result'] = '1'
    # 意见
    key_dic['content'] = '意见qhtest'
    # 处理人姓名
    key_dic['committer_name'] = '处理人姓名1'
    # 处理人证件号
    key_dic['committer_code'] = '处理人证件号1'
    # 处理人所在单位名称
    key_dic['committer_organ_name'] = '处理人所在单位名称1'
    # 处理人所在单位代码
    key_dic['committer_organ_code'] = '处理人所在单位代码1'
    # 处理时间
    key_dic['commit_time'] = dateplus_min(5)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_doc_exec'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['doc_exec_id']
    # return sql_end


# print(ce_doc_exec_in({'audit_result': '1'}))

# 项目信息
def ce_base_project_in(dic_a):
    key_dic = {}
    # 项目ID
    key_dic['base_project_id'] = 'BP_ID' + datenow_hms()
    # 季度计划明细ID
    key_dic['quar_project_id'] = 'QP_ID' + datenow_hms()
    # 项目编号
    key_dic['base_project_code'] = 'BP_CODE' + datenow_hms()
    # 项目名称
    key_dic['base_project_name'] = 'QH测试项目' + datenow_hms()
    # 立项批文编号
    key_dic['approval_num'] = '立项批文编号1'
    # 立项批文名称
    key_dic['approval_name'] = '立项批文名称1'
    # 立项审批时间
    key_dic['project_approval_time'] = dateplus_min(5)
    # 建设计划审批时间
    key_dic['plan_approval_time'] = dateplus_min(5)
    # 审核/核准/备案机关
    key_dic['approval_org'] = '审核/核准/备案机关1'
    # 项目地址
    key_dic['base_project_address'] = '项目地址1'
    # 项目所在行政区划代码
    key_dic['base_project_region_code'] = '行政区划代码1'
    # 项目规模
    key_dic['base_project_scale'] = '项目规模1'
    # 资金来源 1 本级经费 2 上级拨款 9 其他
    key_dic['fund_source'] = '1'
    # 出资比例
    key_dic['fund_scale'] = '出资比例1'
    # 资金落实情况
    key_dic['fund_process'] = '资金落实情况1'
    # 项目投资批复金额
    key_dic['invest_amount'] = 5000000
    # 项目估算金额
    key_dic['project_est_amount'] = 5000000
    # 项目联系人
    key_dic['contactor'] = '项目联系人1'
    # 联系方式
    key_dic['contact_information'] = '13828329384'
    # 招标组织形式 1 自行招标 2 委托招标
    key_dic['tender_organize_form'] = '1'
    # 项目创建时间
    key_dic['base_project_create_time'] = dateplus_min(5)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_base_project'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['base_project_id']
    # return sql_end


# print(ce_base_project_in({'tender_organize_form': '1'}))

# 招标项目基本信息
def ce_tender_project_in(dic_a):
    key_dic = {}
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 季度计划明细ID
    key_dic['quar_project_id'] = 'QP_ID' + datenow_hms()
    # 项目ID
    key_dic['base_project_id'] = 'BP_ID' + datenow_hms()
    # 招标项目编号
    key_dic['tender_project_code'] = 'QH测试项目编号' + datenow_hms()
    # 招标项目名称
    key_dic['tender_project_name'] = 'QH测试招标项目名称' + datenow_hms()
    # 是否X项目 1 是 0 否
    key_dic['x_project_if'] = '0'
    # 建设单位名称
    key_dic['tenderer_name'] = '建设单位名称1'
    # 建设单位代码
    key_dic['tenderer_code'] = '建设单位代码1'
    # 招标代理机构名称
    key_dic['tender_agency_name'] = '招标代理机构名称1'
    # 招标代理机构代码
    key_dic['tender_agency_code'] = '招标代理机构代码1'
    # 招标（采购）项目类型 1 物资类 2 服务类 3 工程类
    key_dic['tender_project_type'] = '1'
    # 按重要程度 1 一般 2 重点 3 重大规划计划 4 规划计划（二类） 5 规划计划（三类） 6 规划计划（四类）
    key_dic['important_type'] = '1'
    # 重要程度分类名称
    key_dic['important_type_name'] = '重要程度分类名称1'
    # 按任务阶段 1 SSANWGHXM 2 SSIWGHXM 3 FGHXM 9 其他
    key_dic['stage_type'] = '1'
    # 任务阶段名称
    key_dic['stage_type_name'] = '任务阶段名称1'
    # 按完成要求 1 ZC 2 YJ 9 其他
    key_dic['completion_type'] = '1'
    # 完成要求名称
    key_dic['completion_type_name'] = '完成要求名称1'
    # 按组织方式 1 PT 2 YXCG 3 YJXY 4 MNDL 5 GXGY 9 其他
    key_dic['organization_type'] = '1'
    # 组织方式名称
    key_dic['organization_type_name'] = '组织方式名称1'
    # 按保障任务性质 1 ZDFZZJSXD 2 ZDFXJSDZZXRW 3 ZZ 4 YXZX 5 ZBCB 6 YW 7 RC 9 其他
    key_dic['ensure_type'] = '1'
    # 保障任务性质名称
    key_dic['ensure_type_name'] = '保障任务性质名称1'
    # 其他属性 01 WXGH 02 BGSB 03 QXQC 04 QBQC 05 JZQC 06 JXQC 07 WHQC 08 BZ 09 YLQC 10 YL 11 JYQC 12 GCWZ 13 YCL
    # 14 YLSB 15 XGKY 16 BGSB 99 其他
    key_dic['other_types'] = '01'
    # 其他属性名称
    key_dic['other_types_name'] = '其他属性名称1'
    # 采购任务下达部门
    key_dic['task_release_org'] = '采购任务下达部门1'
    # 采购任务下达部门编码
    key_dic['task_release_org_code'] = '采购任务下达部门编码1'
    # 采购任务编号
    key_dic['task_code'] = '采购任务编号1'
    # 采购机构名称
    key_dic['inner_agency_name'] = '采购机构名称1'
    # 采购机构代码
    key_dic['inner_agency_code'] = '采购机构代码1'
    # 采购机构类型 1 采购服务站 2 部门采购服务站 3 队属采购机构 4 自行采购单位
    key_dic['inner_agency_type'] = '1'
    # 网络模式 1 外网云平台 2 内网云平台（不见面） 3 内网云平台 4 内网本地（不见面） 5 内网本地
    key_dic['net_mode'] = '1'
    # 招标组织形式 1 自行招标（采购） 2 委托招标（采购）
    key_dic['tender_organize_form'] = '1'
    # 招标方式 1 公开招标 2 邀请招标 3 竞争性谈判 4 询价 5 单一来源采购 9 其他
    key_dic['tender_mode'] = '1'
    # 资格审查方式 1 资格预审 2 资格后审
    key_dic['qual_type'] = '2'
    # 项目划分 1 小型项目 2 中型项目 3 大型项目
    key_dic['project_scale'] = '2'
    # 投标人征集方式 1 公告征集 2 供应商库（JC）抽取 3 书面推荐 4 供应商库（ZDGC库）抽取 9 其他
    key_dic['bidder_collect_form'] = '1'
    # 招标内容与范围及招标方案说明
    key_dic['tender_content'] = '1'
    # 项目通用性
    key_dic['project_common'] = '1'
    # 招标项目建立时间
    key_dic['tender_project_create_time'] = dateplus_min(0)
    # 是否重新招标 1 是 0 否
    key_dic['rebid_if'] = '0'
    # 重新招标上次招标项目ID
    key_dic['last_tender_project_id'] = '重新招标上次招标项目ID'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_project'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return [key_dic['tender_project_code']]
    # return sql_end


# print(ce_tender_project_in({'project_common': '1'}))


# 标段信息
def ce_section_in(dic_a):
    key_dic = {}
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 招标文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 资审文件ID
    key_dic['qual_doc_id'] = 'QD_ID' + datenow_hms()
    # 标段编号
    key_dic['section_code'] = '标段编号1'
    # 标段名称
    key_dic['section_name'] = '标段名称1'
    # 建设类型 1新建工程 2改建工程 3扩建工程 4装修改造
    key_dic['construction_type_code'] = '1'
    # 标段内容
    key_dic['section_content'] = '标段内容1'
    # 标段分类代码
    key_dic['section_classify_code'] = '标段分类代码1'
    # 标段分类名称
    key_dic['section_classify'] = '标段分类名称1'
    # 标段估算价
    key_dic['total_contract_reckon_price'] = 5000000
    # 计划工期
    key_dic['plan_limit_time'] = '计划工期1'
    # 计划开始日期
    key_dic['plan_start_time'] = dateplus_min(1205)
    # 计划竣工日期
    key_dic['plan_completed_time'] = dateplus_min(5)
    # 标段建立时间
    key_dic['section_create_time'] = dateplus_min(5)
    # 标段是否重新招标 1 是 0 否
    key_dic['section_rebid_if'] = '0'
    # 重新招标上次标段ID
    key_dic['last_section_id'] = '重新招标上次标段ID1'
    # 标段重新招标次数
    key_dic['rebid_num'] = 0
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_section'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['section_code']
    # return sql_end


# print(ce_section_in({'section_rebid_if': '0'}))


# 场地使用信息
def ce_venue_info_in(dic_a):
    key_dic = {}
    # 使用信息ID
    key_dic['venu_info_id'] = 'VI_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 场地用途 01 资审开标 02 资审评审 03 评标 04 竞价 05 答疑会 06 论证会 07 清标 08 谈判 09 开标 99 其他
    key_dic['venue_mode'] = '09'
    # 是否远程异地评标 1 是 0 否
    key_dic['remote_eval_if'] = '0'
    # 是否主场 1 是 0 否
    key_dic['is_home'] = '1'
    # 场地名称
    key_dic['venue_name'] = '场地名称1'
    # 标室名称
    key_dic['room'] = '标室名称1'
    # 场地服务机构
    key_dic['venue_service_name'] = '场地服务机构1'
    # 使用开始时间
    key_dic['appointment_begin_time'] = dateplus_min(105)
    # 使用结束时间
    key_dic['appointment_end_time'] = dateplus_min(0)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_venue_info'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['venu_info_id']
    # return sql_end


# print(ce_venue_info_in({'is_home': '0'}))

# 招标（资审）公告
def ce_notice_in(dic_a):
    key_dic = {}
    # 公告ID
    key_dic['notice_id'] = 'NT_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 资审（补遗）文件ID
    key_dic['qual_doc_id'] = 'QD_ID' + datenow_hms()
    # 公告类型 1 招标公告 2 资审公告
    key_dic['notice_type'] = '1'
    # 公告性质 1 首次公告 2 更正公告 3 澄清公告
    key_dic['notice_nature'] = '1'
    # 公告标题
    key_dic['notice_title'] = '公告标题1'
    # 公告内容
    key_dic['notice_content'] = '公告内容公告内容公告内容公告内容1'
    # 公告编制方式 1 按模板编制 2 按通用方式编制
    key_dic['notice_edit'] = '1'
    # 公告发布范围 1 内网发布 2 内外网发布
    key_dic['notice_range'] = '2'
    # 公告发布时间
    key_dic['notice_publish_time'] = dateplus_min(0)
    # 公告源URL
    key_dic['url'] = 'https://www.plap.mil.cn/ '
    # 建设单位名称
    key_dic['tenderer_name'] = '建设单位名称1'
    # 建设单位地址
    key_dic['tenderer_address'] = '建设单位地址1'
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '建设单位联系电话1'
    # 建设单位电子邮件
    key_dic['tenderer_mail'] = '201010021@qq.com'
    # 采购机构名称
    key_dic['inner_agency_name'] = '采购机构名称1'
    # 采购机构地址
    key_dic['inner_agency_address'] = '采购机构地址1'
    # 采购机构联系人
    key_dic['inner_agency_contactor'] = '采购机构联系人1'
    # 采购机构联系电话
    key_dic['inner_agency_phone'] = '采购机构联系电话1'
    # 采购机构电子邮件
    key_dic['inner_agency_mail'] = '采购机构电子邮件1'
    # 公告发布媒介
    key_dic['notice_media'] = '公告发布媒介1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['notice_id']
    # return sql_end


# print(ce_notice_in({'notice_edit': '1'}))


# 招标（资审）公告明细
def ce_notice_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['notice_item_id'] = 'NI_ID' + datenow_hms()
    # 公告ID
    key_dic['notice_id'] = 'NT_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 公告对应的文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 公告对应的资审文件ID
    key_dic['qual_doc_id'] = 'QD_ID' + datenow_hms()
    # 投标人资格要求
    key_dic['bidder_qual'] = '投标人资格要求1'
    # 业绩要求
    key_dic['bidder_kpi'] = '业绩要求1'
    # 其他资质要求
    key_dic['bidder_other_qual'] = '其他资质要求1'
    # 是否允许联投 1 是 0 否
    key_dic['union_bid_if'] = '0'
    # 文件获取开始时间
    key_dic['doc_get_start_time'] = dateplus_min(600)
    # 文件获取截止时间
    key_dic['doc_get_end_time'] = dateplus_min(40)
    # 文件获取方式 1 网上下载 2 线下获取
    key_dic['doc_get_method'] = '1'
    # 文件获取条件
    key_dic['doc_get_condition'] = '文件获取条件1'
    # 文件获取地址
    key_dic['doc_get_address'] = '文件获取地址1'
    # 保证金缴纳截止时间
    key_dic['margin_end_time'] = dateplus_min(600)
    # 澄清答疑截止时间
    key_dic['answer_end_time'] = dateplus_min(600)
    # 文件是否收费 1 是 0 否
    key_dic['charge_if'] = '1'
    # 文件售价
    key_dic['doc_price'] = 5000.01
    # 投标（申请）文件递交方式 1 现场递交 2 系统上传
    key_dic['bid_doc_refer_method'] = '1'
    # 投标（申请）文件递交截止时间
    key_dic['bid_doc_refer_end_time'] = dateplus_min(400)
    # 投标（申请）文件递交地址
    key_dic['bid_doc_refer_address'] = '投标（申请）文件递交地址1'
    # 开标时间/开启时间
    key_dic['bid_open_time'] = dateplus_min(300)
    # 开标方式/开启方式 1 网上开标（开启） 2 线下开标（开启）
    key_dic['bid_open_method'] = '1'
    # 开标地点/资审地点
    key_dic['bid_open_address'] = '开标地点1'
    # 评标时间
    key_dic['eval_time'] = dateplus_min(200)
    # 评标地点
    key_dic['eval_address'] = '评标地点1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_notice_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['notice_item_id']
    # return sql_end


# print(ce_notice_item_in({'union_bid_if': '0'}))

# 投标邀请书
def ce_invitation_in(dic_a):
    key_dic = {}
    # 投标邀请书ID
    key_dic['invitation_id'] = 'IT_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 邀请书性质 1 首次 2 更正 3 澄清
    key_dic['invitation_nature'] = '1'
    # 邀请书标题
    key_dic['invitation_name'] = '邀请书标题1'
    # 邀请书内容
    key_dic['invitation_content'] = '邀请书内容1'
    # 发出时间
    key_dic['invitation_publish_time'] = dateplus_min(600)
    # 源URL
    key_dic['url'] = 'https://www.plap.mil.cn/ '
    # 建设单位地址
    key_dic['tenderer_address'] = '建设单位地址1'
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '建设单位联系电话1'
    # 招标代理机构地址
    key_dic['agency_address'] = '招标代理机构地址1'
    # 招标代理联系人
    key_dic['agency_contactor'] = '招标代理联系人1'
    # 招标代理联系电话
    key_dic['agency_phone'] = '招标代理联系电话1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_invitation'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['invitation_id']
    # return sql_end


# print(ce_invitation_in({'invitation_nature': '1'}))


# 投标邀请书明细
def ce_invitation_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['invitation_item_id'] = 'II_ID' + datenow_hms()
    # 投标邀请书ID
    key_dic['invitation_id'] = 'IT_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 邀请书对应的文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 是否允许联投 1 是 0 否
    key_dic['union_bid_if'] = '0'
    # 文件获取开始时间
    key_dic['doc_get_start_time'] = dateplus_min(900)
    # 文件获取结束时间
    key_dic['doc_get_end_time'] = dateplus_min(30)
    # 文件获取方式 1 网上下载 2 线下获取
    key_dic['tender_doc_get_method'] = '1'
    # 文件获取地点
    key_dic['tender_doc_get_address'] = '文件获取地点1'
    # 澄清答疑截止时间
    key_dic['answer_end_time'] = dateplus_min(30)
    # 文件是否收费 1 是 0 否
    key_dic['charge_if'] = '1'
    # 文件售价
    key_dic['doc_price'] = 500.53
    # 投标（报价）文件递交方式 1 现场递交 2 系统上传
    key_dic['bid_doc_refer_method'] = '1'
    # 投标（报价）文件递交截止时间
    key_dic['bid_doc_refer_end_time'] = dateplus_min(30)
    # 投标（报价）文件递交地址
    key_dic['bid_doc_refer_address'] = '文件递交地址1'
    # 开标时间
    key_dic['bid_open_time'] = dateplus_min(10)
    # 开标方式 1 网上开标（开启） 2 线下开标（开启）
    key_dic['bid_open_method'] = '1'
    # 开标地点
    key_dic['bid_open_address'] = '开标地点1'
    # 评标时间
    key_dic['eval_time'] = dateplus_min(10)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_invitation_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['invitation_item_id']
    # return sql_end


# print(ce_invitation_item_in({'union_bid_if': '0'}))


# 投标邀请发放响应情况
def ce_invitation_result_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['invitation_result_id'] = 'IR_ID' + datenow_hms()
    # 投标邀请书ID
    key_dic['invitation_id'] = 'IT_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 被邀请人名称
    key_dic['invitee_name'] = '被邀请人名称1'
    # 被邀请人代码
    key_dic['invitee_code'] = '被邀请人代码1'
    # 是否接受邀请 1 是 0 否
    key_dic['accept_if'] = '1'
    # 接受/拒绝邀请时间
    key_dic['confirm_time'] = dateplus_min(30)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_invitation_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['invitation_result_id']
    # return sql_end


print(ce_invitation_result_in({'accept_if': '1'}))


# 资审开标
def ce_qual_open_in(dic_a):
    key_dic = {}
    # 资审开标ID
    key_dic['qual_open_id'] = 'QO_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 资审开标时间
    key_dic['qual_open_time'] = dateplus_min(5)
    # 资审开标地点
    key_dic['qual_open_address'] = '资审开标地点' + datenow_hms()
    # 资审开标结果 1 成功 0 失败
    key_dic['qual_open_result'] = '1'
    # 资审开标失败原因类型
    key_dic['failure_reason_type'] = '资审开标失败原因类型1'
    # 资审开标失败原因
    key_dic['faliure_reason'] = '资审开标失败原因1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_open'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['qual_open_id']
    # return sql_end


# print(ce_qual_open_in({'qual_open_result': '1'}))


# 资审开标明细
def ce_qual_open_item_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 资审开标ID
    key_dic['qual_open_id'] = 'QO_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 申请人ID
    key_dic['applicant_id'] = dateplus_min(5)
    # 申请人名称
    key_dic['applicant_name'] = '申请人名称1'
    # 申请人代码
    key_dic['applicant_code'] = '申请人代码1'
    # 是否联合体 1 是 0 否
    key_dic['union_if'] = '0'
    # 申请文件递交时间
    key_dic['apply_refer_time'] = dateplus_min(5)
    # 资审开标阶段是否解密成功 1 是 0 否
    key_dic['passed_if'] = '1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_open_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_qual_open_item_in({'passed_if': '1'}))


# 资审结果
def ce_qual_result_in(dic_a):
    key_dic = {}
    # 资审结果ID
    key_dic['qual_result_id'] = 'QR_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 通过资审的申请人数量
    key_dic['passed_applicant_num'] = 4
    # 评审性质 1 首次评审 2 复评
    key_dic['qual_nature'] = '1'
    # 资审结果 1 成功 0 失败
    key_dic['qual_result'] = '1'
    # 资审评审失败原因类型
    key_dic['faliure_reason_type'] = '资审评审失败原因类型'
    # 资审评审失败原因
    key_dic['faliure_reason'] = '资审评审失败原因1'
    # 资审结果生成时间
    key_dic['result_time'] = dateplus_min(65)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_result'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['qual_result_id']
    # return sql_end


# print(ce_qual_result_in({'qual_result': '1'}))


# 资审结果名单
def ce_qual_result_item_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['item_id'] = 'QR_ID' + datenow_hms()
    # 资审结果ID
    key_dic['qual_result_id'] = 'QR_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 申请人ID
    key_dic['applicant_id'] = 4
    # 申请人名称
    key_dic['applicant_name'] = '1'
    # 申请人代码
    key_dic['applicant_code'] = '1'
    # 是否通过资格审查 1 通过 0 不通过 2 未参与
    key_dic['passed_if'] = '资审评审失败原因类型'
    # 资审不通过的原因
    key_dic['reason'] = '资审评审失败原因1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_qual_result_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['qual_result_id']
    # return sql_end


# print(ce_qual_result_item_in({'qual_result': '1'}))


# 踏勘记录
def ce_survey_in(dic_a):
    key_dic = {}
    # 踏勘记录ID
    key_dic['survey_id'] = 'SV_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_ids'] = 'ST_IDS' + datenow_hms()
    # 踏勘记录提交时间
    key_dic['record_submit_time'] = dateplus_min(335)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_survey'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['survey_id']
    # return sql_end


# print(ce_survey_in({'data_source_code': 'CE-001'}))


# 踏勘记录
def ce_survey_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 踏勘记录ID
    key_dic['survey_id'] = 'SV_ID' + datenow_hms()
    # 踏勘单位名称
    key_dic['survey_company'] = '踏勘单位名称1'
    # 踏勘单位代码
    key_dic['survey_company_code'] = '踏勘单位代码1'
    # 单位代表人
    key_dic['company_contactor'] = '单位代表人1'
    # 单位代表人身份证号
    key_dic['contactor_id_card_num'] = '单位代表人身份证号1'
    # 代表人联系方式
    key_dic['contactor_phone'] = '代表人联系方式'
    # 踏勘时间
    key_dic['survey_time'] = dateplus_min(335)
    # 备注
    key_dic['remark'] = '备注qwqqweqweq'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_survey_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_survey_item_in({'data_source_code': 'CE-001'}))


# 资审开标明细
def ce_bidder_enroll_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['bidder_enroll_id'] = 'BE_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 投标人联系人
    key_dic['bidder_contactor'] = '投标人联系人1'
    # 投标人联系方式
    key_dic['bidder_contactor_tel'] = '投标人联系方式1'
    # 是否联合体 1 是 0 否
    key_dic['union_if'] = '0'
    # 报名类型 1 资审报名 2 投标报名
    key_dic['enroll_type'] = '1'
    # 报名时间
    key_dic['enroll_time'] = dateplus_min(5)
    # 报名确认结果 1 通过 0 不通过
    key_dic['enroll_result'] = '1'
    # 不通过原因
    key_dic['no_pass_reason'] = '不通过原因'
    # 报名结果确认时间
    key_dic['enroll_result_time'] = dateplus_min(5)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_bidder_enroll'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['bidder_enroll_id']
    # return sql_end


# print(ce_bidder_enroll_in({'enroll_result': '1'}))


# 投标人下载（获取）文件情况
def ce_doc_download_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['doc_download_id'] = 'DD_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 招标（补遗）文件ID
    key_dic['tender_doc_id'] = 'TD_ID' + datenow_hms()
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 下载（获取）文件类型 1 资审文件 2 招标文件
    key_dic['doc_type'] = '1'
    # 下载文件IP/获取文件地点
    key_dic['download_ip'] = '下载文件IP/获取文件地点1'
    # 下载（获取）文件时间
    key_dic['download_time'] = dateplus_min(5)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)

    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_doc_download'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['doc_download_id']
    # return sql_end


# print(ce_doc_download_in({'doc_type': '1'}))


# 文件递交情况
def ce_bid_doc_refer_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['doc_refer_id'] = 'DR_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 递交文件类型 1 资审申请文件 2 投标文件
    key_dic['bid_doc_type'] = '2'
    # 递交方式 1 现场递交 2 系统上传
    key_dic['bid_doc_refer_method'] = '1'
    # 文件递交时间
    key_dic['bid_doc_refer_time'] = dateplus_min(5)
    # 文件递交IP地址
    key_dic['net_ip'] = '10.1.1.111'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_bid_doc_refer'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['doc_refer_id']
    # return sql_end


# print(ce_bid_doc_refer_in({'bid_doc_refer_method': '1'}))


# 联合体成员信息
def ce_union_member_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['union_member_id'] = 'UM_ID' + datenow_hms()
    # 联合体ID
    key_dic['union_id'] = 'UN_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 联合体成员名称
    key_dic['union_member_name'] = '联合体成员名称1'
    # 联合体成员代码
    key_dic['union_member_code'] = '联合体成员代码1'
    # 是否联合体牵头人 1 是 0 否
    key_dic['leader_if'] = '1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_union_member'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['union_member_id']
    # return sql_end


# print(ce_union_member_in({'leader_if': '1'}))


# 开标记录
def ce_bid_open_record_in(dic_a):
    key_dic = {}
    # 开标记录ID
    key_dic['record_id'] = 'RC_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 开标记录标题
    key_dic['bid_open_title'] = '开标记录标题1'
    # 开标记录内容
    key_dic['bid_open_content'] = '开标记录内容1'
    # 开标时间
    key_dic['bid_open_time'] = dateplus_min(905)
    # 开标方式 1 现场开标 2 远程开标 3 线下开标
    key_dic['bid_open_type'] = '1'
    # 开标地点
    key_dic['bid_open_address'] = '开标地点1'
    # 开标结果 1 成功 0 失败
    key_dic['bid_open_result'] = '1'
    # 开标负责人
    key_dic['bid_open_manager'] = '开标负责人1'
    # 开标负责人联系方式
    key_dic['manager_phone'] = '联系方式1'
    # 开标失败原因类型
    key_dic['failure_reason_type'] = '开标失败原因类型1'
    # 开标失败原因
    key_dic['failure_reason'] = '开标失败原因1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_bid_open_record'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['record_id']
    # return sql_end


# print(ce_bid_open_record_in({'bid_open_type': '1'}))


# 开标明细
def ce_bid_open_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'RC_ID' + datenow_hms()
    # 开标记录ID
    key_dic['record_id'] = 'RC_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 是否联合体 1 是 0 否
    key_dic['union_if'] = '0'
    # 投标人项目负责人
    key_dic['bidder_manager'] = '投标人项目负责人1'
    # 投标人项目负责人身份证号
    key_dic['bidder_manager_id_card_num'] = '110101198001010037'
    # 投标人联系人
    key_dic['bidder_contactor'] = '投标人联系人1'
    # 投标人联系方式
    key_dic['bidder_contactor_tel'] = '13928374374'
    # 是否递交投标文件 1 是 0 否
    key_dic['bid_if'] = '1'
    # 投标（报价）文件递交时间
    key_dic['bid_doc_refer_time'] = dateplus_min(105)
    # 投标（报价）文件解密状态 1 未解密 2 解密成功
    key_dic['decry_status'] = '1'
    # 解密时间
    key_dic['decry_time'] = dateplus_min(105)
    # 是否缴纳保证金 1 是 0 否
    key_dic['margin_pay_if'] = '1'
    # 保证金缴纳方式
    key_dic['margin_pay_type'] = '1'
    # 保证金缴纳金额
    key_dic['margin_price'] = 50000
    # 保证金缴纳时间
    key_dic['margin_pay_time'] = dateplus_min(105)
    # 投标报价价款形式代码 1 金额 2 费率 3 比率4 优惠率 5 合格率 6下浮率 7 折扣 8 单价 9 其他
    key_dic['price_form_code'] = '1'
    # 金额报价形式投标报价
    key_dic['bid_price'] = 600000.12
    # 其他形式投标报价
    key_dic['other_bid_price'] = '其他形式投标报价1'
    # 投标工期（交货期/服务期）
    key_dic['time_limit'] = '投标工期（交货期/服务期）1'
    # 质量标准
    key_dic['qual_standard'] = '质量标准1'
    # 是否无效投标 1 是 0 否
    key_dic['invalid_if'] = '0'
    # 无效投标原因
    key_dic['invalid_reason'] = '无效投标原因1'
    # 开标时间
    key_dic['bid_open_time'] = dateplus_min(95)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_bid_open_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_bid_open_item_in({'margin_pay_if': '1'}))


# 投标（报价）文件特征码
def ce_doc_char_in(dic_a):
    key_dic = {}
    # 文件特征码ID
    key_dic['file_info_id'] = 'FI_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 投标（报价）文件MD5码
    key_dic['md5'] = 'ashdjadjsahjdsahja'
    # 投标（报价）文件加密锁锁号
    key_dic['encryption_lock'] = '文件加密锁锁号'
    # CPU序列号
    key_dic['cpu_serial'] = 'SN-assadhjasdsajd;SN-assadhjasdsajd1;SN-assadhjasdsajd2'
    # 硬盘序列号
    key_dic['hard_disk_serial'] = 'SN-assadhjasdsajd;SN-assadhjasdsajd3;SN-assadhjasdsajd5'
    # 内存序列号
    key_dic['memory_serial'] = 'SN-assadhjasdsajd'
    # 网卡MAC地址
    key_dic['mac'] = 'SHJJShjKSKSKJKJ;SHJJShjKSKSKJKJ1;SHJJShjKSKSKJKJ2'
    # 投标（报价）文件名称
    key_dic['bid_doc_name'] = '投标（报价）文件名称1;投标（报价）文件名称2'
    # 投标（报价）文件作者
    key_dic['bid_doc_editor'] = 'qhtest'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_doc_char'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['file_info_id']
    # return sql_end


# print(ce_doc_char_in({'data_source_code': 'CE-001'}))


# 评审报告
def ce_eval_report_in(dic_a):
    key_dic = {}
    # 评审报告ID
    key_dic['eval_report_id'] = 'ER_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 评标报告标题
    key_dic['eval_report_title'] = '评标报告标题1'
    # 评审方法 1 综合评审法 2 质量优先法 3 最低价法
    key_dic['eval_method'] = '1'
    # 评标基本情况
    key_dic['eval_report_content'] = '评标基本情况'
    # 评标结果 1 招标失败（流标） 2 重新招标 3 评审结果公示
    key_dic['eval_result'] = '1'
    # 招标失败/重新招标原因类型
    key_dic['faliure_reason_type'] = '招标失败/重新招标原因类型1'
    # 招标失败/重新招标原因
    key_dic['faliure_reason'] = '招标失败/重新招标原因1'
    # 评标性质 1 首次评审 2 重评
    key_dic['re_eval_type'] = '1'
    # 重评次数
    key_dic['re_eval_num'] = 0
    # 重评原因 1 评分项错误 2 分数计算错误 3 汇总错误 9 其他
    key_dic['re_eval_reason'] = 'qhtest'
    # 评标开始时间
    key_dic['eval_start_time'] = dateplus_min(405)
    # 评标结束时间
    key_dic['eval_end_time'] = dateplus_min(15)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_eval_report'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['eval_report_id']
    # return sql_end


# print(ce_eval_report_in({'data_source_code': 'CE-001'}))


# 评标小组名单
def ce_judge_group_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['group_member_id'] = 'GR_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 评委姓名
    key_dic['judge_name'] = '评标报告标题1'
    # 评委身份证件类型 1居民身份证 2军官证 3港澳居民来往内地通行证 4台湾居民来往大陆通行证 5外国护照 6外国人永久居住证 9 其他
    key_dic['judge_id_card_type'] = '1'
    # 评委身份证件号
    key_dic['judge_id_card_num'] = '110101198001010053'
    # 评委专业类别 1 物资技术  2 工程技术 3 服务技术  4 物资服务经济  5 工程经济 9 其他
    key_dic['judge_pro_type'] = '2'
    # 评委类别 1 专家 2 采购单位代表 3 采购代理人员 4 采购机构人员 9 其他
    key_dic['judge_type'] = '1'
    # 是否小组组长 1 是 0 否
    key_dic['leader_if'] = '1'
    # 是否采购单位推荐的专家 1 是 0 否
    key_dic['recommend_if'] = '1'
    # 专家工作单位
    key_dic['expert_unit'] = '专家工作单位1'
    # 专家工作单位代码
    key_dic['expert_unit_code'] = '专家工作单位代码1'
    # 专家来源 1 军队 2 地方 3 库外
    key_dic['expert_origin'] = '1'
    # 评委是否签到 1 是 0 否
    key_dic['sign_in_if'] = '1'
    # 评委签到时间
    key_dic['sign_in_time'] = dateplus_min(95)
    # 评委离场时间
    key_dic['off_time'] = dateplus_min(15)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_judge_group'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['group_member_id']
    # return sql_end


# print(ce_judge_group_in({'data_source_code': 'CE-001'}))


# 投标人评审条款得分
def ce_clause_score_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['clause_score_id'] = 'CS_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 评审步骤名称
    key_dic['step_name'] = '评审步骤名称1'
    # 评审步骤权重
    key_dic['weight'] = 31
    # 评审因素
    key_dic['eval_factor'] = '评审因素1'
    # 是否客观评审项 1 是 0 否
    key_dic['objective_if'] = '1'
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 评委姓名
    key_dic['judge_name'] = '评委姓名1'
    # 评委身份证件号
    key_dic['judge_id_card_num'] = '11010119800101007X'
    # 专家对该供应商该评审因素的打分
    key_dic['clause_score'] = 68
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_clause_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['clause_score_id']
    # return sql_end


# print(ce_clause_score_in({'data_source_code': 'CE-001'}))


# 评审步骤专家打分情况
def ce_step_score_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['step_score_id'] = 'SS_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 评审步骤名称
    key_dic['step_name'] = '评审步骤名称1'
    # 排序
    key_dic['sequence_num'] = 1
    # 评审步骤评审方式 1 打分制 2 通过/符合制 9 其他
    key_dic['step_eval_type'] = '1'
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 评委姓名
    key_dic['judge_name'] = '评委姓名1'
    # 评委身份证件号
    key_dic['judge_id_card_num'] = '11010119800101007X'
    # 专家对该供应商该步骤的打分
    key_dic['step_score'] = 68
    # 非打分制评审结果
    key_dic['step_result'] = 'pass'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_step_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['step_score_id']
    # return sql_end


# print(ce_step_score_in({'data_source_code': 'CE-001'}))


# 投标评审步骤得分情况
def ce_step_total_score_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['step_total_score_id'] = 'ST_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 评审步骤名称
    key_dic['step_name'] = '评审步骤名称1'
    # 排序
    key_dic['sequence_num'] = 1
    # 评审步骤评审方式 1 打分制 2 通过/符合制 9 其他
    key_dic['step_eval_type'] = '1'
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 各专家汇总得分
    key_dic['step_total_score'] = 73
    # 权重
    key_dic['weight'] = 20
    # 权重结果分
    key_dic['weight_result'] = 68
    # 非打分制汇总结果
    key_dic['step_total_result'] = 'pass'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_step_total_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['step_total_score_id']
    # return sql_end


# print(ce_step_total_score_in({'data_source_code': 'CE-001'}))


# 投标人评审明细汇总
def ce_bidder_score_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['bidder_score_id'] = 'BS_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 投标人名称
    key_dic['bidder_name'] = '投标人名称1'
    # 投标人代码
    key_dic['bidder_code'] = '投标人代码1'
    # 价款形式代码 1 金额 2 费率 3 比率 4 优惠率 5 合格率 6下浮率 7 折扣 8 单价 9 其他
    key_dic['price_form_code'] = '1'
    # 金额形式投标价
    key_dic['bid_price'] = 5000000
    # 其他形式投标价
    key_dic['other_bid_price'] = '其他形式投标价1'
    # 金额形式评标价
    key_dic['eval_price'] = 5000000
    # 其他形式评标价
    key_dic['other_eval_price'] = '其他形式评标价1'
    # 是否无效投标 1 是 0 否
    key_dic['invalid_if'] = '0'
    # 无效投标原因
    key_dic['invalid_reason'] = '无效投标原因1'
    # 评审结果得分汇总
    key_dic['total_score'] = 80
    # 评审结果排序
    key_dic['result_order'] = 1
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_bidder_score'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['bidder_score_id']
    # return sql_end


# print(ce_bidder_score_in({'data_source_code': 'CE-001'}))


# 推荐中标候选人
def ce_candidate_in(dic_a):
    key_dic = {}
    # 主键
    key_dic['candidate_id'] = 'CA_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评审轮次
    key_dic['evaluation_num'] = 1
    # 中标候选人名称
    key_dic['candidate_name'] = '中标候选人名称1'
    # 中标候选人代码
    key_dic['candidate_code'] = '中标候选人代码1'
    # 候选人是否区分排名 1 是 0 否
    key_dic['candidate_order_if'] = '1'
    # 中标候选人排名
    key_dic['order'] = 1
    # 推荐时间
    key_dic['recommend_time'] = dateplus_min(65)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_candidate'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['candidate_id']
    # return sql_end


# print(ce_candidate_in({'data_source_code': 'CE-001'}))


# 中标候选人公示
def ce_candidate_notice_in(dic_a):
    key_dic = {}
    # 中标候选人公示ID
    key_dic['candidate_notice_id'] = 'CAN_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 公示标题
    key_dic['candidate_notice_title'] = '公示标题1'
    # 公示性质 1 首次公示 2 更正公示 3 重发公示
    key_dic['candidate_notice_nature'] = '1'
    # 公示发布范围 1 内网公示 2 内外网公示
    key_dic['candidate_notice_range'] = '2'
    # 公示内容
    key_dic['content'] = '公示内容1'
    # 公示URL
    key_dic['url'] = 'https://www.plap.mil.cn/ '
    # 提出异议的渠道和方式
    key_dic['objection_channel'] = '提出异议的渠道和方式'
    # 公示发布时间
    key_dic['candidate_notice_publish_time'] = dateplus_min(165)
    # 公示开始时间
    key_dic['candidate_notice_start_time'] = dateplus_min(160)
    # 公示结束时间
    key_dic['candidate_notice_end_time'] = dateplus_min(65)
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '建设单位联系电话1'
    # 招标代理联系人
    key_dic['agency_contactor'] = '招标代理联系人1'
    # 招标代理联系电话
    key_dic['agency_phone'] = '招标代理联系电话1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_candidate_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['candidate_notice_id']
    # return sql_end


# print(ce_candidate_notice_in({'data_source_code': 'CE-001'}))


# 中标候选人公示明细
def ce_candidate_notice_item_in(dic_a):
    key_dic = {}
    # 公示明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 中标候选人公示ID
    key_dic['candidate_notice_id'] = 'CAN_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 评标结果ID
    key_dic['eval_result_id'] = 'ER_ID' + datenow_hms()
    # 中标候选人名称
    key_dic['candidate_name'] = '中标候选人名称1'
    # 中标候选人代码
    key_dic['candidate_code'] = '中标候选人代码1'
    # 是否联合体 1 是 0 否
    key_dic['union_if'] = '0'
    # 候选人是否排名 1 是 0 否
    key_dic['order_if'] = '1'
    # 中标候选人排名
    key_dic['order'] = 1
    # 价款形式代码 1 金额 2 费率 3 比率# 4 优惠率 5 合格率 6下浮率 7 折扣 8 单价 9 其他
    key_dic['price_form_code'] = '1'
    # 金额形式投标价
    key_dic['bid_price'] = 200000
    # 其他形式投标价
    key_dic['other_bid_price'] = '其他形式投标价1'
    # 投标单位项目负责人
    key_dic['bidder_manager'] = '投标单位项目负责人1'
    # 投标工期（交货期/服务期）
    key_dic['time_limit'] = '投标工期1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_candidate_notice_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['candidate_notice_id']
    # return sql_end


# print(ce_candidate_notice_item_in({'data_source_code': 'CE-001'}))


# 中标结果公告
def ce_win_notice_in(dic_a):
    key_dic = {}
    # 中标结果公告ID
    key_dic['win_notice_id'] = 'WN_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 公告标题
    key_dic['win_notice_title'] = '公告标题1'
    # 公告性质 1 首次 2 更正 3 重发
    key_dic['win_notice_nature'] = '1'
    # 公告发布范围 1 内网发布 2 内外网发布
    key_dic['win_notice_range'] = '1'
    # 公告内容
    key_dic['content'] = '公告内容1'
    # 公告URL
    key_dic['url'] = 'https://www.plap.mil.cn/ '
    # 公告发布时间
    key_dic['win_notice_publish_time'] = dateplus_min(305)
    # 公告开始时间
    key_dic['win_notice_start_time'] = dateplus_min(300)
    # 公告结束时间
    key_dic['win_notice_end_time'] = dateplus_min(65)
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '1392837483'
    # 招标代理联系人
    key_dic['agency_contactor'] = '招标代理联系人1'
    # 招标代理联系电话
    key_dic['agency_phone'] = '1392837484'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_win_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['win_notice_id']
    # return sql_end


# print(ce_win_notice_in({'data_source_code': 'CE-001'}))


# 中标（成交）结果公告_明细
def ce_win_notice_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 中标结果公告ID
    key_dic['win_notice_id'] = 'WN_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 排序
    key_dic['order'] = 1
    # 中标人名称
    key_dic['win_bidder_name'] = '中标人名称1'
    # 中标人代码
    key_dic['win_bidder_code'] = '中标人代码1'
    # 是否联合体 1 是 0 否
    key_dic['union_if'] = '0'
    # 价款形式代码 1 金额 2 费率 3 比率 4 优惠率 5 合格率 6下浮率 7 折扣 8 单价 9 其他
    key_dic['price_form_code'] = '1'
    # 金额形式中标价
    key_dic['win_bid_price'] = 5000000
    # 其他形式中标价
    key_dic['other_win_bid_price'] = '其他形式中标价1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_win_notice_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_win_notice_item_in({'data_source_code': 'CE-001'}))


# 废标公告
def ce_failure_notice_in(dic_a):
    key_dic = {}
    # 废标公告ID
    key_dic['failure_notice_id'] = 'FN_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 公告标题
    key_dic['failure_notice_title'] = '公告标题1'
    # 公告发布范围 1 内网发布 2 内外网发布
    key_dic['win_notice_range'] = '1'
    # 公告内容
    key_dic['content'] = '公告内容1'
    # 公告URL
    key_dic['url'] = 'https://www.plap.mil.cn/ '
    # 公告发布时间
    key_dic['win_notice_publish_time'] = dateplus_min(405)
    # 公告开始时间
    key_dic['win_notice_start_time'] = dateplus_min(305)
    # 公告结束时间
    key_dic['win_notice_end_time'] = dateplus_min(45)
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '1383743843'
    # 招标代理联系人
    key_dic['agency_contactor'] = '招标代理联系人1'
    # 招标代理联系电话
    key_dic['agency_phone'] = '1392384384'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_failure_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['failure_notice_id']
    # return sql_end


# print(ce_failure_notice_in({'data_source_code': 'CE-001'}))


# 废标公告_明细
def ce_failure_notice_item_in(dic_a):
    key_dic = {}
    # 明细ID
    key_dic['item_id'] = 'IT_ID' + datenow_hms()
    # 废标公告ID
    key_dic['failure_notice_id'] = 'FN_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = '公告标题1'
    # 废标原因类型
    key_dic['failure_reason_type'] = '1'
    # 废标原因
    key_dic['failure_reason'] = '废标原因1'
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_failure_notice_item'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['item_id']
    # return sql_end


# print(ce_failure_notice_item_in({'data_source_code': 'CE-001'}))


# 中标结果通知书
def ce_win_note_in(dic_a):
    key_dic = {}
    # 通知书ID
    key_dic['note_id'] = 'NTE_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 标段ID
    key_dic['section_id'] = 'ST_ID' + datenow_hms()
    # 招标项目名称
    key_dic['tender_project_name'] = '招标项目名称1'
    # 标段名称
    key_dic['section_name'] = '标段名称1'
    # 通知书性质 1 首次 2 更正 3 重发
    key_dic['note_nature'] = '1'
    # 通知书类型 1 中标通知书 2 未中标通知书
    key_dic['note_type'] = '1'
    # 建设单位名称
    key_dic['tenderer_name'] = '建设单位名称1'
    # 建设单位代码
    key_dic['tenderer_code'] = '建设单位代码1'
    # 通知书接收人
    key_dic['recipient_name'] = '通知书接收人1'
    # 通知书接收人代码
    key_dic['recipient_code'] = '通知书接收人代码1'
    # 通知书发出时间
    key_dic['note_send_time'] = dateplus_min(205)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_win_note'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['note_id']
    # return sql_end


# print(ce_win_note_in({'data_source_code': 'CE-001'}))


# 异常（终止、暂停）报告
def ce_excepiton_notice_in(dic_a):
    key_dic = {}
    # 异常报告ID
    key_dic['excepiton_report_id'] = 'EXR_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 相关标段ID
    key_dic['section_ids'] = 'ST_IDS' + datenow_hms()
    # 报告名称
    key_dic['excepiton_report_title'] = '报告名称1'
    # 异常报告类型 1 终止 2 暂停 3 恢复 9 其他
    key_dic['excepiton_report_type'] = '1'
    # 异常情况描述
    key_dic['excepiton_report_content'] = '异常情况描述1'
    # 异常发生时项目所处环节 A1 文件编制及审核 A2 项目入场登记 B1 资审场地预约 B2 资审公告 B3 资审澄清与变更 B4 资审开标 B5 资审评标
    # B6 资审结果通知书 C1 场地预约 D1 招标公告/投标邀请书 D2 澄清与变更 D1 开标 D2 评标 E1 候选人公示 E2 确定中标人 E3 结果公告 99 其他
    key_dic['excepiton_step'] = 'A1'
    # 终止/暂停/恢复原因
    key_dic['excepiton_reason'] = '终止/暂停/恢复原因1'
    # 建设单位名称
    key_dic['tenderer_name'] = '建设单位名称1'
    # 建设单位地址
    key_dic['tenderer_address'] = '建设单位地址1'
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '建设单位联系电话1'
    # 建设单位电子邮件
    key_dic['tenderer_mail'] = '建设单位电子邮件1'
    # 招标代理联系电话
    key_dic['agency_phone'] = '招标代理联系电话1'
    # 异常发生时间
    key_dic['excepiton_time'] = dateplus_min(105)
    # 异常报告发布时间
    key_dic['excepiton_report_time'] = dateplus_min(100)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_excepiton_notice'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['excepiton_report_id']
    # return sql_end


# print(ce_excepiton_notice_in({'data_source_code': 'CE-001'}))


# 招标失败报告
def ce_tender_fail_in(dic_a):
    key_dic = {}
    # 招标失败报告ID
    key_dic['tender_fail_id'] = 'TF_ID' + datenow_hms()
    # 招标项目ID
    key_dic['tender_project_id'] = 'TP_ID' + datenow_hms()
    # 相关标段ID
    key_dic['section_ids'] = 'ST_IDS' + datenow_hms()
    # 报告名称
    key_dic['excepiton_report_title'] = '报告名称1'
    # 招标失败情况描述
    key_dic['excepiton_report_content'] = '招标失败情况描述1'
    # 招标失败原因 字典待最终确认
    key_dic['tender_faliure_reason'] = '1'
    # 招标失败处理结果 1 重新招标 2 招标终止
    key_dic['faliure_result'] = '1'
    # 招标失败时项目所处环节 A1 文件编制及审核 A2 项目入场登记 B1 资审场地预约 B2 资审公告 B3 资审澄清与变更 B4 资审开标 B5 资审评标
    # B6 资审结果通知书 C1 场地预约 D1 招标公告/投标邀请书 D2 澄清与变更 D1 开标 D2 评标 E1 候选人公示 E2 确定中标人 E3 结果公告 99 其他
    key_dic['excepiton_step'] = '1'
    # 建设单位名称
    key_dic['tenderer_name'] = '建设单位名称1'
    # 建设单位地址
    key_dic['tenderer_address'] = '建设单位地址1'
    # 建设单位联系人
    key_dic['tenderer_contactor'] = '建设单位联系人1'
    # 建设单位联系电话
    key_dic['tenderer_phone'] = '建设单位联系电话1'
    # 建设单位电子邮件
    key_dic['tenderer_mail'] = '建设单位电子邮件1'
    # 异常发生时间
    key_dic['excepiton_time'] = dateplus_min(105)
    # 异常报告发布时间
    key_dic['excepiton_report_time'] = dateplus_min(100)
    # 数据来源代码
    key_dic['data_source_code'] = 'CE-001'
    # 数据来源名称
    key_dic['data_source_name'] = '工程电子招投标系统'
    # 数据时间戳
    key_dic['data_timestamp'] = dateplus_min(0)
    # 在上一层库的更新时间
    key_dic['source_data_change_timestamp'] = dateplus_min(5)
    # 更新时间
    key_dic['data_change_timestamp'] = dateplus_min(5)
    for key in dic_a:
        key_dic[key] = dic_a[key]
    tup_key = tuple(list(key_dic.keys()))
    tup_value = tuple(list(key_dic.values()))
    tab_name = 'ce_tender_fail'
    sql_1 = f"INSERT INTO {tab_name}{tup_key}"
    sql_2 = sql_1.replace("'", "`")
    sql_3 = f" VALUES {tup_value}"
    sql_end = sql_2 + sql_3
    db = pymysql.connect(host='10.10.10.85',
                         port=3306, user='root',
                         password='GLD@ft321',
                         database='gld_ods_gb')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 执行sql语句
    cursor.execute(sql_end)
    # 提交到数据库执行
    db.commit()
    db.close()
    return key_dic['tender_fail_id']
    # return sql_end

# print(ce_tender_fail_in({'data_source_code': 'CE-001'}))
