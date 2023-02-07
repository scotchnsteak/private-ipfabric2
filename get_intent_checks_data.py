from ipfabric import IPFClient
import os

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")


ipf = IPFClient(BASE_URL, token=TOKEN, verify=False, timeout=30)
ipf.intent.load_intent()  # Load Intent Checks

# Software Configuration Register
confreg = ipf.intent.intent_by_name["Software Configuration Register"]
confreg_green = confreg.result.checks.green
confreg_amber = confreg.result.checks.amber

# Total number of SFP Modules:
sfp = ipf.intent.intent_by_name["SFP Modules (total)"]
sfp_green = sfp.result.checks.green

# End-of-Sale Details:
eos = ipf.intent.intent_by_name["End of Sale Detail"]
eos_green = eos.result.checks.green
eos_blue = eos.result.checks.red

# End-of-Maintenance Detail:
eom = ipf.intent.intent_by_name["End of Maintenance Detail"]
eom_green = eom.result.checks.green
eom_amber = eom.result.checks.amber

# End-of-Support Detail:
eosup = ipf.intent.intent_by_name["End of Support Detail"]
eosup_green = eosup.result.checks.green
eosup_red = eosup.result.checks.red

# End of Sale:
sale = ipf.intent.intent_by_name["End of Sale"]
sale_green = sale.result.checks.green
sale_blue = sale.result.checks.red

# End of Maintenance:
maintenance = ipf.intent.intent_by_name["End of Maintenance"]
maintenance_green = maintenance.result.checks.green
maintenance_amber = maintenance.result.checks.amber

# End of Support:
support = ipf.intent.intent_by_name['End of Support']
support_green = support.result.checks.green
support_red = support.result.checks.red

# Device Reload Reason:
reload = ipf.intent.intent_by_name["Device Reload Reason"]
reload_green = reload.result.checks.green
reload_blue = reload.result.checks.blue
reload_amber = reload.result.checks.amber
reload_red = reload.result.checks.red

# Device Memory Usage (%):
memory = ipf.intent.intent_by_name["Device Memory Usage (%)"]
memory_green = memory.result.checks.green
memory_blue = memory.result.checks.blue
memory_amber = memory.result.checks.amber
memory_red = memory.result.checks.red

# Device Uptime:
uptime = ipf.intent.intent_by_name["Device Uptime"]
uptime_green = uptime.result.checks.green
uptime_blue = uptime.result.checks.blue
uptime_amber = uptime.result.checks.amber
uptime_red = uptime.result.checks.red

# Interfaces:======================================================

# Interface Operational State:
operate = ipf.intent.intent_by_name["Interface Operational State"]
operate_green = operate.result.checks.green
operate_blue = operate.result.checks.blue

# Interface Duplex:
duplex = ipf.intent.intent_by_name["Interface Duplex"]
duplex_blue = duplex.result.checks.blue
duplex_amber = duplex.result.checks.amber

# Maximum Transmission Unit (MTU):
mtu = ipf.intent.intent_by_name["Maximum Transmission Unit (MTU)"]
mtu_green = mtu.result.checks.green
mtu_blue = mtu.result.checks.blue
mtu_amber = mtu.result.checks.amber

# Error-Disabled Interfaces (total):
err = ipf.intent.intent_by_name["Error-Disabled Interfaces (total)"]
err_amber = err.result.checks.amber

# Switched Port Analyzer (SPAN) ports (total):
span = ipf.intent.intent_by_name["Switched Port Analyzer (SPAN) ports (total))"]
span_green = span.result.checks.green

# Edge-Ports with Multiple Neighbors:
edge = ipf.intent.intent_by_name["Edge-Ports with Multiple Neighbors"]
edge_green = edge.result.checks.green
edge_blue = edge.result.checks.blue
edge_amber = edge.result.checks.amber
edge_red = edge.result.checks.red

# Juniper Cluster Link Status:
juniper = ipf.intent.intent_by_name['Juniper Cluster Link Status']
juniper_green = juniper.result.checks.green
juniper_amber = juniper.result.checks.amber

# Edge Port Security:
portsec = ipf.intent.intent_by_name['Edge Port Security']
portsec_green = portsec.result.checks.green
portsec_blue = portsec.result.checks.blue
portsec_amber = portsec.result.checks.amber

# Paired Devices With Different Configs:
pcdiff = ipf.intent.intent_by_name['Paired Devices With Different Configs']
pcdiff_green = pcdiff.result.checks.green
pcdiff_red = pcdiff.result.checks.red

# MLAG Pairs Status:
mlag = ipf.intent.intent_by_name['MLAG Pairs Status']
mlag_green = mlag.result.checks.green
mlag_amber = mlag.result.checks.amber
mlag_red = mlag.result.checks.red

# # vPC Global and Interface Setting Consistency:
# vpcon = ipf.intent.intent_by_name['vPC Global and Interface Setting Inconsistency']
# vpcon_green = vpcon.result.checks.green
# vpcon_red = vpcon.result.checks.red

# vPC Peer Link:
vpcpl = ipf.intent.intent_by_name['Peer Link']
vpcpl_green = vpcpl.result.checks.green
vpcpl_red = vpcpl.result.checks.red

# Cisco VPC Status:
vpcst = ipf.intent.intent_by_name['Cisco VPC Status']
vpcst_green = vpcst.result.checks.green
vpcst_blue = vpcst.result.checks.blue
vpcst_red = vpcst.result.checks.red

# ENDPOINTS: ====================================================================

# Endpoints Resolution:
endpres = ipf.intent.intent_by_name['Endpoints Resolution']
endpres_green = endpres.result.checks.green
endpres_blue = endpres.result.checks.blue

