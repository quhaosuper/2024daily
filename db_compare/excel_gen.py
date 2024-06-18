from openpyxl import Workbook
from datetimetr import *

# 创建一个新的工作簿
workbook = Workbook()

# 选择要写入数据的工作表（默认为第一个工作表）
sheet = workbook.active

# 创建一个数据列表
data = [
    ["表名", "所用主键", "在MongoDB存在MySQL不存在", "MySQL未同步到MongoDB", "值不匹配字段为"],
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# 按顺序写入数据
for row in data:
    sheet.append(row)

# 保存Excel文件
workbook.save(f"{datenow_hms()}.xlsx")

print("Excel文件已生成并数据写入完成。")