import requests
from bs4 import BeautifulSoup
import re

case = '' #Fill your case number here
try: len(case)==13
except: case = input("Looks like we don't have your case number on file.\nEnter your case number here: ")

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
header = {"User-Agent":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
payload = {"changeLocale":"","appReceiptNum":case,"initCaseSearch":"CHECK STATUS"}

r = requests.post(url, headers=header, data=payload)
r_bs = BeautifulSoup(r.content,"lxml")
status = r_bs.find('div',"current-status-sec").text
status = re.sub(r'[\t\n\r]',"",status)
print(status)
