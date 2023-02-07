

from ipfabric import IPFClient
from json import load
import os

from central_control import BASE_URL, TOKEN

# BASE_URL = os.getenv("BASE_URL")
# TOKEN = os.getenv("TOKEN")


ipf = IPFClient(BASE_URL, token=TOKEN, verify=False, timeout=15)

# # Set Intent #XX - TEST
# with open("intents/snmp_test.json", "r") as snmp:
#     data = load(snmp)
#
# r = ipf.post(url="reports",json=data)
# ipf.intent.load_intent()
# print("The check for SNMPv3 is complete.")

# Set Intent #7 - Checking for Paired Devices with Different Configurations:
with open("../intents/pc_config.json", "r") as pc_config:
    data = load(pc_config)

r = ipf.post(url="reports",json=data)
ipf.intent.load_intent()

# Set Intent #23 - Checking for old versions of STP:
with open("../intents/old_stp.json", "r") as old_stp:
    data = load(old_stp)

r = ipf.post(url="reports",json=data)
ipf.intent.load_intent()

# # Set Intent #30 - Root Guard Not Enabled:
# with open("intents/root_guard.json", "r") as root_guard:
#     data = load(root_guard)
#
# r = ipf.post(url="reports",json=data)
# ipf.intent.load_intent()
#
# # Set Intent #31 - BPDU Guard Not Enabled:
# with open("intents/bpdu_guard.json", "r") as bpdu_guard:
#     data = load(bpdu_guard)
#
# r = ipf.post(url="reports",json=data)
# ipf.intent.load_intent()

# Set Intent #32 - Telnet Enabled:
with open("../intents/telnet.json", "r") as telnet:
    data = load(telnet)

r = ipf.post(url="reports",json=data)
ipf.intent.load_intent()

# groups = {n: g.group_id for n, g in ipf.intent.group_by_name.items()}

"""
groups = {dict}  
 'First Hop Redundancy Protocol (FHRP)' = {str} '320668116'
'Quality of Service (QoS)' = {str} '320668112'
'Spanning-Tree Protocol (STP)' = {str} '320668115'
'Interfaces' = {str} '320668114'
'Management Consistency' = {str} '320668109'
'Security' = {str} '320668120'
'Endpoints' = {str} '320668113'
"""
print("The Custom Intents have been set.")








