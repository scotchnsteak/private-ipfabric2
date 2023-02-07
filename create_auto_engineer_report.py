

class AutomaticCheckReport():

    def create_engineer_report(self):

        import pandas as pd
        from pathlib import Path
        from auto_summary_dict import automatic_checks_dict


        Path("DOWNLOADS").mkdir(parents=True, exist_ok=True)

        # Instantiate the writer and the workbook:
        writer = pd.ExcelWriter('DOWNLOADS/AUTOMATIC_CHECKS.xlsx', engine='xlsxwriter')
        workbook = writer.book

        # Instantiating DataFrame and worksheet for main Summary Table:
        df = pd.DataFrame(automatic_checks_dict)
        df = df.T
        df.to_excel(writer, index=False, header=True, sheet_name='SUMMARY')
        worksheet = writer.sheets['SUMMARY']

        # Creating all of the formatting Profiles:
        category_column = workbook.add_format({'bold': True, 'text_wrap': True, 'font_size': 14, 'align': 'left', 'border': 1})
        check_column = workbook.add_format({'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True})
        green_column = workbook.add_format({'bg_color': '#9bbb59', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        green_color = workbook.add_format({'bg_color': '#9bbb59'})
        blue_column = workbook.add_format({'bg_color': '#4f81bd', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        blue_color = workbook.add_format({'bg_color': '#4f81bd'})
        amber_column = workbook.add_format({'bg_color': '#ffc000', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        amber_color = workbook.add_format({'bg_color': '#ffc000'})
        red_column = workbook.add_format({'bg_color': '#ff3232', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        red_color = workbook.add_format({'bg_color': '#ff3232'})
        header_row = workbook.add_format(
            {'bold': True, 'underline': True, 'font_size': 14, 'align': 'center'})
        black_cell = workbook.add_format({'bg_color': 'black'})
        white_cell = workbook.add_format({'bg_color': 'white'})
        tab_column = workbook.add_format({'align': 'left', 'text_wrap': True, 'border': 1, 'valign': 'vcenter', 'text_wrap': True})
        green_column_threshold = workbook.add_format({'bg_color': '#9bbb59', 'align': 'center', 'valign': 'vcenter',
                                                      'border': 1, 'text_wrap': True})
        blue_column_threshold = workbook.add_format({'bg_color': '#4f81bd', 'align': 'center', 'valign': 'vcenter',
                                                      'border': 1, 'text_wrap': True})
        amber_column_threshold = workbook.add_format({'bg_color': '#ffc000', 'align': 'center', 'valign': 'vcenter',
                                                      'border': 1, 'text_wrap': True})
        red_column_threshold = workbook.add_format({'bg_color': '#ff3232', 'align': 'center', 'valign': 'vcenter',
                                                      'border': 1, 'text_wrap': True})


        worksheet.set_row(0, 15, header_row)
        worksheet.set_column(0, 0, 28, category_column)
        worksheet.set_column(1, 1, 25, check_column)
        worksheet.set_column(2, 2, 7, green_column)
        worksheet.set_column(3, 3, 7, blue_column)
        worksheet.set_column(4, 4, 7, amber_column)
        worksheet.set_column(5, 5, 7, red_column)
        worksheet.set_column(6, 6, 25, tab_column)
        worksheet.set_column(7, 7, 25, green_column_threshold)
        worksheet.set_column(8, 8, 25, blue_column_threshold)
        worksheet.set_column(9, 9, 25, amber_column_threshold)
        worksheet.set_column(10, 10, 25, red_column_threshold)

        all_cells = 'C2:K250'
        worksheet.conditional_format(all_cells, {'type': 'text',
                                                 'criteria': 'containing',
                                                 'value': 'black',
                                                 'format': black_cell})

        # Conditional Formatting for all the white cells:
        worksheet.conditional_format(all_cells, {'type': 'text',
                                                 'criteria': 'containing',
                                                 'value': '   ',
                                                 'format': white_cell})

        # Conditional Formatting for Header Cells:
        worksheet.conditional_format('C1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': green_color})

        worksheet.conditional_format('D1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': blue_color})

        worksheet.conditional_format('E1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': amber_color})

        worksheet.conditional_format('F1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': red_color})

        worksheet.conditional_format('H1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': green_color})

        worksheet.conditional_format('I1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': blue_color})

        worksheet.conditional_format('J1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': amber_color})

        worksheet.conditional_format('K1', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': '',
                                            'format': red_color})

        # Fixing Trailing Formatting:
        worksheet.conditional_format('C167:K1000', {
            'type': 'text',
            'criteria': 'not containing',
            'value': 'strings',
            'format': white_cell
        })

        print("The Engineer Report Summary has completed successfully.")

        """
        This is the beginning of the individual tab creation###############################################
        ###################################################################################################
        """

        from ipfabric import IPFClient
        import pandas as pd
        import os

        BASE_URL = os.getenv("BASE_URL")
        TOKEN = os.getenv("TOKEN")

        COLORS = {-1: None, 0: 'green', 10: 'blue', 20: 'amber', 30: 'red'}

        IGNORE_COLUMNS = ['id', 'siteKey', 'neiSiteKey', 'memoryTotalBytes'
                                  'memoryUsedBytes', 'snHw', 'siteKey', 'siteName',
                                  'objectId', 'deviceId', 'neiSiteName', 'neiSiteKey',
                                  'blobKey', 'params']

        def intent_to_df(intent):
            data = ipf.fetch_all(intent["intent"].api_endpoint, filters=create_filter(intent["columns"]),
                                 reports=intent["intent"].web_endpoint)
            [r.pop(c, None) for r in data for c in IGNORE_COLUMNS]

            for row in data:
                for col in intent["columns"]:
                    row[f"{col}-status"] = COLORS[row[col]['severity']]
                    row[col] = row[col]['data']

            return pd.DataFrame(data=data)

        def create_filter(columns):
            filters = list()
            for c in columns:
                tmp = list()
                for s in ['10', '20', '20']:
                    tmp.append({c: ["color", "eq", s]})
                filters.append({'or': tmp})
            return {'or': filters}



        ipf = IPFClient(BASE_URL, token=TOKEN, verify=False, timeout=30)
        ipf.intent.load_intent()

        intents = dict()
        for i in ipf.intent.intent_checks:
            if i.api_endpoint not in intents:
                intents[i.api_endpoint] = {"intent": i, "columns": [i.column]}
            else:
                intents[i.api_endpoint]["columns"].append(i.column)

        def get_col_widths(dataframe):
            return [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) + 1 for col in
                                dataframe.columns]

        # Creating the aaa-accounting tab:
        from get_intent_checks_data import aaa_acc_amber
        df = intent_to_df(intents['/tables/security/aaa/accounting'])
        if len(df.columns) > 1 and aaa_acc_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='aaa-accounting')
            aaa_accounting_sheet = writer.sheets['aaa-accounting']
            for i, width in enumerate(get_col_widths(df)):
                aaa_accounting_sheet.set_column(i, i, width)
            aaa_accounting_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            aaa_accounting_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            aaa_accounting_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The aaa-accounting tab has completed successfully.')
        #

        # Creating the aaa-authentication tab:
        from get_intent_checks_data import aaa_authe_amber
        df = intent_to_df(intents['/tables/security/aaa/authentication'])
        if len(df.columns) > 1 and aaa_authe_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='aaa-authentication')
            aaa_authe_sheet = writer.sheets['aaa-authentication']
            for i, width in enumerate(get_col_widths(df)):
                aaa_authe_sheet.set_column(i, i, width)
            aaa_authe_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            aaa_authe_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            aaa_authe_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The aaa-authentication tab has completed successfully.')

        # Creating the aaa-authorization tab:
        from get_intent_checks_data import aaa_author_amber
        df = intent_to_df(intents['/tables/security/aaa/authorization'])
        if len(df.columns) > 1 and aaa_author_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='aaa-authorization')
            aaa_auth_sheet = writer.sheets['aaa-authorization']
            for i, width in enumerate(get_col_widths(df)):
                aaa_auth_sheet.set_column(i, i, width)
            aaa_auth_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            aaa_auth_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            aaa_auth_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The aaa-authorization tab has completed successfully.')

        # Creating the aaa-lines tab:
        from get_intent_checks_data import (aaa_authe_type_blue, aaa_authe_type_amber, aaa_authe_type_red)
        df = intent_to_df(intents['/tables/security/aaa/lines'])
        if len(df.columns) > 1 and (aaa_authe_type_blue > 0 or aaa_authe_type_amber > 0 or
                aaa_authe_type_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='aaa-lines')
            aaa_lines_sheet = writer.sheets['aaa-lines']
            for i, width in enumerate(get_col_widths(df)):
                aaa_lines_sheet.set_column(i, i, width)
            aaa_lines_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            aaa_lines_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            aaa_lines_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The aaa-lines tab has completed successfully.')

        # Creating the access-points tab:
        from get_intent_checks_data import (acc_pt_con_blue,acc_pt_con_amber,acc_pt_con_red,snr_blue,snr_amber,
        snr_red,acc_pt_radio_signal_blue,acc_pt_radio_signal_amber,acc_pt_radio_signal_red)
        df = intent_to_df(intents['/tables/wireless/access-points'])
        if len(df.columns) > 1 and (acc_pt_con_blue > 0 or acc_pt_con_amber > 0 or
            acc_pt_con_red > 0 or snr_blue > 0 or snr_amber > 0 or snr_red > 0 or acc_pt_radio_signal_blue > 0
            or acc_pt_radio_signal_amber > 0 or acc_pt_radio_signal_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='access-points')
            access_points_sheet = writer.sheets['access-points']
            for i, width in enumerate(get_col_widths(df)):
                access_points_sheet.set_column(i, i, width)
            access_points_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            access_points_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            access_points_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The access-points tab has completed successfully.')

        # Creating the active-gw-root-alignment tab:
        from get_intent_checks_data import stp_fhrp_mismatch_blue
        df = intent_to_df(intents['/tables/fhrp/stproot-alignment'])
        if len(df.columns) > 1 and stp_fhrp_mismatch_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='active-gw-root-alignment')
            active_gateway_sheet = writer.sheets['active-gw-root-alignment']
            for i, width in enumerate(get_col_widths(df)):
                active_gateway_sheet.set_column(i, i, width)
            active_gateway_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            active_gateway_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            active_gateway_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The active-gw-root-alignment tab has completed successfully.')

        # Creating the all-neighbors tab:
        from get_intent_checks_data import cdp_lldp_nei_blue
        df = intent_to_df(intents['/tables/neighbors/all'])
        if len(df.columns) > 1 and cdp_lldp_nei_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='all-neighbors')
            all_neighbors_sheet = writer.sheets['all-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                all_neighbors_sheet.set_column(i, i, width)
            all_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "blue",
                                                'format': blue_color})

            all_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "amber",
                                                'format': amber_color})

            all_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The all-neighbors tab has completed successfully.')

        # Creating the arp-table tab:
        from get_intent_checks_data import proxy_arp_blue
        df = intent_to_df(intents['/tables/addressing/arp'])
        if len(df.columns) > 1 and proxy_arp_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='arp-table')
            arp_sheet = writer.sheets['arp-table']
            for i, width in enumerate(get_col_widths(df)):
                arp_sheet.set_column(i, i, width)
            arp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            arp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            arp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The arp-table tab has completed successfully.')

        # Creating the bgp-neighbors tab:
        from get_intent_checks_data import (bgp_age_blue,bgp_age_amber,bgp_age_red,bgp_nei_blue,bgp_nei_amber,
                                            bgp_nei_red,bgp_rec_blue,bgp_rec_amber)
        df = intent_to_df(intents['/tables/routing/protocols/bgp/neighbors'])
        if len(df.columns) > 1 and (bgp_age_blue > 0 or bgp_age_amber > 0 or bgp_age_red > 0 or bgp_nei_blue > 0
            or bgp_nei_amber > 0 or bgp_nei_red > 0 or bgp_rec_blue > 0 or bgp_rec_amber > 0):
            df = df.drop(df[(df.state == 'established')].index)
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='bgp-neighbors')
            bgp_neighbors_sheet = writer.sheets['bgp-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                bgp_neighbors_sheet.set_column(i, i, width)
            bgp_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            bgp_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            bgp_neighbors_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The bgp-neighbors tab has completed successfully.')

        #
        # Creating the devices tab:
        from get_intent_checks_data import (confreg_amber, uptime_blue,
                                            uptime_amber,uptime_red,memory_blue,memory_amber,
                                            memory_red,reload_red,reload_amber,reload_blue)
        df = intent_to_df(intents['/tables/inventory/devices'])
        if len(df.columns) > 1 and (confreg_amber > 0 or uptime_blue > 0 or uptime_amber or uptime_red > 0
            or memory_blue > 0 or memory_amber > 0 or memory_red > 0 or reload_blue > 0 or reload_amber > 0 or
            reload_red > 0):
            df = df.drop(['mac', 'icon', 'loginType', 'processor', 'rd', 'stpDomain'], axis=1)
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='devices')
            devices_sheet = writer.sheets['devices']
            for i, width in enumerate(get_col_widths(df)):
                devices_sheet.set_column(i, i, width)
            devices_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            devices_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            devices_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The devices tab has completed successfully.')

        # Creating the dhcp-bindings tab:
        from get_intent_checks_data import dhcp_binding_blue,dhcp_binding_amber,dhcp_binding_red
        df = intent_to_df(intents['/tables/security/dhcp/bindings'])
        if len(df.columns) > 1 and (dhcp_binding_blue > 0 or dhcp_binding_amber > 0 or dhcp_binding_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='dhcp-bindings')
            dhcp_bindings_sheet = writer.sheets['dhcp-bindings']
            for i, width in enumerate(get_col_widths(df)):
                dhcp_bindings_sheet.set_column(i, i, width)
            dhcp_bindings_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            dhcp_bindings_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            dhcp_bindings_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The dhcp-bindings tab has completed successfully.')

        # Creating the dhcp-snooping tab:
        from get_intent_checks_data import dhcp_dropped_amber,dhcp_trusted_red,dhcp_enabled_red
        df = intent_to_df(intents['/tables/security/dhcp/snooping'])
        if len(df.columns) > 1 and (dhcp_dropped_amber > 0 or dhcp_trusted_red > 0 or dhcp_enabled_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='dhcp-snooping')
            dhcp_snooping_sheet = writer.sheets['dhcp-snooping']
            for i, width in enumerate(get_col_widths(df)):
                dhcp_snooping_sheet.set_column(i, i, width)
            dhcp_snooping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            dhcp_snooping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            dhcp_snooping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The dhcp-snooping tab has completed successfully.')

        # Creating the dmvpn tab:
        from get_intent_checks_data import dmvpn_amber
        df = intent_to_df(intents['/tables/security/dmvpn'])
        if len(df.columns) > 1 and dmvpn_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='dmvpn')
            dmvpn_sheet = writer.sheets['dmvpn']
            for i, width in enumerate(get_col_widths(df)):
                dmvpn_sheet.set_column(i, i, width)
            dmvpn_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            dmvpn_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            dmvpn_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The dmvpn tab has completed successfully.')

        # Creating the drops-bidirectional tab:
        from get_intent_checks_data import drop_rates_bi_blue,drop_rates_bi_amber,drop_rates_bi_red
        df = intent_to_df(intents['/tables/interfaces/drops/bidirectional'])
        if len(df.columns) > 1 and (drop_rates_bi_blue > 0 or drop_rates_bi_amber > 0 or drop_rates_bi_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-bidirectional')
            drops_bidi_sheet = writer.sheets['drops-bidirectional']
            for i, width in enumerate(get_col_widths(df)):
                drops_bidi_sheet.set_column(i, i, width)
            drops_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-bidirectional-device tab has completed successfully.')

        # Creating the drops-bidirectional-device tab:
        from get_intent_checks_data import drop_rates_dev_bi_blue,drop_rates_dev_bi_amber,drop_rates_dev_bi_red
        df = intent_to_df(intents['/tables/interfaces/drops/bidirectional-device'])
        if len(df.columns) > 1 and (drop_rates_dev_bi_blue > 0 or drop_rates_dev_bi_amber > 0 or
            drop_rates_dev_bi_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-bidirectional-device')
            drops_bidi_dev_sheet = writer.sheets['drops-bidirectional-device']
            for i, width in enumerate(get_col_widths(df)):
                drops_bidi_dev_sheet.set_column(i, i, width)
            drops_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-bidirectional-device tab has completed successfully.')

        # Creating the drops-inbound tab:
        from get_intent_checks_data import (input_drops_blue,input_drops_amber,input_drops_red)
        df = intent_to_df(intents['/tables/interfaces/drops/inbound'])
        if len(df.columns) > 1 and (input_drops_blue > 0 or input_drops_amber > 0 or input_drops_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-inbound')
            drops_inbound_sheet = writer.sheets['drops-inbound']
            for i, width in enumerate(get_col_widths(df)):
                drops_inbound_sheet.set_column(i, i, width)
            drops_inbound_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_inbound_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_inbound_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-inbound tab has completed successfully.')

        # Creating the drops-inbound-device tab:
        from get_intent_checks_data import dev_in_drops_blue,dev_in_drops_amber,dev_in_drops_red
        df = intent_to_df(intents['/tables/interfaces/drops/inbound-device'])
        if len(df.columns) > 1 and (dev_in_drops_blue > 0 or dev_in_drops_amber > 0 or dev_in_drops_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-inbound-device')
            drops_in_dev_sheet = writer.sheets['drops-inbound-device']
            for i, width in enumerate(get_col_widths(df)):
                drops_in_dev_sheet.set_column(i, i, width)
            drops_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-inbound-device tab has completed successfully.')

        # Creating the drops-outbound tab:
        from get_intent_checks_data import output_drops_blue,output_drops_amber,output_drops_red
        df = intent_to_df(intents['/tables/interfaces/drops/outbound'])
        if len(df.columns) > 1 and (output_drops_blue > 0 or output_drops_amber > 0 or output_drops_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-outbound')
            drops_out_sheet = writer.sheets['drops-outbound']
            for i, width in enumerate(get_col_widths(df)):
                drops_out_sheet.set_column(i, i, width)
            drops_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-outbound tab has completed successfully.')

        # Creating the drops-outbound-device tab:
        from get_intent_checks_data import dev_out_drops_blue,dev_out_drops_amber,dev_out_drops_red
        df = intent_to_df(intents['/tables/interfaces/drops/outbound-device'])
        if len(df.columns) > 1 and (dev_out_drops_blue > 0 or dev_out_drops_amber > 0 or dev_out_drops_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='drops-outbound-device')
            drops_out_dev_sheet = writer.sheets['drops-outbound-device']
            for i, width in enumerate(get_col_widths(df)):
                drops_out_dev_sheet.set_column(i, i, width)
            drops_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            drops_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            drops_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The drops-outbound-device tab has completed successfully.')

        # Creating the duplicate-ip tab:
        from get_intent_checks_data import dupe_ip_blue,dupe_ip_amber
        df = intent_to_df(intents['/tables/addressing/duplicate-ip'])
        if len(df.columns) > 1 and (dupe_ip_blue > 0 or dupe_ip_amber):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='duplicate-ip')
            dupe_ip_sheet = writer.sheets['duplicate-ip']
            for i, width in enumerate(get_col_widths(df)):
                dupe_ip_sheet.set_column(i, i, width)
            dupe_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            dupe_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            dupe_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The duplicate-ip tab has completed successfully.')

        # Creating the eigrp-interfaces tab:
        from get_intent_checks_data import eigrp_int_blue
        df = intent_to_df(intents['/tables/routing/protocols/eigrp/interfaces'])
        if len(df.columns) > 1 and eigrp_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='eigrp-interfaces')
            eigrp_int_sheet = writer.sheets['eigrp-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                eigrp_int_sheet.set_column(i, i, width)
            eigrp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            eigrp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            eigrp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The eigrp-interfaces tab has completed successfully.')

        # Creating the eigrp-neighbors tab:
        from get_intent_checks_data import (eigrp_age_blue,eigrp_age_amber,eigrp_age_red)
        df = intent_to_df(intents['/tables/routing/protocols/eigrp/neighbors'])
        if len(df.columns) > 1 and (eigrp_age_blue > 0 or eigrp_age_amber > 0 or eigrp_age_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='eigrp-neighbors')
            eigrp_nei_sheet = writer.sheets['eigrp-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                eigrp_nei_sheet.set_column(i, i, width)
            eigrp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            eigrp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            eigrp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The eigrp-neighbors tab has completed successfully.')

        # Creating the errdisabled tab:
        from get_intent_checks_data import err_amber
        df = intent_to_df(intents['/tables/interfaces/errors/disabled'])
        if len(df.columns) > 1 and err_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errdisabled')
            errdisabled_sheet = writer.sheets['errdisabled']
            for i, width in enumerate(get_col_widths(df)):
                errdisabled_sheet.set_column(i, i, width)
            errdisabled_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            errdisabled_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            errdisabled_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errdisabled tab has completed successfully.')

        # Creating the errors-bidirectional tab:
        from get_intent_checks_data import (error_rates_bi_blue,error_rates_bi_amber,error_rates_bi_red)
        df = intent_to_df(intents['/tables/interfaces/errors/bidirectional'])
        if len(df.columns) > 1 and (error_rates_bi_blue > 0 or error_rates_bi_amber > 0 or error_rates_bi_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-bidirectional')
            err_bidi_sheet = writer.sheets['errors-bidirectional']
            for i, width in enumerate(get_col_widths(df)):
                err_bidi_sheet.set_column(i, i, width)
            err_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_bidi_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-bidirectional tab has completed successfully.')

        # Creating the errors-bidirectional-device tab:
        from get_intent_checks_data import (dev_bi_errors_blue,dev_bi_errors_amber,dev_bi_errors_red)
        df = intent_to_df(intents['/tables/interfaces/errors/bidirectional-device'])
        if len(df.columns) > 1 and (dev_bi_errors_blue > 0 or dev_bi_errors_amber > 0 or dev_bi_errors_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-bidirectional-device')
            err_bidi_dev_sheet = writer.sheets['errors-bidirectional-device']
            for i, width in enumerate(get_col_widths(df)):
                err_bidi_dev_sheet.set_column(i, i, width)
            err_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_bidi_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-bidirectional-device tab has completed successfully.')

        # Creating the errors-inbound tab:
        from get_intent_checks_data import input_errors_blue,input_errors_amber,input_errors_red
        df = intent_to_df(intents['/tables/interfaces/errors/inbound'])
        if len(df.columns) > 1 and (input_errors_blue > 0 or input_errors_amber > 0 or input_errors_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-inbound')
            err_in_sheet = writer.sheets['errors-inbound']
            for i, width in enumerate(get_col_widths(df)):
                err_in_sheet.set_column(i, i, width)
            err_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-inbound tab has completed successfully.')

        # Creating the errors-inbound-device tab:
        from get_intent_checks_data import dev_in_errors_blue,dev_in_errors_amber,dev_in_errors_red
        df = intent_to_df(intents['/tables/interfaces/errors/inbound-device'])
        if len(df.columns) > 1 and (dev_in_errors_blue > 0 or dev_in_errors_amber > 0 or dev_in_errors_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-inbound-device')
            err_in_dev_sheet = writer.sheets['errors-inbound-device']
            for i, width in enumerate(get_col_widths(df)):
                err_in_dev_sheet.set_column(i, i, width)
            err_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-inbound-device tab has completed successfully.')

        # Creating the errors-outbound tab:
        from get_intent_checks_data import output_errors_blue,output_errors_amber,output_errors_red
        df = intent_to_df(intents['/tables/interfaces/errors/outbound'])
        if len(df.columns) > 1 and (output_errors_blue > 0 or output_errors_amber > 0 or output_errors_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-outbound')
            err_out_sheet = writer.sheets['errors-outbound']
            for i, width in enumerate(get_col_widths(df)):
                err_out_sheet.set_column(i, i, width)
            err_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-outbound tab has completed successfully.')

        # Creating the errors-outbound-device tab:
        from get_intent_checks_data import dev_out_errors_blue,dev_out_errors_amber,dev_out_errors_red
        df = intent_to_df(intents['/tables/interfaces/errors/outbound-device'])
        if len(df.columns) > 1 and (dev_out_errors_blue > 0 or dev_out_errors_amber > 0 or dev_out_errors_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='errors-outbound-device')
            err_out_dev_sheet = writer.sheets['errors-outbound-device']
            for i, width in enumerate(get_col_widths(df)):
                err_out_dev_sheet.set_column(i, i, width)
            err_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            err_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            err_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The errors-outbound-device tab has completed successfully.')

        # # # Creating the end-of-life  tab:
        # # df = pd.read_csv("DOWNLOADS/cleaned-tables/end-of-life.csv", keep_default_na=False)
        # # df.to_excel(writer, index=False, sheet_name='end-of-life')
        # # print('The end-of-life tab has completed successfully.')
        #
        # Creating the fans tab:
        from get_intent_checks_data import fan_blue,fan_red
        df = intent_to_df(intents['/tables/inventory/fans'])
        if len(df.columns) > 1 and (fan_blue > 0 or fan_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='fans')
            fans_sheet = writer.sheets['fans']
            for i, width in enumerate(get_col_widths(df)):
                fans_sheet.set_column(i, i, width)
            fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The fans  tab has completed successfully.')

        # Creating the gateway-redundancy tab:
        from get_intent_checks_data import gwy_redu_blue
        df = intent_to_df(intents['/tables/networks/gateway-redundancy'])
        if len(df.columns) > 1 and gwy_redu_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='gateway-redundancy')
            gtwy_redu_sheet = writer.sheets['gateway-redundancy']
            for i, width in enumerate(get_col_widths(df)):
                gtwy_redu_sheet.set_column(i, i, width)
            gtwy_redu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            gtwy_redu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            gtwy_redu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The gateway-redundancy tab has completed successfully.')

        # Creating the group-members tab:
        from get_intent_checks_data import fhrp_members_blue,fhrp_master_blue,fhrp_master_amber,fhrp_master_red
        df = intent_to_df(intents['/tables/fhrp/group-members'])
        if len(df.columns) > 1 and (fhrp_members_blue > 0 or fhrp_master_blue > 0 or
            fhrp_master_amber > 0 or fhrp_master_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='group-members')
            group_members_sheet = writer.sheets['group-members']
            for i, width in enumerate(get_col_widths(df)):
                group_members_sheet.set_column(i, i, width)
            group_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            group_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            group_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The group-members tab has completed successfully.')

        # Creating the group-state tab:
        from get_intent_checks_data import fhrp_active_blue
        df = intent_to_df(intents['/tables/fhrp/group-state'])
        if len(df.columns) > 1 and fhrp_active_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='group-state')
            group_state_sheet = writer.sheets['group-state']
            for i, width in enumerate(get_col_widths(df)):
                group_state_sheet.set_column(i, i, width)
            group_state_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            group_state_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            group_state_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The group-state tab has completed successfully.')

        # Creating the hosts tab:
        from get_intent_checks_data import endpres_blue
        df = intent_to_df(intents['/tables/addressing/hosts'])
        if len(df.columns) > 1 and endpres_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='hosts')
            hosts_sheet = writer.sheets['hosts']
            for i, width in enumerate(get_col_widths(df)):
                hosts_sheet.set_column(i, i, width)
            hosts_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            hosts_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            hosts_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The hosts tab has completed successfully.')

        # Creating the inbound-balancing-table tab:
        from get_intent_checks_data import pc_in_var_blue,pc_in_var_amber,pc_in_var_red
        df = intent_to_df(intents['/tables/interfaces/port-channel/balance/inbound'])
        if len(df.columns) > 1 and (pc_in_var_blue > 0 or pc_in_var_amber > 0 or pc_in_var_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='inbound-balancing-table')
            inbound_balancing_sheet = writer.sheets['inbound-balancing-table']
            for i, width in enumerate(get_col_widths(df)):
                inbound_balancing_sheet.set_column(i, i, width)
            inbound_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            inbound_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            inbound_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The inbound-balancing-table tab has completed successfully.')

        # Creating the interfaces tab:
        from get_intent_checks_data import (duplex_blue,duplex_amber,operate_blue)
        df = intent_to_df(intents['/tables/routing/protocols/ospf/interfaces'])
        if len(df.columns) > 1 and (duplex_blue > 0 or duplex_amber > 0 or operate_blue):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='interfaces')
            interfaces_sheet = writer.sheets['interfaces']
            for i, width in enumerate(get_col_widths(df)):
                interfaces_sheet.set_column(i, i, width)
            interfaces_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            interfaces_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            interfaces_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The interfaces tab has completed successfully.')

        # Creating the ipsec-gateways tab:
        from get_intent_checks_data import ipsec_gateway_red,ipsec_gwy_enc_amber,ipsec_gateway_auth_amber
        df = intent_to_df(intents['/tables/security/ipsec/gateways'])
        if len(df.columns) > 1 and (ipsec_gateway_red > 0 or ipsec_gwy_enc_amber > 0 or ipsec_gateway_auth_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ipsec-gateways')
            ipsec_gateways_sheet = writer.sheets['ipsec-gateways']
            for i, width in enumerate(get_col_widths(df)):
                ipsec_gateways_sheet.set_column(i, i, width)
            ipsec_gateways_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ipsec_gateways_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ipsec_gateways_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ipsec-gateways tab has completed successfully.')

        # Creating the ipsec-tunnels tab:
        from get_intent_checks_data import ipsec_status_red,ipsec_auth_amber,ipsec_enc_amber
        df = intent_to_df(intents['/tables/security/ipsec/tunnels'])
        if len(df.columns) > 1 and (ipsec_status_red > 0 or ipsec_auth_amber > 0 or ipsec_enc_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ipsec-tunnels')
            ipsec_tunnels_sheet = writer.sheets['ipsec-tunnels']
            for i, width in enumerate(get_col_widths(df)):
                ipsec_tunnels_sheet.set_column(i, i, width)
            ipsec_tunnels_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ipsec_tunnels_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ipsec_tunnels_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ipsec-tunnels tab has completed successfully.')

        # Creating the is-is-interfaces tab:
        from get_intent_checks_data import isis_int_blue
        df = intent_to_df(intents['/tables/routing/protocols/is-is/interfaces'])
        if len(df.columns) > 1 and isis_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='is-is-interfaces')
            isis_int_sheet = writer.sheets['is-is-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                isis_int_sheet.set_column(i, i, width)
            isis_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            isis_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            isis_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The is-is-interfaces tab has completed successfully.')

        # Creating the is-is-neighbors tab:
        from get_intent_checks_data import isis_age_blue,isis_age_amber,isis_age_red
        df = intent_to_df(intents['/tables/routing/protocols/is-is/neighbors'])
        if len(df.columns) > 1 and (isis_age_blue > 0 or isis_age_amber > 0 or isis_age_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='is-is-neighbors')
            isis_nei_sheet = writer.sheets['is-is-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                isis_nei_sheet.set_column(i, i, width)
            isis_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            isis_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            isis_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The is-is-neighbors tab has completed successfully.')

        # Creating the juniper-cluster-srx tab:
        from get_intent_checks_data import juniper_amber
        df = intent_to_df(intents['/tables/platforms/cluster/srx'])
        if len(df.columns) > 1 and juniper_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='juniper-cluster-srx')
            juniper_cluster_srx_sheet = writer.sheets['juniper-cluster-srx']
            for i, width in enumerate(get_col_widths(df)):
                juniper_cluster_srx_sheet.set_column(i, i, width)
            juniper_cluster_srx_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            juniper_cluster_srx_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            juniper_cluster_srx_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The juniper-cluster-srx tab has completed successfully.')

        # Creating the ldp-interfaces tab:
        from get_intent_checks_data import ldp_int_blue
        df = intent_to_df(intents['/tables/mpls/ldp/interfaces'])
        if len(df.columns) > 1 and ldp_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ldp-interfaces')
            ldp_int_sheet = writer.sheets['ldp-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                ldp_int_sheet.set_column(i, i, width)
            ldp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ldp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ldp_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ldp-interfaces tab has completed successfully.')

        # Creating the ldp-neighbors tab:
        from get_intent_checks_data import ldp_age_blue,ldp_age_amber,ldp_age_red
        df = intent_to_df(intents['/tables/mpls/ldp/neighbors'])
        if len(df.columns) > 1 and (ldp_age_blue > 0 or ldp_age_amber > 0 or ldp_age_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ldp-neighbors')
            ldp_nei_sheet = writer.sheets['ldp-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                ldp_nei_sheet.set_column(i, i, width)
            ldp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ldp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ldp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ldp-neighbors tab has completed successfully.')

        # Creating the logging-local tab:
        from get_intent_checks_data import local_logg_amber
        df = intent_to_df(intents['/tables/management/logging/local'])
        if len(df.columns) > 1 and local_logg_amber > 0:
            df.to_excel(writer, index=False, sheet_name='logging-local')
            log_local_sheet = writer.sheets['logging-local']
            for i, width in enumerate(get_col_widths(df)):
                log_local_sheet.set_column(i, i, width)
            log_local_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            log_local_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            log_local_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The logging-local tab has completed successfully.')

        # Creating the logging-remote tab:
        from get_intent_checks_data import remote_sys_logg_amber
        df = intent_to_df(intents['/tables/management/logging/remote'])
        if len(df.columns) > 1 and remote_sys_logg_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='logging-remote')
            log_remote_sheet = writer.sheets['logging-remote']
            for i, width in enumerate(get_col_widths(df)):
                log_remote_sheet.set_column(i, i, width)
            log_remote_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            log_remote_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            log_remote_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The logging-remote tab has completed successfully.')

        # Creating the logging-summary tab:
        from get_intent_checks_data import device_logg_amber,device_logg_red
        df = intent_to_df(intents['/tables/management/logging/summary'])
        if len(df.columns) > 1 and (device_logg_amber > 0 or device_logg_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='logging-summary')
            log_summary_sheet = writer.sheets['logging-summary']
            for i, width in enumerate(get_col_widths(df)):
                log_summary_sheet.set_column(i, i, width)
            log_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            log_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            log_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The logging-summary tab has completed successfully.')

        # Creating the l2vpn-circuit-cross-connect tab:
        from get_intent_checks_data import ccc_blue
        df = intent_to_df(intents['/tables/mpls/l2-vpn/point-to-point-vpws'])
        if len(df.columns) > 1 and ccc_blue > 0:
            df.to_excel(writer, index=False, sheet_name='l2vpn-circuit-cross-connect')
            l2vpn_x_connect_sheet = writer.sheets['l2vpn-circuit-cross-connect']
            for i, width in enumerate(get_col_widths(df)):
                l2vpn_x_connect_sheet.set_column(i, i, width)
            l2vpn_x_connect_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            l2vpn_x_connect_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            l2vpn_x_connect_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The l2vpn-circuit-cross-connect tab has completed successfully.')

        # Creating the l2vpn-point-to-multipoint tab:
        from get_intent_checks_data import ptmp_vpls_blue
        df = intent_to_df(intents['/tables/mpls/l2-vpn/point-to-multipoint'])
        if len(df.columns) > 1 and ptmp_vpls_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='l2vpn-point-to-multipoint')
            l2vpn_p2m_sheet = writer.sheets['l2vpn-point-to-multipoint']
            for i, width in enumerate(get_col_widths(df)):
                l2vpn_p2m_sheet.set_column(i, i, width)
            l2vpn_p2m_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            l2vpn_p2m_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            l2vpn_p2m_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The l2vpn-point-to-multipoint tab has completed successfully.')

        # Creating the l2vpn-point-to-point-vpws tab:
        from get_intent_checks_data import ptp_vpws_blue
        df = intent_to_df(intents['/tables/mpls/l2-vpn/point-to-point-vpws'])
        if len(df.columns) > 1 and ptp_vpws_blue:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='l2vpn-point-to-point-vpws')
            l2vpn_p2p_sheet = writer.sheets['l2vpn-point-to-point-vpws']
            for i, width in enumerate(get_col_widths(df)):
                l2vpn_p2p_sheet.set_column(i, i, width)
            l2vpn_p2p_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            l2vpn_p2p_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            l2vpn_p2p_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The l2vpn-point-to-point-vpws tab has completed successfully.')

        # Creating the neighbor-ports-vlan-mismatch tab:
        from get_intent_checks_data import ta_vlm_red
        df = intent_to_df(intents['/tables/spanning-tree/inconsistencies/neighbor-ports-vlan-mismatch'])
        if len(df.columns) > 1 and ta_vlm_red > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='neighbor-ports-vlan-mismatch')
            nei_ports_mismatch_sheet = writer.sheets['neighbor-ports-vlan-mismatch']
            for i, width in enumerate(get_col_widths(df)):
                nei_ports_mismatch_sheet.set_column(i, i, width)
            nei_ports_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            nei_ports_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            nei_ports_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The neighbor-ports-vlan-mismatch tab has completed successfully.')

        # Creating the ntp-sources tab:
        from get_intent_checks_data import ntp_stratum_blue,ntp_stratum_amber,ntp_stratum_red
        df = intent_to_df(intents['/tables/management/ntp/sources'])
        if len(df.columns) > 1 and (ntp_stratum_blue > 0 or ntp_stratum_amber > 0 or ntp_stratum_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ntp-sources')
            ntp_sources_sheet = writer.sheets['ntp-sources']
            for i, width in enumerate(get_col_widths(df)):
                ntp_sources_sheet.set_column(i, i, width)
            ntp_sources_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ntp_sources_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ntp_sources_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ntp-sources tab has completed successfully.')

        # Creating the ntp-summary tab:
        from get_intent_checks_data import (ntp_reachable_blue,ntp_reachable_amber,ntp_reachable_red,
                                            ntp_sources_amber,ntp_sources_red)
        df = intent_to_df(intents['/tables/management/ntp/summary'])
        if len(df.columns) > 1 and (ntp_reachable_blue > 0 or ntp_reachable_amber > 0 or ntp_reachable_red > 0
            or ntp_sources_amber > 0 or ntp_sources_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ntp-summary')
            ntp_summary_sheet = writer.sheets['ntp-summary']
            for i, width in enumerate(get_col_widths(df)):
                ntp_summary_sheet.set_column(i, i, width)
            ntp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ntp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ntp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ntp-summary tab has completed successfully.')

        # Creating the mac-table tab:
        from get_intent_checks_data import mac_source_blue, mac_source_amber
        df = intent_to_df(intents['/tables/addressing/mac'])
        if len(df.columns) > 1 and (mac_source_blue > 0 or mac_source_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mac-table')
            mac_sheet = writer.sheets['mac-table']
            for i, width in enumerate(get_col_widths(df)):
                mac_sheet.set_column(i, i, width)
            mac_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mac_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mac_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mac-table tab has completed successfully.')

        # Creating the managed-ip tab:
        from get_intent_checks_data import ip_dns_blue,ip_dns_amber
        df = intent_to_df(intents['/tables/addressing/managed-devs'])
        if len(df.columns) > 1 and (ip_dns_blue > 0 or ip_dns_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='managed-ip')
            managed_ip_sheet = writer.sheets['managed-ip']
            for i, width in enumerate(get_col_widths(df)):
                managed_ip_sheet.set_column(i, i, width)
            managed_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            managed_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            managed_ip_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The managed-ip tab has completed successfully.')

        # Creating the member-status-table tab:
        from get_intent_checks_data import pc_ms_blue,pc_ms_amber
        df = intent_to_df(intents['/tables/interfaces/port-channel/member-status'])
        if len(df.columns) > 1 and (pc_ms_blue > 0 or pc_ms_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='member-status-table')
            member_status_sheet = writer.sheets['member-status-table']
            for i, width in enumerate(get_col_widths(df)):
                member_status_sheet.set_column(i, i, width)
            member_status_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            member_status_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            member_status_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The member-status-table tab has completed successfully.')

        # Creating the mlag-pairs tab:
        from get_intent_checks_data import mlag_amber,mlag_red
        df = intent_to_df(intents['/tables/platforms/mlag/pairs'])
        if len(df.columns) > 1 and (mlag_amber > 0 or mlag_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mlag-pairs')
            mlag_pairs_sheet = writer.sheets['mlag-pairs']
            for i, width in enumerate(get_col_widths(df)):
                mlag_pairs_sheet.set_column(i, i, width)
            mlag_pairs_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mlag_pairs_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mlag_pairs_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mlag-pairs tab has completed successfully.')

        # Creating the mlag-peer-links tab:
        from get_intent_checks_data import vpcpl_red
        df = intent_to_df(intents['/tables/platforms/mlag/peers'])
        if len(df.columns) > 1 and vpcpl_red > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mlag-peer-links')
            mlag_peer_links_sheet = writer.sheets['mlag-peer-links']
            for i, width in enumerate(get_col_widths(df)):
                mlag_peer_links_sheet.set_column(i, i, width)
            mlag_peer_links_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mlag_peer_links_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mlag_peer_links_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mlag-peer-links tab has completed successfully.')

        # Creating the mlag-vpc tab:
        from get_intent_checks_data import vpcst_blue,vpcst_red
        df = intent_to_df(intents['/tables/platforms/mlag/vpc'])
        if len(df.columns) > 1 and (vpcst_blue > 0 or vpcst_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mlag-vpc')
            mlag_vpc_sheet = writer.sheets['mlag-vpc']
            for i, width in enumerate(get_col_widths(df)):
                mlag_vpc_sheet.set_column(i, i, width)
            mlag_vpc_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mlag_vpc_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mlag_vpc_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mlag-vpc tab has completed successfully.')

        # Creating the mroute-counters tab:
        from get_intent_checks_data import mroute_rpf_amber,mroute_other_amber
        df = intent_to_df(intents['/tables/multicast/routes/counters'])
        if len(df.columns) > 1 and (mroute_rpf_amber > 0 or mroute_other_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mroute-counters')
            mroute_counters_sheet = writer.sheets['mroute-counters']
            for i, width in enumerate(get_col_widths(df)):
                mroute_counters_sheet.set_column(i, i, width)
            mroute_counters_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mroute_counters_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mroute_counters_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mroute-counters tab has completed successfully.')

        # Creating the mtu tab:
        from get_intent_checks_data import mtu_blue,mtu_amber
        df = intent_to_df(intents['/tables/interfaces/mtu'])
        if len(df.columns) > 1 and (mtu_blue > 0 or mtu_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='mtu')
            mtu_sheet = writer.sheets['mtu']
            for i, width in enumerate(get_col_widths(df)):
                mtu_sheet.set_column(i, i, width)
            mtu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            mtu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            mtu_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The mtu tab has completed successfully.')

        # Creating the os-versions tab:
        from get_intent_checks_data import os_ver_blue,os_ver_amber,os_ver_red,unique_os_blue,unique_platform_blue
        df = intent_to_df(intents['/tables/management/osver-consistency'])
        if len(df.columns) > 1 and (os_ver_blue > 0 or os_ver_amber > 0 or os_ver_red > 0
            or unique_os_blue > 0 or unique_platform_blue > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='os-versions')
            os_ver_sheet = writer.sheets['os-versions']
            for i, width in enumerate(get_col_widths(df)):
                os_ver_sheet.set_column(i, i, width)
            os_ver_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            os_ver_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            os_ver_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The os-versions tab has completed successfully.')

        # Creating the ospf-interfaces tab:
        from get_intent_checks_data import ospf_int_blue
        df = intent_to_df(intents['/tables/routing/protocols/ospf/interfaces'])
        if len(df.columns) > 1 and ospf_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ospf-interfaces')
            ospf_int_sheet = writer.sheets['ospf-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                ospf_int_sheet.set_column(i, i, width)
            ospf_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ospf_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ospf_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ospf-interfaces tab has completed successfully.')

        # Creating the ospf-neighbors tab:
        from get_intent_checks_data import (ospf_age_blue,ospf_age_amber,ospf_age_red,ospf_nei_blue,
        ospf_nei_amber,ospf_nei_red,ospf_cost_blue,ospf_cost_amber)
        df = intent_to_df(intents['/tables/routing/protocols/ospf/neighbors'])
        if len(df.columns) > 1 and (ospf_age_blue > 0 or ospf_age_amber > 0 or ospf_age_red > 0 or
                                    ospf_nei_blue > 0 or ospf_nei_amber > 0 or ospf_nei_red > 0 or
                                    ospf_cost_blue > 0 or ospf_cost_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='ospf-neighbors')
            ospf_nei_sheet = writer.sheets['ospf-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                ospf_nei_sheet.set_column(i, i, width)
            ospf_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            ospf_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            ospf_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The ospf-neighbors tab has completed successfully.')
        #
        # # Creating the ospf-v3-interfaces tab:
        # from get_intent_checks_data import (ospfv3_int_blue)
        # df = intent_to_df(intents['/tables/routing/protocols/ospf-v3/interfaces'])
        # if len(df.columns) > 1 and (ospfv3_int_blue > 0):
        #     df = df.dropna(how='all', axis='columns')
        #     if 'Unnamed: 0' in df:
        #         df = df.drop(['Unnamed: 0'], axis=1)
        #     df.to_excel(writer, index=False, sheet_name='ospf-v3-interfaces')
        #     ospf_v3_int_sheet = writer.sheets['ospf-v3-interfaces']
        #     for i, width in enumerate(get_col_widths(df)):
        #         ospf_v3_int_sheet.set_column(i, i, width)
        #     ospf_v3_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                            'criteria': 'containing',
        #                            'value': "blue",
        #                            'format': blue_color})
        #
        #     ospf_v3_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                            'criteria': 'containing',
        #                            'value': "amber",
        #                            'format': amber_color})
        #
        #     ospf_v3_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                                         'criteria': 'containing',
        #                                         'value': "red",
        #                                         'format': red_color})
        #     print('The ospf-v3-interfaces tab has completed successfully.')
        #
        # # Creating the ospf-v3-neighbors tab:
        # from get_intent_checks_data import (ospfv3_nei_blue,ospfv3_nei_amber,ospfv3_nei_red,ospfv3_cost_blue,
        #                                     ospfv3_cost_amber,ospfv3_age_blue,ospfv3_age_amber,ospfv3_age_red)
        # df = intent_to_df(intents['/tables/routing/protocols/ospf-v3/neighbors'])
        # if len(df.columns) > 1 and (ospfv3_nei_blue > 0 or ospfv3_nei_amber > 0 or ospfv3_nei_red > 0 or
        #     ospfv3_cost_blue > 0 or ospfv3_cost_amber > 0 or ospfv3_age_blue > 0 or ospfv3_age_amber > 0
        #     or ospfv3_age_red > 0):
        #     df = df.dropna(how='all', axis='columns')
        #     if 'Unnamed: 0' in df:
        #         df = df.drop(['Unnamed: 0'], axis=1)
        #     df.to_excel(writer, index=False, sheet_name='ospf-v3-neighbors')
        #     ospf_v3_nei_sheet = writer.sheets['ospf-v3-neighbors']
        #     for i, width in enumerate(get_col_widths(df)):
        #         ospf_v3_nei_sheet.set_column(i, i, width)
        #     ospf_v3_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                            'criteria': 'containing',
        #                            'value': "blue",
        #                            'format': blue_color})
        #
        #     ospf_v3_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                            'criteria': 'containing',
        #                            'value': "amber",
        #                            'format': amber_color})
        #
        #     ospf_v3_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
        #                                         'criteria': 'containing',
        #                                         'value': "red",
        #                                         'format': red_color})
        #     print('The ospf-v3-neighbors tab has completed successfully.')

        # Creating the outbound-balancing-table tab:
        from get_intent_checks_data import (pc_out_var_blue,pc_out_var_amber,pc_out_var_red)
        df = intent_to_df(intents['/tables/interfaces/port-channel/balance/outbound'])
        if len(df.columns) > 1 and (pc_out_var_blue > 0 or pc_out_var_amber > 0 or pc_out_var_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='outbound-balancing-table')
            out_balancing_sheet = writer.sheets['outbound-balancing-table']
            for i, width in enumerate(get_col_widths(df)):
                out_balancing_sheet.set_column(i, i, width)
            out_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            out_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            out_balancing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The outbound-balancing-table tab has completed successfully.')

        # # Creating the part-numbers tab:
        # from get_intent_checks_data import ()
        # df = pd.read_csv("DOWNLOADS/cleaned-tables/part-numbers.csv", keep_default_na=False)
        # if len(df.columns) > 1:
        #     df.to_excel(writer, index=False, sheet_name='part-numbers')
        #     print('The part-numbers tab has completed successfully.')

        # Creating the path-verifications tab:
        from get_intent_checks_data import path_flooding_amber,path_verify_amber,path_verify_red
        df = intent_to_df(intents['/tables/networks/path-lookup-checks'])
        if len(df.columns) > 1 and (path_flooding_amber > 0 or path_verify_amber > 0 or path_verify_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='path-verifications')
            path_verify_sheet = writer.sheets['path-verifications']
            for i, width in enumerate(get_col_widths(df)):
                path_verify_sheet.set_column(i, i, width)
            path_verify_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            path_verify_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            path_verify_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The path-verifications tab has completed successfully.')

        # Creating the phones tab:
        from get_intent_checks_data import phonemacs_amber
        df = intent_to_df(intents['/tables/inventory/phones'])
        if len(df.columns) > 1 and phonemacs_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='phones')
            phones_sheet = writer.sheets['phones']
            for i, width in enumerate(get_col_widths(df)):
                phones_sheet.set_column(i, i, width)
            phones_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            phones_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            phones_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The phones tab has completed successfully.')

        # Creating the pim-interfaces tab:
        from get_intent_checks_data import pim_int_blue
        df = intent_to_df(intents['/tables/multicast/pim/interfaces'])
        if len(df.columns) > 1 and pim_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='pim-interfaces')
            pim_int_sheet = writer.sheets['pim-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                pim_int_sheet.set_column(i, i, width)
            pim_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            pim_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            pim_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The pim-interfaces tab has completed successfully.')

        # Creating the pim-neighbors tab:
        from get_intent_checks_data import pim_age_blue,pim_age_amber,pim_age_red
        df = intent_to_df(intents['/tables/multicast/pim/neighbors'])
        if len(df.columns) > 1 and (pim_age_blue > 0 or pim_age_amber > 0 or pim_age_red > 0):
            df.to_excel(writer, index=False, sheet_name='pim-neighbors')
            pim_nei_sheet = writer.sheets['pim-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                pim_nei_sheet.set_column(i, i, width)
            pim_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            pim_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            pim_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The pim-neighbors tab has completed successfully.')

        # Creating the poe-interfaces tab:
        from get_intent_checks_data import poe_state_blue,poe_state_amber
        df = intent_to_df(intents['/tables/platforms/poe/interfaces'])
        if len(df.columns) > 1 and (poe_state_blue > 0 or poe_state_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='poe-interfaces')
            poe_int_sheet = writer.sheets['poe-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                poe_int_sheet.set_column(i, i, width)
            poe_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            poe_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            poe_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The poe-interfaces tab has completed successfully.')

        # Creating the poe-modules tab:
        from get_intent_checks_data import poe_watts_blue,poe_watts_amber,poe_watts_red
        df = intent_to_df(intents['/tables/platforms/poe/modules'])
        if len(df.columns) > 1 and (poe_watts_blue > 0 or poe_watts_amber > 0 or poe_watts_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='poe-modules')
            poe_modules_sheet = writer.sheets['poe-modules']
            for i, width in enumerate(get_col_widths(df)):
                poe_modules_sheet.set_column(i, i, width)
            poe_modules_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            poe_modules_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            poe_modules_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The poe-modules tab has completed successfully.')

        # Creating the policy-map tab:
        from get_intent_checks_data import qos_ef_drops_amber
        df = intent_to_df(intents['/tables/qos/policy-maps'])
        if len(df.columns) > 1 and qos_ef_drops_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='policy-map')
            policy_map_sheet = writer.sheets['policy-map']
            for i, width in enumerate(get_col_widths(df)):
                policy_map_sheet.set_column(i, i, width)
            policy_map_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            policy_map_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            policy_map_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The policy-map tab has completed successfully.')

        # Creating the power-supplies tab:
        from get_intent_checks_data import pwr_state_blue,pwr_state_red
        df = intent_to_df(intents['/tables/inventory/power-supplies'])
        if len(df.columns) > 1 and (pwr_state_blue > 0 or pwr_state_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='power-supplies')
            power_supplies_sheet = writer.sheets['power-supplies']
            for i, width in enumerate(get_col_widths(df)):
                power_supplies_sheet.set_column(i, i, width)
            power_supplies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            power_supplies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            power_supplies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The power-supplies tab has completed successfully.')

        # Creating the power-supplies-fans tab:
        from get_intent_checks_data import pwr_fan_blue,pwr_fan_red
        df = intent_to_df(intents['/tables/inventory/power-supplies-fans'])
        if len(df.columns) > 1 and (pwr_fan_blue > 0 or pwr_fan_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='power-supplies-fans')
            power_fans_sheet = writer.sheets['power-supplies-fans']
            for i, width in enumerate(get_col_widths(df)):
                power_fans_sheet.set_column(i, i, width)
            power_fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            power_fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            power_fans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The power-supplies-fans tab has completed successfully.')

        # Creating the priority-queuing tab:
        from get_intent_checks_data import qos_pri_drops_amber
        df = intent_to_df(intents['/tables/qos/priority-queuing'])
        if len(df.columns) > 1 and qos_pri_drops_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='priority-queuing')
            pri_q_sheet = writer.sheets['priority-queuing']
            for i, width in enumerate(get_col_widths(df)):
                pri_q_sheet.set_column(i, i, width)
            pri_q_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            pri_q_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            pri_q_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The priority-queuing tab has completed successfully.')

        # Creating the pseudowires tab:
        from get_intent_checks_data import pseudo_blue
        df = intent_to_df(intents['/tables/mpls/l2-vpn/pseudowires'])
        if len(df.columns) > 1 and pseudo_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='pseudowires')
            pseudowires_sheet = writer.sheets['pseudowires']
            for i, width in enumerate(get_col_widths(df)):
                pseudowires_sheet.set_column(i, i, width)
            pseudowires_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            pseudowires_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            pseudowires_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The pseudowires tab has completed successfully.')

        # Creating the queuing tab:
        from get_intent_checks_data import q_limit_size_blue,q_limit_size_amber
        df = intent_to_df(intents['/tables/qos/queuing'])
        if len(df.columns) > 1 and (q_limit_size_blue > 0 or q_limit_size_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='queuing')
            queuing_sheet = writer.sheets['queuing']
            for i, width in enumerate(get_col_widths(df)):
                queuing_sheet.set_column(i, i, width)
            queuing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            queuing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            queuing_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The queuing tab has completed successfully.')

        # Creating the random-drops tab:
        from get_intent_checks_data import qos_random_tail_blue,qos_random_tail_amber,qos_random_tail_red
        df = intent_to_df(intents['/tables/qos/random-drops'])
        if len(df.columns) > 1 and (qos_random_tail_blue > 0 or qos_random_tail_amber > 0 or qos_random_tail_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='random-drops')
            random_drops_sheet = writer.sheets['random-drops']
            for i, width in enumerate(get_col_widths(df)):
                random_drops_sheet.set_column(i, i, width)
            random_drops_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            random_drops_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            random_drops_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The random-drops tab has completed successfully.')

        # Creating the rip-interfaces tab:
        from get_intent_checks_data import rip_int_blue
        df = intent_to_df(intents['/tables/routing/protocols/rip/interfaces'])
        if len(df.columns) > 1 and rip_int_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='rip-interfaces')
            rip_int_sheet = writer.sheets['rip-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                rip_int_sheet.set_column(i, i, width)
            rip_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            rip_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            rip_int_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The rip-interfaces tab has completed successfully.')

        # Creating the route-stability tab:
        from get_intent_checks_data import recent_blue,recent_amber,recent_red
        df = intent_to_df(intents['/tables/networks/route-stability'])
        if len(df.columns) > 1 and (recent_blue > 0 or recent_amber > 0 or recent_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='route-stability')
            route_stability_sheet = writer.sheets['route-stability']
            for i, width in enumerate(get_col_widths(df)):
                route_stability_sheet.set_column(i, i, width)
            route_stability_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            route_stability_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            route_stability_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The route-stability tab has completed successfully.')

        # Creating the saved-config-consistency tab:
        from get_intent_checks_data import config_con_blue,config_con_amber
        df = intent_to_df(intents['/tables/management/configuration/saved'])
        if len(df.columns) > 1 and (config_con_blue > 0 or config_con_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='saved-config-consistency')
            config_consistency_sheet = writer.sheets['saved-config-consistency']
            for i, width in enumerate(get_col_widths(df)):
                config_consistency_sheet.set_column(i, i, width)
            config_consistency_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            config_consistency_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            config_consistency_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The saved-config-consistency tab has completed successfully.')

        # Creating the sdwan-sites tab:
        from get_intent_checks_data import sdwan_uptime_blue,sdwan_uptime_amber,sdwan_uptime_red
        df = intent_to_df(intents['/tables/sdwan/sites'])
        if len(df.columns) > 1 and (sdwan_uptime_blue > 0 or sdwan_uptime_amber > 0 or sdwan_uptime_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='sdwan-sites')
            sdwan_sites_sheet = writer.sheets['sdwan-sites']
            for i, width in enumerate(get_col_widths(df)):
                sdwan_sites_sheet.set_column(i, i, width)
            sdwan_sites_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            sdwan_sites_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            sdwan_sites_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The sdwan-sites tab has completed successfully.')

        # Creating the shaping tab:
        from get_intent_checks_data import shaping_child_blue
        df = intent_to_df(intents['/tables/qos/shaping'])
        if len(df.columns) > 1 and shaping_child_blue > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='shaping')
            shaping_sheet = writer.sheets['shaping']
            for i, width in enumerate(get_col_widths(df)):
                shaping_sheet.set_column(i, i, width)
            shaping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            shaping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            shaping_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The shaping tab has completed successfully.')

        # Creating the snmp-communities tab:
        from get_intent_checks_data import snmp_acl_blue,snmp_name_amber
        df = intent_to_df(intents['/tables/management/snmp/communities'])
        if len(df.columns) > 1 and (snmp_acl_blue > 0 or snmp_name_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='snmp-communities')
            snmp_comm_sheet = writer.sheets['snmp-communities']
            for i, width in enumerate(get_col_widths(df)):
                snmp_comm_sheet.set_column(i, i, width)
            snmp_comm_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            snmp_comm_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            snmp_comm_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The snmp-communities tab has completed successfully.')

        # Creating the snmp-summary tab:
        from get_intent_checks_data import snmp_config_blue,snmp_config_amber
        df = intent_to_df(intents['/tables/management/snmp/summary'])
        if len(df.columns) > 1 and (snmp_config_blue > 0 or snmp_config_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='snmp-summary')
            snmp_summary_sheet = writer.sheets['snmp-summary']
            for i, width in enumerate(get_col_widths(df)):
                snmp_summary_sheet.set_column(i, i, width)
            snmp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            snmp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            snmp_summary_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The snmp-summary tab has completed successfully.')

        # Creating the secure-ports-interfaces tab:
        from get_intent_checks_data import portsec_blue,portsec_amber
        df = intent_to_df(intents['/tables/security/secure-ports/interfaces'])
        if len(df.columns) > 1 and (portsec_blue > 0 or portsec_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='secure-ports-interfaces')
            secure_port_ints_sheet = writer.sheets['secure-ports-interfaces']
            for i, width in enumerate(get_col_widths(df)):
                secure_port_ints_sheet.set_column(i, i, width)
            secure_port_ints_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            secure_port_ints_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            secure_port_ints_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The secure-ports-interfaces tab has completed successfully.')

        # Creating the stacks-connections tab:
        from get_intent_checks_data import stack_blue,stack_amber
        df = intent_to_df(intents['/tables/platforms/stack/connections'])
        if len(df.columns) > 1 and (stack_blue > 0 or stack_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stacks-connections')
            stacks_con_sheet = writer.sheets['stacks-connections']
            for i, width in enumerate(get_col_widths(df)):
                stacks_con_sheet.set_column(i, i, width)
            stacks_con_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stacks_con_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stacks_con_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stacks-connections tab has completed successfully.')

        # Creating the stacks-members tab:
        from get_intent_checks_data import stack_uptime_blue,stack_uptime_amber,stack_uptime_red
        df = intent_to_df(intents['/tables/platforms/stack/members'])
        if len(df.columns) > 1 and (stack_uptime_blue > 0 or stack_uptime_amber > 0 or stack_uptime_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stacks-members')
            stacks_members_sheet = writer.sheets['stacks-members']
            for i, width in enumerate(get_col_widths(df)):
                stacks_members_sheet.set_column(i, i, width)
            stacks_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stacks_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stacks_members_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stacks-members tab has completed successfully.')

        # Creating the stp-bridges tab:
        from get_intent_checks_data import (old_stp_blue,old_stp_amber,old_stp_red,stp_pvst_disabled_blue,
                                            stp_pvst_disabled_amber)
        df = intent_to_df(intents['/tables/spanning-tree/bridges'])
        if len(df.columns) > 1 and (old_stp_blue > 0 or old_stp_amber > 0 or old_stp_red > 0 or
            stp_pvst_disabled_blue > 0 or stp_pvst_disabled_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-bridges')
            stp_bridges_sheet = writer.sheets['stp-bridges']
            for i, width in enumerate(get_col_widths(df)):
                stp_bridges_sheet.set_column(i, i, width)
            stp_bridges_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_bridges_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_bridges_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-bridges tab has completed successfully.')

        # Creating the stp-cdp-ports-mismatch tab:
        from get_intent_checks_data import stpcdp_nei_mismatch_amber
        df = intent_to_df(intents['/tables/spanning-tree/inconsistencies/stp-cdp-ports-mismatch'])
        if len(df.columns) > 1 and (stpcdp_nei_mismatch_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-cdp-ports-mismatch')
            stp_cdp_mismatch_sheet = writer.sheets['stp-cdp-ports-mismatch']
            for i, width in enumerate(get_col_widths(df)):
                stp_cdp_mismatch_sheet.set_column(i, i, width)
            stp_cdp_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_cdp_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_cdp_mismatch_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-cdp-ports-mismatch tab has completed successfully.')

        # Creating the stp-inconsistencies tab:
        from get_intent_checks_data import sw_no_stp_amber
        df = intent_to_df(intents['/tables/interfaces/inconsistencies/summary'])
        if len(df.columns) > 1 and sw_no_stp_amber > 0:
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-inconsistencies')
            stp_inconsistencies_sheet = writer.sheets['stp-inconsistencies']
            for i, width in enumerate(get_col_widths(df)):
                stp_inconsistencies_sheet.set_column(i, i, width)
            stp_inconsistencies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_inconsistencies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_inconsistencies_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-inconsistencies tab has completed successfully.')

        # Creating the stp-multiple-stp tab:
        from get_intent_checks_data import mult_stp_amber
        df = intent_to_df(intents['/tables/spanning-tree/inconsistencies/multiple-stp'])
        if len(df.columns) > 1 and (mult_stp_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-multiple-stp')
            multiple_stp_sheet = writer.sheets['stp-multiple-stp']
            multiple_stp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            multiple_stp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            multiple_stp_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-multiple-stp tab has completed successfully.')

        # Creating the stp-neighbors tab:
        from get_intent_checks_data import stp_loops_amber,stp_expected_blue
        df = intent_to_df(intents['/tables/spanning-tree/neighbors'])
        if len(df.columns) > 1 and (stp_loops_amber > 0 and stp_expected_blue):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-neighbors')
            stp_nei_sheet = writer.sheets['stp-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                stp_nei_sheet.set_column(i, i, width)
            stp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': "blue",
                                            'format': blue_color})

            stp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': "amber",
                                            'format': amber_color})

            stp_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-neighbors tab has completed successfully.')

        # Creating the stp-ports-multiple-neighbors tab:
        from get_intent_checks_data import stp_multiple_nei_amber
        df = intent_to_df(intents['/tables/spanning-tree/inconsistencies/ports-multiple-neighbors'])
        if len(df.columns) > 1 and (stp_multiple_nei_amber > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-ports-multiple-neighbors')
            stp_ports_mult_nei_sheet = writer.sheets['stp-ports-multiple-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                stp_ports_mult_nei_sheet.set_column(i, i, width)
            stp_ports_mult_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_ports_mult_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_ports_mult_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-ports-multiple-neighbors tab has completed successfully.')

        # Creating the stp-virtual-ports tab:
        from get_intent_checks_data import stp_virt_blue,stp_virt_amber,stp_virt_red
        df = intent_to_df(intents['/tables/spanning-tree/ports'])
        if len(df.columns) > 1 and (stp_virt_blue > 0 or stp_virt_amber > 0 or stp_virt_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-virtual-ports')
            stp_virt_sheet = writer.sheets['stp-virtual-ports']
            for i, width in enumerate(get_col_widths(df)):
                stp_virt_sheet.set_column(i, i, width)
            stp_virt_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_virt_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_virt_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-virtual-ports tab has completed successfully.')

        # Creating the stp-vlans tab:
        from get_intent_checks_data import vlan_status_blue,vlan_status_amber,vlan_names_blue
        df = intent_to_df(intents['/tables/vlan/device'])
        if len(df.columns) > 1 and (vlan_status_blue > 0 or vlan_status_amber > 0 or vlan_names_blue > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='stp-vlans')
            stp_vlans_sheet = writer.sheets['stp-vlans']
            for i, width in enumerate(get_col_widths(df)):
                stp_vlans_sheet.set_column(i, i, width)
            stp_vlans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            stp_vlans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            stp_vlans_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The stp-vlans tab has completed successfully.')

        # Creating the switchports tab:
        from get_intent_checks_data import edge_blue,edge_amber,edge_red
        df = intent_to_df(intents['/tables/interfaces/switchports'])
        if len(df.columns) > 1 and (edge_blue > 0 or edge_amber > 0 or edge_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='switchports')
            switchports_sheet = writer.sheets['switchports']
            for i, width in enumerate(get_col_widths(df)):
                switchports_sheet.set_column(i, i, width)
            switchports_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            switchports_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            switchports_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The switchport tab has completed successfully.')

        # Creating the telnet-access tab:
        from get_intent_checks_data import telnet_red
        df = intent_to_df(intents['/tables/security/enabled-telnet'])
        if len(df.columns) > 1 and (telnet_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='telnet-access')
            telnet_sheet = writer.sheets['telnet-access']
            for i, width in enumerate(get_col_widths(df)):
                telnet_sheet.set_column(i, i, width)
            telnet_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            telnet_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            telnet_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The telnet-access tab has completed successfully.')

        # Creating the transfer-rates-bidirectional tab:
        from get_intent_checks_data import transfer_rates_bi_blue,transfer_rates_bi_amber,transfer_rates_bi_red
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/bidirectional'])
        if len(df.columns) > 1 and (transfer_rates_bi_blue > 0 or transfer_rates_bi_amber > 0
                                    or transfer_rates_bi_red > 0 ):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-bidir')
            tr_rates_bidir_sheet = writer.sheets['transfer-rates-bidir']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_bidir_sheet.set_column(i, i, width)
            tr_rates_bidir_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_bidir_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_bidir_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-bidirectional tab has completed successfully.')

        # Creating the transfer-rates-bidirectional-device tab:
        from get_intent_checks_data import (transfer_rates_dev_bi_blue,transfer_rates_dev_bi_amber,
                                            transfer_rates_dev_bi_red)
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/bidirectional-device'])
        if len(df.columns) > 1 and (transfer_rates_dev_bi_blue > 0 or transfer_rates_dev_bi_amber > 0 or
                                    transfer_rates_dev_bi_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-bidir-device')
            tr_rates_bidir_dev_sheet = writer.sheets['transfer-rates-bidir-device']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_bidir_dev_sheet.set_column(i, i, width)
            tr_rates_bidir_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_bidir_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_bidir_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-bidirectional-device tab has completed successfully.')

        # # Creating the transfer-rates-inbound tab:
        from get_intent_checks_data import transfer_rates_in_blue,transfer_rates_in_amber,transfer_rates_in_red
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/inbound'])
        if len(df.columns) > 1 and (transfer_rates_in_blue > 0 or transfer_rates_in_amber > 0
                                            or transfer_rates_in_red > 0 ):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-inbound')
            tr_rates_in_sheet = writer.sheets['transfer-rates-inbound']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_in_sheet.set_column(i, i, width)
            tr_rates_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_in_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-inbound tab has completed successfully.')

        # Creating the transfer-rates-inbound-device tab:
        from get_intent_checks_data import (transfer_rates_dev_in_blue,transfer_rates_dev_in_amber,
                                            transfer_rates_dev_in_red)
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/inbound-device'])
        if len(df.columns) > 1 and (transfer_rates_dev_in_blue > 0 or transfer_rates_dev_in_amber > 0 or
                                    transfer_rates_dev_in_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-inbound-device')
            tr_rates_in_dev_sheet = writer.sheets['transfer-rates-inbound-device']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_in_dev_sheet.set_column(i, i, width)
            tr_rates_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_in_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-inbound-device tab has completed successfully.')

        # Creating the transfer-rates-outbound tab:
        from get_intent_checks_data import transfer_rates_out_blue,transfer_rates_out_amber,transfer_rates_out_red
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/outbound'])
        if len(df.columns) > 1 and (transfer_rates_out_blue > 0 or transfer_rates_out_amber > 0 or
                                    transfer_rates_out_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-outbound')
            tr_rates_out_sheet = writer.sheets['transfer-rates-outbound']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_out_sheet.set_column(i, i, width)
            tr_rates_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_out_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-outbound tab has completed successfully.')

        # Creating the transfer-rates-outbound-device tab:
        from get_intent_checks_data import (transfer_rates_dev_out_blue,transfer_rates_dev_out_amber,
                                            transfer_rates_dev_out_red)
        df = intent_to_df(intents['/tables/interfaces/transfer-rates/outbound-device'])
        if len(df.columns) > 1 and (transfer_rates_dev_out_blue > 0 or transfer_rates_dev_out_amber > 0 or
                                    transfer_rates_dev_out_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='transfer-rates-outbound-device')
            tr_rates_out_dev_sheet = writer.sheets['transfer-rates-outbound-device']
            for i, width in enumerate(get_col_widths(df)):
                tr_rates_out_dev_sheet.set_column(i, i, width)
            tr_rates_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            tr_rates_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            tr_rates_out_dev_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The transfer-rates-outbound-device tab has completed successfully.')

        # Creating the unidirectional-neighbors tab:
        from get_intent_checks_data import cdp_lldp_uni_blue
        df = intent_to_df(intents['/tables/neighbors/unidirectional'])
        if len(df.columns) > 1 and (cdp_lldp_uni_blue > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='unidirectional-neighbors')
            uni_nei_sheet = writer.sheets['unidirectional-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                uni_nei_sheet.set_column(i, i, width)
            uni_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            uni_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            uni_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The unidirectional-neighbors tab has completed successfully.')

        # Creating the unmanaged-neighbors tab:
        from get_intent_checks_data import un_nei_amber,un_nei_red
        df = intent_to_df(intents['/tables/interfaces/connectivity-matrix/unmanaged-neighbors/detail'])
        if len(df.columns) > 1 and (un_nei_amber > 0 or un_nei_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df.to_excel(writer, index=False, sheet_name='unmanaged-neighbors')
            un_nei_sheet = writer.sheets['unmanaged-neighbors']
            for i, width in enumerate(get_col_widths(df)):
                un_nei_sheet.set_column(i, i, width)
            un_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            un_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            un_nei_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The unmanaged-neighbors tab has completed successfully.')

        # Creating the wireless-clients tab:
        from get_intent_checks_data import rssi_blue,rssi_amber,rssi_red,snr_blue,snr_amber,snr_red
        df = intent_to_df(intents['/tables/wireless/clients'])
        if len(df.columns) > 1 and (rssi_blue > 0 or rssi_amber > 0 or rssi_red or snr_blue > 0 or
                                    snr_amber > 0 or snr_red > 0):
            df = df.dropna(how='all', axis='columns')
            if 'Unnamed: 0' in df:
                df = df.drop(['Unnamed: 0'], axis=1)
            df = df.replace('amber', 'amber')
            df.to_excel(writer, index=False, sheet_name='wireless-clients')
            wireless_cl_sheet = writer.sheets['wireless-clients']
            for i, width in enumerate(get_col_widths(df)):
                wireless_cl_sheet.set_column(i, i, width)
            wireless_cl_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "blue",
                                   'format': blue_color})

            wireless_cl_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                   'criteria': 'containing',
                                   'value': "amber",
                                   'format': amber_color})

            wireless_cl_sheet.conditional_format('A1:Z1000000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value': "red",
                                                'format': red_color})
            print('The wireless-clients tab has completed successfully.')

        print('The Automatic Checks Summary & Tabs have Completed Successfully')
        writer.save()