# IP Phone - Connected MACs:
phonemacs = ipf.intent.intent_by_name['IP Phone - Connected MACs']
phonemacs_green = phonemacs.result.checks.green
phonemacs_amber = phonemacs.result.checks.amber

# PERFORMANCE: =================================================================

# Transfer Rates (inbound):
transfer_rates_in = ipf.intent.intent_by_name['Transfer Rates (inbound)']
transfer_rates_in_green = transfer_rates_in.result.checks.green
transfer_rates_in_blue = transfer_rates_in.result.checks.blue
transfer_rates_in_amber = transfer_rates_in.result.checks.amber
transfer_rates_in_red = transfer_rates_in.result.checks.red

# Transfer Rates (outbound):
transfer_rates_out = ipf.intent.intent_by_name['Transfer Rates (outbound)']
transfer_rates_out_green = transfer_rates_out.result.checks.green
transfer_rates_out_blue = transfer_rates_out.result.checks.blue
transfer_rates_out_amber = transfer_rates_out.result.checks.amber
transfer_rates_out_red = transfer_rates_out.result.checks.red

# Transfer Rates (bidirectional):
transfer_rates_bi = ipf.intent.intent_by_name['Transfer Rates (bidirectional)']
transfer_rates_bi_green = transfer_rates_bi.result.checks.green
transfer_rates_bi_blue = transfer_rates_bi.result.checks.blue
transfer_rates_bi_amber = transfer_rates_bi.result.checks.amber
transfer_rates_bi_red = transfer_rates_bi.result.checks.red

# Transfer Rates (device-inbound):
transfer_rates_dev_in = ipf.intent.intent_by_name['Transfer Rates (device-inbound)']
transfer_rates_dev_in_green = transfer_rates_dev_in.result.checks.green
transfer_rates_dev_in_blue = transfer_rates_dev_in.result.checks.blue
transfer_rates_dev_in_amber = transfer_rates_dev_in.result.checks.amber
transfer_rates_dev_in_red = transfer_rates_dev_in.result.checks.red

# Transfer Rates (device-outbound):
transfer_rates_dev_out = ipf.intent.intent_by_name['Transfer Rates (device-outbound)']
transfer_rates_dev_out_green = transfer_rates_dev_out.result.checks.green
transfer_rates_dev_out_blue = transfer_rates_dev_out.result.checks.blue
transfer_rates_dev_out_amber = transfer_rates_dev_out.result.checks.amber
transfer_rates_dev_out_red = transfer_rates_dev_out.result.checks.red

# Transfer Rates (device-bidirectional):
transfer_rates_dev_bi = ipf.intent.intent_by_name['Transfer Rates (device-bidirectional)']
transfer_rates_dev_bi_green = transfer_rates_dev_bi.result.checks.green
transfer_rates_dev_bi_blue = transfer_rates_dev_bi.result.checks.blue
transfer_rates_dev_bi_amber = transfer_rates_dev_bi.result.checks.amber
transfer_rates_dev_bi_red = transfer_rates_dev_bi.result.checks.red

# Input errors impact:
input_errors = ipf.intent.intent_by_name['Input errors impact']
input_errors_green = input_errors.result.checks.green
input_errors_blue = input_errors.result.checks.blue
input_errors_amber = input_errors.result.checks.amber
input_errors_red = input_errors.result.checks.red

# Output errors impact:
output_errors = ipf.intent.intent_by_name['Output errors impact']
output_errors_green = output_errors.result.checks.green
output_errors_blue = output_errors.result.checks.blue
output_errors_amber = output_errors.result.checks.amber
output_errors_red = output_errors.result.checks.red

# Error Rates (bidirectional):
error_rates_bi = ipf.intent.intent_by_name['Error Rates (bidirectional)']
error_rates_bi_green = error_rates_bi.result.checks.green
error_rates_bi_blue = error_rates_bi.result.checks.blue
error_rates_bi_amber = error_rates_bi.result.checks.amber
error_rates_bi_red = error_rates_bi.result.checks.red

# Device input errors impact:
dev_in_errors = ipf.intent.intent_by_name['Device input errors impact']
dev_in_errors_green = dev_in_errors.result.checks.green
dev_in_errors_blue = dev_in_errors.result.checks.blue
dev_in_errors_amber = dev_in_errors.result.checks.amber
dev_in_errors_red = dev_in_errors.result.checks.red

# Device output errors impact:
dev_out_errors = ipf.intent.intent_by_name['Device output errors impact']
dev_out_errors_green = dev_out_errors.result.checks.green
dev_out_errors_blue = dev_out_errors.result.checks.blue
dev_out_errors_amber = dev_out_errors.result.checks.amber
dev_out_errors_red = dev_out_errors.result.checks.red

# Error Rates (device-bidirectional):
dev_bi_errors = ipf.intent.intent_by_name['Error Rates (device-bidirectional)']
dev_bi_errors_green = dev_bi_errors.result.checks.green
dev_bi_errors_blue = dev_bi_errors.result.checks.blue
dev_bi_errors_amber = dev_bi_errors.result.checks.amber
dev_bi_errors_red = dev_bi_errors.result.checks.red

# Input drops impact:
input_drops = ipf.intent.intent_by_name['Input drops impact']
input_drops_green = input_drops.result.checks.green
input_drops_blue = input_drops.result.checks.blue
input_drops_amber = input_drops.result.checks.amber
input_drops_red = input_drops.result.checks.red

