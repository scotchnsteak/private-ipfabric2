



import pandas as pd
from pathlib import Path
from auto_summary_dict import automatic_checks_dict
from central_control import BASE_URL, TOKEN


Path("../DOWNLOADS").mkdir(parents=True, exist_ok=True)

# Instantiate the writer and the workbook:
writer = pd.ExcelWriter('../DOWNLOADS/AUTOMATIC_CHECKS.xlsx', engine='xlsxwriter')
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

# Creating the aaa-accounting tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/aaa-accounting.csv", keep_default_na=False)
if len(df.columns) > 1 and ():
    df.to_excel(writer, index=False, sheet_name='aaa-accounting')
    print('The aaa-accounting tab has completed successfully.')

# Creating the aaa-authentication tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/aaa-authentication.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='aaa-authentication')
    print('The aaa-authentication tab has completed successfully.')

# Creating the aaa-authorization tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/aaa-authorization.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='aaa-authorization')
    print('The aaa-authorization tab has completed successfully.')

# Creating the aaa-lines tab:
from get_intent_checks_data import (aaa_authe_type_blue, aaa_authe_type_amber, aaa_authe_type_red)
df = pd.read_csv("../DOWNLOADS/cleaned-tables/aaa-lines.csv", keep_default_na=False)
if len(df.columns) > 1 and (aaa_authe_type_blue !=0 or aaa_authe_type_amber !=0 or
        aaa_authe_type_red !=0):
    df.to_excel(writer, index=False, sheet_name='aaa-lines')
    print('The aaa-lines tab has completed successfully.')

# Creating the access-points tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/access-points.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='access-points')
    print('The access-points tab has completed successfully.')

# Creating the active-gw-root-alignment tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/active-gw-root-alignment.csv", keep_default_na=False)
if len(df.columns) > 1:
    df = df.dropna(how='all', axis='columns')
    if 'Unnamed: 0' in df:
        df = df.drop(['Unnamed: 0'], axis=1)
    df.to_excel(writer, index=False, sheet_name='active-gw-root-alignment')
    print('The active-gw-root-alignment tab has completed successfully.')

# Creating the all-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/all-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df = df.dropna(how='all', axis='columns')
    df.to_excel(writer, index=False, sheet_name='all-neighbors')
    print('The all-neighbors tab has completed successfully.')

# Creating the arp-table tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/arp-table.csv", keep_default_na=False)
if len(df.columns) > 1:
    df = df.dropna(how='all', axis='columns')
    df.to_excel(writer, index=False, sheet_name='arp-table')
    print('The arp-table tab has completed successfully.')

# Creating the bgp-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/bgp-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df = df.dropna(how='all', axis='columns')
    df.to_excel(writer, index=False, sheet_name='bgp-neighbors')
    print('The bgp-neighbors tab has completed successfully.')

# from get_intent_checks_data import (confreg_green, confreg_amber, uptime_green, uptime_blue,
#                                     uptime_amber,uptime_red,memory_green,memory_blue,memory_amber,
#                                     memory_red,reload_red,reload_green,reload_amber,reload_blue)
#
# if (confreg_green or confreg_amber or uptime_green or uptime_blue or uptime_amber or uptime_red or
#         memory_green or memory_blue or memory_amber or memory_red or reload_green or reload_blue or
#         reload_amber or reload_red):

# Creating the devices tab:
df_devices = pd.read_csv("../DOWNLOADS/cleaned-tables/devices.csv", keep_default_na=False)
if len(df.columns) > 1:
    df_devices = df_devices.drop(['mac', 'icon', 'loginType', 'processor', 'rd', 'stpDomain',
                              ], axis=1)
    df_devices = df.dropna(how='all', axis='columns')
    df_devices.to_excel(writer, index=False, sheet_name='devices')
    print('The devices tab has completed successfully.')

# Creating the dhcp-bindings tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/dhcp-bindings.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='dhcp-bindings')
    print('The dhcp-bindings tab has completed successfully.')

# Creating the dhcp-snooping tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/dhcp-snooping.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='dhcp-snooping')
    print('The dhcp-snooping tab has completed successfully.')

# Creating the dmvpn tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/dmvpn.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='dmvpn')
    print('The dmvpn tab has completed successfully.')

# Creating the drops-bidirectional tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-bidirectional.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-bidirectional')
    print('The drops-bidirectional tab has completed successfully.')

