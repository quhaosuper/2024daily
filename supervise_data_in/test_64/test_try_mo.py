# 创建一个空列表，用于存储所有的res集合
res_list = []


def test_pr():
    # 根据i的数量创建相应数量的空列表
    for _ in range(3):
        res_list.append([])

    for i in range(3):
        for j in range(3):
            res = 3

            # 将每个res集合添加到对应索引的列表中
            res_list[i].append(res)

    # 输出 res_list 列表
    print(res_list)
