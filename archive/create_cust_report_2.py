


import pandas as pd
from jinja2 import Template, Environment, FileSystemLoader
import os


df_sites = pd.read_csv("../DOWNLOADS/inventory/sites.csv")
if df_sites.empty == False:
    df_sites = df_sites.drop(['id', 'siteKey', 'siteName'], axis=1)

df_devices = pd.read_csv("../DOWNLOADS/inventory/devices.csv", keep_default_na=False)
if df_devices.empty == False:
    df_devices = df_devices.drop(['id', 'taskKey', 'memoryTotalBytes', 'memoryUsedBytes',
                              'memoryUtilization', 'snHw','uptime', 'siteKey', 'objectId', 'siteName'], axis=1)

df_devices_models = pd.read_csv("../DOWNLOADS/inventory/devices-models.csv", keep_default_na=False)
# if df_devices.empty == False:
#     df_devices = df_devices.drop(['id', 'taskKey', 'memoryTotalBytes', 'memoryUsedBytes',
#                               'memoryUtilization', 'snHw','uptime', 'siteKey', 'objectId', 'siteName'], axis=1)

df_part_numbers = pd.read_csv("../DOWNLOADS/inventory/part-numbers.csv", keep_default_na=False)
if df_part_numbers.empty == False:
    df_part_numbers = df_part_numbers.drop(['id', 'siteKey', 'deviceId', 'siteName'], axis=1)

df_os_versions = pd.read_csv("../DOWNLOADS/inventory/os-versions.csv", keep_default_na=False)
if df_os_versions.empty == False:
    df_os_versions = df_os_versions.drop(['id'], axis=1)

df_cluster_srx = pd.read_csv("../DOWNLOADS/technology/platforms/cluster-srx.csv", keep_default_na=False)
if df_cluster_srx.empty == False:
    df_cluster_srx = df_cluster_srx.drop(['id', 'siteKey', 'siteName'], axis=1)

df_fex_modules = pd.read_csv("../DOWNLOADS/technology/platforms/fex-modules.csv", keep_default_na=False)
if df_fex_modules.empty == False:
    df_fex_modules = df_fex_modules.drop(['id'], axis=1)

df_poe_devices = pd.read_csv("../DOWNLOADS/technology/platforms/poe-devices.csv", keep_default_na=False)
if df_poe_devices.empty == False:
    df_poe_devices = df_poe_devices.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stacks = pd.read_csv("../DOWNLOADS/technology/platforms/stacks.csv", keep_default_na=False)
if df_stacks.empty == False:
    df_stacks = df_stacks.drop(['id', 'siteKey', 'siteName', 'uptimeLow', 'uptimeDiff'], axis=1)

df_power_supplies = pd.read_csv("../DOWNLOADS/technology/platforms/power-supplies.csv", keep_default_na=False)
if df_power_supplies.empty == False:
    df_power_supplies = df_power_supplies.drop(['id', 'siteKey', 'siteName', 'deviceId', 'pwSupplyCircuit', 'pwSupplyName'], axis=1)

df_duplex_mismatch = pd.read_csv("../DOWNLOADS/technology/interfaces/duplex-mismatch.csv", keep_default_na=False)
if df_duplex_mismatch.empty == False:
    df_duplex_mismatch = df_duplex_mismatch.drop(['id', 'siteKey', 'siteName'], axis=1)

df_errdisabled = pd.read_csv("../DOWNLOADS/technology/interfaces/errdisabled.csv", keep_default_na=False)
if df_errdisabled.empty == False:
    df_errdisabled = df_errdisabled.drop(['id', 'siteKey', 'siteName'], axis=1)

df_connectivity_matrix = pd.read_csv("../DOWNLOADS/technology/interfaces/connectivity-matrix.csv", keep_default_na=False)
if df_connectivity_matrix.empty == False:
    df_connectivity_matrix = df_connectivity_matrix.drop(['id', 'siteKey', 'siteName'], axis=1)

df_mtu = pd.read_csv("../DOWNLOADS/technology/interfaces/mtu.csv", keep_default_na=False)
if df_mtu.empty == False:
    df_mtu = df_mtu.drop(['id', 'siteKey', 'siteName'], axis=1)