# Output drops impact:
output_drops = ipf.intent.intent_by_name['Output drops impact']
output_drops_green = output_drops.result.checks.green
output_drops_blue = output_drops.result.checks.blue
output_drops_amber = output_drops.result.checks.amber
output_drops_red = output_drops.result.checks.red

# Drop Rates (bidirectional):
drop_rates_bi = ipf.intent.intent_by_name['Drop Rates (bidirectional)']
drop_rates_bi_green = drop_rates_bi.result.checks.green
drop_rates_bi_blue = drop_rates_bi.result.checks.blue
drop_rates_bi_amber = drop_rates_bi.result.checks.amber
drop_rates_bi_red = drop_rates_bi.result.checks.red

# Device input drops impact:
dev_in_drops = ipf.intent.intent_by_name['Device input drops impact']
dev_in_drops_green = dev_in_drops.result.checks.green
dev_in_drops_blue = dev_in_drops.result.checks.blue
dev_in_drops_amber = dev_in_drops.result.checks.amber
dev_in_drops_red = dev_in_drops.result.checks.red

# Device output drops impact:
dev_out_drops = ipf.intent.intent_by_name['Device output drops impact']
dev_out_drops_green = dev_out_drops.result.checks.green
dev_out_drops_blue = dev_out_drops.result.checks.blue
dev_out_drops_amber = dev_out_drops.result.checks.amber
dev_out_drops_red = dev_out_drops.result.checks.red

# Drop Rates (device-bidirectional):
drop_rates_dev_bi = ipf.intent.intent_by_name['Drop Rates (device-bidirectional)']
drop_rates_dev_bi_green = drop_rates_dev_bi.result.checks.green
drop_rates_dev_bi_blue = drop_rates_dev_bi.result.checks.blue
drop_rates_dev_bi_amber = drop_rates_dev_bi.result.checks.amber
drop_rates_dev_bi_red = drop_rates_dev_bi.result.checks.red

# Access Point - Radio Signal Impact:
acc_pt_radio_signal = ipf.intent.intent_by_name['Access Point - Radio Signal Impact']
acc_pt_radio_signal_green = acc_pt_radio_signal.result.checks.green
acc_pt_radio_signal_blue = acc_pt_radio_signal.result.checks.blue
acc_pt_radio_signal_amber = acc_pt_radio_signal.result.checks.amber
acc_pt_radio_signal_red = acc_pt_radio_signal.result.checks.red

# Access Point - Connected Clients:
acc_pt_con = ipf.intent.intent_by_name['Access Point - Connected Clients']
acc_pt_con_green = acc_pt_con.result.checks.green
acc_pt_con_blue = acc_pt_con.result.checks.blue
acc_pt_con_amber = acc_pt_con.result.checks.amber
acc_pt_con_red = acc_pt_con.result.checks.red

# Wireless Client - RSSI:
rssi = ipf.intent.intent_by_name['Wireless Client - RSSI']
rssi_green = rssi.result.checks.green
rssi_blue = rssi.result.checks.blue
rssi_amber = rssi.result.checks.amber
rssi_red = rssi.result.checks.red

# QoS EF Class Drops:
qos_ef = ipf.intent.intent_by_name['QoS EF Class Drops']
qos_ef_green = qos_ef.result.checks.green
qos_ef_amber = qos_ef.result.checks.amber

# Wireless Client - SNR:
snr = ipf.intent.intent_by_name['Wireless Client - SNR']
snr_green = snr.result.checks.green
snr_blue = snr.result.checks.blue
snr_amber = snr.result.checks.amber
snr_red = snr.result.checks.red

# End-to-End Path Flooding:
path_flooding = ipf.intent.intent_by_name['End-to-End Path Flooding']
path_flooding_green = path_flooding.result.checks.green
path_flooding_amber = path_flooding.result.checks.amber

# End-to-End Path Verification:
path_verify = ipf.intent.intent_by_name['End-to-End Path Verification']
path_verify_green = path_verify.result.checks.green
path_verify_amber = path_verify.result.checks.amber
path_verify_red = path_verify.result.checks.red

# Port-Channel Output Balancing Vairance:
pc_out_var = ipf.intent.intent_by_name['Port-Channel Output Balancing Variance']
pc_out_var_green = pc_out_var.result.checks.green
pc_out_var_blue = pc_out_var.result.checks.blue
pc_out_var_amber = pc_out_var.result.checks.amber
pc_out_var_red = pc_out_var.result.checks.red

# Port-Channel Input Balancing Variance:
pc_in_var = ipf.intent.intent_by_name['Port-Channel Input Balancing Variance']
pc_in_var_green = pc_in_var.result.checks.green
pc_in_var_blue = pc_in_var.result.checks.blue
pc_in_var_amber = pc_in_var.result.checks.amber
pc_in_var_red = pc_in_var.result.checks.red

# MRoute RPF Errors:
mroute_rpf = ipf.intent.intent_by_name['MRoute RPF Errors']
mroute_rpf_green = mroute_rpf.result.checks.green
mroute_rpf_amber = mroute_rpf.result.checks.amber

# Access Point - Signal-to-Noise Ratio (SNR):
ap_snr = ipf.intent.intent_by_name['Access Point - Signal-to-Noise Ratio (SNR)']
ap_snr_green = ap_snr.result.checks.green
ap_snr_blue = ap_snr.result.checks.blue
ap_snr_amber = ap_snr.result.checks.amber
ap_snr_red = ap_snr.result.checks.red

# MRoute Other Errors:
mroute_other = ipf.intent.intent_by_name['MRoute Other Errors']
mroute_other_green = mroute_other.result.checks.green
mroute_other_amber = mroute_other.result.checks.amber

