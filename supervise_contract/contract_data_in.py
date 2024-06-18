import allure
import pytest
import pymysql
import yaml
from test_0630.supervise_contract.contract_mo import *
from test_0630.supervise_data_in.test_64.datetimetr import *


class Test_insert:
    @pytest.mark.parametrize("input_d",
                             yaml.safe_load(open("contract_data.yml", encoding='utf-8')))
    def test_all_1(self, input_d):
        contract_edit_id = contract_edit_in(input_d['dic_contract_edit'])
        for i in range(len(input_d['dic_contract_object_detail'])):
            input_d['dic_contract_object_detail'][i]['CONTRACT_EDIT_ID'] = contract_edit_id
            contract_object_detail_in(input_d['dic_contract_object_detail'][i])
        input_d['dic_contract_archive']['CONTRACT_EDIT_ID'] = contract_edit_id
        contract_archive_in(input_d['dic_contract_archive'])
        input_d['dic_contract_delivery_acceptance']['CONTRACT_EDIT_ID'] = contract_edit_id
        contract_delivery_acceptance_in(input_d['dic_contract_delivery_acceptance'])
        input_d['dic_contract_pay_closing']['CONTRACT_EDIT_ID'] = contract_edit_id
        contract_pay_closing_in(input_d['dic_contract_pay_closing'])
        input_d['dic_contract_proposal_approval']['CONTRACT_EDIT_ID'] = contract_edit_id
        contract_pay_closing_in(input_d['dic_contract_proposal_approval'])
        list_plan_id = list()
        for i in range(len(input_d['dic_contract_conclusion'])):
            input_d['dic_contract_conclusion'][i]['CONTRACT_EDIT_ID'] = contract_edit_id
            list_plan_id.append(contract_conclusion_in(input_d['dic_contract_conclusion'][i]))
        input_d['dic_contract_project']['CONTRACT_PLAN_ID'] = list_plan_id[0]
        contract_project_in(input_d['dic_contract_project'])
        input_d['dic_contract_delivery_project']['CONTRACT_PLAN_ID'] = list_plan_id[0]
        contract_delivery_project_in(input_d['dic_contract_delivery_project'])
        input_d['dic_contract_pay_project']['CONTRACT_PLAN_ID'] = list_plan_id[0]
        contract_pay_project_in(input_d['dic_contract_pay_project'])
        list_implementation_id = list()
        for i in range(len(input_d['dic_contract_implementation'])):
            input_d['dic_contract_implementation'][i]['CONTRACT_EDIT_ID'] = contract_edit_id
            list_implementation_id.append(contract_implementation_in(input_d['dic_contract_implementation'][i]))
        list__modi_id = list()
        for i in range(len(input_d['dic_contract_modi'])):
            input_d['dic_contract_modi'][i]['CONTRACT_EDIT_ID'] = contract_edit_id
            list__modi_id.append(contract_modi_in(input_d['dic_contract_modi'][i]))
        for i in range(len(input_d['dic_contract_change'])):
            for j in range(len(input_d['dic_contract_change'][i])):
                input_d['dic_contract_change'][i][j]['CONTRACT_MODI_ID'] = list__modi_id[i]
                contract_change_in(input_d['dic_contract_change'][i][j])
        for i in range(len(input_d['dic_contract_cancel'])):
            input_d['dic_contract_cancel'][i]['CONTRACT_EDIT_ID'] = contract_edit_id
            list__modi_id.append(contract_cancel_in(input_d['dic_contract_cancel'][i]))