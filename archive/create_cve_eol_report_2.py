
from ipfabric import IPFClient
from ipfabric.tools import Vulnerabilities
from collections import defaultdict
import pandas as pd
from pathlib import Path
import os
from central_control import BASE_URL, TOKEN

# BASE_URL = os.getenv("BASE_URL")
# TOKEN = os.getenv("TOKEN")


Path("../DOWNLOADS").mkdir(parents=True, exist_ok=True)


def load_cve(ipf):
    devices = ipf.inventory.devices.all()
    vuln = Vulnerabilities(ipf=ipf, cve_limit=200)
    versions = vuln.check_versions()
    cves = defaultdict(dict)
    for v in versions:
        if v.family not in cves[v.vendor]:
            cves[v.vendor][v.family] = defaultdict(dict)
        cves[v.vendor][v.family][v.version] = v.cves
    return devices, cves


def load_eol(ipf):
    eol = ipf.fetch_all(
        'tables/reports/eof/detail',
        columns=["hostname", "siteName", "deviceSn", "vendor", "pid", "replacement", "sn", "endSale", "endMaintenance",
                 "endSupport", "url", "dscr"],
        filters={"or": [{"endSale": ["empty", False]}, {"endMaintenance": ["empty", False]},
                        {"endSupport": ["empty", False]}]}
    )
    return eol


def parse_cve(devices, cves):
    data, clean, error = list(), list(), list()
    for dev in devices:
        if dev['vendor'] and dev['family'] and dev['version'] and dev['vendor'] in cves and \
                dev['family'] in cves[dev['vendor']] and dev['version'] in cves[dev['vendor']][dev['family']]:
            if cves[dev['vendor']][dev['family']][dev['version']].error:
                error.append([dev['hostname'], dev['siteName'], dev['snHw'], dev['loginIp'], dev['vendor'],
                              dev['family'], dev['version'], cves[dev['vendor']][dev['family']][dev['version']].error])
                continue
            elif cves[dev['vendor']][dev['family']][dev['version']].total_results == 0:
                clean.append([dev['hostname'], dev['siteName'], dev['snHw'], dev['loginIp'], dev['vendor'],
                              dev['family'], dev['version']])
                continue
            for c in cves[dev['vendor']][dev['family']][dev['version']].cves:
                data.append([dev['hostname'], dev['siteName'], dev['snHw'], dev['loginIp'], dev['vendor'],
                             dev['family'], dev['version'], c.cve_id, c.description, c.url])
        else:
            error.append([dev['hostname'], dev['siteName'], dev['snHw'], dev['loginIp'], dev['vendor'], dev['family'],
                          dev['version']])
    return data, clean, error



ipf = IPFClient(BASE_URL, token=TOKEN, verify=False, timeout=15)
devices, cves = load_cve(ipf)

data, clean, error = parse_cve(devices, cves)

eol = load_eol(ipf)

df = pd.DataFrame(
    data, columns=['device', 'site', 'serial', 'ip', 'vendor', 'family', 'version', 'cve_id',
                   'cve_description', 'cve_url']
)
df_clean = pd.DataFrame(clean, columns=['device', 'site', 'serial', 'ip', 'vendor', 'family', 'version'])
df_error = pd.DataFrame(error, columns=['device', 'site', 'serial', 'ip', 'vendor', 'family', 'version', 'error'])
df_eol = pd.DataFrame(eol)
for eolt in ['endSale', 'endMaintenance', 'endSupport']:
    df_eol[eolt] = df_eol[eolt].values.astype(dtype='datetime64[ms]')
writer = pd.ExcelWriter('../DOWNLOADS/CVE_report.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='CVE DATA', index=False)
df_clean.to_excel(writer, sheet_name='Clean Devices', index=False)
df_error.to_excel(writer, sheet_name='CVE ERROR', index=False)
df_eol.to_excel(writer, sheet_name='End of Life', index=False)
writer.save()

print("The CVE and EOL data was downloaded successfully.")