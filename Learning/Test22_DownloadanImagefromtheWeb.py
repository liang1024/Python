import random
import urllib.request
'''
从web上下载一张图片,默认保存在源码同目录
'''
def download_web_image(url):
    name = random.randrange(1, 10000)
    file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, file_name)


download_web_image("https://avatars0.githubusercontent.com/u/18343332?v=3&s=460")