df_storm_control = pd.read_csv("../DOWNLOADS/technology/interfaces/storm-control-broadcast.csv", keep_default_na=False)
if df_storm_control.empty == False:
    df_storm_control = df_storm_control.drop(['id', 'siteKey', 'siteName'], axis=1)

df_transceivers = pd.read_csv("../DOWNLOADS/technology/interfaces/transceivers-inventory.csv", keep_default_na=False)
if df_transceivers.empty == False:
    df_transceivers = df_transceivers.drop(['id', 'siteKey', 'siteName'], axis=1)

df_pppoe_interfaces = pd.read_csv("../DOWNLOADS/technology/interfaces/pppoe-interfaces.csv", keep_default_na=False)
if df_pppoe_interfaces.empty == False:
    df_pppoe_interfaces = df_pppoe_interfaces.drop(['id', 'siteKey', 'siteName'], axis=1)

df_all_neighbors = pd.read_csv("../DOWNLOADS/technology/cdp-lldp/all-neighbors.csv", keep_default_na=False)
if df_all_neighbors.empty == False:
    df_all_neighbors = df_all_neighbors.drop(['id', 'siteKey', 'siteName'], axis=1)

df_unmanaged_neighbors = pd.read_csv("../DOWNLOADS/technology/cdp-lldp/unmanaged-neighbors.csv", keep_default_na=False)
if df_unmanaged_neighbors.empty == False:
    df_unmanaged_neighbors = df_unmanaged_neighbors.drop(['id', 'siteKey', 'siteName'], axis=1)

df_unidirectional_neighbors = pd.read_csv("../DOWNLOADS/technology/cdp-lldp/unidirectional-neighbors.csv", keep_default_na=False)
if df_unidirectional_neighbors.empty == False:
    df_unidirectional_neighbors = df_unidirectional_neighbors.drop(['id', 'siteKey', 'siteName'], axis=1)

df_inbound_balancing = pd.read_csv("../DOWNLOADS/technology/port-channels/inbound-balancing-table.csv", keep_default_na=False)
if df_inbound_balancing.empty == False:
    df_inbound_balancing = df_inbound_balancing.drop(['id', 'siteKey', 'siteName'], axis=1)

df_outbound_balancing = pd.read_csv("../DOWNLOADS/technology/port-channels/outbound-balancing-table.csv", keep_default_na=False)
if df_outbound_balancing.empty == False:
    df_outbound_balancing = df_outbound_balancing.drop(['id', 'siteKey', 'siteName'], axis=1)

df_member_status = pd.read_csv("../DOWNLOADS/technology/port-channels/member-status-table.csv", keep_default_na=False)
if df_member_status.empty == False:
    df_member_status = df_member_status.drop(['id', 'siteKey', 'siteName'], axis=1)

df_mlag_vpc = pd.read_csv("../DOWNLOADS/technology/port-channels/mlag-vpc.csv", keep_default_na=False)
if df_mlag_vpc.empty == False:
    df_mlag_vpc = df_mlag_vpc.drop(['id', 'siteKey', 'siteName'], axis=1)

df_device_summary = pd.read_csv("../DOWNLOADS/technology/vlans/device-summary.csv", keep_default_na=False)
if df_device_summary.empty == False:
    df_device_summary = df_device_summary.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stp_stability = pd.read_csv("../DOWNLOADS/technology/spanning-tree/stp-stability.csv", keep_default_na=False)
if df_stp_stability.empty == False:
    df_stp_stability = df_stp_stability.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stp_bridges = pd.read_csv("../DOWNLOADS/technology/spanning-tree/stp-bridges.csv", keep_default_na=False)
if df_stp_bridges.empty == False:
    df_stp_bridges = df_stp_bridges.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stp_instances = pd.read_csv("../DOWNLOADS/technology/spanning-tree/stp-instances.csv", keep_default_na=False)
if df_stp_instances.empty == False:
    df_stp_instances = df_stp_instances.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stp_guards = pd.read_csv("../DOWNLOADS/technology/spanning-tree/stp-guards.csv", keep_default_na=False)
if df_stp_guards.empty == False:
    df_stp_guards = df_stp_guards.drop(['id', 'siteKey', 'siteName'], axis=1)