# Environment: ===================================================================

# Power-Supply State:
pwr_state = ipf.intent.intent_by_name['Power-Supply State']
pwr_state_green = pwr_state.result.checks.green
pwr_state_blue = pwr_state.result.checks.blue
pwr_state_red = pwr_state.result.checks.red

# Power-Supply Fan State:
pwr_fan = ipf.intent.intent_by_name['Power-Supply Fan State']
pwr_fan_green = pwr_fan.result.checks.green
pwr_fan_blue = pwr_fan.result.checks.blue
pwr_fan_red = pwr_fan.result.checks.red

# Module State:
mod_state = ipf.intent.intent_by_name['Module State']
mod_state_green = mod_state.result.checks.green
mod_state_blue = mod_state.result.checks.blue
mod_state_red = mod_state.result.checks.red

# PoE Interface State:
poe_state = ipf.intent.intent_by_name['PoE Interface State']
poe_state_green = poe_state.result.checks.green
poe_state_blue = poe_state.result.checks.blue
poe_state_amber = poe_state.result.checks.amber

# Stack Port State:
stack = ipf.intent.intent_by_name['Stack Port State']
stack_green = stack.result.checks.green
stack_blue = stack.result.checks.blue
stack_amber = stack.result.checks.amber

# PoE Module Watts Used (%):
poe_watts = ipf.intent.intent_by_name['PoE Module Watts Used (%)']
poe_watts_green = poe_watts.result.checks.green
poe_watts_blue = poe_watts.result.checks.blue
poe_watts_amber = poe_watts.result.checks.amber
poe_watts_red = poe_watts.result.checks.red

# Fan Module State:
fan = ipf.intent.intent_by_name['Fan Module State']
fan_green = fan.result.checks.green
fan_blue = fan.result.checks.blue
fan_red = fan.result.checks.red

# STABILITY: ===================================================================

# OSPF Session Age:
ospf_age = ipf.intent.intent_by_name['OSPF Session Age']
ospf_age_green = ospf_age.result.checks.green
ospf_age_blue = ospf_age.result.checks.blue
ospf_age_amber = ospf_age.result.checks.amber
ospf_age_red = ospf_age.result.checks.red

# OSPFv3 Session Age:
ospfv3_age = ipf.intent.intent_by_name['OSPFv3 Session Age']
ospfv3_age_green = ospfv3_age.result.checks.green
ospfv3_age_blue = ospfv3_age.result.checks.blue
ospfv3_age_amber = ospfv3_age.result.checks.amber
ospfv3_age_red = ospfv3_age.result.checks.red

# EIGRP Session Age:
eigrp_age = ipf.intent.intent_by_name['EIGRP Session Age']
eigrp_age_green = eigrp_age.result.checks.green
eigrp_age_blue = eigrp_age.result.checks.blue
eigrp_age_amber = eigrp_age.result.checks.amber
eigrp_age_red = eigrp_age.result.checks.red

# IS-IS Session Age:
isis_age = ipf.intent.intent_by_name['IS-IS Session Age']
isis_age_green = isis_age.result.checks.green
isis_age_blue = isis_age.result.checks.blue
isis_age_amber = isis_age.result.checks.amber
isis_age_red = isis_age.result.checks.red

# BGP Session Age:
bgp_age = ipf.intent.intent_by_name['BGP Session Age']
bgp_age_green = bgp_age.result.checks.green
bgp_age_blue = bgp_age.result.checks.blue
bgp_age_amber = bgp_age.result.checks.amber
bgp_age_red = bgp_age.result.checks.red

# LDP Session Age:
ldp_age = ipf.intent.intent_by_name['LDP Session Age']
ldp_age_green = ldp_age.result.checks.green
ldp_age_blue = ldp_age.result.checks.blue
ldp_age_amber = ldp_age.result.checks.amber
ldp_age_red = ldp_age.result.checks.red

# PIM Session Age:
pim_age = ipf.intent.intent_by_name['PIM Session Age']
pim_age_green = pim_age.result.checks.green
pim_age_blue = pim_age.result.checks.blue
pim_age_amber = pim_age.result.checks.amber
pim_age_red = pim_age.result.checks.red

# # Device Reload Reason:
# reload = ipf.intent.intent_by_name["Device Reload Reason"]
# reload_green = reload.result.checks.green
# reload_blue = reload.result.checks.blue
# reload_amber = reload.result.checks.amber
# reload_red = reload.result.checks.red

# DMVPN Tunnel State:
dmvpn = ipf.intent.intent_by_name['DMVPN Tunnel State']
dmvpn_green = dmvpn.result.checks.green
dmvpn_amber = dmvpn.result.checks.amber

# # Device Uptime:
# uptime = ipf.intent.intent_by_name["Device Uptime"]
# uptime_green = uptime.result.checks.green
# uptime_blue = uptime.result.checks.blue
# uptime_amber = uptime.result.checks.amber
# uptime_red = uptime.result.checks.red

# Recent Route Convergence:
recent = ipf.intent.intent_by_name['Recent Route Convergence']
recent_green = recent.result.checks.green
recent_blue = recent.result.checks.blue
recent_amber = recent.result.checks.amber
recent_red = recent.result.checks.red

# Stack Members Uptime:
stack_uptime = ipf.intent.intent_by_name['Stack Members Uptime']
stack_uptime_green = stack_uptime.result.checks.green
stack_uptime_blue = stack_uptime.result.checks.blue
stack_uptime_amber = stack_uptime.result.checks.amber
stack_uptime_red = stack_uptime.result.checks.red

