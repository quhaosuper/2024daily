from implement_module import *


class Test_insert:
    @pytest.mark.parametrize("input_d",
                             yaml.safe_load(open("./implement_in.yml", encoding='utf-8')))
    def test_all_1(self, input_d):
        list_re_fi_ap_id = []
        list_ori_re_id = []
        list_re_pro_id = []
        for i in range(len(input_d['dic_requirment_first_approval'])):
            tup_first_approval = purchase_requirment_first_approval_in(input_d['dic_requirment_first_approval'][i])
            list_re_fi_ap_id.append(tup_first_approval[0])
            list_ori_re_id.append(tup_first_approval[1])
            list_re_pro_id.append(tup_first_approval[2])
        for i in range(len(input_d['dic_first_approval_content'])):
            input_d['dic_first_approval_content'][i]['REQUIRMENT_FIRST_APPROVAL_ID'] = list_re_fi_ap_id[i]
            purchase_requirment_first_approval_content(input_d['dic_first_approval_content'][i])
        for i in range(len(input_d['dic_task_assign'])):
            input_d['dic_task_assign'][i]['ORIGIN_REQUIRE_ID'] = list_ori_re_id[0]
            input_d['dic_task_assign'][i]['REQUIREMENT_PROXY_ID'] = list_re_pro_id[0]
            purchase_task_assign_in(input_d['dic_task_assign'][i])
        list_re_rv_ap_id = []
        list_pue_ann_id = []
        for i in range(len(input_d['dic_requirment_review_approval'])):
            input_d['dic_requirment_review_approval'][i]['ORIGIN_REQUIRE_ID'] = list_ori_re_id[0]
            input_d['dic_requirment_review_approval'][i]['REQUIREMENT_PROXY_ID'] = list_re_pro_id[0]
            list_re_rv_ap_id.append(purchase_requirment_review_approval_in
                                    (input_d['dic_requirment_review_approval'][i]))
        for i in range(len(input_d['dic_review_approval_content'])):
            input_d['dic_review_approval_content'][i]['REQUIRMENT_REVIEW_APPROVAL_ID'] = list_re_rv_ap_id[i]
            purchase_requirment_review_approval_content_in(input_d['dic_review_approval_content'][i])
        for i in range(len(input_d['dic_opinion_announcement'])):
            input_d['dic_opinion_announcement'][i]['ORIGIN_REQUIRE_ID'] = list_ori_re_id[0]
            list_pue_ann_id.append(purchase_opinion_announcement_in(input_d['dic_opinion_announcement'][i]))
        for i in range(len(input_d['dic_announcement_feedback'])):
            for j in range(len(input_d['dic_announcement_feedback'][i])):
                input_d['dic_announcement_feedback'][i][j]['OPINION_ANNOUNCEMENT_ID'] = list_pue_ann_id[i]
                annoucement_feedback_in(input_d['dic_announcement_feedback'][i][j])

        list_excute_ui = []
        dic_excute = input_d['dic_excute']
        if dic_excute['purchase_project'] == 0:
            return
        else:
            input_d['dic_purchase_project']['ORIGIN_REQUIRE_ID'] = list_ori_re_id[0]
            tup_purchase_project = purchase_project_in(input_d['dic_purchase_project'])
            purchaseprojectid = tup_purchase_project[0]
            purchaseprojectname = tup_purchase_project[1]
            purchaseprojectcode = tup_purchase_project[2]
            list_purchasesectionid = []
            list_purchasesectioncode = []
            list_purchasesectiondetailid = []
            list_openbidid = []
            list_evaluationevalreportid = []
            list_evalcommitteeid = []
            for i in range(len(input_d['dic_purchase_section'])):
                input_d['dic_purchase_section'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                list_a = purchase_section_in(input_d['dic_purchase_section'][i])
                list_purchasesectionid.append(list_a[0])
                list_purchasesectioncode.append(list_a[1])
            for i in range(len(input_d['dic_section_detail'])):
                for j in range(len(input_d['dic_section_detail'][i])):
                    input_d['dic_section_detail'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    list_purchasesectiondetailid.append(section_detail_in(input_d['dic_section_detail'][i][j]))
        list_excute_ui.append('采购项目信息数仓同步')
        list_excute_ui.append('采购包信息数仓同步')
        list_purchase_file_id = []
        if dic_excute['invite_bid'] == 0:
            print(purchaseprojectid, purchaseprojectname)
            return
        else:
            for i in range(len(input_d['dic_purchase_file'])):
                input_d['dic_purchase_file'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dic_purchase_file'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                list_purchase_file_id.append(purchase_file_in(input_d['dic_purchase_file'][i]))
            for i in range(len(input_d['dic_purchase_file_section'])):
                input_d['dic_purchase_file'][i]['PURCHASE_FILE_ID'] = list_purchase_file_id[i]
                input_d['dic_purchase_file'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                purchase_file_section_in(input_d['dic_purchase_file_section'][i])
            for i in range(len(input_d['dic_section_clause_type'])):
                for j in range(len(input_d['dic_section_clause_type'][i])):
                    input_d['dic_section_clause_type'][i][j]['PURCHASE_FILE_ID'] = list_purchase_file_id[i]
                    input_d['dic_section_clause_type'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    purchase_section_clause_type_in(input_d['dic_section_clause_type'][i][j])
            for i in range(len(input_d['dic_purchase_section_clause'])):
                purchase_section_clause_in(input_d['dic_purchase_section_clause'][i])
            for i in range(len(input_d['dic_section_technical_requirement'])):
                for j in range(len(input_d['dic_section_technical_requirement'][i])):
                    input_d['dic_section_technical_requirement'][i][j]['PURCHASE_FILE_ID'] = purchaseprojectid
                    input_d['dic_section_technical_requirement'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    section_technical_requirement_in(input_d['dic_section_technical_requirement'][i][j])
            for i in range(len(input_d['dic_section_special_qualification'])):
                for j in range(len(input_d['dic_section_special_qualification'][i])):
                    input_d['dic_section_special_qualification'][i][j]['PURCHASE_FILE_ID'] = purchaseprojectid
                    input_d['dic_section_special_qualification'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    section_special_qualification_in(input_d['dic_section_special_qualification'][i][j])
            for i in range(len(input_d['dic_purchase_doc_approval'])):
                for j in range(len(input_d['dic_purchase_doc_approval'][i])):
                    input_d['dic_purchase_doc_approval'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_purchase_doc_approval'][i][j]['PURCHASE_FILE_ID'] = list_purchase_file_id[i]
                    purchase_doc_approval_in(input_d['dic_purchase_doc_approval'][i][j])
            list_tender_notice_id = []
            for i in range(len(input_d['dic_purchase_tender_notice'])):
                input_d['dic_purchase_tender_notice'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                list_tender_notice_id.append(purchase_tender_notice_in(input_d['dic_purchase_tender_notice'][i]))
            for i in range(len(input_d['dic_tender_notice_section'])):
                for j in range(len(input_d['dic_tender_notice_section'][i])):
                    input_d['dic_tender_notice_section'][i][j]['TENDER_NOTICE_ID'] = list_tender_notice_id[0]
                    input_d['dic_tender_notice_section'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_tender_notice_section'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    purchase_tender_notice_section_in(input_d['dic_tender_notice_section'][i][j])
            for i in range(len(input_d['dic_file_download'])):
                input_d['dic_file_download'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dic_file_download'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                purchase_file_download_in(input_d['dic_file_download'][i])
            for i in range(len(input_d['dic_tender_file_submit'])):
                for j in range(len(input_d['dic_tender_file_submit'][i])):
                    input_d['dic_tender_file_submit'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_tender_file_submit'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    purchase_tender_file_submit_in(input_d['dic_tender_file_submit'][i][j])
        if dic_excute['open_bid'] == 0:
            print(purchaseprojectid, purchaseprojectname)
            return
        else:
            for i in range(len(input_d['dic_open_bid_record'])):
                input_d['dic_open_bid_record'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dic_open_bid_record'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                list_openbidid.append(purchase_open_bid_record(input_d['dic_open_bid_record'][i]))
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dic_supplier_list'])):
                    input_d['dic_supplier_list'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_supplier_list'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dic_supplier_list'][j]['OPEN_BID_ID'] = list_openbidid[i]
                    purchase_supplier_list_in(input_d['dic_supplier_list'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dic_file_info'])):
                    input_d['dic_file_info'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_file_info'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    purchase_file_info_in(input_d['dic_file_info'][j])
        list_excute_ui.append('开标记录')
        list_excute_ui.append('开标明细/供应商名单')
        list_excute_ui.append('投标（报价）文件特征码信息数仓同步')
        list_qual_exami_id = []
        list_qual_sectionid = []
        list_comp_rev_id = []
        list_comp_sectionid = []
        if dic_excute['evaluation_bid'] == 0:
            print(purchaseprojectid, purchaseprojectname)
            return
        else:
            for i in range(len(input_d['dict_evaluation_report'])):
                input_d['dict_evaluation_report'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dict_evaluation_report'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                list_evaluationevalreportid.append(evaluation_report_in(input_d['dict_evaluation_report'][i]))
            for i in range(len(input_d['dict_eval_committee'])):
                input_d['dict_eval_committee'][i]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dict_eval_committee'][i]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                list_evalcommitteeid.append(eval_committee_in(input_d['dict_eval_committee'][i]))
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_expert_list'])):
                    input_d['dict_expert_list'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_expert_list'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dict_expert_list'][j]['EVAL_COMMITTEE_ID'] = list_evalcommitteeid[i]
                    expert_list_in(input_d['dict_expert_list'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_supplier_score_detail'])):
                    input_d['dict_supplier_score_detail'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_supplier_score_detail'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    supplier_score_detail_in(input_d['dict_supplier_score_detail'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_score_detail'])):
                    input_d['dict_score_detail'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_score_detail'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    score_detail_in(input_d['dict_score_detail'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_candidate_list'])):
                    input_d['dict_candidate_list'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_candidate_list'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    candidate_list_in(input_d['dict_candidate_list'][j])
            for i in range(len(input_d['dict_supplier_score'])):
                for j in range(len(input_d['dict_supplier_score'][i])):
                    for h in range(len(input_d['dict_supplier_score'][i][j])):
                        input_d['dict_supplier_score'][i][j][h]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                        input_d['dict_supplier_score'][i][j][h]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                        supplier_score_in(input_d['dict_supplier_score'][i][j][h])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_neg_offer'])):
                    input_d['dict_neg_offer'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_neg_offer'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dict_neg_offer'][j]['EVALUATION_EVAL_REPORT_ID'] = list_evaluationevalreportid[i]
                    neg_offer_in(input_d['dict_neg_offer'][j])
            for i in range(len(input_d['dic_qualification_examination'])):
                for j in range(len(input_d['dic_qualification_examination'][i])):
                    input_d['dic_qualification_examination'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_qualification_examination'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    list_qual = qualification_examination_in(input_d['dic_qualification_examination'][i][j])
                    list_qual_exami_id.append(list_qual[0])
                    list_qual_sectionid.append(list_qual[1])
            for i in range(len(input_d['dict_qualification_panel'])):
                for j in range(len(input_d['dict_qualification_panel'][i])):
                    input_d['dict_qualification_panel'][i][j]['QUALIFICATION_EXAMINATION_ID'] = list_qual_exami_id[i]
                    input_d['dict_qualification_panel'][i][j]['PURCHASE_SECTION_ID'] = list_qual_sectionid[i]
                    qualification_panel_in(input_d['dict_qualification_panel'][i][j])
            for i in range(len(input_d['dict_qualification_examination_detail'])):
                for j in range(len(input_d['dict_qualification_examination_detail'][i])):
                    input_d['dict_qualification_examination_detail'][i][j]['QUALIFICATION_EXAMINATION_ID']\
                        = list_qual_exami_id[i]
                    input_d['dict_qualification_examination_detail'][i][j]['PURCHASE_SECTION_ID']\
                        = list_qual_sectionid[i]
                    qualification_examination_detail_in(input_d['dict_qualification_examination_detail'][i][j])
            for i in range(len(input_d['dict_examination_result'])):
                for j in range(len(input_d['dict_examination_result'][i])):
                    input_d['dict_examination_result'][i][j]['QUALIFICATION_EXAMINATION_ID'] = list_qual_exami_id[i]
                    input_d['dict_examination_result'][i][j]['PURCHASE_SECTION_ID'] = list_qual_sectionid[i]
                    qualification_examination_result_in(input_d['dict_examination_result'][i][j])

            for i in range(len(input_d['dic_compliance_review'])):
                for j in range(len(input_d['dic_compliance_review'][i])):
                    input_d['dic_compliance_review'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_compliance_review'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    list_comp = compliance_review_in(input_d['dic_compliance_review'][i][j])
                    list_comp_rev_id.append(list_comp[0])
                    list_comp_sectionid.append(list_comp[1])
            for i in range(len(input_d['dict_compliance_review_team'])):
                for j in range(len(input_d['dict_compliance_review_team'][i])):
                    input_d['dict_compliance_review_team'][i][j]['COMPLIANCE_REVIEW_ID'] = list_comp_rev_id[i]
                    input_d['dict_compliance_review_team'][i][j]['PURCHASE_SECTION_ID'] = list_comp_sectionid[i]
                    compliance_review_team_in(input_d['dict_compliance_review_team'][i][j])
            for i in range(len(input_d['dict_comp_review_detail'])):
                for j in range(len(input_d['dict_comp_review_detail'][i])):
                    input_d['dict_comp_review_detail'][i][j]['COMPLIANCE_REVIEW_ID'] = list_comp_rev_id[i]
                    input_d['dict_comp_review_detail'][i][j]['PURCHASE_SECTION_ID'] = list_comp_sectionid[i]
                    compliance_review_detail_in(input_d['dict_comp_review_detail'][i][j])
            for i in range(len(input_d['dict_comp_review_result'])):
                for j in range(len(input_d['dict_comp_review_result'][i])):
                    input_d['dict_comp_review_result'][i][j]['COMPLIANCE_REVIEW_ID'] = list_comp_rev_id[i]
                    input_d['dict_comp_review_result'][i][j]['PURCHASE_SECTION_ID'] = list_comp_sectionid[i]
                    compliance_review_result_in(input_d['dict_comp_review_result'][i][j])
            list_core_rev_id = []
            list_core_sectionid = []
            for i in range(len(input_d['dic_core_product_review'])):
                for j in range(len(input_d['dic_core_product_review'][i])):
                    input_d['dic_core_product_review'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dic_core_product_review'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    list_core = core_product_review_in(input_d['dic_core_product_review'][i][j])
                    list_core_rev_id.append(list_core[0])
                    list_core_sectionid.append(list_core[1])
            for i in range(len(input_d['dict_core_review_result'])):
                for j in range(len(input_d['dict_core_review_result'][i])):
                    input_d['dict_core_review_result'][i][j]['CORE_PRODUCT_REVIEW_ID'] = list_comp_rev_id[i]
                    input_d['dict_core_review_result'][i][j]['PURCHASE_SECTION_ID'] = list_comp_sectionid[i]
                    core_product_review_result_in(input_d['dict_core_review_result'][i][j])
            for i in range(len(input_d['dict_comp_review_score'])):
                for j in range(len(input_d['dict_comp_review_score'][i])):
                    input_d['dict_comp_review_score'][i][j]['CORE_PRODUCT_REVIEW_ID'] = list_comp_rev_id[i]
                    input_d['dict_comp_review_score'][i][j]['PURCHASE_SECTION_ID'] = list_comp_sectionid[i]
                    core_product_review_score_in(input_d['dict_comp_review_score'][i][j])
            for i in range(len(input_d['dict_offline_expert_roster'])):
                for j in range(len(input_d['dict_offline_expert_roster'][i])):
                    input_d['dict_offline_expert_roster'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    offline_expert_roster_in(input_d['dict_offline_expert_roster'][i][j])
            for i in range(len(input_d['dict_offline_evaluation_score'])):
                for j in range(len(input_d['dict_offline_evaluation_score'][i])):
                    input_d['dict_offline_evaluation_score'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    offline_evaluation_score_in(input_d['dict_offline_evaluation_score'][i][j])
            for i in range(len(input_d['dict_offline_evaluation_result'])):
                for j in range(len(input_d['dict_offline_evaluation_result'][i])):
                    input_d['dict_offline_evaluation_result'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    offline_evaluation_result_in(input_d['dict_offline_evaluation_result'][i][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_qual_after_member'])):
                    input_d['dict_qual_after_member'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_qual_after_member'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    qual_after_member_in(input_d['dict_qual_after_member'][j])
        list_excute_ui.append('评审结果记录')
        list_excute_ui.append('评审委员会组建')
        list_excute_ui.append('评审委员会名单-数仓同步')
        list_excute_ui.append('供应商评审明细汇总数仓同步')
        list_excute_ui.append('专家打分细项数仓同步')
        list_excute_ui.append('预中标供应商数仓同步')
        list_excute_ui.append('供应商评审条款得分')
        list_excute_ui.append('价格谈判轮次记录')
        list_excute_ui.append('后审资格审查小组名单')
        if dic_excute['win_bid'] == 0:
            print(purchaseprojectid, purchaseprojectname)
            return
        else:
            for i in range(len(input_d['dict_performance_evaluation_score'])):
                for j in range(len(input_d['dict_performance_evaluation_score'][i])):
                    input_d['dict_performance_evaluation_score'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_performance_evaluation_score'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    performance_evaluation_score_in(input_d['dict_performance_evaluation_score'][i][j])
            for i in range(len(input_d['dict_perf_eva_score_detail'])):
                for j in range(len(input_d['dict_perf_eva_score_detail'][i])):
                    input_d['dict_perf_eva_score_detail'][i][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    input_d['dict_perf_eva_score_detail'][i][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    performance_evaluation_score_detail_in(input_d['dict_perf_eva_score_detail'][i][j])
            input_d['dict_win_notice']['PURCHASE_PROJECT_ID'] = purchaseprojectid
            winnoticeid = win_notice_in(input_d['dict_win_notice'])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_qual_after_member'])):
                    input_d['dict_win_supplier'][j]['WIN_NOTICE_ID'] = winnoticeid
                    input_d['dict_win_supplier'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    win_supplier_in(input_d['dict_win_supplier'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_qual_after_member'])):
                    input_d['dict_bid_object_detail'][j]['WIN_NOTICE_ID'] = winnoticeid
                    input_d['dict_bid_object_detail'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dict_bid_object_detail'][j]['PURCHASE_SECTION_DETAIL_ID'] = list_purchasesectiondetailid[i]
                    bid_object_detail_in(input_d['dict_bid_object_detail'][j])
                input_d['dict_faliure_bid_notice']['PURCHASE_PROJECT_ID'] = purchaseprojectid
                input_d['dict_faliure_bid_notice']['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
            faliure_bid_notice_in(input_d['dict_faliure_bid_notice'])
            input_d['dict_rebid_project']['PURCHASE_PROJECT_ID'] = purchaseprojectid
            input_d['dict_rebid_project']['PURCHASE_PROJECT_CODE'] = purchaseprojectcode
            purchaserebid = rebid_project_in(input_d['dict_rebid_project'])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_rebid_section'])):
                    input_d['dict_rebid_section'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dict_rebid_section'][j]['PURCHASE_SECTION_CODE'] = list_purchasesectioncode[i]
                    input_d['dict_rebid_section'][j]['PURCHASE_REBID_ID'] = purchaserebid
                    rebid_section_in(input_d['dict_rebid_section'][j])
            for i in range(len(input_d['dic_purchase_section'])):
                for j in range(len(input_d['dict_win_note'])):
                    input_d['dict_win_note'][j]['PURCHASE_SECTION_ID'] = list_purchasesectionid[i]
                    input_d['dict_win_note'][j]['PURCHASE_PROJECT_ID'] = purchaseprojectid
                    win_note_in(input_d['dict_win_note'][j])

        list_excute_ui.append('中标（成交）结果公告信息数仓同步')
        list_excute_ui.append('中标（成交）结果公告中标人信息数仓同步')
        list_excute_ui.append('中标（成交）标的明细信息数仓同步')
        list_excute_ui.append('流废标（终止）公示')
        list_excute_ui.append('流标处理_项目表数仓同步')
        list_excute_ui.append('流标处理_包表数仓同步')
        list_excute_ui.append('（未）中标（成交）结果通知书')
        # act_universal_list_row0(list_excute_ui)
        print(purchaseprojectid, purchaseprojectname, list_excute_ui)
