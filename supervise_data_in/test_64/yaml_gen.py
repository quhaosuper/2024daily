from yaml_gen_data_test import *


def quali_exam_detail(num_d, num_s, num_e):
    detail_items = list_data_times('明细项', num_d)
    suppliers = list_data_times('供应商名称', num_s)
    experts = list_data_times('专家', num_e)

    # 生成所有可能的排列组合数据
    all_combinations = list(itertools.product(detail_items, suppliers, experts))

    # 根据排列组合数据生成对应的数据项
    generated_data = []
    for combination in all_combinations:
        detail_name, supplier_name, expert_name = combination
        data_item = {
            'DETAIL_ID': f'明细项ID_{detail_name}',
            'DETAIL_NAME': detail_name,
            'SUPPLIER_NAME': supplier_name,
            'SUPPLIER_CODE': f'供应商代码_{supplier_name}',
            'EXPERT_ID': f'专家ID_{expert_name}',
            'EXPERT_NAME': expert_name,
            'ID_CARD': f'专家身份证件号_{expert_name}',
            'PASS_OR_NOT': '1',
            'REASON_FOR_REJECTION': f'不通过理由_{expert_name}'
        }
        generated_data.append(data_item)

    # 将数据写入yaml文件
    file_name = f'资格性审查明细表_{datetime.datetime.now().strftime("%m-%d_%H%M%S")}.yaml'
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(generated_data, file, default_flow_style=False, allow_unicode=True)

    print(f'已生成文件: {file_name}')


# quali_exam_detail(3, 4, 4)


def core_pro_rev_detail(num_p, num_s, num_e):
    pro_items = list_data_times('产品名称', num_p)
    suppliers = list_data_times('供应商名称', num_s)
    experts = list_data_times('专家', num_e)

    # 生成所有可能的排列组合数据
    all_combinations = list(itertools.product(pro_items, suppliers, experts))

    # 根据排列组合数据生成对应的数据项
    generated_data = []
    for combination in all_combinations:
        pro_name, supplier_name, expert_name = combination
        data_item = {
            'PRODUCT_ID': f'ID_{pro_name}',
            'PRODUCT_NAME': pro_name,
            'SUPPLIER_NAME': supplier_name,
            'SUPPLIER_CODE': f'供应商代码_{supplier_name}',
            'EXPERT_NAME': expert_name,
            'DOCUMENT_TYPE': '1',
            'ID_CARD': f'专家身份证件号_{expert_name}',
            'TECHNICAL_SCORE': 30,
            'BUSINESS_RATING': 30,
            'PRICE_RATING': 30,
            'SCORE_SUMMARY': 90
        }
        generated_data.append(data_item)

    # 将数据写入yaml文件
    file_name = f'同品牌评审得分表_{datetime.datetime.now().strftime("%m-%d_%H%M%S")}.yaml'
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(generated_data, file, default_flow_style=False, allow_unicode=True)

    print(f'已生成文件: {file_name}')


# core_pro_rev_detail(4, 4, 4)

def purchase_section_clause(num_lv1, num_lv2):
    lv1_id = list_data_times('一级评审项ID', num_lv1)
    lv2_id = list_data_times('二级评审项', num_lv2)

    # 生成所有可能的排列组合数据
    all_combinations = list(itertools.product(lv1_id, lv2_id))

    # 根据排列组合数据生成对应的数据项
    generated_data = []
    for combination in all_combinations:
        lv1_id, lv2_id = combination
        data_item = {
            # 二级评审项ID
            'EVAL_LEVEL2_ID': f'{lv2_id}_ID',
            # 一级评审项ID
            'EVAL_LEVEL1_ID': f'{lv1_id}',
            # 评审因素
            'EVAL_LEVEL2_ITEM': f'{lv2_id}',
            # 序号
            'CLAUSE_SEQUENCE': 1,
            # 是否客观评审项 1 是 0 否
            'IS_OBJECTIVE': '1',
            # 二级评审项分数
            'EVAL_LEVEL2_SCORE': 60,
            # 评分项权重
            'EVAL_ITEM_RATE': 11
        }
        generated_data.append(data_item)

    # 将数据写入yaml文件
    file_name = f'采购包评审条款小类_{datetime.datetime.now().strftime("%m-%d_%H%M%S")}.yaml'
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(generated_data, file, default_flow_style=False, allow_unicode=True)

    print(f'已生成文件: {file_name}')


purchase_section_clause(2, 4)
