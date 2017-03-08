'''
Keyword Arguments ：参数
'''


def dumb_sentence(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)


dumb_sentence()
dumb_sentence("Sally", "farts", "gently")
# 给固定的参数赋值
dumb_sentence(item="awesome")
dumb_sentence(item="awesome", action="is")

dumb_sentence("哈哈")
dumb_sentence("", "", "哈哈")