# Creating the drops-bidirectional-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-bidirectional-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-bidirectional-device')
    print('The drops-bidirectional-device tab has completed successfully.')

# Creating the drops-inbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-inbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-inbound')
    print('The drops-inbound tab has completed successfully.')

# Creating the drops-inbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-inbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-inbound-device')
    print('The drops-inbound-device tab has completed successfully.')

# Creating the drops-outbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-outbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-outbound')
    print('The drops-outbound tab has completed successfully.')

# Creating the drops-outbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/drops-outbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='drops-outbound-device')
    print('The drops-outbound-device tab has completed successfully.')

# Creating the duplicate-ip tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/duplicate-ip.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='duplicate-ip')
    print('The duplicate-ip tab has completed successfully.')

# Creating the eigrp-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/eigrp-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='eigrp-interfaces')
    print('The eigrp-interfaces tab has completed successfully.')

# Creating the eigrp-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/eigrp-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='eigrp-neighbors')
    print('The eigrp-neighbors tab has completed successfully.')

# Creating the errdisabled tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errdisabled.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errdisabled')
    print('The errdisabled tab has completed successfully.')

# Creating the errors-bidirectional tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-bidirectional.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-bidirectional')
    print('The errors-bidirectional tab has completed successfully.')

# Creating the errors-bidirectional-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-bidirectional-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-bidirectional-device')
    print('The errors-bidirectional-device tab has completed successfully.')

# Creating the errors-inbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-inbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-inbound')
    print('The errors-inbound tab has completed successfully.')

# Creating the errors-inbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-inbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-inbound-device')
    print('The errors-inbound-device tab has completed successfully.')

# Creating the errors-outbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-outbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-outbound')
    print('The errors-outbound tab has completed successfully.')

# Creating the errors-outbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/errors-outbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='errors-outbound-device')
    print('The errors-outbound-device tab has completed successfully.')

# # Creating the end-of-life  tab:
# df = pd.read_csv("DOWNLOADS/cleaned-tables/end-of-life.csv", keep_default_na=False)
# df.to_excel(writer, index=False, sheet_name='end-of-life')
# print('The end-of-life tab has completed successfully.')

# Creating the fans tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/fans.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='fans ')
    print('The fans  tab has completed successfully.')

# Creating the gateway-redundancy tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/gateway-redundancy.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='gateway-redundancy')
    print('The gateway-redundancy tab has completed successfully.')

# Creating the group-members tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/group-members.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='group-members')
    print('The group-members tab has completed successfully.')

# Creating the group-state tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/group-state.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='group-state')
    print('The group-state tab has completed successfully.')

# Creating the hosts tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/hosts.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='hosts')
    print('The hosts tab has completed successfully.')

# Creating the inbound-balancing-table tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/inbound-balancing-table.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='inbound-balancing-table')
    print('The inbound-balancing-table tab has completed successfully.')

# Creating the interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='interfaces')
    print('The interfaces tab has completed successfully.')

# Creating the ipsec-gateways tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ipsec-gateways.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ipsec-gateways')
    print('The ipsec-gateways tab has completed successfully.')

# Creating the ipsec-tunnels tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ipsec-tunnels.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ipsec-tunnels')
    print('The ipsec-tunnels tab has completed successfully.')

# Creating the is-is-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/is-is-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='is-is-interfaces')
    print('The is-is-interfaces tab has completed successfully.')

# Creating the is-is-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/is-is-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='is-is-neighbors')
    print('The is-is-neighbors tab has completed successfully.')

# Creating the juniper-cluster-srx tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/juniper-cluster-srx.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='juniper-cluster-srx')
    print('The juniper-cluster-srx tab has completed successfully.')

# Creating the ldp-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ldp-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ldp-interfaces')
    print('The ldp-interfaces tab has completed successfully.')

# Creating the ldp-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ldp-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ldp-neighbors')
    print('The ldp-neighbors tab has completed successfully.')

# Creating the logging-local tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/logging-local.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='logging-local')
    print('The logging-local tab has completed successfully.')

# Creating the logging-remote tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/logging-remote.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='logging-remote')
    print('The logging-remote tab has completed successfully.')

# Creating the logging-summary tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/logging-summary.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='logging-summary')
    print('The logging-summary tab has completed successfully.')

# Creating the l2vpn-circuit-cross-connect tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/l2vpn-circuit-cross-connect.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='l2vpn-circuit-cross-connect')
    print('The l2vpn-circuit-cross-connect tab has completed successfully.')