# SDWAN Sites Uptime:
sdwan_uptime = ipf.intent.intent_by_name['SDWAN Sites Uptime']
sdwan_uptime_green = sdwan_uptime.result.checks.green
sdwan_uptime_blue = sdwan_uptime.result.checks.blue
sdwan_uptime_amber = sdwan_uptime.result.checks.amber
sdwan_uptime_red = sdwan_uptime.result.checks.red

# SECURITY: ====================================================================

# IPSec Tunnel Status:
ipsec_status = ipf.intent.intent_by_name['IPSec Tunnel Status']
ipsec_status_green = ipsec_status.result.checks.green
ipsec_status_red = ipsec_status.result.checks.red


# IPSec Tunnel Authentication:
ipsec_auth = ipf.intent.intent_by_name['IPSec Tunnel Authentication']
ipsec_auth_green = ipsec_auth.result.checks.green
ipsec_auth_amber = ipsec_auth.result.checks.amber

# IPSec Gateway Status:
ipsec_gateway = ipf.intent.intent_by_name['IPSec Gateway Status']
ipsec_gateway_green = ipsec_gateway.result.checks.green
ipsec_gateway_red = ipsec_gateway.result.checks.red

# IPSec Gateway Authentication:
ipsec_gateway_auth = ipf.intent.intent_by_name['IPSec Gateway Authentication']
ipsec_gateway_auth_green = ipsec_gateway_auth.result.checks.green
ipsec_gateway_auth_amber = ipsec_gateway_auth.result.checks.amber

# DMVPN Tunnel State: above

# IPSec Tunnel Encryption:
ipsec_enc = ipf.intent.intent_by_name['IPSec Tunnel Encryption']
ipsec_enc_green = ipsec_enc.result.checks.green
ipsec_enc_amber = ipsec_enc.result.checks.amber

# IPSec Gateway Encryption:
ipsec_gwy_enc = ipf.intent.intent_by_name['IPSec Gateway Encryption']
ipsec_gwy_enc_green = ipsec_gwy_enc.result.checks.green
ipsec_gwy_enc_amber = ipsec_gwy_enc.result.checks.amber

# MPLS PSEUDO-WIRES: ===========================================================

# All Pseudowires state:
pseudo = ipf.intent.intent_by_name['All Pseudowires state']
pseudo_green = pseudo.result.checks.green
pseudo_blue = pseudo.result.checks.blue

# CCC state:
ccc = ipf.intent.intent_by_name['CCC state']
ccc_green = ccc.result.checks.green
ccc_blue = ccc.result.checks.blue

# PTP VPWS State:
ptp_vpws = ipf.intent.intent_by_name['PTP VPWS State']
ptp_vpws_green = ptp_vpws.result.checks.green
ptp_vpws_blue = ptp_vpws.result.checks.blue

# PTMP VPLS State:
ptmp_vpls = ipf.intent.intent_by_name['PTMP VPLS State']
ptmp_vpls_green = ptmp_vpls.result.checks.green
ptmp_vpls_blue = ptmp_vpls.result.checks.blue

# Neighborship Compliance: ====================================================

# Duplex Mismatch or Missing: above

# STP Neighborship Expected State:
stp_expected = ipf.intent.intent_by_name['STP Neighborship Expected State']
stp_expected_green = stp_expected.result.checks.green
stp_expected_blue = stp_expected.result.checks.blue

# STP/CDP Neighbor Information Mismatch:
stpcdp_nei_mismatch = ipf.intent.intent_by_name['STP/CDP Neighbor Information Mismatch']
stpcdp_nei_mismatch_amber = stpcdp_nei_mismatch.result.checks.amber

# CDP/LLDP unidirectional:
cdp_lldp_uni = ipf.intent.intent_by_name['CDP/LLDP unidirectional']
cdp_lldp_uni_blue = cdp_lldp_uni.result.checks.blue

# CDP/LLDP Neighbor State:
cdp_lldp_nei = ipf.intent.intent_by_name['CDP/LLDP Neighbor State']
cdp_lldp_nei_green = cdp_lldp_nei.result.checks.green
cdp_lldp_nei_blue = cdp_lldp_nei.result.checks.blue

# OSPF Neighbor State:
ospf_nei = ipf.intent.intent_by_name['OSPF Neighbor State']
ospf_nei_green = ospf_nei.result.checks.green
ospf_nei_blue = ospf_nei.result.checks.blue
ospf_nei_amber = ospf_nei.result.checks.amber
ospf_nei_red = ospf_nei.result.checks.red

# OSPF Cost Consistency:
ospf_cost = ipf.intent.intent_by_name['OSPF Cost Consistency']
ospf_cost_green = ospf_cost.result.checks.green
ospf_cost_blue = ospf_cost.result.checks.blue
ospf_cost_amber = ospf_cost.result.checks.amber

# OSPF Interface Neighbors:
ospf_int = ipf.intent.intent_by_name['OSPF Interface Neighbors']
ospf_int_green = ospf_int.result.checks.green
ospf_int_blue = ospf_int.result.checks.blue

# OSPFv3 Neighbor State:
ospfv3_nei = ipf.intent.intent_by_name['OSPFv3 Neighbor State']
ospfv3_nei_green = ospfv3_nei.result.checks.green
ospfv3_nei_blue = ospfv3_nei.result.checks.blue
ospfv3_nei_amber = ospfv3_nei.result.checks.amber
ospfv3_nei_red = ospfv3_nei.result.checks.red

