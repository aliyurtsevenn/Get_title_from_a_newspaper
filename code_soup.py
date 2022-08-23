import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

url = 'https://www.resmigazete.gov.tr/eskiler/2022/08/20220816-2.htm'
reqs = requests.get(url)

uClient = uReq(url)
page = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page, "html.parser")

all_texts = page_soup.findAll("span", style='font-size:9.0pt;font-family:Arial;color:navy')

for each in all_texts:
    print(each.get_text(strip=True))