# Creating the l2vpn-point-to-multipoint tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/l2vpn-point-to-multipoint.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='l2vpn-point-to-multipoint')
    print('The l2vpn-point-to-multipoint tab has completed successfully.')

# Creating the l2vpn-point-to-point-vpws tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/l2vpn-point-to-point-vpws.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='l2vpn-point-to-point-vpws')
    print('The l2vpn-point-to-point-vpws tab has completed successfully.')

# Creating the neighbor-ports-vlan-mismatch tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/neighbor-ports-vlan-mismatch.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='neighbor-ports-vlan-mismatch')
    print('The neighbor-ports-vlan-mismatch tab has completed successfully.')

# Creating the ntp-sources tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ntp-sources.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ntp-sources')
    print('The ntp-sources tab has completed successfully.')

# Creating the ntp-summary tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ntp-summary.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ntp-summary')
    print('The ntp-summary tab has completed successfully.')

# Creating the mac-table tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mac-table.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mac-table')
    print('The mac-table tab has completed successfully.')

# Creating the managed-ip tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/managed-ip.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='managed-ip')
    print('The managed-ip tab has completed successfully.')

# Creating the member-status-table tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/member-status-table.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='member-status-table')
    print('The member-status-table tab has completed successfully.')

# Creating the mlag-pairs tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mlag-pairs.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mlag-pairs')
    print('The mlag-pairs tab has completed successfully.')

# Creating the mlag-peer-links tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mlag-peer-links.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mlag-peer-links')
    print('The mlag-peer-links tab has completed successfully.')

# Creating the mlag-vpc tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mlag-vpc.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mlag-vpc')
    print('The mlag-vpc tab has completed successfully.')

# Creating the mroute-counters tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mroute-counters.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mroute-counters')
    print('The mroute-counters tab has completed successfully.')

# Creating the mtu tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/mtu.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='mtu')
    print('The mtu tab has completed successfully.')

# Creating the os-versions tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/os-versions.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='os-versions')
    print('The os-versions tab has completed successfully.')

# Creating the ospf-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ospf-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ospf-interfaces')
    print('The ospf-interfaces tab has completed successfully.')

# Creating the ospf-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ospf-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ospf-neighbors')
    print('The ospf-neighbors tab has completed successfully.')

# Creating the ospf-v3-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ospf-v3-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ospf-v3-interfaces')
    print('The ospf-v3-interfaces tab has completed successfully.')

# Creating the ospf-v3-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/ospf-v3-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='ospf-v3-neighbors')
    print('The ospf-v3-neighbors tab has completed successfully.')

# Creating the outbound-balancing-table tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/outbound-balancing-table.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='outbound-balancing-table')
    print('The outbound-balancing-table tab has completed successfully.')

# Creating the part-numbers tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/part-numbers.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='part-numbers')
    print('The part-numbers tab has completed successfully.')

# Creating the path-verifications tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/path-verifications.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='path-verifications')
    print('The path-verifications tab has completed successfully.')

# Creating the phones tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/phones.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='phones')
    print('The phones tab has completed successfully.')

# Creating the pim-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/pim-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='pim-interfaces')
    print('The pim-interfaces tab has completed successfully.')

# Creating the pim-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/pim-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='pim-neighbors')
    print('The pim-neighbors tab has completed successfully.')

# Creating the poe-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/poe-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='poe-interfaces')
    print('The poe-interfaces tab has completed successfully.')

# Creating the poe-modules tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/poe-modules.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='poe-modules')
    print('The poe-modules tab has completed successfully.')

# Creating the policy-map tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/policy-map.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='policy-map')
    print('The policy-map tab has completed successfully.')

# Creating the power-supplies tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/power-supplies.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='power-supplies')
    print('The power-supplies tab has completed successfully.')

# Creating the power-supplies-fans tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/power-supplies-fans.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='power-supplies-fans')
    print('The power-supplies-fans tab has completed successfully.')

# Creating the priority-queuing tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/priority-queuing.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='priority-queuing')
    print('The priority-queuing tab has completed successfully.')

# Creating the pseudowires tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/pseudowires.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='pseudowires')
    print('The pseudowires tab has completed successfully.')

# Creating the queuing tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/queuing.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='queuing')
    print('The queuing tab has completed successfully.')

