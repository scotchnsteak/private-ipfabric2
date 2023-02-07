from download_all import DownloadAll
from create_cve_eol_report import DownloadCVE
from create_cust_report import CreateCustomerReport
from create_auto_engineer_report import AutomaticCheckReport
# from test import Test
from set_custom_intents import SetCustomIntents
from clean_tables import CleanTables
import pandas as pd
import os

# Create the dataframe from the Control_Sheet excel sheet.  Then
# use the values in the excel sheet to create the global environment
# variables.
df = pd.read_excel('Control_Sheet.xlsx', sheet_name='Control')
company_name = str(df.loc[0][1])
BASE_URL = str(df.loc[1][1])
TOKEN = str(df.loc[2][1])
get_all_downloads = bool(df.loc[3][1])
get_eol_info = bool(df.loc[4][1])
get_customer_report = bool(df.loc[5][1])
create_engineer_report = bool(df.loc[6][1])
run_test = bool(df.loc[7][1])
set_custom_intents = bool(df.loc[8][1])
os.environ["company_name"] = company_name
os.environ["BASE_URL"] = BASE_URL
os.environ["TOKEN"] = TOKEN
os.environ["white"] = '   '
os.environ["black"] = 'black'


if set_custom_intents:
    custom_intents = SetCustomIntents()
    custom_intents.set_custom_intents()

if get_all_downloads:
    download_all = DownloadAll()
    download_all.download_all_func()
    get_clean_tables = CleanTables()
    get_clean_tables.clean_tables()

if get_eol_info:
    cve_eol_info = DownloadCVE()
    cve_eol_info.cve_eol_info()

if get_customer_report:
    customer_report = CreateCustomerReport()
    customer_report.create_customer_report()

if create_engineer_report:
    engineer_report = AutomaticCheckReport()
    engineer_report.create_engineer_report()

if run_test:
    testing = Test()
    testing.run_test()





