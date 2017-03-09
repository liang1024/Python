'''
Word Frequency Counter:
'''

import requests
from bs4 import BeautifulSoup
import operator

# http://china.nba.com/news/

'''
爬取网页数据，并根据空格分段
'''


def start(url):
    word_list = []
    source_code = requests.get(url).text
    # print(source_code)
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll("a", {"class": "s xst"}):
        content = post_text.string
        # print(content)
        words = content.lower().split()
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)


'''
替换多余字符
'''


def clean_up_list(word_list):
    clean_up_list = []
    symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='”、“"
    for word in word_list:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            # print(word)
            clean_up_list.append(word)
    create_dictionary(clean_up_list)


'''
打印出现字符与次数
'''
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            # print(word_count,word)
            word_count[word] += 1
        else:
            # print(word_count,word)
            word_count[word] = 1
        # print("----------------")
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


# start("http://china.nba.com/news/")
# start("http://r.qidian.com/?chn=21")
start("http://www.52pojie.cn/forum-39-1.html")