# Creating the random-drops tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/random-drops.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='random-drops')
    print('The random-drops tab has completed successfully.')

# Creating the rip-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/rip-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='rip-interfaces')
    print('The rip-interfaces tab has completed successfully.')

# Creating the route-stability tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/route-stability.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='route-stability')
    print('The route-stability tab has completed successfully.')

# Creating the saved-config-consistency tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/saved-config-consistency.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='saved-config-consistency')
    print('The saved-config-consistency tab has completed successfully.')

# Creating the sdwan-sites tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/sdwan-sites.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='sdwan-sites')
    print('The sdwan-sites tab has completed successfully.')

# Creating the shaping tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/shaping.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='shaping')
    print('The shaping tab has completed successfully.')

# Creating the snmp-communities tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/snmp-communities.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='snmp-communities')
    print('The snmp-communities tab has completed successfully.')

# Creating the snmp-summary tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/snmp-summary.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='snmp-summary')
    print('The snmp-summary tab has completed successfully.')

# Creating the secure-ports-interfaces tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/secure-ports-interfaces.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='secure-ports-interfaces')
    print('The secure-ports-interfaces tab has completed successfully.')

# Creating the stacks-connections tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stacks-connections.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stacks-connections')
    print('The stacks-connections tab has completed successfully.')

# Creating the stacks-members tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stacks-members.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stacks-members')
    print('The stacks-members tab has completed successfully.')

# Creating the stp-bridges tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-bridges.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-bridges')
    print('The stp-bridges tab has completed successfully.')

# Creating the stp-cdp-ports-mismatch tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-cdp-ports-mismatch.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-cdp-ports-mismatch')
    print('The stp-cdp-ports-mismatch tab has completed successfully.')

# Creating the stp-inconsistencies tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-inconsistencies.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-inconsistencies')
    print('The stp-inconsistencies tab has completed successfully.')

# Creating the stp-multiple-stp tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-multiple-stp.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-multiple-stp')
    print('The stp-multiple-stp tab has completed successfully.')

# Creating the stp-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-neighbors')
    print('The stp-neighbors tab has completed successfully.')

# Creating the stp-ports-multiple-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-ports-multiple-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-ports-multiple-neighbors')
    print('The stp-ports-multiple-neighbors tab has completed successfully.')

# Creating the stp-virtual-ports tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-virtual-ports.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-virtual-ports')
    print('The stp-virtual-ports tab has completed successfully.')

# Creating the stp-vlans tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/stp-vlans.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='stp-vlans')
    print('The stp-vlans tab has completed successfully.')

# Creating the switchport tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/switchports.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='switchports')
    print('The switchport tab has completed successfully.')

# Creating the telnet-access tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/telnet-access.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='telnet-access')
    print('The telnet-access tab has completed successfully.')

# Creating the transfer-rates-bidirectional tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-bidirectional.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-bidir')
    print('The transfer-rates-bidirectional tab has completed successfully.')

# Creating the transfer-rates-bidirectional-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-bidirectional-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-bidir-device')
    print('The transfer-rates-bidirectional-device tab has completed successfully.')

# Creating the transfer-rates-inbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-inbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-inbound')
    print('The transfer-rates-inbound tab has completed successfully.')

# Creating the transfer-rates-inbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-inbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-inbound-device')
    print('The transfer-rates-inbound-device tab has completed successfully.')

# Creating the transfer-rates-outbound tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-outbound.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-outbound')
    print('The transfer-rates-outbound tab has completed successfully.')

# Creating the transfer-rates-outbound-device tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/transfer-rates-outbound-device.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='transfer-rates-outbound-device')
    print('The transfer-rates-outbound-device tab has completed successfully.')

# Creating the unidirectional-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/unidirectional-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='unidirectional-neighbors')
    print('The unidirectional-neighbors tab has completed successfully.')

# Creating the unmanaged-neighbors tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/unmanaged-neighbors.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='unmanaged-neighbors')
    print('The unmanaged-neighbors tab has completed successfully.')

# Creating the wireless-clients tab:
df = pd.read_csv("../DOWNLOADS/cleaned-tables/wireless-clients.csv", keep_default_na=False)
if len(df.columns) > 1:
    df.to_excel(writer, index=False, sheet_name='wireless-clients')
    print('The wireless-clients tab has completed successfully.')

print('The Automatic Checks Summary Completed Successfully')
writer.save()