# OSPFv3 Cost Consistency:
ospfv3_cost = ipf.intent.intent_by_name['OSPFv3 Cost Consistency']
ospfv3_cost_green = ospfv3_cost.result.checks.green
ospfv3_cost_blue = ospfv3_cost.result.checks.blue
ospfv3_cost_amber = ospfv3_cost.result.checks.amber

# OSPFv3 Interface Neighbors:
ospfv3_int = ipf.intent.intent_by_name['OSPFv3 Interface Neighbors']
ospfv3_int_green = ospfv3_int.result.checks.green
ospfv3_int_blue = ospfv3_int.result.checks.blue


# EIGRP Interface Neighbors:
eigrp_int = ipf.intent.intent_by_name['EIGRP Interface Neighbors']
eigrp_int_green = eigrp_int.result.checks.green
eigrp_int_blue = eigrp_int.result.checks.blue


# BGP Neighbor State:
bgp_nei = ipf.intent.intent_by_name["BGP Neighbor State"]
bgp_nei_green = bgp_nei.result.checks.green
bgp_nei_blue = bgp_nei.result.checks.blue
bgp_nei_amber = bgp_nei.result.checks.amber
bgp_nei_red = bgp_nei.result.checks.red

# BGP Received Prefixes:
bgp_rec = ipf.intent.intent_by_name['BGP Received Prefixes']
bgp_rec_green = bgp_rec.result.checks.green
bgp_rec_blue = bgp_rec.result.checks.blue
bgp_rec_amber = bgp_rec.result.checks.amber

# IS-IS Interface Neighbors:
isis_int = ipf.intent.intent_by_name['IS-IS Interface Neighbors']
isis_int_green = isis_int.result.checks.green
isis_int_blue = isis_int.result.checks.blue

# RIP Interface Neighbors:
rip_int = ipf.intent.intent_by_name['RIP Interface Neighbors']
rip_int_green = rip_int.result.checks.green
rip_int_blue = rip_int.result.checks.blue

# LDP Interface Neighbors:
ldp_int = ipf.intent.intent_by_name['LDP Interface Neighbors']
ldp_int_green = ldp_int.result.checks.green
ldp_int_blue = ldp_int.result.checks.blue

# PIM Interfaces Neighbors:
pim_int = ipf.intent.intent_by_name['PIM Interfaces Neighbors']
pim_int_green = pim_int.result.checks.green
pim_int_blue = pim_int.result.checks.blue

# Unmanaged Neighbors:
un_nei = ipf.intent.intent_by_name['Unmanaged Neighbors']
un_nei_green = un_nei.result.checks.green
un_nei_amber = un_nei.result.checks.amber
un_nei_red = un_nei.result.checks.red

# Port-Channel Members State:
pc_ms = ipf.intent.intent_by_name['Port-Channel Members State']
pc_ms_green = pc_ms.result.checks.green
pc_ms_blue = pc_ms.result.checks.blue
pc_ms_amber = pc_ms.result.checks.amber

# Trunk Allowed VLAN Mismatch:
ta_vlm = ipf.intent.intent_by_name['Trunk Allowed VLAN Mismatch']
ta_vlm_green = ta_vlm.result.checks.green
ta_vlm_red = ta_vlm.result.checks.red

# SPANNING-TREE PROTOCOL (STP):==================================================

# STP Virtual Port Status:
stp_virt = ipf.intent.intent_by_name['STP Virtual Port Status']
stp_virt_green = stp_virt.result.checks.green
stp_virt_blue = stp_virt.result.checks.blue
stp_virt_amber = stp_virt.result.checks.amber
stp_virt_red = stp_virt.result.checks.red

# Switchport VLANs Without STP:
sw_no_stp = ipf.intent.intent_by_name['Switchport VLANs Without STP']
sw_no_stp_amber = sw_no_stp.result.checks.amber

# STP Loops:
stp_loops = ipf.intent.intent_by_name['STP Loops']
stp_loops_green = stp_loops.result.checks.green
stp_loops_amber = stp_loops.result.checks.amber

# STP Ports with Multiple Neighbors:
stp_multiple_nei = ipf.intent.intent_by_name['STP Ports with Multiple Neighbors']
stp_multiple_nei_amber = stp_multiple_nei.result.checks.amber

# Old STP Versions:
old_stp = ipf.intent.intent_by_name['Old STP Versions']
old_stp_green = old_stp.result.checks.green
old_stp_blue = old_stp.result.checks.blue
old_stp_amber = old_stp.result.checks.amber
old_stp_red = old_stp.result.checks.red

# Multiple STP Links Between Two Devices:
mult_stp = ipf.intent.intent_by_name['Multiple STP Links Between Two Devices']
mult_stp_amber = mult_stp.result.checks.amber

# VLAN status verification:
vlan_status = ipf.intent.intent_by_name['VLAN status verification']
vlan_status_green = vlan_status.result.checks.green
vlan_status_blue = vlan_status.result.checks.blue
vlan_status_amber = vlan_status.result.checks.amber

# VLAN Names:
vlan_names = ipf.intent.intent_by_name['VLAN Names']
vlan_names_green = vlan_names.result.checks.green
vlan_names_blue = vlan_names.result.checks.blue

# STP mode PVST or disabled:
stp_pvst_disabled = ipf.intent.intent_by_name['SPT mode PVST or disabled']
stp_pvst_disabled_blue = stp_pvst_disabled.result.checks.blue
stp_pvst_disabled_amber = stp_pvst_disabled.result.checks.amber

# Managed IP Address DNS Consistency:
ip_dns = ipf.intent.intent_by_name['Managed IP Address DNS Consistency']
ip_dns_green = ip_dns.result.checks.green
ip_dns_blue = ip_dns.result.checks.blue
ip_dns_amber = ip_dns.result.checks.amber

