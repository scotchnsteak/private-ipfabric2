
class DownloadAll():

    def download_all_func(self):

        from ipfabric import IPFClient
        from ipfabric.tools import DeviceConfigs
        from pathlib import Path
        import pandas as pd
        import os

        BASE_URL = os.getenv("BASE_URL")
        TOKEN = os.getenv("TOKEN")

        # Creating the directories needed for all the files downloaded from IP Fabric.
        Path("DOWNLOADS/configs").mkdir(parents=True, exist_ok=True)
        Path("DOWNLOADS/raw-tables").mkdir(parents=True, exist_ok=True)
        Path("DOWNLOADS/logs").mkdir(parents=True, exist_ok=True)

        ipf = IPFClient(BASE_URL, token=TOKEN, verify=False, timeout=30)
        cfg = DeviceConfigs(ipf)

        # Retrieve All Devices:
        devices = ipf.inventory.devices.all()

        def make_safe_filename(s):
            def safe_char(c):
                return c if c.isalnum() else "_"

            return "".join(safe_char(c) for c in s).rstrip("_")

        # Download both the configs file and the logs file:
        for device in devices:
            config = cfg.get_configuration(sn=device['sn'], sanitized=False, date='$last')
            if config:
                with open('DOWNLOADS/configs/' + make_safe_filename(device['hostname']) + '.txt', 'w') as file:
                    print(f"Config file downloaded for: {device['hostname']}")
                    file.write(config.text)
            else:
                print(f"Missing Config {device['hostname']}")
            if device['taskKey']:
                with open('DOWNLOADS/logs/' + make_safe_filename(device['hostname']) + '.txt', 'w') as file:
                    print(f"Log file downloaded for: {device['hostname']}")
                    file.write(cfg.get_text_log(device))  # cfg.get_test_log in 0.8.5 will be cfg.get_text_log in 0.8.6
            else:
                print(f"Missing Log File {device['hostname']}")

        # Download Sites table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/sites'))
        df.to_csv('DOWNLOADS/raw-tables/sites.csv')
        print("The Sites table has downloaded successfully.")

        # Download Devices table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.inventory.devices.all())
        df.to_csv('DOWNLOADS/raw-tables/devices.csv')
        print("The Devices table has downloaded successfully.")

        # Download Devices table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/summary/models'))
        df.to_csv('DOWNLOADS/raw-tables/device-models.csv')
        print("The Devices Models table has downloaded successfully.")

        # Download Devices table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/summary/platforms'))
        df.to_csv('DOWNLOADS/raw-tables/devices-platforms.csv')
        print("The Devices Platforms table has downloaded successfully.")

        # Download Devices table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/summary/families'))
        df.to_csv('DOWNLOADS/raw-tables/devices-families.csv')
        print("The Devices Families table has downloaded successfully.")

        # Download Devices table to CSV File to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/summary/vendors'))
        df.to_csv('DOWNLOADS/raw-tables/devices-vendors.csv')
        print("The Devices Vendors table has downloaded successfully.")

        # Download All Neighbors to CSV File in the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/pn'))
        df.to_csv('DOWNLOADS/raw-tables/part-numbers.csv')
        print("The All Neighbors table has downloaded successfully.")

        # Download Connectivity Matrix to CSV File in the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/osver-consistency'))
        df.to_csv('DOWNLOADS/raw-tables/os-versions.csv')
        print("The Connectivity Matrix table has downloaded successfully.")

        # Download OS-Version to check for Version Consistencey to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/interfaces.csv')
        print("The OS-Version table has downloaded successfully.")

        # Download the Hosts Table to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/hosts'))
        df.to_csv('DOWNLOADS/raw-tables/hosts.csv')
        print("The Hosts Table has downloaded successfully.")

        # Download the EOL Milestones Table to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/reports/eof/summary'))
        df.to_csv('DOWNLOADS/raw-tables/end-of-life-milestones.csv')
        print("The EOL Milestones table has downloaded successfully.")

        # Download the EOL Milestones Table to the inventory folder:
        df = pd.json_normalize(ipf.fetch_all('tables/reports/eof/detail'))
        df.to_csv('DOWNLOADS/raw-tables/end-of-life-milestones-detail.csv')
        print("The EOL Milestones Detail table has downloaded successfully.")

        # Download the Management Changes Table to the management folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/management/discovery-runs'))
        # df.to_csv('DOWNLOADS/management/changes.csv')
        # print("The Management Changes Table has downloaded successfully.")

        # # Download the Discovery-History Table to the management folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/inventory/discovery-history', snapshot=False))
        # df.to_csv('DOWNLOADS/management/discovery-history.csv')
        # print("The Discovery-History Table has downloaded successfully.")

        # Download the Juniper Cluster Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/cluster/srx'))
        df.to_csv('DOWNLOADS/raw-tables/juniper-cluster-srx.csv')
        print("The Juniper Cluster Table has downloaded successfully.")

        # Download the FEX Modules Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/fex/modules'))
        df.to_csv('DOWNLOADS/raw-tables/fex-modules.csv')
        print("The FEX Modules Table has downloaded successfully.")

        # Download the FEX Modules Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/fex/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/fex-modules-interfaces.csv')
        print("The FEX Modules Interfaces Table has downloaded successfully.")

        # # Download the VDC Devices Table to the tech/platforms folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/platforms/vdc/devices', snapshot=False))
        # df.to_csv('DOWNLOADS/technology/platforms/vdc-devices.csv')
        # print("The VDC Devices Table has downloaded successfully.")

        # # Download the VSS Overview Table to the tech/platforms folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/platforms/vss/overvie', snapshot=False))
        # df.to_csv('DOWNLOADS/technology/platforms/vss-overview.csv')
        # print("The VSS Overview Table has downloaded successfully.")

        # Download the VSS Overview Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/vss/chassis'))
        df.to_csv('DOWNLOADS/raw-tables/vss-chassis.csv')
        print("The VSS Chassis Table has downloaded successfully.")

        # Download the VSS Overview Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/vss/vsl'))
        df.to_csv('DOWNLOADS/raw-tables/vss-vsl.csv')
        print("The VSS VSL Table has downloaded successfully.")

        # Download the POE Devices Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/poe/devices'))
        df.to_csv('DOWNLOADS/raw-tables/poe-devices.csv')
        print("The POE Devices Table has downloaded successfully.")

        # Download the POE Devices Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/poe/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/poe-interfaces.csv')
        print("The POE Interfaces Table has downloaded successfully.")

        # Download the POE Devices Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/poe/modules'))
        df.to_csv('DOWNLOADS/raw-tables/poe-modules.csv')
        print("The POE Modules Table has downloaded successfully.")

        # Download the Stacks Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/stack'))
        df.to_csv('DOWNLOADS/raw-tables/stacks.csv')
        print("The Stacks Table has downloaded successfully.")

        # Download the Stacks Members Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/stack/members'))
        df.to_csv('DOWNLOADS/raw-tables/stacks-members.csv')
        print("The Stacks Members Table has downloaded successfully.")

        # Download the Stacks Connections Table to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/stack/connections'))
        df.to_csv('DOWNLOADS/raw-tables/stacks-connections.csv')
        print("The Stacks Connections Table has downloaded successfully.")

        # Download the Power Supplies to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/power-supplies'))
        df.to_csv('DOWNLOADS/raw-tables/power-supplies.csv')
        print("The Power Supplies table has downloaded successfully.")

        # Download the Power Supplies Fans to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/power-supplies-fans'))
        df.to_csv('DOWNLOADS/raw-tables/power-supplies-fans.csv')
        print("The Power Supplies Fans table has downloaded successfully.")

        # Download the Fans to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/fans'))
        df.to_csv('DOWNLOADS/raw-tables/fans.csv')
        print("The Fans table has downloaded successfully.")

        # Download the Modules Fans to the tech/platforms folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/modules'))
        df.to_csv('DOWNLOADS/raw-tables/modules.csv')
        print("The Modules table has downloaded successfully.")

        # Download the Current Data Rates Inbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/load/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/current-rates-inbound.csv')
        print("The Current Data Rates Inbound table has downloaded successfully.")

        # Download the Current Data Rates Outbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/load/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/current-rates-outbound.csv')
        print("The Current Data Rates Outbound table has downloaded successfully.")

        # Download the Current Data Rates to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/load/bidirectional'))
        df.to_csv('DOWNLOADS/raw-tables/current-rates-bidirectional.csv')
        print("The Current Data Rates Bidirectional table has downloaded successfully.")

        # Download the Average Data Rates Inbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-inbound.csv')
        print("The Average Data Rates Inbound table has downloaded successfully.")

        # Download the Average Data Rates Outbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-outbound.csv')
        print("The Average Data Rates Outbound table has downloaded successfully.")

        # Download the Average Data Rates Bidirectional to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/bidirectional'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-bidirectional.csv')
        print("The Average Data Rates Bidirectional table has downloaded successfully.")

        # Download the Average Data Rates Inbound-Device to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/inbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-inbound-device.csv')
        print("The Average Data Rates Inbound-Device table has downloaded successfully.")

        # Download the Average Data Rates Outbound-Deviceto the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/outbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-outbound-device.csv')
        print("The Average Data Rates Outbound-Device table has downloaded successfully.")

        # Download the Average Data Rates Bidirectional-Device to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transfer-rates/bidirectional-device'))
        df.to_csv('DOWNLOADS/raw-tables/transfer-rates-bidirectional-device.csv')
        print("The Average Data Rates Bidirectional-device table has downloaded successfully.")

        # Download the Average Error Rates Inbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/errors-inbound.csv')
        print("The Average Error Rates Inbound table has downloaded successfully.")

        # Download the Average Error Rates Outbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/errors-outbound.csv')
        print("The Average Error Rates Outbound table has downloaded successfully.")

        # Download the Average Error Rates Bidirectional to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/bidirectional'))
        df.to_csv('DOWNLOADS/raw-tables/errors-bidirectional.csv')
        print("The Average Error Rates Bidirectional table has downloaded successfully.")

        # Download the Average Error Rates Inbound-Device to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/inbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/errors-inbound-device.csv')
        print("The Average Error Rates Inbound-Device table has downloaded successfully.")

        # Download the Average Error Rates Outbound-Device to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/outbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/errors-outbound-device.csv')
        print("The Average Error Rates Outbound-Device table has downloaded successfully.")

        # Download the Average Error Rates Bidirectional-Device to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/bidirectional-device'))
        df.to_csv('DOWNLOADS/raw-tables/errors-bidirectional-device.csv')
        print("The Average Error Rates Bidirectional-Device table has downloaded successfully.")

        # Download the Average Drop Rates Inbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/drops-inbound.csv')
        print("The Average Drop Rates table has downloaded successfully.")

        # Download the Average Drop Rates Outbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/drops-outbound.csv')
        print("The Average Drop Rates Outbound table has downloaded successfully.")

        # Download the Average Drop Rates Bidirectional to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/bidirectional'))
        df.to_csv('DOWNLOADS/raw-tables/drops-bidirectional.csv')
        print("The Average Drop Rates Bidirectional table has downloaded successfully.")

        # Download the Average Drop Rates Inbound-Devices to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/inbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/drops-inbound-device.csv')
        print("The Average Drop Rates Inbound Devices table has downloaded successfully.")

        # Download the Average Drop Rates Outbound-Devices to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/outbound-device'))
        df.to_csv('DOWNLOADS/raw-tables/drops-outbound-device.csv')
        print("The Average Drop Rates Outbound-Devices table has downloaded successfully.")

        # Download the Average Drop Rates Bidirectional-Devices to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/drops/bidirectional-device'))
        df.to_csv('DOWNLOADS/raw-tables/drops-bidirectional-device.csv')
        print("The Average Drop Rates Bidirectional-Devices table has downloaded successfully.")

        # Download the Duplex Mismatch Interfaces to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/duplex'))
        df.to_csv('DOWNLOADS/raw-tables/duplex-mismatch.csv')
        print("The Duplex Mismatch Interfaces table has downloaded successfully.")

        # Download the Error Disabled Interfaces to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/errors/disabled'))
        df.to_csv('DOWNLOADS/raw-tables/errdisabled.csv')
        print("The Error Disabled Interfaces table has downloaded successfully.")

        # Download the Connectivity Matrix to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/connectivity-matrix'))
        df.to_csv('DOWNLOADS/raw-tables/connectivity-matrix.csv')
        print("The Connectivity Matrix table has downloaded successfully.")

        # Download the Unmanaged Neighbors Summary to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/connectivity-matrix/unmanaged-neighbors/summary'))
        df.to_csv('DOWNLOADS/raw-tables/unmanaged-neighbors-summary.csv')
        print("The Unmanaged Neighbors Summary table has downloaded successfully.")

        # Download the Unmanaged Neighbors Details to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/connectivity-matrix/unmanaged-neighbors/detail'))
        df.to_csv('DOWNLOADS/raw-tables/unmanaged-neighbors-details.csv')
        print("The Unmanaged Neighbors Details table has downloaded successfully.")

        # Download the Switchport Intefaces to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/switchports'))
        df.to_csv('DOWNLOADS/raw-tables/switchports.csv')
        print("The Switchport Intefaces table has downloaded successfully.")

        # Download the MTU Interfaces to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/mtu'))
        df.to_csv('DOWNLOADS/raw-tables/mtu.csv')
        print("The MTU Interfaces table has downloaded successfully.")

        # Download the Storm Control Broadcast to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/storm-control/broadcast'))
        df.to_csv('DOWNLOADS/raw-tables/storm-control-broadcast.csv')
        print("The Storm Control Broadcast table has downloaded successfully.")

        # Download the Storm Control Unicast to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/storm-control/unicast'))
        df.to_csv('DOWNLOADS/raw-tables/storm-control-unicast.csv')
        print("The Storm Control Unicast table has downloaded successfully.")

        # Download the Storm Control Multicast to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/storm-control/multicast'))
        df.to_csv('DOWNLOADS/raw-tables/storm-control-multicast.csv')
        print("The Storm Control Multicast table has downloaded successfully.")

        # Download the Storm Control All-Traffic to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/storm-control/all'))
        df.to_csv('DOWNLOADS/raw-tables/storm-control-all-traffic.csv')
        print("The Storm Control All-Traffic table has downloaded successfully.")

        # Download the Transceivers Inventory to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transceivers/inventory'))
        df.to_csv('DOWNLOADS/raw-tables/transceivers-inventory.csv')
        print("The Transceivers Inventory table has downloaded successfully.")

        # Download the Transceivers Statistics to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transceivers/statistics'))
        df.to_csv('DOWNLOADS/raw-tables/transceivers-statistics.csv')
        print("The Transceivers Statistics table has downloaded successfully.")

        # Download the Transceivers Thresholds to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transceivers/thresholds'))
        df.to_csv('DOWNLOADS/raw-tables/transceivers-thresholds.csv')
        print("The Transceivers Thresholds table has downloaded successfully.")

        # Download the Transceivers Errors to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/transceivers/errors'))
        df.to_csv('DOWNLOADS/raw-tables/transceivers-errors.csv')
        print("The Transceivers Errors table has downloaded successfully.")

        # Download the PPPoE Interfaces to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/pppoe'))
        df.to_csv('DOWNLOADS/raw-tables/pppoe-interfaces.csv')
        print("The PPPoE Interfaces table has downloaded successfully.")

        # Download the PPPoE Sessions to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/pppoe/sessions'))
        df.to_csv('DOWNLOADS/raw-tables/pppoe-sessions.csv')
        print("The PPPoE Sessions table has downloaded successfully.")

        # Download the Interface Counters Inbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/counters/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/counters-inbound.csv')
        print("The Counters Inbound table has downloaded successfully.")

        # Download the Interface Counters Outbound to the interfaces folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/counters/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/counters-outbound.csv')
        print("The Counters Outbound table has downloaded successfully.")

        # Download the All Neighbors to the cdp-lldp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/neighbors/all'))
        df.to_csv('DOWNLOADS/raw-tables/all-neighbors.csv')
        print("The All Neighbors table has downloaded successfully.")

        # Download the Unmanaged Neighbors to the cdp-lldp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/neighbors/unmanaged'))
        df.to_csv('DOWNLOADS/raw-tables/unmanaged-neighbors.csv')
        print("The Unmanaged Neighbors table has downloaded successfully.")

        # Download the Unidirectional Neighbors to the cdp-lldp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/neighbors/unidirectional'))
        df.to_csv('DOWNLOADS/raw-tables/unidirectional-neighbors.csv')
        print("The Unidirectional Neighbors table has downloaded successfully.")

        # Download the Port-Channel Inbound Load-Balancing to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/port-channel/balance/inbound'))
        df.to_csv('DOWNLOADS/raw-tables/inbound-balancing-table.csv')
        print("The Port-Channel Inbound Load-Balancing table has downloaded successfully.")

        # Download the Port-Channel Outbound Load-Balancing to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/port-channel/balance/outbound'))
        df.to_csv('DOWNLOADS/raw-tables/outbound-balancing-table.csv')
        print("The Port-Channel Outbound Load-Balancing table has downloaded successfully.")

        # Download the Port-Channel Member Status to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/port-channel/member-status'))
        df.to_csv('DOWNLOADS/raw-tables/member-status-table.csv')
        print("The Port-Channel Member Status table has downloaded successfully.")

        # Download the Port-Channel MLAG VPC INFO to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/mlag/vpc'))
        df.to_csv('DOWNLOADS/raw-tables/mlag-vpc.csv')
        print("The Port-Channel MLAG VPC INFO table has downloaded successfully.")

        # Download the Port-Channel MLAG Switches to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/mlag/switches'))
        df.to_csv('DOWNLOADS/raw-tables/mlag-switches.csv')
        print("The Port-Channel MLAG Switches table has downloaded successfully.")

        # Download the Port-Channel MLAG Peers to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/mlag/peers'))
        df.to_csv('DOWNLOADS/raw-tables/mlag-peer-links.csv')
        print("The Port-Channel MLAG Peers table has downloaded successfully.")

        # Download the Port-Channel MLAG Pairs to the port-channel folder:
        df = pd.json_normalize(ipf.fetch_all('tables/platforms/mlag/pairs'))
        df.to_csv('DOWNLOADS/raw-tables/mlag-pairs.csv')
        print("The Port-Channel MLAG Pairs table has downloaded successfully.")

        # Download the VLAN Device Summary to the vlans folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vlan/device-summary'))
        df.to_csv('DOWNLOADS/raw-tables/device-summary.csv')
        print("The VLAN Device Summary table has downloaded successfully.")

        # Download the VLAN Device Detail to the vlans folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vlan/device'))
        df.to_csv('DOWNLOADS/raw-tables/device-detail.csv')
        print("The VLAN Device Detail table has downloaded successfully.")

        # Download the VLAN Network Summary to the vlans folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vlan/network-summary'))
        df.to_csv('DOWNLOADS/raw-tables/network-summary.csv')
        print("The VLAN Device Summary table has downloaded successfully.")

        # Download the VLAN Site Summary to the vlans folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vlan/site-summary'))
        df.to_csv('DOWNLOADS/raw-tables/site-summary.csv')
        print("The VLAN Site Summary table has downloaded successfully.")

        # Download the VLAN L3-Gateways to the vlans folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vlan/l3-gateways'))
        df.to_csv('DOWNLOADS/raw-tables/l3-gateways.csv')
        print("The VLAN L3-Gateways table has downloaded successfully.")

        # Download the STP Stability Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/topology'))
        df.to_csv('DOWNLOADS/raw-tables/stp-stability.csv')
        print("The STP Stability Summary table has downloaded successfully.")

        # Download the STP Bridges Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/bridges'))
        df.to_csv('DOWNLOADS/raw-tables/stp-bridges.csv')
        print("The STP Bridges Summary table has downloaded successfully.")

        # Download the STP Instances Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/instances'))
        df.to_csv('DOWNLOADS/raw-tables/stp-instances.csv')
        print("The STP Instances Summary table has downloaded successfully.")

        # Download the STP VLANs Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/vlans'))
        df.to_csv('DOWNLOADS/raw-tables/stp-vlans.csv')
        print("The STP VLANs Summary table has downloaded successfully.")

        # Download the STP Virtual Ports Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/ports'))
        df.to_csv('DOWNLOADS/raw-tables/stp-virtual-ports.csv')
        print("The STP Virtual Ports Summary table has downloaded successfully.")

        # Download the STP Neighbors to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/stp-neighbors.csv')
        print("The STP Neighbors table has downloaded successfully.")

        # Download the STP Guards Summary to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/guards'))
        df.to_csv('DOWNLOADS/raw-tables/stp-guards.csv')
        print("The STP Guards Summary table has downloaded successfully.")

        # Download the STP Inconsistencies to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/interfaces/inconsistencies/summary'))
        df.to_csv('DOWNLOADS/raw-tables/stp-inconsistencies.csv')
        print("The STP Inconsistencies table has downloaded successfully.")

        # Download the Neighbor Ports VLAN Mismatch to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/inconsistencies/neighbor-ports-vlan-mismatch'))
        df.to_csv('DOWNLOADS/raw-tables/neighbor-ports-vlan-mismatch.csv')
        print("The Neighbor Ports VLAN Mismatch table has downloaded successfully.")

        # Download the Ports With Multiple Neighbors to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/inconsistencies/ports-multiple-neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/stp-ports-multiple-neighbors.csv')
        print("The Ports with Multiple Neighbors table has downloaded successfully.")

        # Download the STP CDP Ports Mismatch to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/inconsistencies/stp-cdp-ports-mismatch'))
        df.to_csv('DOWNLOADS/raw-tables/stp-cdp-ports-mismatch.csv')
        print("The STP CDP Ports Mismatch table has downloaded successfully.")

        # Download the Multiple STP to the spanning-tree folder:
        df = pd.json_normalize(ipf.fetch_all('tables/spanning-tree/inconsistencies/multiple-stp'))
        df.to_csv('DOWNLOADS/raw-tables/stp-multiple-stp.csv')
        print("The STP Multiple STP table has downloaded successfully.")

        # Download the ARP Table to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/arp'))
        df.to_csv('DOWNLOADS/raw-tables/arp-table.csv')
        print("The ARP Table table has downloaded successfully.")

        # Download the Managed IP Info to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/mac'))
        df.to_csv('DOWNLOADS/raw-tables/mac-table.csv')
        print("The Managed IP Info table has downloaded successfully.")

        # Download the Managed IPs to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/managed-devs'))
        df.to_csv('DOWNLOADS/raw-tables/managed-ip.csv')
        print("The Managed IPs table has downloaded successfully.")

        # Download the Duplicate IPs to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/duplicate-ip'))
        df.to_csv('DOWNLOADS/raw-tables/duplicate-ip.csv')
        print("The Duplicate IPs table has downloaded successfully.")

        # Download the NAT Rules to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/nat/rules'))
        df.to_csv('DOWNLOADS/raw-tables/nat-rules.csv')
        print("The NAT Rules table has downloaded successfully.")

        # Download the NAT Pools to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/addressing/nat/pools'))
        df.to_csv('DOWNLOADS/raw-tables/nat-pools.csv')
        print("The NAT Pools table has downloaded successfully.")

        # Download the FHRP State to the fhrp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/group-state'))
        df.to_csv('DOWNLOADS/raw-tables/group-state.csv')
        print("The FHRP State table has downloaded successfully.")

        # Download the FHRP Group Members to the fhrp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/group-members'))
        df.to_csv('DOWNLOADS/raw-tables/group-members.csv')
        print("The FHRP Group Members table has downloaded successfully.")

        # Download the FHRP STP Gateway Root Alignment to the fhrp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/stproot-alignment'))
        df.to_csv('DOWNLOADS/raw-tables/active-gw-root-alignment.csv')
        print("The FHRP STP Gateway Root Alignment table has downloaded successfully.")

        # Download the FHRP Active Gateway Balancing to the fhrp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/balancing'))
        df.to_csv('DOWNLOADS/raw-tables/active-gw-balancing.csv')
        print("The FHRP Active Gateway Balancing table has downloaded successfully.")

        # Download the GLBP Forwarders to the fhrp folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/glbp-forwarders'))
        df.to_csv('DOWNLOADS/raw-tables/glbp-forwarders.csv')
        print("The GLBP Forwarders table has downloaded successfully.")

        # Download the Virtual Gateways to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/fhrp/virtual-gateways'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-gateways.csv')
        print("The Virtual Gateways table has downloaded successfully.")

        # Download the Managed Networks to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks'))
        df.to_csv('DOWNLOADS/raw-tables/managed-networks.csv')
        print("The Managed Networks table has downloaded successfully.")

        # Download the Gateway Redundancy to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks'))
        df.to_csv('DOWNLOADS/raw-tables/gateway-redundancy.csv')
        print("The Gateway Redundancy table has downloaded successfully.")

        # Download the Network Summary Protocols to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols.csv')
        print("The Networks Summary Protocols table has downloaded successfully.")

        # Download the Network Summary Protocols BGP to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols/BGP'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols-bgp.csv')
        print("The Networks Summary Protocols BGP table has downloaded successfully.")

        # Download the Network Summary Protocols EIGRP to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols-eigrp.csv')
        print("The Networks Summary Protocols EIGRP table has downloaded successfully.")

        # Download the Network Summary Protocols IS-IS to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols/isis'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols-isis.csv')
        print("The Networks Summary Protocols IS-IS table has downloaded successfully.")

        # Download the Network Summary Protocols OSPF to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols/ospf'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols-ospf.csv')
        print("The Networks Summary Protocols OSPF table has downloaded successfully.")

        # # Download the Network Summary Protocols OSPFv3 to the networks folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols/ospfv3'))
        # df.to_csv('DOWNLOADS/raw-tables/summary-protocols-ospfv3.csv')
        # print("The Networks Summary Protocols OSPFv3 table has downloaded successfully.")

        # Download the Network Summary Protocols RIP to the networks folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/summary/protocols'))
        df.to_csv('DOWNLOADS/raw-tables/summary-protocols-rip.csv')
        print("The Networks Summary Protocols RIP table has downloaded successfully.")

        # Download the Routes to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/routes'))
        df.to_csv('DOWNLOADS/raw-tables/routes.csv')
        print("The Routes table has downloaded successfully.")

        # Download the Route Stability Table to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/route-stability'))
        df.to_csv('DOWNLOADS/raw-tables/route-stability.csv')
        print("The Route Stability Table table has downloaded successfully.")

        # Download the OSPF Neighbors to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/ospf/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/ospf-neighbors.csv')
        print("The OSPF Neighbors table has downloaded successfully.")

        # Download the OSPF Interfaces to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/ospf/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/ospf-interfaces.csv')
        print("The OSPF Interfaces table has downloaded successfully.")

        # # Download the OSPFv3 Neighbors to the routing folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/ospf-v3/neighbors'))
        # df.to_csv('DOWNLOADS/raw-tables/ospf-v3-neighbors.csv')
        # print("The OSPFv3 Neighbors table has downloaded successfully.")
        #
        # # Download the OSPFv3 Interfaces to the routing folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/ospf-v3/interfaces'))
        # df.to_csv('DOWNLOADS/raw-tables/ospf-v3-interfaces.csv')
        # print("The OSPFv3 Interfaces table has downloaded successfully.")

        # Download the BGP Neighbors to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/bgp/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/bgp-neighbors.csv')
        print("The BGP Neighbors table has downloaded successfully.")

        # Download the BGP Address Families to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/bgp/address-families'))
        df.to_csv('DOWNLOADS/raw-tables/bgp-address-families.csv')
        print("The BGP Address Families table has downloaded successfully.")

        # Download the EIGRP Neighbors to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/eigrp/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/eigrp-neighbors.csv')
        print("The EIGRP Neighbors table has downloaded successfully.")

        # Download the EIGRP Interfaces to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/eigrp/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/eigrp-interfaces.csv')
        print("The EIGRP Interfaces table has downloaded successfully.")

        # Download the RIP Neighbors to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/rip/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/rip-neighbors.csv')
        print("The RIP Neighbors table has downloaded successfully.")

        # Download the RIP Interfaces to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/rip/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/rip-interfaces.csv')
        print("The RIP Interfaces table has downloaded successfully.")

        # Download the IS-IS Neighbors to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/is-is/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/is-is-neighbors.csv')
        print("The IS-IS Neighbors table has downloaded successfully.")

        # Download the IS-IS Interfaces to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/routing/protocols/is-is/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/is-is-interfaces.csv')
        print("The IS-IS Interfaces table has downloaded successfully.")

        # Download the Path Lookup Checks to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/networks/path-lookup-checks'))
        df.to_csv('DOWNLOADS/raw-tables/path-verifications.csv')
        print("The Path Lookup Checks table has downloaded successfully.")

        # Download the VRF Summary to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vrf/summary'))
        df.to_csv('DOWNLOADS/raw-tables/vrf-summary.csv')
        print("The VRF Summary table has downloaded successfully.")

        # Download the VRF Detail to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vrf/detail'))
        df.to_csv('DOWNLOADS/raw-tables/vrf-detail.csv')
        print("The VRF Detail table has downloaded successfully.")

        # Download the VRF Interfaces to the routing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vrf/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/vrf-interfaces.csv')
        print("The VRF Interfaces table has downloaded successfully.")

        # Download the LDP Neighbors to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/ldp/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/ldp-neighbors.csv')
        print("The LDP Neighbors table has downloaded successfully.")

        # Download the LDP Interfaces to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/ldp/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/ldp-interfaces.csv')
        print("The LDP Interfaces table has downloaded successfully.")

        # Download the MPLS Forwarding to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/forwarding'))
        df.to_csv('DOWNLOADS/raw-tables/mpls-forwarding.csv')
        print("The MPLS Forwarding table has downloaded successfully.")

        # Download the PE Routers to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l3-vpn/pe-routers'))
        df.to_csv('DOWNLOADS/raw-tables/l3vpn-pe-routers.csv')
        print("The PE Routers table has downloaded successfully.")

        # Download the PE VRFs to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l3-vpn/pe-vrfs'))
        df.to_csv('DOWNLOADS/raw-tables/l3vpn-pe-vrfs.csv')
        print("The PE VRFs table has downloaded successfully.")

        # Download the PE Targets to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l3-vpn/vrf-targets'))
        df.to_csv('DOWNLOADS/raw-tables/l3vpn-vrf-targets.csv')
        print("The PE Targets table has downloaded successfully.")

        # # Download the PE Routes to the mpls folder:
        # df = pd.json_normalize(ipf.fetch_all('tables/mpls/l3-vpn/pe-routes'))
        # df.to_csv('DOWNLOADS/technology/mpls/l3vpn-pe-routes.csv')
        # print("The PE Routes table has downloaded successfully.")

        # Download the P2P VPWS to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l2-vpn/point-to-point-vpws'))
        df.to_csv('DOWNLOADS/raw-tables/l2vpn-point-to-point-vpws.csv')
        print("The P2P VPWS table has downloaded successfully.")

        # Download the P2-Multipoint to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l2-vpn/point-to-multipoint'))
        df.to_csv('DOWNLOADS/raw-tables/l2vpn-point-to-multipoint.csv')
        print("The P2-Multipoint table has downloaded successfully.")

        # Download the Circuit Cross Connect to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l2-vpn/curcit-cross-connect'))
        df.to_csv('DOWNLOADS/raw-tables/l2vpn-circuit-cross-connect.csv')
        print("The Circuit Cross Connect table has downloaded successfully.")

        # Download the Pseudowires to the mpls folder:
        df = pd.json_normalize(ipf.fetch_all('tables/mpls/l2-vpn/pseudowires'))
        df.to_csv('DOWNLOADS/raw-tables/pseudowires.csv')
        print("The Pseudowires table has downloaded successfully.")

        # Download the PIM Neighbors to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/pim-neighbors.csv')
        print("The PIM Neighbors table has downloaded successfully.")

        # Download the PIM Interfaces to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/pim-interfaces.csv')
        print("The PIM Interfaces table has downloaded successfully.")

        # Download the MRoute Overview to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/overview'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-overview.csv')
        print("The MRoute Overview table has downloaded successfully.")

        # Download the MRoute Table to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/table'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-table.csv')
        print("The MRoute Table has downloaded successfully.")

        # Download the MRoute Outgoing Interfaces to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/outgoing-interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-outgoing-interfaces.csv')
        print("The MRoute Outgoing Interfaces table has downloaded successfully.")

        # Download the MRoute Counters to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/counters'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-counters.csv')
        print("The MRoute Counters table has downloaded successfully.")

        # Download the MRoute First-Hop to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/first-hop-router'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-first-hop-router.csv')
        print("The MRoute First Hop Router table has downloaded successfully.")

        # Download the MRoute Sources to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/routes/sources'))
        df.to_csv('DOWNLOADS/raw-tables/mroute-sources.csv')
        print("The MRoute Sources table has downloaded successfully.")

        # Download the IGMP Routes to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/igmp/groups'))
        df.to_csv('DOWNLOADS/raw-tables/igmp-groups.csv')
        print("The IGMP Routes table has downloaded successfully.")

        # Download the IGMP Interfaces to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/igmp/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/igmp-interfaces.csv')
        print("The IGMP Interfaces table has downloaded successfully.")

        # Download the IGMP Snooping to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/igmp/snooping/global'))
        df.to_csv('DOWNLOADS/raw-tables/igmp-snooping-global.csv')
        print("The IGMP Snooping Global table has downloaded successfully.")

        # Download the IGMP Snooping VLANs to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/igmp/snooping/vlans'))
        df.to_csv('DOWNLOADS/raw-tables/igmp-snooping-vlans.csv')
        print("The IGMP Snooping VLANs table has downloaded successfully.")

        # Download the IGMP Snooping Groups to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/igmp/snooping/groups'))
        df.to_csv('DOWNLOADS/raw-tables/igmp-snooping-groups.csv')
        print("The IGMP Snooping Groups table has downloaded successfully.")

        # Download the Multiast MACs to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/mac'))
        df.to_csv('DOWNLOADS/raw-tables/macs.csv')
        print("The Multiast MACs table has downloaded successfully.")

        # Download the RP Overview to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/rp/overview'))
        df.to_csv('DOWNLOADS/raw-tables/rp-overview.csv')
        print("The RP Overview table has downloaded successfully.")

        # Download the RP BSR to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/rp/bsr'))
        df.to_csv('DOWNLOADS/raw-tables/rp-bsr.csv')
        print("The RP BSR table has downloaded successfully.")

        # Download the RP Mappings to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/rp/mappings'))
        df.to_csv('DOWNLOADS/raw-tables/rp-mappings.csv')
        print("The RP Mappings table has downloaded successfully.")

        # Download the RP Mappings Groups to the multicast folder:
        df = pd.json_normalize(ipf.fetch_all('tables/multicast/pim/rp/mappings-groups'))
        df.to_csv('DOWNLOADS/raw-tables/rp-mappings-groups.csv')
        print("The RP Mappings Groups table has downloaded successfully.")

        # Download the AAA Servers to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/servers'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-servers.csv')
        print("The AAA Servers table has downloaded successfully.")

        # Download the AAA Lines to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/lines'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-lines.csv')
        print("The AAA Lines table has downloaded successfully.")

        # Download the AAA Authentication to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/authentication'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-authentication.csv')
        print("The AAA Authentication table has downloaded successfully.")

        # Download the AAA Authorization to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/authorization'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-authorization.csv')
        print("The AAA Authorization table has downloaded successfully.")

        # Download the AAA Accounting to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/accounting'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-accounting.csv')
        print("The AAA Accounting table has downloaded successfully.")

        # Download the AAA Users to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/users'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-users.csv')
        print("The AAA Users table has downloaded successfully.")

        # Download the AAA Password-Strength to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/aaa/password-strength'))
        df.to_csv('DOWNLOADS/raw-tables/aaa-password-strength.csv')
        print("The AAA Password-Strength table has downloaded successfully.")

        # Download the Telnet Access to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/enabled-telnet'))
        df.to_csv('DOWNLOADS/raw-tables/telnet-access.csv')
        print("The Telnet Access table has downloaded successfully.")

        # Download the Saved Config Consistency to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/configuration/saved'))
        df.to_csv('DOWNLOADS/raw-tables/saved-config-consistency.csv')
        print("The Saved Config Consistency table has downloaded successfully.")

        # Download the NTP Summary to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/ntp/summary'))
        df.to_csv('DOWNLOADS/raw-tables/ntp-summary.csv')
        print("The NTP Summary table has downloaded successfully.")

        # Download the NTP Sources to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/ntp/sources'))
        df.to_csv('DOWNLOADS/raw-tables/ntp-sources.csv')
        print("The NTP Sources table has downloaded successfully.")

        # Download the Port Mirroring to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/port-mirroring'))
        df.to_csv('DOWNLOADS/raw-tables/port-mirroring.csv')
        print("The Port Mirroring table has downloaded successfully.")

        # Download the Logging Summary to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/logging/summary'))
        df.to_csv('DOWNLOADS/raw-tables/logging-summary.csv')
        print("The Logging Summary table has downloaded successfully.")

        # Download the Logging Remote to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/logging/remote'))
        df.to_csv('DOWNLOADS/raw-tables/logging-remote.csv')
        print("The Logging Remote table has downloaded successfully.")

        # Download the Logging Local to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/logging/local'))
        df.to_csv('DOWNLOADS/raw-tables/logging-local.csv')
        print("The Logging Local table has downloaded successfully.")

        # Download the Flow Overview to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/overview'))
        df.to_csv('DOWNLOADS/raw-tables/flow-overview.csv')
        print("The Flow Overview table has downloaded successfully.")

        # Download the Flow Devices to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/netflow/devices'))
        df.to_csv('DOWNLOADS/raw-tables/netflow-flow-devices.csv')
        print("The Netflow Devices table has downloaded successfully.")

        # Download the Flow Collectors to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/netflow/collectors'))
        df.to_csv('DOWNLOADS/raw-tables/netflow-collectors.csv')
        print("The Netflow Collectors table has downloaded successfully.")

        # Download the Flow Interfaces to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/netflow/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/netflow-interfaces.csv')
        print("The Netflow Interfaces table has downloaded successfully.")

        # Download the SFlow Devices to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/sflow/devices'))
        df.to_csv('DOWNLOADS/raw-tables/sflow-devices.csv')
        print("The SFlow Devices table has downloaded successfully.")

        # Download the Flow Collectors to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/sflow/collectors'))
        df.to_csv('DOWNLOADS/raw-tables/sflow-collectors.csv')
        print("The SFlow Collectors table has downloaded successfully.")

        # Download the Flow Sources to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/flow/sflow/sources'))
        df.to_csv('DOWNLOADS/raw-tables/sflow-sources.csv')
        print("The SFlow Sources table has downloaded successfully.")

        # Download the SNMP Summary to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/snmp/summary'))
        df.to_csv('DOWNLOADS/raw-tables/snmp-summary.csv')
        print("The SNMP Summary table has downloaded successfully.")

        # Download the SNMP Communities to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/snmp/communities'))
        df.to_csv('DOWNLOADS/raw-tables/snmp-communities.csv')
        print("The SNMP Communities table has downloaded successfully.")

        # Download the SNMP Trap Hosts to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/snmp/trap-hosts'))
        df.to_csv('DOWNLOADS/raw-tables/snmp-trap-hosts.csv')
        print("The SNMP Trap Hosts table has downloaded successfully.")

        # Download the SNMP Users to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/snmp/users'))
        df.to_csv('DOWNLOADS/raw-tables/snmp-users.csv')
        print("The SNMP Users table has downloaded successfully.")

        # Download the PTP Local Clock to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/ptp/local-clock'))
        df.to_csv('DOWNLOADS/raw-tables/ptp-local-clock.csv')
        print("The PTP Local Clock table has downloaded successfully.")

        # Download the PTP Masters to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/ptp/masters'))
        df.to_csv('DOWNLOADS/raw-tables/ptp-masters.csv')
        print("The PTP Masters table has downloaded successfully.")

        # Download the PTP Interfaces to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/ptp/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/ptp-interfaces.csv')
        print("The PTP Interfaces table has downloaded successfully.")

        # Download Licenses Summary to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses/summary'))
        df.to_csv('DOWNLOADS/raw-tables/licenses-summary.csv')
        print("The Licenses Summary table has downloaded successfully.")

        # Download Licenses to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses'))
        df.to_csv('DOWNLOADS/raw-tables/licenses.csv')
        print("The Licenses table has downloaded successfully.")

        # Download Licenses Detail to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses/detail'))
        df.to_csv('DOWNLOADS/raw-tables/licenses-detail.csv')
        print("The Licenses Detail table has downloaded successfully.")

        # Download Smartnet Authorization to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses/cisco-smart-licenses/authorization'))
        df.to_csv('DOWNLOADS/raw-tables/smartnet-authorization.csv')
        print("The Smartnet Authorization table has downloaded successfully.")

        # Download Smartnet Registration to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses/cisco-smart-licenses/registration'))
        df.to_csv('DOWNLOADS/raw-tables/smartnet-registration.csv')
        print("The Smartnet Registration table has downloaded successfully.")

        # Download Smartnet Reservations to the management folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/licenses/cisco-smart-licenses/reservations'))
        df.to_csv('DOWNLOADS/raw-tables/smartnet-reservations.csv')
        print("The Smartnet Reservations table has downloaded successfully.")

        # Download the Security ACL Global Policies to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/acl/global-policies'))
        df.to_csv('DOWNLOADS/raw-tables/acl-global-policies.csv')
        print("The Security ACL Global Policies table has downloaded successfully.")

        # Download the Security ACL to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/acl'))
        df.to_csv('DOWNLOADS/raw-tables/acls.csv')
        print("The Security ACL table has downloaded successfully.")

        # Download the ACL Interfaces to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/acl/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/acl-interfaces.csv')
        print("The ACL Interfaces table has downloaded successfully.")

        # Download Security DMVPN to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/dmvpn'))
        df.to_csv('DOWNLOADS/raw-tables/dmvpn.csv')
        print("The Security DMVPN table has downloaded successfully.")

        # Download DHCP Snooping to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/dhcp/snooping'))
        df.to_csv('DOWNLOADS/raw-tables/dhcp-snooping.csv')
        print("The DHCP Snooping table has downloaded successfully.")

        # Download DHCP Binding to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/dhcp/bindings'))
        df.to_csv('DOWNLOADS/raw-tables/dhcp-bindings.csv')
        print("The DHCP Bindings table has downloaded successfully.")

        # Download IPSec Tunnels to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/ipsec/tunnels'))
        df.to_csv('DOWNLOADS/raw-tables/ipsec-tunnels.csv')
        print("The IPSec Tunnels table has downloaded successfully.")

        # Download IPSec Gateways to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/ipsec/gateways'))
        df.to_csv('DOWNLOADS/raw-tables/ipsec-gateways.csv')
        print("The IPSec Gateways table has downloaded successfully.")

        # Download Secure Ports Devices to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/secure-ports/devices'))
        df.to_csv('DOWNLOADS/raw-tables/secure-ports-devices.csv')
        print("The Secure Ports Devices table has downloaded successfully.")
        #
        # Download Secure Ports Interfaces to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/secure-ports/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/secure-ports-interfaces.csv')
        print("The Secure Ports Interfaces table has downloaded successfully.")

        # Download Secure Ports Users to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/secure-ports/users'))
        df.to_csv('DOWNLOADS/raw-tables/secure-ports-users.csv')
        print("The Secure Ports Users table has downloaded successfully.")

        # Download the Zone Firewall Policies to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/zone-firewall/policies'))
        df.to_csv('DOWNLOADS/raw-tables/zone-firewall-policies.csv')
        print("The Zone Firewall Policies table has downloaded successfully.")

        # Download the Zone Firewall Interfaces to the security folder:
        df = pd.json_normalize(ipf.fetch_all('tables/security/zone-firewall/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/zone-firewall-interfaces.csv')
        print("The Zone Firewall Interfaces table has downloaded successfully.")

        # Download Load Balancing Virtual Servers to the load-balancing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/load-balancing/virtual-servers'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-servers.csv')
        print("The Load Balancing Virtual Servers table has downloaded successfully.")

        # Download Load Balancing Virtual Servers Pools to the load-balancing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/load-balancing/virtual-servers/pools'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-servers-pools.csv')
        print("The Load Balancing Virtual Servers Pools table has downloaded successfully.")

        # Download Load Balancing Virtual Servers Pool Members to the load-balancing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/load-balancing/virtual-servers/pool-members'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-servers-pool-members.csv')
        print("The Load Balancing Virtual Servers Pool Members table has downloaded successfully.")

        # Download Load Balancing F5 Partitions to the load-balancing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/load-balancing/f5-partitions'))
        df.to_csv('DOWNLOADS/raw-tables/f5-partitions.csv')
        print("The Load Balancing F5 Partitions table has downloaded successfully.")

        # Download Wireless Controllers to the wireless folder:
        df = pd.json_normalize(ipf.fetch_all('tables/wireless/controllers'))
        df.to_csv('DOWNLOADS/raw-tables/controllers.csv')
        print("The Wireless Controllers table has downloaded successfully.")

        # Download Wireless APs to the wireless folder:
        df = pd.json_normalize(ipf.fetch_all('tables/wireless/access-points'))
        df.to_csv('DOWNLOADS/raw-tables/access-points.csv')
        print("The Wireless APs table has downloaded successfully.")

        # Download Wireless Radios to the wireless folder:
        df = pd.json_normalize(ipf.fetch_all('tables/wireless/radio'))
        df.to_csv('DOWNLOADS/raw-tables/radios-detail.csv')
        print("The Wireless Radios table has downloaded successfully.")

        # Download Wireless SSID-Summary to the wireless folder:
        df = pd.json_normalize(ipf.fetch_all('tables/wireless/ssid-summary'))
        df.to_csv('DOWNLOADS/raw-tables/ssid-summary.csv')
        print("The Wireless SSID-Summary table has downloaded successfully.")

        # Download Wireless Clients to the wireless folder:
        df = pd.json_normalize(ipf.fetch_all('tables/wireless/clients'))
        df.to_csv('DOWNLOADS/raw-tables/wireless-clients.csv')
        print("The Wireless Clients table has downloaded successfully.")

        # Download Phones to the voip folder:
        df = pd.json_normalize(ipf.fetch_all('tables/inventory/phones'))
        df.to_csv('DOWNLOADS/raw-tables/phones.csv')
        print("The Phones table has downloaded successfully.")

        # Download ACI Endpoints to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/aci/endpoints'))
        df.to_csv('DOWNLOADS/raw-tables/aci-endpoint.csv')
        print("The ACI Endpoints table has downloaded successfully.")

        # Download ACI VLANs to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/aci/vlan'))
        df.to_csv('DOWNLOADS/raw-tables/aci-vlan.csv')
        print("The ACI VLANs table has downloaded successfully.")

        # Download ACI VRF to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/aci/vrf'))
        df.to_csv('DOWNLOADS/raw-tables/aci-vrf.csv')
        print("The ACI VRF table has downloaded successfully.")

        # Download ACI DTEP to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/aci/dtep'))
        df.to_csv('DOWNLOADS/raw-tables/aci-dtep.csv')
        print("The ACI DTEP table has downloaded successfully.")

        # Download VXLAN VTEPs to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vxlan/vtep'))
        df.to_csv('DOWNLOADS/raw-tables/vxlan-vtep.csv')
        print("The VXLAN VTEPs table has downloaded successfully.")

        # Download VXLAN Peers to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vxlan/peers'))
        df.to_csv('DOWNLOADS/raw-tables/vxlan-peers.csv')
        print("The VXLAN Peers table has downloaded successfully.")

        # Download VXLAN Interfaces to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vxlan/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/vxlan-interfaces.csv')
        print("The VXLAN Interfaces table has downloaded successfully.")

        # Download VXLAN VNI to the sdn folder:
        df = pd.json_normalize(ipf.fetch_all('tables/vxlan/vni'))
        df.to_csv('DOWNLOADS/raw-tables/vxlan-vni.csv')
        print("The VXLAN VNI table has downloaded successfully.")

        # Download SDWAN Sites to the sdwan folder:
        df = pd.json_normalize(ipf.fetch_all('tables/sdwan/sites'))
        df.to_csv('DOWNLOADS/raw-tables/sdwan-sites.csv')
        print("The SDWAN Sites table has downloaded successfully.")

        # Download SDWAN Links to the sdwan folder:
        df = pd.json_normalize(ipf.fetch_all('tables/sdwan/links'))
        df.to_csv('DOWNLOADS/raw-tables/sdwan-links.csv')
        print("The SDWAN Links table has downloaded successfully.")

        # Download QoS Policy Maps to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/policy-maps'))
        df.to_csv('DOWNLOADS/raw-tables/policy-map.csv')
        print("The QoS Policy Maps table has downloaded successfully.")

        # Download QoS Shaping to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/shaping'))
        df.to_csv('DOWNLOADS/raw-tables/shaping.csv')
        print("The QoS Shaping table has downloaded successfully.")

        # Download QoS Queuing to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/queuing'))
        df.to_csv('DOWNLOADS/raw-tables/queuing.csv')
        print("The QoS Queuing table has downloaded successfully.")

        # Download QoS Policing to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/policing'))
        df.to_csv('DOWNLOADS/raw-tables/policing.csv')
        print("The QoS Policing table has downloaded successfully.")

        # Download QoS Priority Queuing to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/priority-queuing'))
        df.to_csv('DOWNLOADS/raw-tables/priority-queuing.csv')
        print("The QoS Priority Queuing table has downloaded successfully.")

        # Download QoS Marking to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/marking'))
        df.to_csv('DOWNLOADS/raw-tables/marking.csv')
        print("The QoS Marking table has downloaded successfully.")

        # Download QoS Random Drops to the qos folder:
        df = pd.json_normalize(ipf.fetch_all('tables/qos/random-drops'))
        df.to_csv('DOWNLOADS/raw-tables/random-drops.csv')
        print("The QoS Random Drops table has downloaded successfully.")

        # Download UDLD Neighbors to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/oam/unidirectional-link-detection/neighbors'))
        df.to_csv('DOWNLOADS/raw-tables/udld-neighbors.csv')
        print("The UDLD Neighbors table has downloaded successfully.")

        # Download UDLD Interfaces to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/management/oam/unidirectional-link-detection/interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/udld-interfaces.csv')
        print("The UDLD Interfaces table has downloaded successfully.")

        # Download Cloud Virtual Machines to the addressing folder:
        df = pd.json_normalize(ipf.fetch_all('tables/cloud/virtual-machines'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-machines.csv')
        print("The Cloud Virtual Machines table has downloaded successfully.")

        # Download Cloud Virtual Machines Interfaces table:
        df = pd.json_normalize(ipf.fetch_all('tables/cloud/virtual-machines-interfaces'))
        df.to_csv('DOWNLOADS/raw-tables/virtual-machines-interfaces.csv')
        print("The Cloud Virtual Machines Interfaces table has downloaded successfully.")







