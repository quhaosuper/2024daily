from supervision_module import *


@allure.feature("tbd")
class Test_insert:
    @pytest.mark.parametrize("input_d",
                             yaml.safe_load(open("plan_require_in_supervisor.yml", encoding='utf-8')))
    @allure.story("tbd")
    def test_all_1(self, input_d):
        list_excute_ui = []
        dic_excute = input_d['dic_excute']
        if dic_excute['plan_quar'] == 0:
            return
        else:
            year_project_id = plan_year_in(input_d['dic_plan_year'])
            input_d['dic_plan_quar']['YEAR_PROJECT_ID'] = year_project_id
            tup_plan_quar = plan_quar_in(input_d['dic_plan_quar'])
            plan_quar_project_name = tup_plan_quar[0]
            quar_project_id = tup_plan_quar[1]
            agent_code = tup_plan_quar[2]
            agent_name = tup_plan_quar[3]
            unit_name = tup_plan_quar[4]
            unit_code = tup_plan_quar[5]
        # print(agent_code, agent_name, unit_name, unit_code)
        list_excute_ui.append('季度明细计划')
        for i in range(len(input_d['dic_plan_approval'])):
            if input_d['dic_plan_approval'][i]['PLAN_TYPE'] == '1':
                input_d['dic_plan_approval'][i]['OBJECT_ID'] = year_project_id
            else:
                input_d['dic_plan_approval'][i]['OBJECT_ID'] = quar_project_id
            purchase_plan_approval_in(input_d['dic_plan_approval'][i])
        require_id = '1'
        o_require_id = '1'
        require_pro_name = '1'
        if dic_excute['require_compilation'] == 0:
            print(plan_quar_project_name, quar_project_id)
            # act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_require_compilation'])):
                input_d['dic_require_compilation'][i]['QUAR_PROJECT_ID'] = quar_project_id
                input_d['dic_require_compilation'][i]['PURCHASE_AGENT_CODE'] = agent_code
                input_d['dic_require_compilation'][i]['PURCHASE_AGENT_NAME'] = agent_name
                input_d['dic_require_compilation'][i]['PURCHASE_UNIT_CODE'] = unit_code
                input_d['dic_require_compilation'][i]['PURCHASE_UNIT_NAME'] = unit_name
                if i == 0:
                    res_tup = require_compilation_in(input_d['dic_require_compilation'][i])
                    require_id = res_tup[0]
                    o_require_id = res_tup[1]
                    require_pro_name = res_tup[2]
                else:
                    input_d['dic_require_compilation'][i]['REQUIRE_ID'] = require_id
                    input_d['dic_require_compilation'][i]['ORIGIN_REQUIRE_ID'] = o_require_id
                    input_d['dic_require_compilation'][i]['REQUIRE_PROJECT_NAME'] = require_pro_name
                    require_compilation_in(input_d['dic_require_compilation'][i])
        list_excute_ui.append('采购需求编制')
        list_intention_notice_id = []
        if dic_excute['intention_notice'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_intention_notice'])):
                input_d['dic_intention_notice'][i]['REQUIRE_ID'] = require_id
                ele1 = intention_notice_in(input_d['dic_intention_notice'][i])
                time.sleep(1)
                list_intention_notice_id.append(ele1)
        list_excute_ui.append('采购意向公开数仓同步')
        if dic_excute['require_survey'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            list_require_survey_id = []
            for j in range(len(input_d['dic_require_survey'])):
                input_d['dic_require_survey'][j]['REQUIRE_ID'] = require_id
                input_d['dic_require_survey'][j]['QUAR_PROJECT_ID'] = quar_project_id
                ele2 = require_survey_in(input_d['dic_require_survey'][j])
                time.sleep(1)
                list_require_survey_id.append(ele2)
        list_excute_ui.append('采购需求调查概况')
        if dic_excute['survey_detail'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            list_surveydetail = []
            for i in range(len(input_d['dic_survey_detail'])):
                input_d['dic_survey_detail'][i]['REQUIRE_SURVEY_ID'] = list_require_survey_id[i]
                ele3 = survey_detail_in(input_d['dic_survey_detail'][i])
                time.sleep(1)
                list_surveydetail.append(ele3)
        list_excute_ui.append('采购需求调查明细')
        if dic_excute['purchase_demonstration'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            list_purchase_demonstration = []
            for i in range(len(input_d['dic_purchase_demonstration'])):
                input_d['dic_purchase_demonstration'][i]['QUAR_PROJECT_ID'] = quar_project_id
                input_d['dic_purchase_demonstration'][i]['REQUIRE_ID'] = require_id
                ele4 = purchase_demonstration_in(input_d['dic_purchase_demonstration'][i])
                time.sleep(1)
                list_purchase_demonstration.append(ele4)
        list_excute_ui.append('采购需求专项论证同步')
        if dic_excute['demonstration_detail'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            list_demonstration_detail = []
            for i in range(len(input_d['dic_demonstration_detail'])):
                for j in range(len(input_d['dic_demonstration_detail'][i])):
                    input_d['dic_demonstration_detail'][i][j]['DEMONSTRATION_ID'] = list_purchase_demonstration[i]
                    ele5 = demonstration_detail_in(input_d['dic_demonstration_detail'][i][j])
                    time.sleep(1)
                    list_demonstration_detail.append(ele5)
        list_excute_ui.append('采购需求专项论证明细')
        list_requirement_id = []
        if dic_excute['require_project'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail)
            act_universal_list_row0(list_excute_ui)
            return
        else:

            for i in range(len(input_d['dic_require_project'])):
                input_d['dic_require_project'][i]['QUAR_PROJECT_ID'] = quar_project_id
                input_d['dic_require_project'][i]['REQUIRE_ID'] = require_id
                input_d['dic_require_project'][i]['PURCHASE_AGENT_CODE'] = agent_code
                input_d['dic_require_project'][i]['PURCHASE_AGENT_NAME'] = agent_name
                input_d['dic_require_project'][i]['PURCHASE_UNIT_CODE'] = unit_code
                input_d['dic_require_project'][i]['PURCHASE_UNIT_NAME'] = unit_name
                ele6 = require_project_in(input_d['dic_require_project'][i])
                time.sleep(1)
                list_requirement_id.append(ele6)
        list_excute_ui.append('采购需求编制项目概况')
        list_require_section_id = []
        if dic_excute['require_project'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_require_section'])):
                input_d['dic_require_section'][i]['REQUIREMENT_ID'] = list_requirement_id[0]
                ele7 = require_section_in(input_d['dic_require_section'][i])
                time.sleep(1)
                list_require_section_id.append(ele7)
        list_excute_ui.append('采购需求编制分包情况数仓同步')
        list_section_detail_id = []
        if dic_excute['require_project'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_section_detail'])):
                for j in range(len(input_d['dic_section_detail'][i])):
                    input_d['dic_section_detail'][i][j]['REQUIRE_SECTION_ID'] = list_require_section_id[i]
                    ele8 = section_detail_in(input_d['dic_section_detail'][i][j])
                    time.sleep(1)
                    list_section_detail_id.append(ele8)
        list_excute_ui.append('采购需求编制分包标的明细')
        list_require_notice_id = []
        if dic_excute['require_notice'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_require_notice'])):
                input_d['dic_require_notice'][i]['REQUIRE_ID'] = require_id
                ele9 = require_notice_in(input_d['dic_require_notice'][i])
                time.sleep(1)
                list_require_notice_id.append(ele9)
        list_excute_ui.append('采购需求公示')
        list_require_check_id = []
        if dic_excute['require_check'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id,
                  list_require_notice_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_require_check'])):
                input_d['dic_require_check'][i]['REQUIRE_ID'] = require_id
                ele10 = require_check_in(input_d['dic_require_check'][i])
                time.sleep(1)
                list_require_check_id.append(ele10)
        list_excute_ui.append('采购需求审查')
        if dic_excute['require_submit'] == 0:
            print(plan_quar_project_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
                  list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id,
                  list_require_notice_id, list_require_check_id)
            act_universal_list_row0(list_excute_ui)
            return
        else:
            for i in range(len(input_d['dic_require_submit'])):
                input_d['dic_require_submit'][i]['REQUIRE_ID'] = require_id
                ele11 = require_submit_in(input_d['dic_require_submit'][i])
                time.sleep(1)
        list_excute_ui.append('采购需求项目提报数仓同步')
        # act_universal_list_row0(list_excute_ui)
        print(plan_quar_project_name, o_require_id, require_pro_name, quar_project_id, require_id, list_intention_notice_id, list_require_survey_id,
              list_surveydetail, list_purchase_demonstration, list_demonstration_detail, list_requirement_id,
              list_require_notice_id, list_require_check_id)
        print(list_excute_ui)