# MAC Address Source:
mac_source = ipf.intent.intent_by_name['MAC Address Source']
mac_source_green = mac_source.result.checks.green
mac_source_blue = mac_source.result.checks.blue
mac_source_amber = mac_source.result.checks.amber

# Proxy ARP:
proxy_arp = ipf.intent.intent_by_name['Proxy ARP']
proxy_arp_green = proxy_arp.result.checks.green
proxy_arp_blue = proxy_arp.result.checks.blue

# Duplicate IP Addresses:
dupe_ip = ipf.intent.intent_by_name['Duplicate IP Addresses']
dupe_ip_blue = dupe_ip.result.checks.blue
dupe_ip_amber = dupe_ip.result.checks.amber

# Management Consistency: =====================================================

# AAA Authorization Method:
aaa_author = ipf.intent.intent_by_name['AAA Authorization Method']
aaa_author_green = aaa_author.result.checks.green
aaa_author_amber = aaa_author.result.checks.amber

# AAA Accounting Method:
aaa_acc = ipf.intent.intent_by_name['AAA Accounting Method']
aaa_acc_green = aaa_acc.result.checks.green
aaa_acc_amber = aaa_acc.result.checks.amber

# AAA Authentication Method:
aaa_authe = ipf.intent.intent_by_name['AAA Authentication Method']
aaa_authe_green = aaa_authe.result.checks.green
aaa_authe_amber = aaa_authe.result.checks.amber

# NTP Stratum Level:
ntp_stratum = ipf.intent.intent_by_name['NTP Stratum Level']
ntp_stratum_green = ntp_stratum.result.checks.green
ntp_stratum_blue = ntp_stratum.result.checks.blue
ntp_stratum_amber = ntp_stratum.result.checks.amber
ntp_stratum_red = ntp_stratum.result.checks.red

# NTP Time Offset:
ntp_offset = ipf.intent.intent_by_name['NTP Time Offset']
ntp_offset_green = ntp_offset.result.checks.green
ntp_offset_blue = ntp_offset.result.checks.blue
ntp_offset_amber = ntp_offset.result.checks.amber
ntp_offset_red = ntp_offset.result.checks.red

# NTP Network Round-Trip Time:
ntp_rtt = ipf.intent.intent_by_name['NTP Network Round-Trip Time']
ntp_rtt_green = ntp_rtt.result.checks.green
ntp_rtt_blue = ntp_rtt.result.checks.blue
ntp_rtt_amber = ntp_rtt.result.checks.amber
ntp_rtt_red = ntp_rtt.result.checks.red

# Remote System Logging Destination Port:
remote_logg = ipf.intent.intent_by_name['Remote System Logging Destination Port']
remote_logg_green = remote_logg.result.checks.green
remote_logg_blue = remote_logg.result.checks.blue
remote_logg_amber = remote_logg.result.checks.amber

# SNMP Community Name:
snmp_name = ipf.intent.intent_by_name['SNMP Community Name']
snmp_name_green = snmp_name.result.checks.green
snmp_name_amber = snmp_name.result.checks.amber

# SNMP Configuration Compliance:
snmp_config = ipf.intent.intent_by_name['SNMP Configuration Compliance']
snmp_config_green = snmp_config.result.checks.green
snmp_config_blue = snmp_config.result.checks.blue
snmp_config_amber = snmp_config.result.checks.amber

# Saved Config Consistency:
config_con = ipf.intent.intent_by_name['Saved Config Consistency']
config_con_green = config_con.result.checks.green
config_con_blue = config_con.result.checks.blue
config_con_amber = config_con.result.checks.amber

# DHCP Snooping Dropped Packets:
dhcp_dropped = ipf.intent.intent_by_name['DHCP Snooping Dropped Packets']
dhcp_dropped_green = dhcp_dropped.result.checks.green
dhcp_dropped_amber = dhcp_dropped.result.checks.amber

# DHCP Snooping Trusted Port:
dhcp_trusted = ipf.intent.intent_by_name['DHCP Snooping Trusted Port']
dhcp_trusted_green = dhcp_trusted.result.checks.green
dhcp_trusted_red = dhcp_trusted.result.checks.red

# DHCP Snooping Enabled VLANs:
dhcp_enabled = ipf.intent.intent_by_name['DHCP Snooping Enabled VLANs']
dhcp_enabled_green = dhcp_enabled.result.checks.green
dhcp_enabled_red = dhcp_enabled.result.checks.red

# DHCP Binding session expiration:
dhcp_binding = ipf.intent.intent_by_name['DHCP Binding session expiration']
dhcp_binding_green = dhcp_binding.result.checks.green
dhcp_binding_blue = dhcp_binding.result.checks.blue
dhcp_binding_amber = dhcp_binding.result.checks.amber
dhcp_binding_red = dhcp_binding.result.checks.red

# AAA Authentication Type:
aaa_authe_type = ipf.intent.intent_by_name['AAA Authentication Type']
aaa_authe_type_green = aaa_authe_type.result.checks.green
aaa_authe_type_blue = aaa_authe_type.result.checks.blue
aaa_authe_type_amber = aaa_authe_type.result.checks.amber
aaa_authe_type_red = aaa_authe_type.result.checks.red

# SNMP Community & ACL:
snmp_acl = ipf.intent.intent_by_name['SNMP Community & ACL']
snmp_acl_green = snmp_acl.result.checks.green
snmp_acl_blue = snmp_acl.result.checks.blue

