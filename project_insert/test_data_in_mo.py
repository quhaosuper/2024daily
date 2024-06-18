from project_in_mo import *
import pytest
import yaml
import copy


class Test_insert:
    @pytest.mark.parametrize("input_d",
                             yaml.safe_load(open("all_in_public.yml", encoding='utf-8')))
    def test_gongkai(self, input_d):
        list_excute_ui = []
        dic_excute = input_d['dic_excute']
        base_project_id = ce_base_project_in(input_d['dic_base_project'])
        list_tender_doc_id = []
        list_tender_doc = ce_tender_doc_in(input_d['dic_tender_doc'][0])
        list_tender_doc_id.append(list_tender_doc[0])
        tender_project_id = list_tender_doc[1]
        section_ids = list_tender_doc[2]
        list_section_id = section_ids.split(';')
        if len(input_d['dic_tender_doc']) > 0:
            for i in range(len(input_d['dic_tender_doc'])):
                if i > 0:
                    input_d['dic_tender_doc'][i]['tender_project_id'] = tender_project_id
                    input_d['dic_tender_doc'][i]['section_ids'] = section_ids
                    list_tender_doc_id.append(ce_tender_doc_in(input_d['dic_tender_doc'][i])[0])
        # print(list_section_id)
        input_d['dic_tender_project']['tender_project_id'] = tender_project_id
        input_d['dic_tender_project']['base_project_id'] = base_project_id
        tender_project_code = ce_tender_project_in(input_d['dic_tender_project'])[0]
        list_item_id = []
        for i in range(len(input_d['dic_tender_doc_item'])):
            for j in range(len(input_d['dic_ce_section'])):
                input_d['dic_tender_doc_item'][i]['tender_doc_id'] = list_tender_doc_id[i]
                input_d['dic_tender_doc_item'][i]['section_id'] = list_section_id[j]
                ele1 = ce_tender_doc_item_in(input_d['dic_tender_doc_item'][i])
                list_item_id.append(ele1)
        list_step_id = []
        list_step_name = []
        for i in range(len(input_d['dic_tender_doc_step'])):
            for j in range(len(input_d['dic_tender_doc_step'][i])):
                input_d['dic_tender_doc_step'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                input_d['dic_tender_doc_step'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_tender_doc_step_in(input_d['dic_tender_doc_step'][i][j])
                list_step_id.append(ele1[0])
                list_step_name.append(ele1[1])

        list_clause_id = []
        for i in range(len(input_d['dic_tender_doc_clause'])):
            for j in range(len(input_d['dic_tender_doc_clause'][i])):
                step_id = list_step_id.pop(0)
                for h in range(len(input_d['dic_tender_doc_clause'][i][j])):
                    input_d['dic_tender_doc_clause'][i][j][h]['tender_doc_id'] = list_tender_doc_id[0]
                    input_d['dic_tender_doc_clause'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_tender_doc_clause'][i][j][h]['step_id'] = step_id
                    ele1 = ce_tender_doc_clause_in(input_d['dic_tender_doc_clause'][i][j][h])
                    list_clause_id.append(ele1)

        list_qual_doc_id = []
        for i in range(len(input_d['dic_qual_doc'])):
            input_d['dic_qual_doc'][i]['tender_project_id'] = tender_project_id
            input_d['dic_qual_doc'][i]['section_ids'] = section_ids
            ele1 = ce_qual_doc_in(input_d['dic_qual_doc'][i])
            list_qual_doc_id.append(ele1)

        list_item_id2 = []
        for i in range(len(input_d['dic_qual_doc_item'])):
            input_d['dic_qual_doc_item'][i]['qual_doc_id'] = list_qual_doc_id[i]
            input_d['dic_qual_doc_item'][i]['section_id'] = list_section_id[i]
            ele1 = ce_qual_doc_item_in(input_d['dic_qual_doc_item'][i])
            list_item_id2.append(ele1)

        for i in range(len(input_d['dic_doc_exec'])):
            for j in range(len(input_d['dic_doc_exec'][i])):
                input_d['dic_doc_exec'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_doc_exec'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                input_d['dic_doc_exec'][i][j]['section_id'] = list_section_id[i]
                ce_doc_exec_in(input_d['dic_doc_exec'][i][j])

        for i in range(len(input_d['dic_ce_section'])):
            input_d['dic_ce_section'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_section'][i]['section_id'] = list_section_id[i]
            input_d['dic_ce_section'][i]['tender_doc_id'] = list_tender_doc_id[0]
            input_d['dic_ce_section'][i]['qual_doc_id'] = list_qual_doc_id[0]
            ce_section_in(input_d['dic_ce_section'][i])

        for i in range(len(input_d['dic_venue_info'])):
            for j in range(len(input_d['dic_venue_info'][i])):
                input_d['dic_venue_info'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_venue_info'][i][j]['section_id'] = list_section_id[i]
                ce_venue_info_in(input_d['dic_venue_info'][i][j])
        list_notice_id = []
        for i in range(len(input_d['dic_ce_notice'])):
            input_d['dic_ce_notice'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_notice'][i]['tender_doc_id'] = list_tender_doc_id[0]
            input_d['dic_ce_notice'][i]['qual_doc_id'] = list_qual_doc_id[0]
            ele1 = ce_notice_in(input_d['dic_ce_notice'][i])
            list_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_notice_item'])):
            for j in range(len(input_d['dic_ce_notice_item'][i])):
                input_d['dic_ce_notice_item'][i][j]['notice_id'] = list_notice_id[j]
                input_d['dic_ce_notice_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_notice_item'][i][j]['section_id'] = list_section_id[i]
                input_d['dic_ce_notice_item'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                input_d['dic_ce_notice_item'][i][j]['qual_doc_id'] = list_qual_doc_id[0]
                ce_notice_item_in(input_d['dic_ce_notice_item'][i][j])

        list_survey_id = []
        for i in range(len(input_d['dic_ce_survey'])):
            input_d['dic_ce_survey'][i]['section_ids'] = section_ids
            input_d['dic_ce_survey'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_survey_in(input_d['dic_ce_survey'][i])
            list_survey_id.append(ele1)

        for i in range(len(input_d['dic_ce_survey_item'])):
            input_d['dic_ce_survey_item'][i]['survey_id'] = list_survey_id[i]
            ce_survey_item_in(input_d['dic_ce_survey_item'][i])

        list_bidder_enroll_id = []
        for i in range(len(input_d['dic_ce_bidder_enroll'])):
            for j in range(len(input_d['dic_ce_bidder_enroll'][i])):
                input_d['dic_ce_bidder_enroll'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bidder_enroll'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_bidder_enroll_in(input_d['dic_ce_bidder_enroll'][i][j])
                list_bidder_enroll_id.append(ele1)

        list_doc_download_id = []
        for i in range(len(input_d['dic_ce_doc_download'])):
            for j in range(len(input_d['dic_ce_doc_download'][i])):
                input_d['dic_ce_doc_download'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_doc_download'][i][j]['section_id'] = list_section_id[i]
                input_d['dic_ce_doc_download'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                ele1 = ce_doc_download_in(input_d['dic_ce_doc_download'][i][j])
                list_doc_download_id.append(ele1)

        list_doc_refer_id = []
        for i in range(len(input_d['dic_ce_bid_doc_refer'])):
            for j in range(len(input_d['dic_ce_bid_doc_refer'][i])):
                input_d['dic_ce_bid_doc_refer'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bid_doc_refer'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_bid_doc_refer_in(input_d['dic_ce_bid_doc_refer'][i][j])
                list_doc_refer_id.append(ele1)

        for i in range(len(input_d['dic_ce_union_member'])):
            for j in range(len(input_d['dic_ce_union_member'][i])):
                input_d['dic_ce_union_member'][i][j]['section_id'] = list_section_id[i]
                ce_union_member_in(input_d['dic_ce_union_member'][i][j])

        list_record_id = []
        for i in range(len(input_d['dic_ce_bid_open_record'])):
            input_d['dic_ce_bid_open_record'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_bid_open_record'][i]['section_id'] = list_section_id[i]
            ele1 = ce_bid_open_record_in(input_d['dic_ce_bid_open_record'][i])
            list_record_id.append(ele1)

        for i in range(len(input_d['dic_ce_bid_open_item'])):
            for j in range(len(input_d['dic_ce_bid_open_item'][i])):
                input_d['dic_ce_bid_open_item'][i][j]['record_id'] = list_record_id[i]
                input_d['dic_ce_bid_open_item'][i][j]['section_id'] = list_section_id[i]
                ce_bid_open_item_in(input_d['dic_ce_bid_open_item'][i][j])

        for i in range(len(input_d['dic_ce_doc_char'])):
            for j in range(len(input_d['dic_ce_doc_char'][i])):
                input_d['dic_ce_doc_char'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_doc_char'][i][j]['section_id'] = list_section_id[i]
                ce_doc_char_in(input_d['dic_ce_doc_char'][i][j])

        for i in range(len(input_d['dic_eval_report'])):
            for j in range(len(input_d['dic_eval_report'][i])):
                input_d['dic_eval_report'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_eval_report'][i][j]['section_id'] = list_section_id[i]
                ce_eval_report_in(input_d['dic_eval_report'][i][j])

        for i in range(len(input_d['dic_ce_judge_group'])):
            for j in range(len(input_d['dic_ce_judge_group'][i])):
                input_d['dic_ce_judge_group'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_judge_group'][i][j]['section_id'] = list_section_id[i]
                ce_judge_group_in(input_d['dic_ce_judge_group'][i][j])

        list_step_name1 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_clause_score'])):
            for j in range(len(input_d['dic_ce_clause_score'][i])):
                step_name = list_step_name1.pop(0)
                for h in range(len(input_d['dic_ce_clause_score'][i][j])):
                    input_d['dic_ce_clause_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_clause_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_clause_score'][i][j][h]['step_name'] = step_name
                    ce_clause_score_in(input_d['dic_ce_clause_score'][i][j][h])

        list_step_name2 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_step_score'])):
            for j in range(len(input_d['dic_ce_step_score'][i])):
                step_name = list_step_name2.pop(0)
                for h in range(len(input_d['dic_ce_step_score'][i][j])):
                    input_d['dic_ce_step_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_step_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_step_score'][i][j][h]['step_name'] = step_name
                    ce_step_score_in(input_d['dic_ce_step_score'][i][j][h])
                    time.sleep(1)

        list_step_name3 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_step_total_score'])):
            for j in range(len(input_d['dic_ce_step_total_score'][i])):
                step_name = list_step_name3.pop(0)
                for h in range(len(input_d['dic_ce_step_total_score'][i][j])):
                    input_d['dic_ce_step_total_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_step_total_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_step_total_score'][i][j][h]['step_name'] = step_name
                    ce_step_total_score_in(input_d['dic_ce_step_total_score'][i][j][h])

        for i in range(len(input_d['dic_ce_bidder_score'])):
            for j in range(len(input_d['dic_ce_bidder_score'][i])):
                input_d['dic_ce_bidder_score'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bidder_score'][i][j]['section_id'] = list_section_id[i]
                ce_bidder_score_in(input_d['dic_ce_bidder_score'][i][j])

        for i in range(len(input_d['dic_ce_candidate'])):
            for j in range(len(input_d['dic_ce_candidate'][i])):
                input_d['dic_ce_candidate'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_candidate'][i][j]['section_id'] = list_section_id[i]
                ce_candidate_in(input_d['dic_ce_candidate'][i][j])
        list_candidate_notice_id = []
        for i in range(len(input_d['dic_ce_candidate_notice'])):
            input_d['dic_ce_candidate_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_candidate_notice_in(input_d['dic_ce_candidate_notice'][i])
            list_candidate_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_candidate_notice_item'])):
            for j in range(len(input_d['dic_ce_candidate_notice_item'][i])):
                input_d['dic_ce_candidate_notice_item'][i][j]['candidate_notice_id'] = list_candidate_notice_id[0]
                input_d['dic_ce_candidate_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_candidate_notice_item_in(input_d['dic_ce_candidate_notice_item'][i][j])

        list_win_notice_id = []
        for i in range(len(input_d['dic_ce_win_notice'])):
            input_d['dic_ce_win_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_win_notice_in(input_d['dic_ce_win_notice'][i])
            list_win_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_win_notice_item'])):
            for j in range(len(input_d['dic_ce_win_notice_item'][i])):
                input_d['dic_ce_win_notice_item'][i][j]['win_notice_id'] = list_win_notice_id[0]
                input_d['dic_ce_win_notice_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_win_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_win_notice_item_in(input_d['dic_ce_win_notice_item'][i][j])

        list_failure_notice_id = []
        for i in range(len(input_d['dic_ce_failure_notice'])):
            input_d['dic_ce_failure_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_failure_notice_in(input_d['dic_ce_failure_notice'][i])
            list_failure_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_failure_notice_item'])):
            for j in range(len(input_d['dic_ce_failure_notice_item'][i])):
                input_d['dic_ce_failure_notice_item'][i][j]['failure_notice_id'] = list_failure_notice_id[0]
                input_d['dic_ce_failure_notice_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_failure_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_failure_notice_item_in(input_d['dic_ce_failure_notice_item'][i][j])

        for i in range(len(input_d['dic_ce_win_note'])):
            for j in range(len(input_d['dic_ce_win_note'][i])):
                input_d['dic_ce_win_note'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_win_note'][i][j]['section_id'] = list_section_id[i]
                ce_win_note_in(input_d['dic_ce_win_note'][i][j])

    @pytest.mark.parametrize("input_d",
                             yaml.safe_load(open("all_in_invite.yml", encoding='utf-8')))
    def test_yaoqing(self, input_d):
        list_excute_ui = []
        dic_excute = input_d['dic_excute']
        base_project_id = ce_base_project_in(input_d['dic_base_project'])
        list_tender_doc_id = []
        list_tender_doc = ce_tender_doc_in(input_d['dic_tender_doc'][0])
        list_tender_doc_id.append(list_tender_doc[0])
        tender_project_id = list_tender_doc[1]
        section_ids = list_tender_doc[2]
        list_section_id = section_ids.split(';')
        if len(input_d['dic_tender_doc']) > 0:
            for i in range(len(input_d['dic_tender_doc'])):
                if i > 0:
                    input_d['dic_tender_doc'][i]['tender_project_id'] = tender_project_id
                    input_d['dic_tender_doc'][i]['section_ids'] = section_ids
                    list_tender_doc_id.append(ce_tender_doc_in(input_d['dic_tender_doc'][i])[0])
        # print(list_section_id)
        input_d['dic_tender_project']['tender_project_id'] = tender_project_id
        input_d['dic_tender_project']['base_project_id'] = base_project_id
        tender_project_code = ce_tender_project_in(input_d['dic_tender_project'])[0]
        list_item_id = []
        for i in range(len(input_d['dic_tender_doc_item'])):
            for j in range(len(input_d['dic_ce_section'])):
                input_d['dic_tender_doc_item'][i]['tender_doc_id'] = list_tender_doc_id[i]
                input_d['dic_tender_doc_item'][i]['section_id'] = list_section_id[j]
                ele1 = ce_tender_doc_item_in(input_d['dic_tender_doc_item'][i])
                list_item_id.append(ele1)
        list_step_id = []
        list_step_name = []
        for i in range(len(input_d['dic_tender_doc_step'])):
            for j in range(len(input_d['dic_tender_doc_step'][i])):
                input_d['dic_tender_doc_step'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                input_d['dic_tender_doc_step'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_tender_doc_step_in(input_d['dic_tender_doc_step'][i][j])
                list_step_id.append(ele1[0])
                list_step_name.append(ele1[1])

        list_clause_id = []
        for i in range(len(input_d['dic_tender_doc_clause'])):
            for j in range(len(input_d['dic_tender_doc_clause'][i])):
                step_id = list_step_id.pop(0)
                for h in range(len(input_d['dic_tender_doc_clause'][i][j])):
                    input_d['dic_tender_doc_clause'][i][j][h]['tender_doc_id'] = list_tender_doc_id[0]
                    input_d['dic_tender_doc_clause'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_tender_doc_clause'][i][j][h]['step_id'] = step_id
                    ele1 = ce_tender_doc_clause_in(input_d['dic_tender_doc_clause'][i][j][h])
                    list_clause_id.append(ele1)

        list_qual_doc_id = []
        for i in range(len(input_d['dic_qual_doc'])):
            input_d['dic_qual_doc'][i]['tender_project_id'] = tender_project_id
            input_d['dic_qual_doc'][i]['section_ids'] = section_ids
            ele1 = ce_qual_doc_in(input_d['dic_qual_doc'][i])
            list_qual_doc_id.append(ele1)

        list_item_id2 = []
        for i in range(len(input_d['dic_qual_doc_item'])):
            input_d['dic_qual_doc_item'][i]['qual_doc_id'] = list_qual_doc_id[i]
            input_d['dic_qual_doc_item'][i]['section_id'] = list_section_id[i]
            ele1 = ce_qual_doc_item_in(input_d['dic_qual_doc_item'][i])
            list_item_id2.append(ele1)

        for i in range(len(input_d['dic_doc_exec'])):
            for j in range(len(input_d['dic_doc_exec'][i])):
                input_d['dic_doc_exec'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_doc_exec'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                input_d['dic_doc_exec'][i][j]['section_id'] = list_section_id[i]
                ce_doc_exec_in(input_d['dic_doc_exec'][i][j])

        for i in range(len(input_d['dic_ce_section'])):
            input_d['dic_ce_section'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_section'][i]['section_id'] = list_section_id[i]
            input_d['dic_ce_section'][i]['tender_doc_id'] = list_tender_doc_id[0]
            input_d['dic_ce_section'][i]['qual_doc_id'] = list_qual_doc_id[0]
            ce_section_in(input_d['dic_ce_section'][i])

        for i in range(len(input_d['dic_venue_info'])):
            for j in range(len(input_d['dic_venue_info'][i])):
                input_d['dic_venue_info'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_venue_info'][i][j]['section_id'] = list_section_id[i]
                ce_venue_info_in(input_d['dic_venue_info'][i][j])

        list_invitation_id = []
        for i in range(len(input_d['dic_ce_invitation'])):
            input_d['dic_ce_invitation'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_invitation'][i]['tender_doc_id'] = list_tender_doc_id[0]
            ele1 = ce_invitation_in(input_d['dic_ce_invitation'][i])
            list_invitation_id.append(ele1)

        for i in range(len(input_d['dic_ce_invitation_item'])):
            for j in range(len(input_d['dic_ce_invitation_item'][i])):
                input_d['dic_ce_invitation_item'][i][j]['invitation_id'] = list_invitation_id[j]
                input_d['dic_ce_invitation_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_invitation_item'][i][j]['section_id'] = list_section_id[i]
                ce_invitation_item_in(input_d['dic_ce_invitation_item'][i][j])

        for i in range(len(input_d['dic_ce_invitation_result'])):
            for j in range(len(input_d['dic_ce_invitation_result'][i])):
                for h in range(len(input_d['dic_ce_invitation_result'][i][j])):
                    input_d['dic_ce_invitation_result'][i][j][h]['invitation_id'] = list_invitation_id[j]
                    input_d['dic_ce_invitation_result'][i][j][h]['section_id'] = list_section_id[i]
                    ce_invitation_result_in(input_d['dic_ce_invitation_result'][i][j][h])

        for i in range(len(input_d['dic_venue_info'])):
            for j in range(len(input_d['dic_venue_info'][i])):
                input_d['dic_venue_info'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_venue_info'][i][j]['section_id'] = list_section_id[i]
                ce_venue_info_in(input_d['dic_venue_info'][i][j])

        list_bidder_enroll_id = []
        for i in range(len(input_d['dic_ce_bidder_enroll'])):
            for j in range(len(input_d['dic_ce_bidder_enroll'][i])):
                input_d['dic_ce_bidder_enroll'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bidder_enroll'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_bidder_enroll_in(input_d['dic_ce_bidder_enroll'][i][j])
                list_bidder_enroll_id.append(ele1)

        list_doc_download_id = []
        for i in range(len(input_d['dic_ce_doc_download'])):
            for j in range(len(input_d['dic_ce_doc_download'][i])):
                input_d['dic_ce_doc_download'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_doc_download'][i][j]['section_id'] = list_section_id[i]
                input_d['dic_ce_doc_download'][i][j]['tender_doc_id'] = list_tender_doc_id[0]
                ele1 = ce_doc_download_in(input_d['dic_ce_doc_download'][i][j])
                list_doc_download_id.append(ele1)

        list_doc_refer_id = []
        for i in range(len(input_d['dic_ce_bid_doc_refer'])):
            for j in range(len(input_d['dic_ce_bid_doc_refer'][i])):
                input_d['dic_ce_bid_doc_refer'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bid_doc_refer'][i][j]['section_id'] = list_section_id[i]
                ele1 = ce_bid_doc_refer_in(input_d['dic_ce_bid_doc_refer'][i][j])
                list_doc_refer_id.append(ele1)

        for i in range(len(input_d['dic_ce_union_member'])):
            for j in range(len(input_d['dic_ce_union_member'][i])):
                input_d['dic_ce_union_member'][i][j]['section_id'] = list_section_id[i]
                ce_union_member_in(input_d['dic_ce_union_member'][i][j])

        list_record_id = []
        for i in range(len(input_d['dic_ce_bid_open_record'])):
            input_d['dic_ce_bid_open_record'][i]['tender_project_id'] = tender_project_id
            input_d['dic_ce_bid_open_record'][i]['section_id'] = list_section_id[i]
            ele1 = ce_bid_open_record_in(input_d['dic_ce_bid_open_record'][i])
            list_record_id.append(ele1)

        for i in range(len(input_d['dic_ce_bid_open_item'])):
            for j in range(len(input_d['dic_ce_bid_open_item'][i])):
                input_d['dic_ce_bid_open_item'][i][j]['record_id'] = list_record_id[i]
                input_d['dic_ce_bid_open_item'][i][j]['section_id'] = list_section_id[i]
                ce_bid_open_item_in(input_d['dic_ce_bid_open_item'][i][j])

        for i in range(len(input_d['dic_ce_doc_char'])):
            for j in range(len(input_d['dic_ce_doc_char'][i])):
                input_d['dic_ce_doc_char'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_doc_char'][i][j]['section_id'] = list_section_id[i]
                ce_doc_char_in(input_d['dic_ce_doc_char'][i][j])

        for i in range(len(input_d['dic_eval_report'])):
            for j in range(len(input_d['dic_eval_report'][i])):
                input_d['dic_eval_report'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_eval_report'][i][j]['section_id'] = list_section_id[i]
                ce_eval_report_in(input_d['dic_eval_report'][i][j])

        for i in range(len(input_d['dic_ce_judge_group'])):
            for j in range(len(input_d['dic_ce_judge_group'][i])):
                input_d['dic_ce_judge_group'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_judge_group'][i][j]['section_id'] = list_section_id[i]
                ce_judge_group_in(input_d['dic_ce_judge_group'][i][j])

        list_step_name1 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_clause_score'])):
            for j in range(len(input_d['dic_ce_clause_score'][i])):
                step_name = list_step_name1.pop(0)
                for h in range(len(input_d['dic_ce_clause_score'][i][j])):
                    input_d['dic_ce_clause_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_clause_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_clause_score'][i][j][h]['step_name'] = step_name
                    ce_clause_score_in(input_d['dic_ce_clause_score'][i][j][h])

        list_step_name2 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_step_score'])):
            for j in range(len(input_d['dic_ce_step_score'][i])):
                step_name = list_step_name2.pop(0)
                for h in range(len(input_d['dic_ce_step_score'][i][j])):
                    input_d['dic_ce_step_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_step_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_step_score'][i][j][h]['step_name'] = step_name
                    ce_step_score_in(input_d['dic_ce_step_score'][i][j][h])
                    time.sleep(1)

        list_step_name3 = copy.deepcopy(list_step_name)
        for i in range(len(input_d['dic_ce_step_total_score'])):
            for j in range(len(input_d['dic_ce_step_total_score'][i])):
                step_name = list_step_name3.pop(0)
                for h in range(len(input_d['dic_ce_step_total_score'][i][j])):
                    input_d['dic_ce_step_total_score'][i][j][h]['tender_project_id'] = tender_project_id
                    input_d['dic_ce_step_total_score'][i][j][h]['section_id'] = list_section_id[i]
                    input_d['dic_ce_step_total_score'][i][j][h]['step_name'] = step_name
                    ce_step_total_score_in(input_d['dic_ce_step_total_score'][i][j][h])
                    time.sleep(1)

        for i in range(len(input_d['dic_ce_bidder_score'])):
            for j in range(len(input_d['dic_ce_bidder_score'][i])):
                input_d['dic_ce_bidder_score'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_bidder_score'][i][j]['section_id'] = list_section_id[i]
                ce_bidder_score_in(input_d['dic_ce_bidder_score'][i][j])

        for i in range(len(input_d['dic_ce_candidate'])):
            for j in range(len(input_d['dic_ce_candidate'][i])):
                input_d['dic_ce_candidate'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_candidate'][i][j]['section_id'] = list_section_id[i]
                ce_candidate_in(input_d['dic_ce_candidate'][i][j])
        list_candidate_notice_id = []
        for i in range(len(input_d['dic_ce_candidate_notice'])):
            input_d['dic_ce_candidate_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_candidate_notice_in(input_d['dic_ce_candidate_notice'][i])
            list_candidate_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_candidate_notice_item'])):
            for j in range(len(input_d['dic_ce_candidate_notice_item'][i])):
                input_d['dic_ce_candidate_notice_item'][i][j]['candidate_notice_id'] = list_candidate_notice_id[0]
                input_d['dic_ce_candidate_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_candidate_notice_item_in(input_d['dic_ce_candidate_notice_item'][i][j])

        list_win_notice_id = []
        for i in range(len(input_d['dic_ce_win_notice'])):
            input_d['dic_ce_win_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_win_notice_in(input_d['dic_ce_win_notice'][i])
            list_win_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_win_notice_item'])):
            for j in range(len(input_d['dic_ce_win_notice_item'][i])):
                input_d['dic_ce_win_notice_item'][i][j]['win_notice_id'] = list_win_notice_id[0]
                input_d['dic_ce_win_notice_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_win_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_win_notice_item_in(input_d['dic_ce_win_notice_item'][i][j])

        list_failure_notice_id = []
        for i in range(len(input_d['dic_ce_failure_notice'])):
            input_d['dic_ce_failure_notice'][i]['tender_project_id'] = tender_project_id
            ele1 = ce_failure_notice_in(input_d['dic_ce_failure_notice'][i])
            list_failure_notice_id.append(ele1)

        for i in range(len(input_d['dic_ce_failure_notice_item'])):
            for j in range(len(input_d['dic_ce_failure_notice_item'][i])):
                input_d['dic_ce_failure_notice_item'][i][j]['failure_notice_id'] = list_failure_notice_id[0]
                input_d['dic_ce_failure_notice_item'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_failure_notice_item'][i][j]['section_id'] = list_section_id[i]
                ce_failure_notice_item_in(input_d['dic_ce_failure_notice_item'][i][j])

        for i in range(len(input_d['dic_ce_win_note'])):
            for j in range(len(input_d['dic_ce_win_note'][i])):
                input_d['dic_ce_win_note'][i][j]['tender_project_id'] = tender_project_id
                input_d['dic_ce_win_note'][i][j]['section_id'] = list_section_id[i]
                ce_win_note_in(input_d['dic_ce_win_note'][i][j])