
from yaml_gen_data_test import *


suppliers = list_data_times('供应商名称', 20)


# 生成所有可能的排列组合数据
all_combinations = list(itertools.product(suppliers))

# 根据排列组合数据生成对应的数据项
generated_data = []
for supplier_name in suppliers:

    data_item = {
        'SUPPLIER_NAME': supplier_name,
        'SUPPLIER_CODE': f'供应商代码_{supplier_name}',
        'PASS_OR_NOT': '1'
    }
    generated_data.append(data_item)

# 将数据写入yaml文件
file_name = f'资格性审查结果表_{datetime.datetime.now().strftime("%m-%d_%H%M%S")}.yaml'
with open(file_name, 'w', encoding='utf-8') as file:
    yaml.dump(generated_data, file, default_flow_style=False, allow_unicode=True)

print(f'已生成文件: {file_name}')