# Local System Logging Severity:
local_logg = ipf.intent.intent_by_name['Local System Logging Severity']
local_logg_green = local_logg.result.checks.green
local_logg_amber = local_logg.result.checks.amber

# Remote System Logging Severity:
remote_sys_logg = ipf.intent.intent_by_name['Remote System Logging Severity']
remote_sys_logg_green = remote_sys_logg.result.checks.green
remote_sys_logg_amber = remote_sys_logg.result.checks.amber

# NTP Reahcable Soruces:f
ntp_reachable = ipf.intent.intent_by_name['NTP Reachable Sources']
ntp_reachable_green = ntp_reachable.result.checks.green
ntp_reachable_blue = ntp_reachable.result.checks.blue
ntp_reachable_amber = ntp_reachable.result.checks.amber
ntp_reachable_red = ntp_reachable.result.checks.red

# Devices with Telnet Access (total):
telnet = ipf.intent.intent_by_name['Devices with Telnet Access (total)']
telnet_red = telnet.result.checks.red

# Device Logging Configuration:
device_logg = ipf.intent.intent_by_name['Device Logging Configuration']
device_logg_green = device_logg.result.checks.green
device_logg_amber = device_logg.result.checks.amber
device_logg_red = device_logg.result.checks.red

# NTP Configured Sources:
ntp_sources = ipf.intent.intent_by_name['NTP Configured Sources']
ntp_sources_green = ntp_sources.result.checks.green
ntp_sources_amber = ntp_sources.result.checks.amber
ntp_sources_red = ntp_sources.result.checks.red

# OPERATING SYSTEM (OS):=======================================================

# Operating System Version (%):
os_ver = ipf.intent.intent_by_name['Operating System Version (%)']
os_ver_green = os_ver.result.checks.green
os_ver_blue = os_ver.result.checks.blue
os_ver_amber = os_ver.result.checks.amber
os_ver_red = os_ver.result.checks.red

# Devices with Unique OS:
unique_os = ipf.intent.intent_by_name['Devices with Unique OS']
unique_os_green = unique_os.result.checks.green
unique_os_blue = unique_os.result.checks.blue

# Devices with Unique Platform:
unique_platform = ipf.intent.intent_by_name['Devices with Unique Platform']
unique_platform_green = unique_platform.result.checks.green
unique_platform_blue = unique_platform.result.checks.blue

# QUALITY OF SERVICE (QOS):===================================================

# QoS Random And Tail Drops:
qos_random_tail = ipf.intent.intent_by_name['QoS Random And Tail Drops']
qos_random_tail_green = qos_random_tail.result.checks.green
qos_random_tail_blue = qos_random_tail.result.checks.blue
qos_random_tail_amber = qos_random_tail.result.checks.amber
qos_random_tail_red = qos_random_tail.result.checks.red

# QoS EF Class Drops:
qos_ef_drops = ipf.intent.intent_by_name['QoS EF Class Drops']
qos_ef_drops_green = qos_ef_drops.result.checks.green
qos_ef_drops_amber = qos_ef_drops.result.checks.amber

# QoS Priority Queue Drops:
qos_pri_drops = ipf.intent.intent_by_name['QoS Priority Queue Drops']
qos_pri_drops_green = qos_pri_drops.result.checks.green
qos_pri_drops_amber = qos_pri_drops.result.checks.amber

# Queue Limit Size (packets):
q_limit_size = ipf.intent.intent_by_name['Queue Limit Size (packets)']
q_limit_size_green = q_limit_size.result.checks.green
q_limit_size_blue = q_limit_size.result.checks.blue
q_limit_size_amber = q_limit_size.result.checks.amber

# Shaping Queues Child Policy:
shaping_child = ipf.intent.intent_by_name['Shaping Queues Child Policy']
shaping_child_green = shaping_child.result.checks.green
shaping_child_blue = shaping_child.result.checks.blue

# FIRST HOP REDUNDANCY PROTOCOL (FHRP):=========================================

# Gateway Redundancy:
gwy_redu = ipf.intent.intent_by_name['Gateway Redundancy']
gwy_redu_green = gwy_redu.result.checks.green
gwy_redu_blue = gwy_redu.result.checks.blue

# Virtual Gateways Consistency:
virt_gwy = ipf.intent.intent_by_name['Virtual Gateways Consistency']
virt_gwy_green = virt_gwy.result.checks.green
virt_gwy_blue = virt_gwy.result.checks.blue
virt_gwy_amber = virt_gwy.result.checks.amber

# FHRP Active Group Priority:
fhrp_active = ipf.intent.intent_by_name['FHRP Active Group Priority']
fhrp_active_green = fhrp_active.result.checks.green
fhrp_active_blue = fhrp_active.result.checks.blue

# FHRP Group Members:
fhrp_members = ipf.intent.intent_by_name['FHRP Group Members']
fhrp_members_green = fhrp_members.result.checks.green
fhrp_members_blue = fhrp_members.result.checks.blue

# STP Root And FHRP Active Mismatch:
stp_fhrp_mismatch = ipf.intent.intent_by_name["STP Root And FHRP Active Mismatch"]
stp_fhrp_mismatch_blue = stp_fhrp_mismatch.result.checks.blue

# FHRP Master Inconsistency:
fhrp_master = ipf.intent.intent_by_name['FHRP Master Inconsistency']
fhrp_master_green = fhrp_master.result.checks.green
fhrp_master_blue = fhrp_master.result.checks.blue
fhrp_master_amber = fhrp_master.result.checks.amber
fhrp_master_red = fhrp_master.result.checks.red






