df_stp_inconsistencies = pd.read_csv("../DOWNLOADS/technology/spanning-tree/stp-inconsistencies.csv", keep_default_na=False)
if df_stp_inconsistencies.empty == False:
    df_stp_inconsistencies = df_stp_inconsistencies.drop(['id', 'siteKey', 'siteName'], axis=1)

df_managed_ip = pd.read_csv("../DOWNLOADS/technology/addressing/managed-ip.csv", keep_default_na=False)
if df_managed_ip.empty == False:
    df_managed_ip = df_managed_ip.drop(['id', 'siteKey', 'siteName'], axis=1)

df_duplicate_ip = pd.read_csv("../DOWNLOADS/technology/addressing/duplicate-ip.csv", keep_default_na=False)
if df_duplicate_ip.empty == False:
    df_duplicate_ip = df_duplicate_ip.drop(['id'], axis=1)

df_nat_rules = pd.read_csv("../DOWNLOADS/technology/addressing/nat-rules.csv", keep_default_na=False)
if df_nat_rules.empty == False:
    df_nat_rules = df_nat_rules.drop(['id', 'siteKey', 'siteName'], axis=1)

df_fhrp_group_state = pd.read_csv("../DOWNLOADS/technology/fhrp/group-state.csv", keep_default_na=False)
if df_fhrp_group_state.empty == False:
    df_fhrp_group_state = df_fhrp_group_state.drop(['id', 'siteKey', 'siteName'], axis=1)

df_fhrp_group_members = pd.read_csv("../DOWNLOADS/technology/fhrp/group-members.csv", keep_default_na=False)
if df_fhrp_group_members.empty == False:
    df_fhrp_group_members = df_fhrp_group_members.drop(['id'], axis=1)

df_fhrp_root = pd.read_csv("../DOWNLOADS/technology/fhrp/active-gw-root-alignment.csv", keep_default_na=False)
if df_fhrp_root.empty == False:
    df_fhrp_root = df_fhrp_root.drop(['id', 'siteKey', 'siteName'], axis=1)

df_fhrp_glbp_forwarders = pd.read_csv("../DOWNLOADS/technology/fhrp/glbp-forwarders.csv", keep_default_na=False)
if df_fhrp_glbp_forwarders.empty == False:
    df_fhrp_glbp_forwarders = df_fhrp_glbp_forwarders.drop(['id', 'siteKey', 'siteName'], axis=1)

df_fhrp_virtual_gateways = pd.read_csv("../DOWNLOADS/technology/fhrp/virtual-gateways.csv", keep_default_na=False)
if df_fhrp_virtual_gateways.empty == False:
    df_fhrp_virtual_gateways = df_fhrp_virtual_gateways.drop(['id', 'siteKey', 'siteName'], axis=1)

df_managed_networks = pd.read_csv("../DOWNLOADS/technology/networks/managed-networks.csv", keep_default_na=False)
if df_managed_networks.empty == False:
    df_managed_networks = df_managed_networks.drop(['id', 'siteKey', 'mask', 'siteName'], axis=1)

df_gateway_redundancy = pd.read_csv("../DOWNLOADS/technology/networks/gateway-redundancy.csv", keep_default_na=False)
if df_gateway_redundancy.empty == False:
    df_gateway_redundancy = df_gateway_redundancy.drop(['id', 'siteKey'], axis=1)

df_route_stability = pd.read_csv("../DOWNLOADS/technology/routing/route-stability.csv", keep_default_na=False)
if df_route_stability.empty == False:
    df_route_stability = df_route_stability.drop(['id'], axis=1)

