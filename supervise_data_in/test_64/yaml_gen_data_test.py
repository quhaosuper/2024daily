import yaml
import itertools
import datetime


def detail_times(items_num):
    list_res = []
    n = 1
    while items_num > 0:
        res = '明细项' + str(n)
        list_res.append(res)
        n += 1
        items_num -= 1
    return list_res


# print(detail_times(3))

def list_data_times(sample, num):
    list_res = []
    n = 1
    while num > 0:
        res = sample + str(n)
        list_res.append(res)
        n += 1
        num -= 1
    return list_res


# print(list_data_times('供应商名称', 4))
