
'''
下载网络中的文件并保存
'''

from urllib import request

Gspc="http://chart.finance.yahoo.com/table.csv?s=^GSPC&a=1&b=8&c=2017&d=2&e=8&f=2017&g=d&ignore=.csv"

def download_stock_data(csv_url):
    # 打开一个网络文件
    response=request.urlopen(csv_url)
    # 读取
    csv=response.read()
    # 转换为字符串
    csv_str=str(csv)
    # 分离分割线
    lines=csv_str.split("\\n")
    # 保存的文件
    dest_url=r'gspc.csv'
    # 创建文件
    fx=open(dest_url,'w')
    # 写入
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_stock_data(Gspc)