df_ospf_nei = pd.read_csv("../DOWNLOADS/technology/routing/ospf-neighbors.csv", keep_default_na=False)
if df_ospf_nei.empty == False:
    df_ospf_nei = df_ospf_nei.drop(['id', 'siteKey', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_ospf_v3nei = pd.read_csv("../DOWNLOADS/technology/routing/ospf-v3-neighbors.csv", keep_default_na=False)
if df_ospf_v3nei.empty == False:
    df_ospf_v3nei = df_ospf_v3nei.drop(['id', 'siteKey'], axis=1)

df_bgp_nei = pd.read_csv("../DOWNLOADS/technology/routing/bgp-neighbors.csv", keep_default_na=False)
if df_bgp_nei.empty == False:
    df_bgp_nei = df_bgp_nei.drop(['id', 'siteKey', 'currStateTime', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_eigrp_nei = pd.read_csv("../DOWNLOADS/technology/routing/eigrp-neighbors.csv", keep_default_na=False)
if df_eigrp_nei.empty == False:
    df_eigrp_nei = df_eigrp_nei.drop(['id', 'siteKey', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_rip_nei = pd.read_csv("../DOWNLOADS/technology/routing/rip-neighbors.csv", keep_default_na=False)
if df_rip_nei.empty == False:
    df_rip_nei = df_rip_nei.drop(['id', 'siteKey', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_isis_nei = pd.read_csv("../DOWNLOADS/technology/routing/is-is-neighbors.csv", keep_default_na=False)
if df_isis_nei.empty == False:
    df_isis_nei = df_isis_nei.drop(['id', 'siteKey', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_path_verification = pd.read_csv("../DOWNLOADS/technology/routing/path-verifications.csv", keep_default_na=False)
if df_path_verification.empty == False:
    df_path_verification = df_path_verification.drop(['id', 'siteKey'], axis=1)

df_vrf_summary = pd.read_csv("../DOWNLOADS/technology/routing/vrf-summary.csv", keep_default_na=False)
if df_vrf_summary.empty == False:
    df_vrf_summary = df_vrf_summary.drop(['id'], axis=1)

df_ldp_nei = pd.read_csv("../DOWNLOADS/technology/mpls/ldp-neighbors.csv", keep_default_na=False)
if df_ldp_nei.empty == False:
    df_ldp_nei = df_ldp_nei.drop(['id', 'siteKey'], axis=1)

df_mpls_forwarding = pd.read_csv("../DOWNLOADS/technology/mpls/mpls-forwarding.csv", keep_default_na=False)
if df_mpls_forwarding.empty == False:
    df_mpls_forwarding = df_mpls_forwarding.drop(['id', 'siteKey'], axis=1)

df_l3vpn_routers = pd.read_csv("../DOWNLOADS/technology/mpls/l3vpn-pe-routers.csv", keep_default_na=False)
if df_l3vpn_routers.empty == False:
    df_l3vpn_routers = df_l3vpn_routers.drop(['id', 'siteKey'], axis=1)

df_l2vpn_p2p = pd.read_csv("../DOWNLOADS/technology/mpls/l2vpn-point-to-point-vpws.csv", keep_default_na=False)
if df_l2vpn_p2p.empty == False:
    df_l2vpn_p2p = df_l2vpn_p2p.drop(['id', 'siteKey'], axis=1)

df_pim_nei = pd.read_csv("../DOWNLOADS/technology/multicast/pim-neighbors.csv", keep_default_na=False)
if df_pim_nei.empty == False:
    df_pim_nei = df_pim_nei.drop(['id', 'siteKey', 'neiSiteName', 'siteName', 'neiSiteKey'], axis=1)

df_mroute_overview = pd.read_csv("../DOWNLOADS/technology/multicast/mroute-overview.csv", keep_default_na=False)
if df_mroute_overview.empty == False:
    df_mroute_overview = df_mroute_overview.drop(['id', 'siteKey', 'siteName'], axis=1)

df_igmp_groups = pd.read_csv("../DOWNLOADS/technology/multicast/igmp-groups.csv", keep_default_na=False)
if df_igmp_groups.empty == False:
    df_igmp_groups = df_igmp_groups.drop(['id', 'siteKey', 'uptime', 'siteName'], axis=1)

df_igmp_snooping = pd.read_csv("../DOWNLOADS/technology/multicast/igmp-snooping-global.csv", keep_default_na=False)
if df_igmp_snooping.empty == False:
    df_igmp_snooping = df_igmp_snooping.drop(['id', 'siteKey', 'siteName'], axis=1)

df_multicast_macs = pd.read_csv("../DOWNLOADS/technology/multicast/macs.csv", keep_default_na=False)
if df_multicast_macs.empty == False:
    df_multicast_macs = df_multicast_macs.drop(['id', 'siteKey', 'siteName'], axis=1)

df_rp_overview = pd.read_csv("../DOWNLOADS/technology/multicast/rp-overview.csv", keep_default_na=False)
if df_rp_overview.empty == False:
    df_rp_overview = df_rp_overview.drop(['id', 'siteKey', 'siteName'], axis=1)

df_aaa_servers = pd.read_csv("../DOWNLOADS/technology/management/aaa-servers.csv", keep_default_na=False)
if df_aaa_servers.empty == False:
    df_aaa_servers = df_aaa_servers.drop(['id', 'siteKey', 'siteName'], axis=1)

df_telnet_access = pd.read_csv("../DOWNLOADS/technology/management/telnet-access.csv", keep_default_na=False)
if df_telnet_access.empty == False:
    df_telnet_access = df_telnet_access.drop(['id', 'siteKey', 'uptime', 'siteName'], axis=1)

df_saved_configs = pd.read_csv("../DOWNLOADS/technology/management/saved-config-consistency.csv", keep_default_na=False)
if df_saved_configs.empty == False:
    df_saved_configs = df_saved_configs.drop(['id', 'siteKey', 'uptime', 'blobKey', 'siteName'], axis=1)

df_ntp_summary = pd.read_csv("../DOWNLOADS/technology/management/ntp-summary.csv", keep_default_na=False)
if df_ntp_summary.empty == False:
    df_ntp_summary = df_ntp_summary.drop(['id', 'siteKey', 'siteName'], axis=1)

df_port_mirroring = pd.read_csv("../DOWNLOADS/technology/management/port-mirroring.csv", keep_default_na=False)
if df_port_mirroring.empty == False:
    df_port_mirroring = df_port_mirroring.drop(['id', 'siteKey', 'siteName'], axis=1)

df_log_summary = pd.read_csv("../DOWNLOADS/technology/management/logging-summary.csv", keep_default_na=False)
if df_log_summary.empty == False:
    df_log_summary = df_log_summary.drop(['id', 'siteKey', 'siteName'], axis=1)

df_flow_overview = pd.read_csv("../DOWNLOADS/technology/management/flow-overview.csv", keep_default_na=False)
if df_flow_overview.empty == False:
    df_flow_overview = df_flow_overview.drop(['id', 'siteKey', 'siteName'], axis=1)

df_snmp_summary = pd.read_csv("../DOWNLOADS/technology/management/snmp-summary.csv", keep_default_na=False)
if df_snmp_summary.empty == False:
    df_snmp_summary = df_snmp_summary.drop(['id', 'siteKey', 'siteName'], axis=1)

df_ptp_local_clock = pd.read_csv("../DOWNLOADS/technology/management/ptp-local-clock.csv", keep_default_na=False)
if df_ptp_local_clock.empty == False:
    df_ptp_local_clock = df_ptp_local_clock.drop(['id', 'siteKey', 'siteName'], axis=1)

df_acl_interfaces = pd.read_csv("../DOWNLOADS/technology/security/acl-interfaces.csv", keep_default_na=False)
if df_acl_interfaces.empty == False:
    df_acl_interfaces = df_acl_interfaces.drop(['id', 'siteKey', 'siteName'], axis=1)

df_dmvpn = pd.read_csv("../DOWNLOADS/technology/security/dmvpn.csv", keep_default_na=False)
if df_dmvpn.empty == False:
    df_dmvpn = df_dmvpn.drop(['id', 'siteKey', 'siteName'], axis=1)

df_dhcp_snooping = pd.read_csv("../DOWNLOADS/technology/security/dhcp-snooping.csv", keep_default_na=False)
if df_dhcp_snooping.empty == False:
    df_dhcp_snooping = df_dhcp_snooping.drop(['id', 'siteKey', 'siteName'], axis=1)

df_ipsec_tunnels = pd.read_csv("../DOWNLOADS/technology/security/ipsec-tunnels.csv", keep_default_na=False)
if df_ipsec_tunnels.empty == False:
    df_ipsec_tunnels = df_ipsec_tunnels.drop(['id', 'siteKey', 'siteName'], axis=1)

df_secure_ports_devices = pd.read_csv("../DOWNLOADS/technology/security/secure-ports-devices.csv", keep_default_na=False)
if df_secure_ports_devices.empty == False:
    df_secure_ports_devices = df_secure_ports_devices.drop(['id', 'siteKey', 'siteName'], axis=1)

df_zone_fw_policies = pd.read_csv("../DOWNLOADS/technology/security/zone-firewall-policies.csv", keep_default_na=False)
if df_zone_fw_policies.empty == False:
    df_zone_fw_policies = df_zone_fw_policies.drop(['id', 'siteKey', 'siteName'], axis=1)

df_lb_virtual_servers = pd.read_csv("../DOWNLOADS/technology/load-balancing/virtual-servers.csv", keep_default_na=False)
if df_lb_virtual_servers.empty == False:
    df_lb_virtual_servers = df_lb_virtual_servers.drop(['id', 'siteKey', 'siteName'], axis=1)

df_wireless_controllers = pd.read_csv("../DOWNLOADS/technology/wireless/controllers.csv", keep_default_na=False)
if df_wireless_controllers.empty == False:
    df_wireless_controllers = df_wireless_controllers.drop(['id', 'siteKey', 'siteName'], axis=1)

df_wireless_aps = pd.read_csv("../DOWNLOADS/technology/wireless/access-points.csv", keep_default_na=False)
if df_wireless_aps.empty == False:
    df_wireless_aps = df_wireless_aps.drop(['id', 'siteKey', 'siteName'], axis=1)

df_wireless_clients = pd.read_csv("../DOWNLOADS/technology/wireless/clients.csv", keep_default_na=False)
if df_wireless_clients.empty == False:
    df_wireless_clients = df_wireless_clients.drop(['id', 'siteKey', 'siteName', 'inBytesRate', 'inPktsRate',
                                                    'outBytesRate', 'outPktsRate', 'pktsRate'], axis=1)

df_voip_phones = pd.read_csv("../DOWNLOADS/technology/voip/phones.csv", keep_default_na=False)
if df_voip_phones.empty == False:
    df_voip_phones = df_voip_phones.drop(['id', 'siteKey', 'siteName'], axis=1)

df_aci_endpoints = pd.read_csv("../DOWNLOADS/technology/sdn/aci-endpoint.csv", keep_default_na=False)
if df_aci_endpoints.empty == False:
    df_aci_endpoints = df_aci_endpoints.drop(['id', 'siteKey', 'siteName'], axis=1)

df_vxlan_vteps = pd.read_csv("../DOWNLOADS/technology/sdn/vxlan-vtep.csv", keep_default_na=False)
if df_vxlan_vteps.empty == False:
    df_vxlan_vteps = df_vxlan_vteps.drop(['id', 'siteKey', 'siteName'], axis=1)

df_sdwan_sites = pd.read_csv("../DOWNLOADS/technology/sdwan/sdwan-sites.csv", keep_default_na=False)
if df_sdwan_sites.empty == False:
    df_sdwan_sites = df_sdwan_sites.drop(['id', 'siteKey', 'siteName'], axis=1)

df_udld_nei = pd.read_csv("../DOWNLOADS/technology/oam/udld-neighbors.csv", keep_default_na=False)
if df_udld_nei.empty == False:
    df_udld_nei = df_udld_nei.drop(['id', 'siteKey', 'siteName'], axis=1)

company_name = os.getenv("company_name")
company_name = company_name.title()

env = Environment(loader=FileSystemLoader('../templates'))

template = env.get_template('customer_template.html')

html = template.render(page_title_text='Network Assessment Data',
                       title_text=f'{company_name} Network Assessment Data',
                       sites_text='-All Sites-',
                       df_sites=df_sites,
                       devices_text='-All Devices-',
                       df_devices=df_devices,
                       devices_models_text='-All Device Models-',
                       df_devices_models=df_devices_models,
                       part_numbers_text='-All Part Numbers-',
                       df_part_numbers=df_part_numbers,
                       os_versions_text='-OS Versions-',
                       df_os_versions=df_os_versions,
                       cluster_srx_text='-Cluster SRX Information-',
                       df_cluster_srx=df_cluster_srx,
                       fex_modules_text="-FEX Modules-",
                       df_fex_modules=df_fex_modules,
                       poe_devices_text="-All POE Devices-",
                       df_poe_devices=df_poe_devices,
                       stacks_text="-All Stacked Switches-",
                       df_stacks=df_stacks,
                       power_supplies_text="-All Power Supplies-",
                       df_power_supplies=df_power_supplies,
                       duplex_mismatch_text="-Duplex Mismatches-",
                       df_duplex_mismatch=df_duplex_mismatch,
                       errdisabled_text="-Errdisabled Links-",
                       df_errdisabled=df_errdisabled,
                       connectivity_matrix_text="-Connectivity Matrix-",
                       df_connectivity_matrix=df_connectivity_matrix,
                       mtu_text="-MTUs on the Network-",
                       df_mtu=df_mtu,
                       storm_control_text="-Storm Control-",
                       df_storm_control=df_storm_control,
                       transceivers_text="-All Transceivers-",
                       df_transceivers=df_transceivers,
                       pppoe_interfaces_text="-All PPPOE Interfaces-",
                       df_pppoe_interfaces=df_pppoe_interfaces,
                       all_neighbors_text="-All Neighbors-",
                       df_all_neighbors=df_all_neighbors,
                       unmanaged_neighbors_text="-All Unmanaged Neighbors-",
                       df_unmanaged_neighbors=df_unmanaged_neighbors,
                       unidirectional_neighbors_text="-All Unidirectional Neighbors-",
                       df_unidirectional_neighbors=df_unidirectional_neighbors,
                       inbound_balancing_text="-Inbound Load-Balancing Table-",
                       df_inbound_balancing=df_inbound_balancing,
                       outbound_balancing_text="-Outbound Load-Balancing Table-",
                       df_outbound_balancing=df_outbound_balancing,
                       member_status_text="-Port-Channel Member Status Table-",
                       df_member_status=df_member_status,
                       mlag_vpc_text="-MLAG VPC Table-",
                       df_mlag_vpc=df_mlag_vpc,
                       device_summary_text="-Device Summary-",
                       df_device_summary=df_device_summary,
                       stp_stability_text="-STP Stability Table-",
                       df_stp_stability=df_stp_stability,
                       stp_bridges_text="-STP Bridges-",
                       df_stp_bridges=df_stp_bridges,
                       stp_instances_text="-STP Instances-",
                       df_stp_instances=df_stp_instances,
                       stp_guards_text="-STP Guards-",
                       df_stp_guards=df_stp_guards,
                       stp_inconsistencies_text="-STP Inconsistencies-",
                       df_stp_inconsistencies=df_stp_inconsistencies,
                       managed_ip_text="-Managed IP-",
                       df_managed_ip=df_managed_ip,
                       duplicate_ip_text="-Duplicate IP Addresses-",
                       df_duplicate_ip=df_duplicate_ip,
                       nat_rules_text="-NAT Rules-",
                       df_nat_rules=df_nat_rules,
                       fhrp_group_state_text="-FHRP Group State Table-",
                       df_fhrp_group_state=df_fhrp_group_state,
                       fhrp_group_members_text="-FHRP Group Members-",
                       df_fhrp_group_members=df_fhrp_group_members,
                       fhrp_root_text="-FHRP Root Table-",
                       df_fhrp_root=df_fhrp_root,
                       fhrp_glbp_forwarders_text="-FHRP GLBP Forwarders-",
                       df_fhrp_glbp_forwarders=df_fhrp_glbp_forwarders,
                       fhrp_virtual_gateways_text="-FHRP Virtual Gateways-",
                       df_fhrp_virtual_gateways=df_fhrp_virtual_gateways,
                       managed_networks_text="-Managed Networks-",
                       df_managed_networks=df_managed_networks,
                       gateway_redundancy_text="-Gateway Redundancy-",
                       df_gateway_redundancy=df_gateway_redundancy,
                       route_stability_text="-Route Stability-",
                       df_route_stability=df_route_stability,
                       ospf_nei_text="-OSPF Neighbors-",
                       df_ospf_nei=df_ospf_nei,
                       ospf_v3nei_text="-OSPFv3 Neighbors-",
                       df_ospf_v3nei=df_ospf_v3nei,
                       bgp_nei_text="-BGP Neighbors-",
                       df_bgp_nei=df_bgp_nei,
                       eigrp_nei_text="-EIGRP Neighbors-",
                       df_eigrp_nei=df_eigrp_nei,
                       rip_nei_text="-RIP Neighbors-",
                       df_rip_nei=df_rip_nei,
                       isis_nei_text="-IS-IS Neighbors-",
                       df_isis_nei=df_isis_nei,
                       path_verification_text="-Path Verification-",
                       df_path_verification=df_path_verification,
                       vrf_summary_text="-VRF Summary-",
                       df_vrf_summary=df_vrf_summary,
                       ldp_nei_text="-LDP Neighbors-",
                       df_ldp_nei=df_ldp_nei,
                       mpls_forwarding_text="-MPLS Forwarding-",
                       df_mpls_forwarding=df_mpls_forwarding,
                       l3vpn_routers_text="-L3-VPN Routers-",
                       df_l3vpn_routers=df_l3vpn_routers,
                       l2vpn_p2p_text="-L2-VPN Point-to-Point VPWS-",
                       df_l2vpn_p2p=df_l2vpn_p2p,
                       pim_nei_text="-PIM Neighbors-",
                       df_pim_nei=df_pim_nei,
                       mroute_overview_text="-MRoute Overview-",
                       df_mroute_overview=df_mroute_overview,
                       igmp_groups_text="-IGMP Groups-",
                       df_igmp_groups=df_igmp_groups,
                       igmp_snooping_text="-IGMP Snooping-",
                       df_igmp_snooping=df_igmp_snooping,
                       multicast_macs_text="-Multi-cast MAC Addresses-",
                       df_multicast_macs=df_multicast_macs,
                       rp_overview_text="-RP Overview-",
                       df_rp_overview=df_rp_overview,
                       aaa_servers_text="-AAA Servers-",
                       df_aaa_servers=df_aaa_servers,
                       telnet_access_text="-Telnet Access-",
                       df_telnet_access=df_telnet_access,
                       saved_configs_text="-Saved Configs-",
                       df_saved_configs=df_saved_configs,
                       ntp_summary_text="-NTP Summary-",
                       df_ntp_summary=df_ntp_summary,
                       port_mirroring_text="-Port Mirroring-",
                       df_port_mirroring=df_port_mirroring,
                       log_summary_text="-Log Summary-",
                       df_log_summary=df_log_summary,
                       flow_overview_text="-Flow Overview-",
                       df_flow_overview=df_flow_overview,
                       snmp_summary_text="-SNMP Summary-",
                       df_snmp_summary=df_snmp_summary,
                       ptp_local_clock_text="-PTP Local Clock-",
                       df_ptp_local_clock=df_ptp_local_clock,
                       acl_interfaces_text="-ACL Interfaces-",
                       df_acl_interfaces=df_acl_interfaces,
                       dmvpn_text="-DMVPNs-",
                       df_dmvpn=df_dmvpn,
                       dhcp_snooping_text="-DHCP Snooping-",
                       df_dhcp_snooping=df_dhcp_snooping,
                       ipsec_tunnels_text="-IPSec Tunnels-",
                       df_ipsec_tunnels=df_ipsec_tunnels,
                       secure_ports_devices_text="-Secure Ports Devices-",
                       df_secure_ports_devices=df_secure_ports_devices,
                       zone_fw_policies_text="-Zone Firewall Policies-",
                       df_zone_fw_policies=df_zone_fw_policies,
                       lb_virtual_servers_text="-Load-balancing Virtual Servers-",
                       df_lb_virtual_servers=df_lb_virtual_servers,
                       wireless_controllers_text="-Wireless Controllers-",
                       df_wireless_controllers=df_wireless_controllers,
                       wireless_aps_text="-Wireless Access-Points-",
                       df_wireless_aps=df_wireless_aps,
                       wireless_clients_text="-Wireless Clients-",
                       df_wireless_clients=df_wireless_clients,
                       voip_phones_text="-VOIP Phones-",
                       df_voip_phones=df_voip_phones,
                       aci_endpoint_text="-ACI Endpoints-",
                       df_aci_endpoints=df_aci_endpoints,
                       vxlan_vteps_text="-VXLan VTEPs-",
                       df_vxlan_vteps=df_vxlan_vteps,
                       sdwan_sites_text="-SD-WAN Sites-",
                       df_sdwan_sites=df_sdwan_sites,
                       udld_nei_text="-UDLD Neighbors-",
                       df_udld_nei=df_udld_nei,
                       )

with open(f'DOWNLOADS/{company_name}_customer_report.html', 'w') as f:
    f.write(html)

print("The Customer Report has been generated.")