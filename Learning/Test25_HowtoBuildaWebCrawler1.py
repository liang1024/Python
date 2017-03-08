import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while page<=max_pages:
        url='http://www.baidu.com'
        soure_code=requests.get(url)
        plain_text=soure_code.text
        print("code: ",plain_text)
        soup=BeautifulSoup(plain_text)
        # for link in soup.find_all('a'):


trade_spider(1)