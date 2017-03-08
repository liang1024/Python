import requests
from bs4 import BeautifulSoup

'''
爬取网页文字+网页超链接
'''
def spider_textAndherf():
        url='https://book.douban.com/latest?icn=index-latestbook-all'
        soure_code=requests.get(url)
        plain_text=soure_code.text
        # 打印网页文本内容
        # print("code: ",plain_text)
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.find_all('a'):
            # 打印网页所有超链接
            print(link.get("href"))


'''
爬取时光Top100:电影排行榜   10页的title+url
'''
def trade_spider(max_pages):
    page=1
    url=""
    while page <= max_pages :
        # 翻页
        if page is 1:
            url = 'http://www.mtime.com/top/movie/top100/'
            print("-------------第1页-----------------")
        else:
            url ='http://www.mtime.com/top/movie/top100/index-'+str(page)+".html"
            print("-------------第"+str(page)+"页-----------------")

        # 获取网页文本内容
        soure_code=requests.get(url)
        plain_text=soure_code.text
        # 打印网页文本内容
        # print("code: ",plain_text)
        # 解析
        soup=BeautifulSoup(plain_text,"html.parser")

        # 根据界面标签名不同爬取信息
        if page is 1:
            for link in soup.find_all('a', {"class": "c_fff"}):
                print(link.get("href"))
                print(link.string)
        else:
            for link in soup.find_all('a', {"class": "c_blue"}):
                print(link.get("href"))
                print(link.string)
        page+=1

# spider_textAndherf()
#
trade_spider(10)


